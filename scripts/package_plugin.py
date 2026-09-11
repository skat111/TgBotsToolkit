from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
out = root.parent / 'telegram-bot-toolkit.zip'
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for path in root.rglob('*'):
        if path.is_file() and '__pycache__' not in path.parts:
            archive.write(path, path.relative_to(root.parent))
print(out)
