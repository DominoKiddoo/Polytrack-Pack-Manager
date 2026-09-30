import os
import sys
import shutil
import json
from pathlib import Path
import runpy
from settingsutils import get_settings_path


def getRightPath(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, relative_path)

def getScriptPath(name):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_dir, name)

os.system('cls' if os.name == 'nt' else 'printf "\033c"')

print(r"""
 ____       _     ____            _                                     
/ ___|  ___| |_  |  _ \ __ _  ___| | __                                 
\___ \ / _ \ __| | |_) / _` |/ __| |/ /                                 
 ___) |  __/ |_  |  __/ (_| | (__|   <                                  
|____/ \___|\__| |_|   \__,_|\___|_|\_\                                                                                              
 _____                                       _                        _ 
|  ___| __ ___  _ __ ___    _ __   __ _  ___| | ____ _  __ _  ___  __| |
| |_ | '__/ _ \| '_ ` _ \  | '_ \ / _` |/ __| |/ / _` |/ _` |/ _ \/ _` |
|  _|| | | (_) | | | | | | | |_) | (_| | (__|   < (_| | (_| |  __/ (_| |
|_|  |_|  \___/|_| |_| |_| | .__/ \__,_|\___|_|\_\__,_|\__, |\___|\__,_|
                           |_|                         |___/                      
Set pack from a .asar file        
        """)
try:
    while True:
        choice = input("Path of pack to replace with (type exit to exit): ").strip().strip('"')

        if choice.lower() == "exit":
            runpy.run_path(getScriptPath("main.py"))
            sys.exit()

        if not Path(choice).is_file():
            print("\nThis file does not exist\n")
            continue
        if not Path(choice).suffix.lower() == ".asar":
            print("\nThis file is not in the .asar format!\n")
            continue

        settingspath = get_settings_path()
            
        with open(settingspath, 'r', encoding='utf-8') as file:
            loadedJson = json.load(file)

        
        print("Loading pack..")

        dest = os.path.join(loadedJson["pathToFolder"], "resources", "app.asar")

        shutil.copy(choice, dest)

        print(f"Changed pack to {Path(choice).name}")
        break
except Exception as e:
    print(f"\nThere was an error! Please make sure your polytrack path is set!\nDetails: {e}")



input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))