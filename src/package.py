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
 ____            _                         
|  _ \ __ _  ___| | ____ _  __ _  ___ _ __ 
| |_) / _` |/ __| |/ / _` |/ _` |/ _ \ '__|
|  __/ (_| | (__|   < (_| | (_| |  __/ |   
|_|   \__,_|\___|_|\_\__,_|\__, |\___|_|   
                           |___/     
Turn your packs into usable .asar files      
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
            askOutput(base)
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

def askOutput(finalpath):
    path = input("\nPath to place final packaged pack: ")
    base = Path(path.strip().strip('"'))

    if (base.is_dir()):
        print("Packaging..")
        create_archive(Path(finalpath), Path(base / f"{Path(finalpath).name}.asar"))
        print(f"\nPackaged pack '{finalpath.name}' at {base}")
    else: 
        print("\nPath is not a folder/does not exist!")
        askOutput(finalpath)


package()

input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))