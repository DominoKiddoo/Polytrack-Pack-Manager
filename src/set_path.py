from pathlib import Path
import json
import os
import sys
import runpy

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
 ____       _     ____       _   _     
/ ___|  ___| |_  |  _ \ __ _| |_| |__  
\___ \ / _ \ __| | |_) / _` | __| '_ \ 
 ___) |  __/ |_  |  __/ (_| | |_| | | |
|____/ \___|\__| |_|   \__,_|\__|_| |_|
""")
def addPath():
    parent_path = input("Please input a path for where your polytrack folder is (type exit to exit): ")

    if parent_path.lower() == "exit":
        runpy.run_path(getScriptPath("main.py"))
        sys.exit()


    try:
        base = Path(parent_path.strip().strip('"'))
        exe_exists = (base / "PolyTrack.exe").is_file()

        dir_exists = (base / "resources").is_dir()
        asar_exists = (base / "resources" / "app.asar").is_file()

        if exe_exists and dir_exists and asar_exists:
            settingspath = getRightPath('settings.json')

            if not os.path.exists(settingspath):
                with open(settingspath, 'w', encoding='utf-8') as file:
                    json.dump({"pathToFolder": ""}, file, indent=4)
            
            with open(settingspath, 'r', encoding='utf-8') as file:
                loadedJson = json.load(file)
                
            loadedJson["pathToFolder"] = parent_path
            with open(settingspath, 'w', encoding='utf-8') as file:
                json.dump(loadedJson, file, indent=4)
            print(f"\nFolder\n{base}\nSet as PolyTrack folder!")
            
        else:
            print("\nThis folder does not meet the requirements. Ensure it has PolyTrack.exe, and the 'resources' folder including an app.asar file!\n")
            addPath()
    except Exception as e:
        print("\nThere was an error!\n" + e)
        addPath()




addPath()


input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))