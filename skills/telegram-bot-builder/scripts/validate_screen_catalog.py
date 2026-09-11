"""Validate the framework-neutral Telegram screen catalog."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references" / "screen-catalog.json"
ACTIONS = {
    "url", "callback_data", "web_app", "login_url", "switch_inline_query",
    "switch_inline_query_current_chat", "switch_inline_query_chosen_chat",
    "copy_text", "callback_game", "pay", "disabled"
}


def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    screens = data.get("screens", [])
    errors = []
    ids = [screen.get("id") for screen in screens]
    if not screens:
        errors.append("catalog has no screens")
    if len(ids) != len(set(ids)):
        errors.append("screen ids must be unique")

    for screen in screens:
        screen_id = screen.get("id", "<missing>")
        if screen.get("presentation") not in {"text", "photo"}:
            errors.append(f"{screen_id}: unsupported presentation")
        if not screen.get("html"):
            errors.append(f"{screen_id}: missing html")
        if screen.get("presentation") == "photo" and not screen.get("media_key"):
            errors.append(f"{screen_id}: photo screen has no media_key")

        for row_index, row in enumerate(screen.get("buttons", [])):
            if not row:
                errors.append(f"{screen_id}: empty button row {row_index}")
            for column_index, button in enumerate(row):
                location = f"{screen_id}[{row_index}][{column_index}]"
                if not button.get("text"):
                    errors.append(f"{location}: missing text")
                actions = ACTIONS.intersection(button)
                if len(actions) != 1:
                    errors.append(f"{location}: expected exactly one action, got {sorted(actions)}")
                callback = button.get("callback_data")
                if callback and len(callback.encode("utf-8")) > 64:
                    errors.append(f"{location}: static callback_data exceeds 64 bytes")
                if "disabled" in button and button["disabled"] != {}:
                    errors.append(f"{location}: disabled must be an empty DisabledButton object")
                if button.get("pay") is True and (row_index != 0 or column_index != 0):
                    errors.append(f"{location}: pay button must be first in the first row")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Screen catalog is valid: {len(screens)} screens")


if __name__ == "__main__":
    main()
