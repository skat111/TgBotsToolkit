"""Generate a runnable Telegram bot starter for a supported framework."""
import argparse
from pathlib import Path
import shutil

SKILL_ROOT = Path(__file__).resolve().parents[1]
STARTERS = SKILL_ROOT / "assets" / "starters"
SUPPORTED = ("aiogram", "python-telegram-bot", "telegraf", "grammy")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("framework", choices=SUPPORTED)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--production", action="store_true", help="Add Docker, PostgreSQL, Redis, migrations, locales, webhook settings, and tests")
    args = parser.parse_args()

    source = STARTERS / args.framework
    destination = args.destination.resolve()
    if destination.exists() and any(destination.iterdir()):
        raise SystemExit(f"Destination is not empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    if args.production:
        shutil.copytree(STARTERS / "production-common", destination, dirs_exist_ok=True)
        shutil.copytree(STARTERS / "production" / args.framework, destination, dirs_exist_ok=True)
    mode = "production" if args.production else "basic"
    print(f"Created {mode} {args.framework} starter at {destination}")


if __name__ == "__main__":
    main()
