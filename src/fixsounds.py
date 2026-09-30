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
 _____ _                           
|  ___(_)_  __                     
| |_  | \ \/ /                     
|  _| | |>  <                      
|_|   |_/_/\_\                                              
 ____                        _     
/ ___|  ___  _   _ _ __   __| |___ 
\___ \ / _ \| | | | '_ \ / _` / __|
 ___) | (_) | |_| | | | | (_| \__ \
|____/ \___/ \__,_|_| |_|\__,_|___/
""")
print("""
Essentially, some sounds in polytrack are played at a much lower volume.
This script goes through a directory and makes all the sounds play at the volume in game that you hear in the file explorer preview
ONLY run this when you are FULLY DONE editing the sounds in game as it cant be reverted and will make some of your sounds VERY LOUD when
previewing them
""")
sounds = {
    "checkpoint": 30.5,
    "click": 42.5,
    "collision": 18.4,
    "editor_edit": 26,
    "engine": 10.9,
    "music": 12,
    "position_tick": 40,
    "record": 26,
    "skidding": 13.4,
    "suspension": 10.9,
    "tires": 10.9,
}

while True:
    path = input("\nInput path for sound folder (type exit to exit): ")
    base = Path(path.strip().strip('"'))

    if path.lower() == "exit":
        runpy.run_path(getScriptPath("main.py"))
        sys.exit()
    
    extensions = ("**/*.mp3", "**/*.ogg")
    if (base.is_dir()):
        for pattern in extensions:
            for file in base.glob(pattern):
                if (file.stem in sounds):
                    print(f"Found {file.name}, processing..")
                    audio = AudioSegment.from_file(file)
                    normalised = normalize(audio)
                    louder = normalised + sounds[file.stem]
                    louder.export(Path(base / file.name), format=file.suffix.lower().lstrip('.'))
                    print(f"Finished processing {file.stem} (+{sounds[file.stem]}db)\n")
                    time.sleep(0.5)



        break
    else:
        print("\nPath not a valid folder!")
        continue

input("\nPress Enter to go back...")
runpy.run_path(getScriptPath("main.py"))