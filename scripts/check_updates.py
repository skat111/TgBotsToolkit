#!/usr/bin/env python3
"""Check and safely install the newest Telegram Bot Toolkit GitHub release."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, subprocess, tempfile, urllib.request, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "telegram-bot-toolkit"
ASSET = f"{PLUGIN_NAME}.zip"

def local_version():
    return json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]

def repo_slug(value=None):
    value = value or os.environ.get("TELEGRAM_BOT_TOOLKIT_REPO")
    if value: return value.rstrip("/").removesuffix(".git").split("github.com/")[-1]
    try:
        url = subprocess.check_output(["git", "-C", str(ROOT), "remote", "get-url", "origin"], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception: return None
    return url.rstrip("/").removesuffix(".git").split("github.com/")[-1].replace(":", "/")

def api(slug, path):
    req = urllib.request.Request("https://api.github.com/repos/" + slug + path,
        headers={"Accept":"application/vnd.github+json", "User-Agent":PLUGIN_NAME})
    token = os.environ.get("GITHUB_TOKEN")
    if token: req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)

def latest(slug): return api(slug, "/releases/latest")

def checksum(data):
    return hashlib.sha256(data).hexdigest()

def safe_extract(zf, destination):
    base = destination.resolve()
    for info in zf.infolist():
        target = (destination / info.filename).resolve()
        if target != base and base not in target.parents: raise ValueError("archive path traversal")
    zf.extractall(destination)

def install(release, allow_unverified=False):
    asset = next((a for a in release.get("assets", []) if a["name"] == ASSET), None)
    digest_asset = next((a for a in release.get("assets", []) if a["name"] == ASSET + ".sha256"), None)
    if not asset: raise RuntimeError(f"release has no {ASSET}")
    if not digest_asset and not allow_unverified: raise RuntimeError("release has no checksum asset")
    req = urllib.request.Request(asset["browser_download_url"], headers={"User-Agent":PLUGIN_NAME})
    with urllib.request.urlopen(req, timeout=120) as r: data = r.read()
    if digest_asset:
        req = urllib.request.Request(digest_asset["browser_download_url"], headers={"User-Agent":PLUGIN_NAME})
        with urllib.request.urlopen(req, timeout=30) as r: expected = r.read().decode().split()[0].lower()
        if checksum(data) != expected: raise RuntimeError("release checksum mismatch")
    with tempfile.TemporaryDirectory(prefix="telegram-toolkit-") as td:
        stage = Path(td) / "stage"; stage.mkdir()
        with zipfile.ZipFile(__import__("io").BytesIO(data)) as zf: safe_extract(zf, stage)
        candidates = [p for p in stage.rglob("plugin.json") if p.parent.name == ".codex-plugin"]
        if len(candidates) != 1: raise RuntimeError("archive must contain exactly one .codex-plugin/plugin.json")
        source = candidates[0].parent.parent
        manifest = json.loads(candidates[0].read_text(encoding="utf-8"))
        if manifest.get("name") != PLUGIN_NAME: raise RuntimeError("unexpected plugin name")
        backup_dir = ROOT.parent / (ROOT.name + ".backups"); backup_dir.mkdir(exist_ok=True)
        backup = backup_dir / (release.get("tag_name", "unknown").replace("/", "_") + ".zip")
        if not backup.exists():
            with zipfile.ZipFile(backup, "w", zipfile.ZIP_DEFLATED) as out:
                for p in ROOT.rglob("*"):
                    if p.is_file(): out.write(p, p.relative_to(ROOT.parent))
        old = ROOT.parent / (ROOT.name + ".previous")
        if old.exists(): shutil.rmtree(old)
        ROOT.rename(old)
        try: shutil.copytree(source, ROOT)
        except Exception:
            if ROOT.exists(): shutil.rmtree(ROOT)
            old.rename(ROOT); raise
        shutil.rmtree(old)
    print(json.dumps({"status":"installed", "tag":release.get("tag_name"), "version":manifest.get("version")}, ensure_ascii=False))

def main():
    p = argparse.ArgumentParser(); p.add_argument("--repo"); p.add_argument("--check", action="store_true"); p.add_argument("--install", action="store_true"); p.add_argument("--allow-unverified", action="store_true")
    a = p.parse_args(); slug = repo_slug(a.repo)
    if not slug or "/" not in slug:
        print(json.dumps({"status":"unconfigured", "message":"Set TELEGRAM_BOT_TOOLKIT_REPO=owner/repo or add a GitHub origin."})); return 0
    try: release = latest(slug)
    except Exception as e: print(json.dumps({"status":"unavailable", "error":str(e)})); return 0
    state = ROOT / ".codex-plugin" / "installed-release.json"; installed = json.loads(state.read_text()) if state.exists() else {}
    current = local_version(); tag = release.get("tag_name"); available = installed.get("tag") != tag
    result = {"status":"update_available" if available else "current", "repo":slug, "current_version":current, "latest_tag":tag, "latest_name":release.get("name")}
    print(json.dumps(result, ensure_ascii=False))
    if a.install and available:
        install(release, a.allow_unverified)
        (ROOT / ".codex-plugin" / "installed-release.json").write_text(json.dumps({"tag":tag, "installed_version":local_version()}, indent=2), encoding="utf-8")
    return 0
if __name__ == "__main__": raise SystemExit(main())
