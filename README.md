
# Polytrack Pack Manager - Currently compatible with PolyTrack 0.6.3

CLI-Based tool to help with polytrack modding. Includes a collection of helpers to make creating packs much easier. With packs, you can edit  all the in game files including:
* Audio
* Images
* Models
* Tracks
* Code
Allowing for endless posibilities.

Currently only supports windows. For the best way to learn how to use this tool, read this entire readme!

For developer tips, read [here](#developer-tips)

## What is Polytrack?

PolyTrack is a low-poly racing game with loops, jumps and high speeds, where every millisecond counts. The game is heavily inspired by TrackMania, where you race against the clock to improve your time on different tracks.

The game includes a level editor where you can create tracks, which you can then export and share with others.

https://kodub.itch.io/polytrack

## Installation

Parts of this program require FFmpeg. Please install that [here](https://ffmpeg.org/)

Go to the releases tab and download the exe, and use the `Set path` command located in the utilities  catagory. You will be prompted to input the path for where your polytrack is. More info can be found below.

### Building from the source
Clone the repo, and run
```
pip install -r requirements.txt
pyinstaller main.spec
```

After install launch the exe and select
`Utilities` then `Select Path`
And put in the path to your polytrack folder. More info can be found [here](#set-path)
## Issues/making pr's
If you find an issue, describe it in the issues tab.  
If you want to make a pr, feel free to do that too! I want this to be the pest polytrack modding tool out there

## Sharing packs
There is currently no official way of sharing packs. You'd have to message them to your friends, or upload them to a cloud service such as Google Drive or Dropbox.



## Tools explained
There are 3 catagories of utilities,
* Creating packs
* Installing packs
* Utilities

You select between them on launch. It will look something like

```

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

? Select a catagory (Use arrow keys)
 » Creating packs
   Installing packs
   Utility
   Exit
```

Let's go over each catagory, their helpers and what they do.

## Creating packs
This catagory contains 4 helpers for creating packs.

### Create new pack
Clones the default pack to a destination of your choosing. The pack cloned has all the code formatted and beautified for easy editing.

**EXAMPLE USAGE**

```
 _   _                 ____            _
| \ | | _____      __ |  _ \ __ _  ___| | __
|  \| |/ _ \ \ /\ / / | |_) / _` |/ __| |/ /
| |\  |  __/\ V  V /  |  __/ (_| | (__|   <
|_| \_|\___| \_/\_/   |_|   \__,_|\___|_|\_\
This tool creates a fresh copy of the assets for you to edit


Path for new pack (type exit to exit): C:\Users\me\Documents\packs\raw
Pack name: my awesome pack
Cloning default..

Created new pack (myawesomepack) at C:\Users\me\Documents\packs\raw

Press Enter to go back...
```


### Package pack to .asar
Packages a folder (like the one created using `New pack`) into a .asar file. Asar stands for Atom Shell Archive Format, and bundles multiple application files (in our case assets and code). 

These are 'packs' and can be installed through other tools this program has.

**EXAMPLE USAGE**
```
 ____            _
|  _ \ __ _  ___| | ____ _  __ _  ___ _ __
| |_) / _` |/ __| |/ / _` |/ _` |/ _ \ '__|
|  __/ (_| | (__|   < (_| | (_| |  __/ |
|_|   \__,_|\___|_|\_\__,_|\__, |\___|_|
                           |___/
Turn your packs into usable .asar files


Path of unpackaged pack (type exit to exit):
C:\Users\me\Documents\packs\raw\myawesomepack

Path to place final packaged pack: C:\Users\me\Documents\packs
Packaging..

Packaged pack 'myawesomepack' at C:\Users\me\Documents\packs

Press Enter to go back...

```

### Fix pack sounds
Essentially, some sounds in polytrack are played at a much lower volume. This script goes through a directory and makes all the sounds play at the volume in game that you hear in the file explorer preview. 

ONLY run this when you are FULLY DONE editing the sounds in game as it cant be reverted and will make some of your sounds VERY LOUD when
previewing them.

It goes through and checks file names and adds decibels, according to this table:

| Sound name | Added decibels |
| -------- | -------- 
| checkpoint |30.5|
| click | 42.5 |
| collision |18.4|
| editor_edit |26|
| engine |10.9|
| music |12|
| position_tick |40|
| record |26|
| skidding | 13.4|
| suspension |10.9
| tires |10.9|

**EXAMPLE USAGE**
```

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


Essentially, some sounds in polytrack are played at a much lower volume.
This script goes through a directory and makes all the sounds play at the volume in game that you hear in the file explorer preview
ONLY run this when you are FULLY DONE editing the sounds in game as it cant be reverted and will make some of your sounds VERY LOUD when
previewing them


Input path for sound folder (type exit to exit): C:\Users\me\Documents\packs\raw\myawesomepack\audio
Found checkpoint.mp3, processing..
Finished processing checkpoint (+30.5db)

Found click.mp3, processing..
Finished processing click (+42.5db)

Found collision.mp3, processing..
Finished processing collision (+18.4db)

Found editor_edit.mp3, processing..
Finished processing editor_edit (+26db)

Found engine.mp3, processing..
Finished processing engine (+10.9db)

Found music.mp3, processing..
Finished processing music (+12db)

Found position_tick.mp3, processing..
Finished processing position_tick (+40db)

Found record.mp3, processing..
Finished processing record (+26db)

Found skidding.mp3, processing..
Finished processing skidding (+13.4db)

Found suspension.mp3, processing..
Finished processing suspension (+10.9db)

Found tires.mp3, processing..
Finished processing tires (+10.9db)

Found checkpoint.ogg, processing..
Finished processing checkpoint (+30.5db)

Found click.ogg, processing..
Finished processing click (+42.5db)

Found collision.ogg, processing..
Finished processing collision (+18.4db)

Found editor_edit.ogg, processing..
Finished processing editor_edit (+26db)

Found engine.ogg, processing..
Finished processing engine (+10.9db)

Found music.ogg, processing..
Finished processing music (+12db)

Found position_tick.ogg, processing..
Finished processing position_tick (+40db)

Found record.ogg, processing..
Finished processing record (+26db)

Found skidding.ogg, processing..
Finished processing skidding (+13.4db)

Found suspension.ogg, processing..
Finished processing suspension (+10.9db)

Found tires.ogg, processing..
Finished processing tires (+10.9db)


Press Enter to go back...
```

### Quick sound convert
Copies all sounds in a folder but converted the ogg format. Used because polytrack stores all sounds in both `.mp3` and `.ogg` formats. As it is a hastle to change all your mp3 audio files into ogg manually, this script can do it fast!

**EXAMPLE USAGE**
```

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


Copies all sounds in a folder but converted the ogg format.
Used because polytrack stores a .mp3 and .ogg version of each sound


Input path for sound folder (type exit to exit): C:\Users\me\Documents\packs\raw\myawesomepack\audio
Found checkpoint.mp3, converting to ogg..
Converted checkpoint.mp3 to checkpoint.ogg 

Found click.mp3, converting to ogg..
Converted click.mp3 to click.ogg 

Found collision.mp3, converting to ogg..
Converted collision.mp3 to collision.ogg 

Found editor_edit.mp3, converting to ogg..
Converted editor_edit.mp3 to editor_edit.ogg 

Found engine.mp3, converting to ogg..
Converted engine.mp3 to engine.ogg 

Found music.mp3, converting to ogg..
Converted music.mp3 to music.ogg 

Found position_tick.mp3, converting to ogg..
Converted position_tick.mp3 to position_tick.ogg 

Found record.mp3, converting to ogg..
Converted record.mp3 to record.ogg 

Found skidding.mp3, converting to ogg..
Converted skidding.mp3 to skidding.ogg 

Found suspension.mp3, converting to ogg..
Converted suspension.mp3 to suspension.ogg 

Found tires.mp3, converting to ogg..
Converted tires.mp3 to tires.ogg 


Press Enter to go back...
```

## Installing packs
This catagory contains 2 helpers for installing packs.

### Install pack from packaged
This installs a pack from a packaged .asar file. Designed for the end user to install packs downloaded from others, or the internet (if this even gets that big haha).

**EXAMPLE USAGE**
```

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
        
Path of pack to replace with (type exit to exit) "C:\Users\me\Documents\packs\myawesomepack.asar"
Loading pack..
Changed pack to myawesomepack.asar

Press Enter to go back...
```

### Install pack from unpackaged
This installs a pack from an unpackaged folder. Designed for quick testing.

**EXAMPLE USAGE**
```

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


Path of unpackaged pack (type exit to exit): C:\Users\me\Documents\packs\raw\myawesomepack
Setting pack..

Set pack to myawesomepack

Press Enter to go back...
```

## Utility
This catagory contains 2 overall utility/misc helpers.

### Set path
One of (if not the most) important commands in this entire software! It would simply not work without it. This command lets you set your polytrack folder. This is used to set packs, reset and more!

**EXAMPLE USAGE**
```

 ____       _     ____       _   _     
/ ___|  ___| |_  |  _ \ __ _| |_| |__  
\___ \ / _ \ __| | |_) / _` | __| '_ \ 
 ___) |  __/ |_  |  __/ (_| | |_| | | |
|____/ \___|\__| |_|   \__,_|\__|_| |_|

Please input a path for where your polytrack folder is (type exit to exit): C:\Users\me\Desktop\PolyTrack-v0.6.3-win32-x64

Folder
C:\Users\me\Desktop\PolyTrack-v0.6.3-win32-x64
Set as PolyTrack folder!

Press Enter to go back...
```

### Reset to default
Resets the active pack to the default vanilla one.

**EXAMPLE USAGE**
```
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

Are you SURE you want to reset your selected pack to default (Y/N)? y
Cloning default..
Reset to default pack!

Press Enter to go back...
```

## Developer tips
After some testing, I found out using the 'Fix Sounds' tool isn't the best way to help with sounds being too quiet. Below is a cheatsheet for modifying volume/speed of sounds through code:

(THESE ARE ACCURATE FOR PolyTrack 0.6.3)

**Volume of `click.mp3/ogg`**  
Found in `playUIClick()` in `main.bundle.js` specifically  
`n.gain.value = .0075, t.connect(n), n.connect(this.destinationSfx), t.start(0)`

**Volume and playback rate of `editor_edit.mp3/ogg`**  

Found in `112.bundle.js`, specifically
```
                    const e = (0, i.gn)(this, Ft, "f").getBuffer("editor_edit");
                    if (null != e && null != (0, i.gn)(this, Ft, "f").context && null != (0, i.gn)(this, Ft, "f").destinationSfx) {
                        const t = (0, i.gn)(this, Ft, "f").context.createBufferSource();
                        t.buffer = e, t.playbackRate.value = .7;
                        const n = (0, i.gn)(this, Ft, "f").context.createGain();
                        n.gain.value = .05, t.connect(n), n.connect((0, i.gn)(this, Ft, "f").destinationSfx), t.start(0)
                    }(0, i.GG)(this, Yt, t, "f")

```

**Volume and playback rate of `record.mp3/ogg`**  
Found in `main.bundle.js`, specifically
```
            (0, R.GG)(this, $e, setTimeout((() => {
                const t = e.getBuffer("record");
                if (null != t && null != e.context && null != e.destinationSfx) {
                    const n = e.context.createBufferSource();
                    n.buffer = t, n.playbackRate.value = 1.35;
                    const i = e.context.createGain();
                    i.gain.value = .05, n.connect(i), i.connect(e.destinationSfx), n.start(0)
                }
            }), 600), "f")
```

**Volume and playback rate of `engine.mp3/ogg`**  
Found in `main.bundle.js`, specifically
```
                        const e = (0, l.gn)(this, G, "f").getBuffer("engine");
                        if (null != e && null != (0, l.gn)(this, G, "f").context) {
                            const t = (0, l.gn)(this, G, "f").context.createBufferSource();
                            t.buffer = e, t.loop = !0, t.playbackRate.value = .7;
                            const n = (0, l.gn)(this, G, "f").context.createGain();
                            n.gain.value = 0, t.connect(n), n.connect((0, l.gn)(this, K, "f")), t.start(0, 2 * Math.random()), (0, l.GG)(this, O, {
                                source: t,
                                gain: n
                            }, "f")
                        }
```

**Volume and playback rate of `checkpoint.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                        const e = (0, l.gn)(this, G, "f").getBuffer("checkpoint");
                        if (null != e && null != (0, l.gn)(this, G, "f").context && null != (0, l.gn)(this, G, "f").destinationMaster) {
                            const n = (0, l.gn)(this, G, "f").context.createBufferSource();
                            n.buffer = e, n.playbackRate.value = 1.25;
                            const i = (0, l.gn)(this, G, "f").context.createGain();
                            i.gain.value = .03 * t, n.connect(i), i.connect((0, l.gn)(this, G, "f").destinationMaster), n.start(0)
                        }
```

**Volume and playback rate of `collision.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                        const t = (0, l.gn)(this, G, "f").getBuffer("collision");
                        if (null != t && null != (0, l.gn)(this, G, "f").context) {
                            const n = (0, l.gn)(this, G, "f").context.createBufferSource();
                            n.buffer = t, n.playbackRate.value = .1 + .15 * Math.min(e / 4e3, 1);
                            const i = (0, l.gn)(this, G, "f").context.createGain();
                            i.gain.value = Math.max(.3, Math.min(e / 4e3, 1)) / 2.5, n.connect(i), i.connect((0, l.gn)(this, K, "f")), n.start(0)
                        }
```

**Volume and playback rate of `engine.mp3/ogg`**  
Found in `main.bundle.js`, specifically
```
                       const e = (0, l.gn)(this, G, "f").getBuffer("engine");
                        if (null != e && null != (0, l.gn)(this, G, "f").context) {
                            const t = (0, l.gn)(this, G, "f").context.createBufferSource();
                            t.buffer = e, t.loop = !0, t.playbackRate.value = .7;
                            const n = (0, l.gn)(this, G, "f").context.createGain();
                            n.gain.value = 0, t.connect(n), n.connect((0, l.gn)(this, K, "f")), t.start(0, 2 * Math.random()), (0, l.GG)(this, O, {
                                source: t,
                                gain: n
                            }, "f")
                        }
```

**Volume of `music.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                    const e = this.getBuffer("music");
                    if (null != e && null != this.context && null != this.destinationMaster) {
                        const t = this.context.createBufferSource();
                        t.buffer = e, t.loop = !0;
                        const n = this.context.createGain();
                        n.gain.value = 0, t.connect(n), n.connect(this.destinationMaster), t.start(0), (0, R.GG)(this, y, {
                            source: t,
                            gain: n
                        }, "f")
                    }
```

**Volume of `position_tick.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                                                const e = n.getBuffer("position_tick");
                                                if (null != e && null != n.context && null != n.destinationSfx) {
                                                    const t = n.context.createBufferSource();
                                                    t.buffer = e;
                                                    const i = n.context.createGain();
                                                    i.gain.value = .01, t.connect(i), i.connect(n.destinationSfx), t.start(0)
                                                }
```

**Volume of `skidding.mp3/ogg`**  
Found in `main.bundle.js`, specifically
```
                        const e = (0, l.gn)(this, G, "f").getBuffer("skidding");
                        if (null != e && null != (0, l.gn)(this, G, "f").context) {
                            (0, l.GG)(this, Ie, [], "f");
                            const t = 4;
                            for (let n = 0; n < t; ++n) {
                                const i = (0, l.gn)(this, G, "f").context.createBufferSource();
                                i.buffer = e, i.loop = !0, i.playbackRate.value = .5;
                                const r = (0, l.gn)(this, G, "f").context.createGain();
                                r.gain.value = 0, i.connect(r), r.connect((0, l.gn)(this, q, "f")[n]), i.start(0, n / t * 3.5 + .25 * Math.random()), (0, l.gn)(this, Ie, "f").push({
                                    source: i,
                                    gain: r
                                })
                            }
                        }
```

**Volume and playback rate of `suspension.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                            const e = Math.abs((0, l.gn)(this, te, "f").wheelSuspensionVelocity[t]);
                            if (e > 4 && null != (0, l.gn)(this, G, "f")) {
                                const n = (0, l.gn)(this, G, "f").getBuffer("suspension");
                                if (null != n && null != (0, l.gn)(this, G, "f").context) {
                                    const i = (0, l.gn)(this, G, "f").context.createBufferSource();
                                    i.buffer = n, i.playbackRate.value = .7 + .1 * Math.random();
                                    const r = (0, l.gn)(this, G, "f").context.createGain();
                                    r.gain.value = Math.min(.285, e / 140), i.connect(r), r.connect((0, l.gn)(this, q, "f")[t]), i.start((0, l.gn)(this, G, "f").context.currentTime + .02 * Math.random()), (0, l.gn)(this, V, "f")[t] = .1
                                }
                            }
```

**Volume and playback rate of `tires.mp3/ogg`**  
Found in `main.bundle.js`, specifically

```
                        if (null != e && null != (0, l.gn)(this, G, "f").context) {
                            (0, l.GG)(this, H, [], "f");
                            const t = 4;
                            for (let n = 0; n < t; n++) {
                                const i = (0, l.gn)(this, G, "f").context.createBufferSource();
                                i.buffer = e, i.loop = !0, i.playbackRate.value = .3;
                                const r = (0, l.gn)(this, G, "f").context.createGain();
                                r.gain.value = 0, i.connect(r), r.connect((0, l.gn)(this, q, "f")[n]), i.start(0, n / t * 3.5 + .25 * Math.random()), (0, l.gn)(this, H, "f").push({
                                    source: i,
                                    gain: r
                                })
                            }
                        }
```
