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
import math
from pydub import AudioSegment
from pydub.effects import normalize
import time
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
  ___        _      _                                  _ 
 / _ \ _   _(_) ___| | __    ___  ___  _   _ _ __   __| |
| | | | | | | |/ __| |/ /   / __|/ _ \| | | | '_ \ / _` |
| |_| | |_| | | (__|   <    \__ \ (_) | |_| | | | | (_| |
 \__\_\\__,_|_|\___|_|\_\   |___/\___/ \__,_|_| |_|\__,_|                                                    
  ____                          _                      
 / ___|___  _ ____   _____ _ __| |_                    
| |   / _ \| '_ \ \ / / _ \ '__| __|                   
| |__| (_) | | | \ V /  __/ |  | |_                    
 \____\___/|_| |_|\_/ \___|_|   \__|
""")
print("""
Copies all sounds in a folder but converted the ogg format.
Used because polytrack stores a .mp3 and .ogg version of each sound
""")

while True:
    path = input("\nInput path for sound folder (type exit to exit): ")
    base = Path(path.strip().strip('"'))

    if path.lower() == "exit":
        runpy.run_path(getScriptPath("main.py"))
        sys.exit()
    
    if (base.is_dir()):
        for file in base.iterdir():
            if (file.suffix.lower() == ".mp3"):
                print(f"Found {file.name}, converting to ogg..")
                audio = AudioSegment.from_file(file)
                audio.export(Path(base / f"{file.stem}.ogg"), format="ogg")

                print(f"Converted {file.name} to {file.stem}.ogg \n")
                time.sleep(0.5)


        break
    else:
        print("\nPath not a valid folder!")
        continue

input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))