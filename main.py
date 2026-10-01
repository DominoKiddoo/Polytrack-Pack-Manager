import time
import questionary
import subprocess
import sys
import os
import runpy
import json
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


try:
    while True:
        os.system('cls' if os.name == 'nt' else 'printf "\033c"')

        print(r"""
 ____       _       _                  _                         
|  _ \ ___ | |_   _| |_ _ __ __ _  ___| | __                     
| |_) / _ \| | | | | __| '__/ _` |/ __| |/ /                     
|  __/ (_) | | |_| | |_| | | (_| | (__|   <                      
|_|   \___/|_|\__, |\__|_|  \__,_|\___|_|\_\                     
 ____         |___/     __  __                                   
|  _ \ __ _  ___| | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |_) / _` |/ __| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
|  __/ (_| | (__|   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
|_|   \__,_|\___|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                |___/           
        """)


        settingspath = get_settings_path()
        try:
            with open(settingspath, 'r', encoding='utf-8') as file:
                loadedJson = json.load(file)
        except:
            pass

        if not os.path.exists(settingspath) or loadedJson["pathToFolder"] == "":
            print("IMPORTANT: YOU HAVE NOT SET A POLYTRACK FOLDER PATH! PLEASE SELECT 'Utility', THEN SELECT 'Set Path' TO SET THE PATH TO YOUR FOLDER!\n")

        catagory = questionary.select(
            "Select a catagory",
            choices=[
                "Creating packs",
                "Installing packs",
                "Utility",
                "Exit"
            ]
        ).ask()
        sys.stdout.write("\033[A\033[K")
        sys.stdout.flush()

        if catagory == "Exit":
            sys.exit()
        if catagory is None:
            raise KeyboardInterrupt


        os.system('cls' if os.name == 'nt' else 'printf "\033c"')

        answer = ""

        if catagory == "Creating packs":
            answer = questionary.select(
                "What do you want to do?",
                choices=[
                    'Create new pack', # implemented
                    'Package pack to .asar',  # implemented
                    'Fix pack sounds', # implemented
                    'Quick sound convert',
                    'Go back'
                ]
            ).ask()
            sys.stdout.write("\033[A\033[K")
            sys.stdout.flush()
        elif catagory == "Installing packs":
            answer = questionary.select(
                "What do you want to do?",
                choices=[
                    'Install pack from packaged', # implemented
                    'Install pack from unpackaged', # implemented
                    'Go back'
                ]
            ).ask()
            sys.stdout.write("\033[A\033[K")
            sys.stdout.flush()
        elif catagory == "Utility":
            answer = questionary.select(
                "What do you want to do?",
                choices=[
                    'Set path',  # implemented
                    'Reset to default',  # implemented
                    'Go back'
                ]
            ).ask()
            sys.stdout.write("\033[A\033[K")
            sys.stdout.flush()
        if answer is None:
            raise KeyboardInterrupt

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        if answer == 'Go back':
            continue

        if answer == 'Set path':
            runpy.run_path(getScriptPath("src/set_path.py"))
            break
        elif answer == 'Reset to default':
            runpy.run_path(getScriptPath("src/reset.py"))
            break
        elif answer == 'Create new pack':
            runpy.run_path(getScriptPath("src/new.py"))
            break
        elif answer == 'Package pack to .asar':
            runpy.run_path(getScriptPath("src/package.py"))
            break
        elif answer == 'Install pack from packaged':
            runpy.run_path(getScriptPath("src/setpackaged.py"))
            break
        elif answer == 'Install pack from unpackaged':
            runpy.run_path(getScriptPath("src/setunpackaged.py"))
            break
        elif answer == 'Fix pack sounds':
            runpy.run_path(getScriptPath("src/fixsounds.py"))
            break
        elif answer == 'Quick sound convert':
            runpy.run_path(getScriptPath("src/quickcopy.py"))
            break
except KeyboardInterrupt:
    pass
