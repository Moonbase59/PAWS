# -*- coding: utf-8 -*-

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                                  <full name of game>                          #
#                Created by <name of author> (c) <copyright year>               #
#                                                                               #
# <description of game>                                                         #
#                                                                               #
# Created by: <name of author>                                                  #
# Created on: <copyright year>                                                   #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#********************************************************************************
#                                 Style Guidelines                              #
#                                                                               #
C="""
  To organize PAWS all the files share the same design conventions. The
  files have been organized into sections to make it easier to navigate
  through them with a text editor.

  The major sections are marked by boxes with borders made of ******'s that
  stretch across the entire page. If you search for #*** you can jump from
  section to section. The sections provide an overview of the entire file.

  Within each section you'll find a set of related classes, objects, and
  functions. If you use the Notepad++ text editor, the Alt-0 keystroke will
  fold the file into its smallest, most easily navigated form. Clicking a +
  to the left of a folded section will allow you to unfold only that
  section. Thus you can keep most of the file folded, seeing only the part
  you're actually interested in. This helps tremendously.

  COLOR CODES

  This source code is best read with a color coding editor, preferably
  Notepad++ using 18 point Lucinda Console font, in 1280x1024 resolution
  (large fonts).

  The following colors were used:

  Grey          - Comments (italics)
  Orange        - Quoted Text (bold)
  Bright Blue   - Python and PAWS keywords (bold)
  Green         - Local Variables (bold)
  Purple        - Operators, parentheses, etc.
  Red           - Numbers
  """

#*******************************************************************************
#                           Import Game Engine & Libraries
#
C="""
  Python doesn't know where any of the other pieces of our game are, so we
  have to tell it. To do this we have to "import" them.

  The two most important pieces are the "game engine" and the "world
  library".

  1. The game engine is the part of the program that does all the "dirty
     work". For instance it asks the player to enter commands and translates
     those commands into verbs and objects for you. It handles saving and
     restoring games, it handles the initial game set up and so forth. The
     game engine is stored in Core.py (source code) and Core.pyc (compiled
     code). Don't change these files! (Unless you REALLY know what you're
     doing! :))

  2. The world library is the part of the program that builds the
     underpinnings of the game universe, it defines what a room is, what an
     actor is, what a door is, and so on. The object library is contained in
     Universe.py (source code) and Universe.pyc (compiled code) Don't change
     these files!

  Since each of these modules is used in its entirity we import everything,
  that is, we import all objects in these files. This is frowned upon in
  "official" Python circles, but it makes writing the game a LOT easier!

  3. To convert a PAWS 2.0 game to run with PAWS 1.5 the two lines below
  need to be changed from:

  from PAWS.Core import *
  from PAWS.Universe import *

  to

  from PAWS import *
  from Universe import *

  That's all there is to it!
  """

from PAWS.Core import *      # Game Engine (already written for you)
from PAWS.Universe import *  # Game World Library (already written for you)

#********************************************************************************
#                               G A M E   D A T A
#
C="""
  This is simple enough. You're the author, your copyright is the year you
  wrote your game (or range of years), and the game's name is what you call
  it.

  The game version should start at version 1.0 and while it's being
  developed you may want to put the word Alpha after it. This means it's an
  "alpha" copy, a work in progress. When you finish it and you want a few
  people to test it, change "Alpha" to "Beta". A beta copy is one that is in
  preliminary testing. Once the game is finished, remove the word "Beta".

  The IntroText is what the player sees just after the game's title and
  copyright notices, but before the first command prompt. It introduces the
  player into your game: why they're there, what the situation is, and
  (perhaps) what they have to do about it.

  If you want to have help for the player (perhaps listing commands unique
  to your game) you may put them in Game.HelpText just after the
  Game.IntroText. When the player clicks Hints on the Help menu or types
  "help" the text will appear.
  """

Game.Author = u"<name of author>"
Game.Copyright = u"<copyright year>"
Game.Name = u"<full name of game>"
Game.Version = u"1.0 Alpha"

Game.IntroText = u"""
                 Put your game introduction here.
                 """

#********************************************************************************
#                  G A M E   S E T U P   /   W R A P U P
#
C="""
  Every game you write has to have a "user set up". This is where you can do
  anything special needed to set up your game. Fortunately, very few games
  need anything unusual in terms of setup, so you can copy the setup from
  one game to another.

  The only thing you have to do is change the name of your setup function,
  and change the StartingLocation to the room the player starts in.

  Like most games, this game doesn't have a post game wrap up, because it's
  generally not needed. If you use it, it's the last chance you have to
  print text on the screen--after the end game wrap up ends the game shuts
  down.

  If you want to copy the wrap up function to another game, remember to
  rename it.
  """

def MyUserSetUpGame():
    Global.Production = FALSE
    P.AP().CurrentActor = Global.Player
    P.CA().StartingLocation = StartingRoom

#--- Hook New Functions To Engine

C="""
  The line below hooks your set up game function to the engine in place of
  the default one. If you don't do that, no set up will take place, since
  the default user setup does nothing--not even put the player in the right
  starting room!

  The original Cloak used a post game wrap up, so there was a second line to
  hook the wrap up game function to the engine. If you don't do that your
  wrap up function won't be called.

  Many games (including this version of Cloak) don't use a wrap up. For
  those games either comment out the second line or delete it entirely (note
  we have no second line!).
  """

Engine.UserSetUpGame = MyUserSetUpGame

#********************************************************************************
#                            R O O M   B L U E P R I N T S
#
C="""
  Python requires every object you create start with a blueprint. Python
  calls that blueprint a "class". The word class comes from the ivory tower
  computer scientists who created the idea of objects in the first place. So
  don't worry about it, just remember "class = blueprint".
  """

class MakeRoom(ClassSmartRoom):
   """
   Just an example of a room blueprint. This one doesn't anything beyond
   what ClassSmartRoom does. Notice it uses "Make" instead of "Class" in
   the room. I think this makes it more intuitive to use.

   For simple games this is probably the only rooom blueprint you'll need.
   """

   def SetMyProperties(self):
        pass

#********************************************************************************
#                         T H I N G   B L U E P R I N T S
#
# As you'd expect, things use blueprints just like rooms do--and for exactly the
# same reason.

class MakeItem(ClassItem):
    """
    This is just an example of a thing blueprint, it's VERY simple, actually
    nothing more than a synonym for ClassItem, but renaming it makes the
    code read more naturally.

    Notice this blueprint has only the word "pass" in it, meaning it doesn't
    define anything new, all the functionality is coming from ClassItem.
    """
    pass

#********************************************************************************
#                           A C T O R   B L U E P R I N T S
#
C="""
  As you'd expect, actors use blueprints just like rooms do--and for exactly
  the same reason. In fact, actors almost always need blueprints because
  actors mimic living creatures--and that's really hard to do.
  """

# <put actor blueprints here>

#********************************************************************************
#                             V E R B   B L U E P R I N T S
#
C="""
  Simple game almost never need new verbs, but if you have verbs that do new
  things (and aren't simply synonyms for the verbs in Universe) put the
  blueprints here.
  """

# <put verb blueprints here>

#********************************************************************************
#                               M A K E   R O O M S
#
C="""
  In this section we finally start MAKING rooms! Up to now we've just been
  drawing blueprints, so to speak. But in this section we make the rooms the
  player will travel through.
  """

StartingRoom = MakeRoom()
StartingRoom.NamePhrase=u"Starting Room"
StartingRoom.SetDesc(u"L",u"""
                         You’re in a room with no exits. So quit looking
                         around and finish writing your game already!
                         """)

#********************************************************************************
#                              M A K E   T H I N G S
#
C="""
  These are the things the player will interact with. But we're actually
  making them here, not just drawing blueprints.
  """

# <put things here>

#********************************************************************************
#                              M A K E   A C T O R S
#
# These are the actors the player will interact with. But we're actually making
# them here, not just drawing blueprints.

# <put actors here>

#********************************************************************************
#                              M A K E   A D V E R B S
#
# Adverbs are seldom used in interactive fiction, but if you need them, define
# them here.

# <put adverbs here>

#********************************************************************************
#                                M A K E   V E R B S
#
C="""
  The only verbs you usually need are synonyms for verbs already defined in
  Universe. Those go here, as well as any verbs you've created blueprints
  for in the section above.
  """

# <put verbs here>

#********************************************************************************
#                                      M A P S
#
C="""
  Maps have to be defined last because Python requires you define things
  before you use them. By putting the maps as the last part of the file
  we're making sure all rooms have already been created.

  Notice only the directions actually used are defined. If you don't define
  a direction PAWS will provide an appropriate complaint.
  """

# <put your maps here>

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                       End Of <game name> Game                                 #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
