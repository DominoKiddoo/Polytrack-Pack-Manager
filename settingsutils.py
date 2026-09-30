import os
import sys
from pathlib import Path


def get_settings_path():
    if getattr(sys, "frozen", False):
        appdata = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        sdir = appdata / "Polytrack Pack Manager"
        sdir.mkdir(parents=True, exist_ok=True)
        settings_path = sdir / "settings.json"
        if not settings_path.exists():
            settings_path.write_text('{"pathToFolder": ""}', encoding="utf-8")
        return settings_path

    return Path(__file__).resolve().parent / "src" / "settings.json"