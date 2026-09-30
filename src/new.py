import os
import sys
import shutil
import json
import pathlib
import asar
from pathlib import Path
from asar import extract_archive
import re
import runpy
from settingsutils import get_settings_path

def getScriptPath(name):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_dir, name)

def getRightPath(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, relative_path)

os.system('cls' if os.name == 'nt' else 'printf "\033c"')

print(r"""
 _   _                 ____            _    
| \ | | _____      __ |  _ \ __ _  ___| | __
|  \| |/ _ \ \ /\ / / | |_) / _` |/ __| |/ /
| |\  |  __/\ V  V /  |  __/ (_| | (__|   < 
|_| \_|\___| \_/\_/   |_|   \__,_|\___|_|\_\
This tool creates a fresh copy of the assets for you to edit
""")

def newPack():
    path = input("\nPath for new pack (type exit to exit): ")
    if path.lower() == "exit":
        runpy.run_path(getScriptPath("main.py"))
        sys.exit()
    base = Path(path.strip().strip('"'))
    if (base.is_dir()):
        while True:
            name = input("Pack name: ")
            if (name == ""):
                print("\nPack name must not be empty\n")
                continue
            safe_name = re.sub(r'[^a-zA-Z0-9_-]', '', name)
            if not safe_name:
                continue
            break
        print("Cloning default..")


        extract_archive(Path(getRightPath("app.asar")), Path(base / safe_name))

        print(f"\nCreated new pack ({safe_name}) at {base}")
    else: 
        print("\nPath is not a folder/does not exist!")
        newPack()

newPack()
input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))

