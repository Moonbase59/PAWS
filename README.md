PAWS 2.1
========

PAWS stands for **Python Adventure Writing System**. It was originally written by **Roger Plowman**. Essentially it’s a python library which allows you to write your own text adventure games. What I liked about this library is that it has a huge technical document explaining every class and method. On top of that the code is hugely commented and there is an example and tutorial with lots of comment to get you started. In olden times, you could get it from http://home.fuse.net/wolfonenet/PAWS.htm.

The project seems abandonend since about 2008, the web page doesn’t exist anymore and Roger Plowman unreachable. I strongly feel this interesting and well-working system to write and run Interactive Fiction should be kept from vanishing in the dark realms of Nowhereland and it could also benefit from a little polishing and a few extensions, especially for foreign languages like German.

So I went about keeping and improving an already very sophisticated and well-written system and create what I blatantly call PAWS 2.1, while trying to keep it compatible with the olden but golden version 1.5 and 2.0.3 games out there, like the included "Thief’s Quest" (also written by Roger Plowman).

It still requires **Python 2.7** to run, and **wxWidgets** being installed (either the older "unicode"-versions or the newer unicode-only version). [WxPython.org](https://wxpython.org/) even have [installers for Windows & MacOS](https://wxpython.org/download.php#msw).

**May PAWS never die and the Creative Force be with you!**


## Some technical stuff

### PAWS 2.1 does Unicode!

PAWS 2.1 is fully Unicode-aware and will play nicely with all these beautiful characters from almost every language (finally!). For new games, you should therefore specify the source file’s _encoding_ within the first two lines like this (it should always be UTF-8):

````python
# -*- coding: utf-8 -*-
````

Also, each and every string literal in your game should be a Unicode string, like this (notice the lowercase _u_ before the strings):

````python
self.SetDesc(u"Odor", u"All I can smell is fresh air.")
````

### PAWS 2.1 works on Linux, Mac, Windows, …

Yeah, really. Almost on every machine that you can manage to install _Python 2.7_ and _wxPython_ on. And this version even gets all these beautiful Unicode characters right. See the _screenshots_ at the end of this page.

### Playing older games (v1.5/2.0.3)

I very much tried to keep the core and PAWS’ "Universe" compatible with older games, like from version 1.5 and 2.0.3. You’ll probably only have to change the following two lines in those games’ source files:

_Change …_

````python
from PAWS import *
from Universe import *
````

_to …_

````python
from PAWS.Core import *
from PAWS.Universe import *
````

and—in most cases—you should be ready to run! This is how got Roger’s original **Thieves’ Quest** game up and running again. (Which is included in a slightly debugged and Unicode-friendly version.)

### Bugs fixed

I found and tried to repair a lot of bugs, some in the _Core_ and most of them in the _Universe_ module which led to erratic behaviour in the game and lots of error messages on the console. Surely I didn’t find everything (and will probably try to fix more), so all the fault is mine and all the credit should go to _Roger Plowman_.

### Manuals (How to write your own Adventure)

Unfortunately, I couldn’t get hold of Roger’s great manuals for the 2.0.3 version. Sadly, you’ll have to make with the included manuals of version 1.5, and adapt a little here and there. They’re still worth reading, though. If anyone knows about or even _has_ the version 2.0.3 manuals, **please let me know!**

### Other miscellanea on the Internet

* Roger’s original page (seems gone): http://home.fuse.net/wolfonenet/PAWS.htm
* [PAWS Version 2.0.3 on Archive.org’s Wayback Machine](https://web.archive.org/web/20150219103902/http://home.fuse.net/wolfonenet/PAWS.htm). Sadly, no source file ZIPs and manuals.
* [Parsiya’s Malware Adventure](https://github.com/parsiya/malwareadventure). This is where I found the seemingly last v2.0.3 PAWS playing modules, the base of my work with this version.
* [Roger Firth’s »Cloak of Darkness«](http://www.firthworks.com/roger/). A well-defined mini adventure, coded in many different languages (playable PAWS version included here).


## How to play Adventures

Git clone (or download) this repo, change directory to where `LoadTerminal.pyy` lives, and start it, i.e.

```` bash
cd /home/username
git clone https://github.com/Moonbase59/PAWS.git Adventures
cd Adventures
python LoadTerminal.pyy
````

Alternatively, on some Linux DEs like _XFCE_ or _Cinnamon_, you can create a so-called "Desktop Starter" like the following one and simply double-click it’s icon on the Desktop to play.

```` ini
[Desktop Entry]
Version=1.0
Type=Application
Name=PAWS Adventures
Comment=Start a selection of PAWS Adventures
Exec=python LoadTerminal.pyy
Icon=
Path=/home/username/Adventures
Terminal=false
StartupNotify=false
````

To avoid complaints from the desktop environment, you _might_ need to make the newly-created starter executable.

Once started, from PAWS’ terminal window select **File/Pick Game …**, pick a game and play it. Games are all the `*.py` files in the starting directory. This is also why we used the extension `*.pyy` for `LoadTerminal` – it won’t show up in the game file browser.

![Linux](linux.png "Linux Screenshot")   
_Linux Screenshot_

![Windows](windows.png "Windows Screenshot")   
_Windows Screenshot_

**Have fun!**
