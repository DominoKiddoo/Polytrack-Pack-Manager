from pathlib import Path
import json
import os
import sys
import runpy
from asar import *
import re
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
 ____       _     ____            _                                                 
/ ___|  ___| |_  |  _ \ __ _  ___| | __                                             
\___ \ / _ \ __| | |_) / _` |/ __| |/ /                                             
 ___) |  __/ |_  |  __/ (_| | (__|   <                                              
|____/ \___|\__| |_|   \__,_|\___|_|\_\                                                                                                                                
 _____                                                   _                        _ 
|  ___| __ ___  _ __ ___    _   _ _ __  _ __   __ _  ___| | ____ _  __ _  ___  __| |
| |_ | '__/ _ \| '_ ` _ \  | | | | '_ \| '_ \ / _` |/ __| |/ / _` |/ _` |/ _ \/ _` |
|  _|| | | (_) | | | | | | | |_| | | | | |_) | (_| | (__|   < (_| | (_| |  __/ (_| |
|_|  |_|  \___/|_| |_| |_|  \__,_|_| |_| .__/ \__,_|\___|_|\_\__,_|\__, |\___|\__,_|
                                       |_|                         |___/            
Set pack from a folder that has not been packaged to a .asar file        
""")


def hasfolder(path, name):
    target = Path(path) / name
    return target.is_dir()

def package():
    path = input("\nPath of unpackaged pack (type exit to exit): ")

    if path.lower() == "exit":
        runpy.run_path(getScriptPath("main.py"))
        sys.exit()
    base = Path(path.strip().strip('"'))

    if (base.is_dir()):
        index =  Path(base) / "index.html"

        if (hasfolder(base, "audio") and hasfolder(base, "electron") and hasfolder(base, "images") and hasfolder(base, "lib") and hasfolder(base, "models") and hasfolder(base, "tracks") and index.is_file()):
            change(base)
        else:
            print("""
This is not a valid pack! Please insure it contains the following folders:
- audio
- electron
- images
- lib
- models
- tracks
And an index.html file.

            """)
            package()

    else: 
        print("\nPath is not a folder/does not exist!")
        package()

def change(finalpath):
    try:
        settingspath = get_settings_path()

        with open(settingspath, 'r', encoding='utf-8') as file:
            loadedJson = json.load(file)
            
        dest = os.path.join(loadedJson["pathToFolder"], "resources", "app.asar")

        print("Setting pack..")
        create_archive(Path(finalpath), Path(dest))
        print(f"\nSet pack to {finalpath.name}")
    except Exception as e:
        print(f"\nThere was an error! Please make sure your polytrack path is set!\nDetails: {e}")



package()

input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))