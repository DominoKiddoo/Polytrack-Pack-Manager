import os
import sys
import shutil
import json
import pathlib
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
 ____                _                       
|  _ \ ___  ___  ___| |_                     
| |_) / _ \/ __|/ _ \ __|                    
|  _ <  __/\__ \  __/ |_                     
|_| \_\___||___/\___|\__|                                                          
 _              _       __             _ _   
| |_ ___     __| | ___ / _| __ _ _   _| | |_ 
| __/ _ \   / _` |/ _ \ |_ / _` | | | | | __|
| || (_) | | (_| |  __/  _| (_| | |_| | | |_ 
 \__\___/   \__,_|\___|_|  \__,_|\__,_|_|\__|
""")
try:

    choice = input("Are you SURE you want to reset your selected pack to default (Y/N)? ")

    if (choice.lower() == "y"):
        settingspath = get_settings_path()
        
        with open(settingspath, 'r', encoding='utf-8') as file:
            loadedJson = json.load(file)

        
        print("Cloning default..")
        dest = os.path.join(loadedJson["pathToFolder"], "resources")
        shutil.copy(getRightPath("app.asar"), dest)
        print("Reset to default pack!")
    else:
        print("Did not reset!")
except Exception as e:
    print(f"\nThere was an error! Please make sure your polytrack path is set!\nDetails: {e}")



input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))


