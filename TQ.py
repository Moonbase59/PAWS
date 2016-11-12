# -*- coding: utf-8 -*-

#*********************************************************************
#                          Thief's Quest
#                      Roger Plowman (c) 1999-2001
#
# You're a thief, and the wizard who's home you were burgling caught
# you! Can you say "Oops?" We knew you would …
#*********************************************************************


# This version of Thief's Quest is intended both as a fun game and a tool to
# illustrate how to write games with PAWS and Universe. As such it is heavily
# commented, and comes with a complete description in exhaustive detail.  I
# recommend that you play the game BEFORE reading the TQ technical manual,
# otherwise you'll spoil your enjoyment of what really is a very nice game
# (even if I do say so myself!).
#
# Thief's Quest was developed in Python, under Windows 98 but should be binary
# compatible with any Python 1.5.2 interpreter. If not, simply run the source
# code in the interpreter to recompile the pyc's.
#
# The comments are intended for game authors who've never programmed before,
# they may be a bit long-winded for experienced programmers.
#
# One final note: Python is CASE SENSITIVE, which means not only do you have to
# spell everything correctly, you also have to capitalize it correctly! Almost
# all the truly frustrating problems a beginner will have come from problems
# with capitalization.


#               Starting
#    O/S          Date       Language         Computer
#  ======       ========    ==========      =============
#
#  RSTS/E       04/17/78    Basic-Plus      DEC PDP-11/70 (6 Levels)
#  CP/M         08/01/83    S-Basic         Kaypro II     (3 Levels)
#  MS-DOS       11/17/88    ADVSYS          PC/AT         (4 Levels)
#  MS-DOS       09/14/96    Alan            PC/Pentium    (.1 Levels)
#  MS-DOS       09/20/96    Hugo            PC/Pentium    (.1 Levels)
#  MS-DOS       09/27/96    TADS/WorldClass PC/Pentium    (1 Level)
#  Win95/RAVEL  03/31/97    TADS/Universe   PC/Pentium    (1 Level)
#  Win98        07/26/98    PAWS/Universe   PC/Pentium    (10 Levels)*
#
# * Completed!
#
# This adventure is a rewrite of QUEST as found in both the RSTS/E and
# CP/M operating systems.  Unfortunately the CP/M version source code
# was tragically lost to hard disk formatitus with complications of
# non-backupitis.
#
# This version follows the CP/M version more closely than the RSTS/E
# version, but is very different from either. Note the original 3
# versions of the game were called simply "QUEST", it was renamed
# "Thief's Quest" in 1996 to avoid confusion with other IF games
# called Quest.


#=====================================================================
# Color Codes
#
# This source code is best read with a color coding editor, preferably
# ScopeEdit. I developed using the "Lucinda Console" font, in Bold,
# sized at 15 points in 1280x1024 resolution (large fonts).
#
# The following colors were used:
#
# White Background
# ----------------
#
# Black         - Local Variables, symbols, most Verb Classes
# Grey          - Comments
# Orange        - Quoted Text
#
# Light Blue    - Python & PAWS Module names
# Bright Blue   - Python keywords
# Rose          - Python functions/Object Methods
#
# Purple        - PAWS Constants, numbers
# Pink          - PAWS/TQ Object Instances
# Red           - PAWS/TQ Object Methods
# Dark Green    - PAWS/TQ Object Properties
# Brown         - PAWS/TQ Classes (excluding most verb classes)
#
# Color Background
# ~~~~~~~~~~~~~~~~
#
# Black On Pink   - Click to zoom into text "fold". Sort of like
#                   a URL on the web, except it shows you the code
#                   labeled by the fold you clicked.
#
#==================================================================

#==================================================================
# A color-coding editor (like ScopeEdit) also helps you keep the
# capitalization of stuff right. If a word doesn't change color you
# either mis-spelled it or didn't capitalize correctly. This helps,
# A LOT!
#
# The color coding editor I used in the creation of this code is
# called ScopeEdit version 1.8. It's shareware and costs $79.00 U.S.,
# but it's worth every penny for 3 reasons. 1) It color codes your
# game so that spelling and capitalization mistakes are easy to catch
# and 2) it has very good basic editing features. It folows Windows
# conventions very closely. (Sorry, ScopeEdit is Windows only).
#
# And 3) it does text folding (aka code nesting). This lets you create
# an outline of your program, one that you can expand or collapse as
# you need to.
#
# PAWS, Universe, and Thief's Quest have all been written with this
# idea in mind. No single part of the code is more than a screenfull
# long. For instance, even though the Universe library is over 5,000
# lines of code, the collapsed outline (using ScopeEdit) fits on a
# single screen!
#
# This simple yet incredibly powerful feature means that you can
# concentrate on a single part of the program, and not be distracted
# by the rest of it.
#
# I've included the ScopeEdit document "Edit Shell.SE" so you can
# look at PAWS with folding if you own a copy of ScopeEdit. I've also
# included the highlighting file "Python.SEO" so you can see the color
# coding.
#
# To download a demo of ScopeEdit off the Web, go to:
#
#   www.loginov.com
#
# If you like it you can register it online with a credit card and
# download the full version immediately.
#
# By the way, I didn't write ScopeEdit, but it's so good I'm willing
# to plug it!
#
# You might also try Origami Gold, a $20 shareware editor (Windows
# only) which not only supports color-coding (limited to 255 keywords
# alas, and it doesn't highlight text) which also does "folding".
# Origami is much cruder than ScopeEdit, and be warned it has a few
# rough edges, but then it's 1/4 the price of ScopeEdit as well.
#
#===========================================================================


#===============================
# Import game engine & libraries
#===============================


# Python doesn't know where any of the other pieces of our game are, so
# we have to tell it. To do this we have to "import" them.
#
# The two most important pieces are the "game engine" and the "world
# library".

# 1. The game engine is the part of the program that does all the "dirty
#    work". For instance it asks the player to enter commands and
#    translates those commands into verbs and objects for you. It handles
#    saving and restoring games, it handles the initial game set up and so
#    forth. The game engine is stored in PAWS.py (source code) and
#    PAWS.pyc (compiled code). Don't change these files! (Unless you
#    REALLY know what you're doing! :))
#
# 2. The world library is the part of the program that builds the
#    underpinnings of the game universe, it defines what a room is, what
#    an actor is, what a door is, and so on. The object library is
#    contained in Universe.py (source code) and Universe.pyc (compiled
#    code) Don't change these files!
#
# Since each of these modules is used in its entirity we import everything,
# that is, we import all objects in these files. This is frowned upon in
# "official" Python circles, but it makes writing the game a LOT easier!


#from PAWS import *
#from Universe import *
# The ONLY change needed fpr PAWS 2.03:
from PAWS.Core import *
from PAWS.Universe import *


#********************************************************************
#                          G A M E   D A T A
#********************************************************************

# Here we "fill in the blanks" of Game instance.

Game.Author    = u"Roger Plowman, some corrections by Matthias C. Hormann"
Game.Copyright = u"1978–2016"
Game.Name      = u"THIEF’S QUEST - Getting OUT!"
Game.Version   = u"8.1.0 Alpha"


#-----------------------
# Game Introductory Text
#-----------------------


# Python allows you to mark strings with single or double quotes like
# other programming languages you may have used, but it has a new feature
# not available to most: the *TRIPLE* quote.
#
# A triple quote lets you start a string that runs until you end it with
# another triple quote. You can include as many lines of text as you like.
#
# You needn't worry about formatting, either! Since PAWS and Universe
# use the Say() function instead of Python's "print" command PAWS handles
# the formatting.
#
# This means you can make the text attractive in your source code and
# still have it display correctly when the game is played. VERY handy!
#
# Notice how we used the ~n symbol (which causes Say() to line break) in
# combination with the real line breaks? This lets us have the best of
# both worlds, attractive source code and a clear idea of where line
# breaks will occur when the text is said.


Game.IntroText = u"""
~title The story so far … ~l ~n

~i »So, thief, ye want to steal from a wizard, do ye?« ~l ~p

The old bearded wizard pulls up his sleeves and light blazes from his
hands as he begins to make mystic passes through the air. You feel your
body freeze in place as the magic snares you like a fly caught in
treacle. ~p

~i »Let thy punishment fit the crime! Ye wanted to steal from
a wizard? Then, by my beard, so ye SHALL!« ~l ~p

Your eyes begin to water from the flare of light surrounding the wizard’s
hands. It begins to creep up his arms, enveloping his shoulders. Fear
starts to gnaw at your belly. You wonder just exactly what the wizard is
up to … ~p

~i »Ye shall steal from me until ye are sick of it, until ye want nothing
more than a release from thy constant crimes, until ye have no more
larceny left in thy soul! Foul beast, know thy fate is upon thee!« ~l ~p

Unable to close your eyes, the blast blinds you as all manner of colors
explode from the wizard, slamming into you with numbing force. ~p

You cringe instinctively, throwing up your hands to shield your face. ~p

Realizing you’re able to move again you slowly straighten up from your
crouch, looking around warily. Angry wizards tossing spells around tend to
make anybody cringe, especially a thief the wizard caught red handed in his
tower—but wait! You aren’t IN his tower anymore … where are you? ~n
"""


#********************************************************************************
#                               Adverbs
#
# Adverbs modify verbs, words like "quickly", "slowly", "carefully", etc. They are
# recognizable but don't do anything by default, the Action() method of a verb
# has to specifically modify its action.
#********************************************************************************

CarefullyAdverb = ClassAdverb(u"carefully")
CloselyAdverb = ClassAdverb(u"closely")


#***************************************************************************
#                                F U N C T I O N S
#***************************************************************************


#-------------------------------
# Thief's Quest User Set Up Game
#-------------------------------


# This function is essential in any game you write. First, it sets the
# player's character's starting location and second it tells the parser
# who the current actor is before the player types their first command.
#
# When you define this function you also have to tell the Engine to use it
# in place of the PAWS default.
#
# You can probably just copy this function to your own game library and
# rename it from TQUserSetUpGame to MyUserSetUpGame or something, then
# change the starting location to your own game's first room.


def TQUserSetUpGame():
    """Code required for user game set up"""

    #--------------------
    # Is Game Production?
    #--------------------

    # When you create your own game, in your xxUserSetUpGame() function,
    # change Global.Production from FALSE to TRUE when your game is
    # finished. This will disable the Debug verb so players can't
    # cheat by turning on the debugger.

    Global.Production = FALSE


    #------------
    # First Actor
    #------------

    # The parser needs to be told who the current actor is because it
    # doesn't know until the player types in their first command. And the
    # first room is entered before that happens …


    P.AP().CurrentActor = Global.Player


    #-------------------------------------
    # Player Character's Starting Location
    #-------------------------------------

    # In Thief's Quest (and Universe) the player's character is always
    # referred to as P.CA(). The starting location is the first
    # room the player sees when the game starts. In our case it's the
    # Start Cliff, the cliff with the word START carved on it. :)

    P.CA().StartingLocation = StartCliff


    #---------------------------------
    # Ask About Additional Conventions
    #---------------------------------

    Answer = Terminal.Input(u"This game uses additional conventions most IF doesn’t. View them (Y/N)? ")

    if len(Answer)==0: Answer=u"No"

    if string.lower(Answer[0]) == u"y":
        Say(u"""
            ~n Thief’s Quest is a game involving great subtlety—by design. To aid
            you in doing both quick scanning of a scene and detailed analysis TQ
            uses ~b adverbs. ~l Thus to make a cursory examination of an object
            you’d type 'examine rock' or 'x rock'. To really inspect an item with
            a fine tooth comb you might type 'x rock closely' or 'inspect rock
            carefully'. ~p
            Likewise, if you want to be more precise in other commands you might
            say things like 'take rock carefully', 'move east slowly', etc. ~p
            Thief’s Quest involves use of all 5 senses, sight, hearing, taste,
            touch, and smell. To win the game you must use *all* your senses,
            not just your eyes. ~p
            The player’s character has been forced into a
            situation not of their own choosing where nothing is as it seems and
            paranoia is just common sense. Trust nothing, examine everything,
            believe no one … ~p ~m
            """)

#--------------------------------------------------
# Replace Engine's default_UserSetUpGame() function
#--------------------------------------------------

Engine.UserSetUpGame = TQUserSetUpGame



#*************************************************************************
#                   F O U N D A T I O N   C L A S S E S
#*************************************************************************

# The classes in Thief's Quest deal almost exclusively with room
# extensions, letting us have an Outside and a Cavern and a Lit Cavern and
# a Pine Forest and so forth …


#=====================================================================
#                               TQ Room Class
#=====================================================================


# This room is defined simply to make all rooms have a set of universal
# properties in addition to those supplied by Universe. This allows us
# to test properties without worrying about whether they exist or not.
#
# Notice we're also using the Dictionary description service, this
# replaces the normal sensory descriptions in the room with ones from
# the Descriptions dictionary. This means that all TQRooms have
# default sensory description dictionaries.


class ClassTQRoom(ServiceDictDescription,ClassRoom):

    #------------------------
    # Set Class's Default Map
    #------------------------

    # The default map is the complaint given when a player moves in a
    # direction the game author didn't set explicitly in the room map. In this
    # case there is *no* default map.

    DefaultMap = {}


    #------------------
    # Set My Properties
    #------------------

    # Please note that we call all SetMyProperties() methods (one per
    # service used) before the instance properties, but AFTER the base class
    # SetMyProperties. This allows service-defined properties to be defaulted,
    # yet still overridden by the class being defined.

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.HasBeechTree = FALSE
        self.CliffMessageIsVisible = FALSE
        self.HasCliff = FALSE
        self.HasForest = FALSE
        self.HasForestPath = FALSE
        self.HasMound = FALSE
        self.HasPineTree = FALSE
        self.HasStream = FALSE
        self.IsOutside = TRUE


    #-----------------
    # Feel Description
    #-----------------

    # The FeelDesc() method supplied by ServiceDictDescription is inappropriate
    # for rooms, so we override it, basically calling ClassRoom's FeelDesc
    # method.

    def FeelDesc(self): return ClassRoom.FeelDesc(self)


#---------------
# TQ Class Actor
#---------------

# Just like the regular actor, except it has the Alerted property.

class ClassTQActor(ClassActor):

    def SetMyProperties(self):
        self.Alerted = FALSE


#====================================================================
#                               Outside Class
#====================================================================

# This class defines a basic room that has the IsOutside property set
# to TRUE. It's used to handle things like "look at sky", because Sky
# is a floating object who's WHERE() method reports the current
# actor's location when IsOutside is true. Likewise Wall is a
# floating location that reports None when IsOutside is true. (Thus
# "get wall" when outside responds "There's no wall here."

class ClassOutside(ClassTQRoom):
    """Class for a basic outdoors 'room'."""

    #------------
    # Default map
    #------------


    # Ok, this is new. DefaultMap is not a normal (instance) property
    # like IsLit or Map, it's a CLASS property.
    #
    # Instance properties are unique to each instance of a class. For
    # example the IsLit property for Clearing can be different than the
    # property for Deep Cave, even though both were created with ClassRoom.
    #
    # This is because IsLit is an instance property. It's unique each and
    # every instance of a class.
    #
    # DefaultMap, on the other hand is the SAME for EVERY instace created
    # from this class.
    #
    # Say you made a Clearing, and a Forest. Both would share the same
    # default map. You can tell the difference between a Class property and
    # an instance property because an instance property definition inside
    # a class always has the word "self." in front of it, where a class
    # property doesn't.


    DefaultMap = {North:      u"You can’t go that way.",
                  Northeast:  u"You can’t go that way.",
                  East:       u"You can’t go that way.",
                  Southeast:  u"You can’t go that way.",
                  South:      u"You can’t go that way.",
                  Southwest:  u"You can’t go that way.",
                  West:       u"You can’t go that way.",
                  Northwest:  u"You can’t go that way.",
                  Up:         u"There’s nothing climbable here.",
                  Down:       u"There’s no way down.",
                  Upstream:   u"There’s no stream here.",
                  Downstream: u"There’s no stream here.",
                  In:         u"There’s nothing here to enter.",
                  Out:        u"There’s nothing here to exit."}


    def SetMyProperties(self):
        """Sets default instance properties"""
        self.HasWall = FALSE
        self.SetDesc(u"Odor", u"All I can smell is fresh air.")


#===========================================================================
#                               Cavern Class
#===========================================================================

# This is the class for dark caverns. As you can see the default map is
# different, and IsLit is false. (ClassRoom's default is true). The
# DefaultMap also has different messages.

class ClassCavern(ClassTQRoom):
    """Class for a basic cavern 'room'."""


    DefaultMap = {North:      u"There is a wall there.",
                  Northeast:  u"There is a wall there.",
                  East:       u"There is a wall there.",
                  Southeast:  u"There is a wall there.",
                  South:      u"There is a wall there.",
                  Southwest:  u"There is a wall there.",
                  West:       u"There is a wall there.",
                  Northwest:  u"There is a wall there.",
                  Up:         u"Climbing the walls already? Tisk.",
                  Down:       u"The floor is in the way.",
                  Upstream:   u"There’s no stream here.",
                  Downstream: u"There’s no stream here.",
                  In:         u"There’s nothing here to enter.",
                  Out:        u"There’s nothing here to exit."}


    def SetMyProperties(self):
        """Sets default instance properties"""
        self.IsLit = FALSE
        self.IsOutside = FALSE
        self.NamePhrase = u"Cavern"
        self.SetDesc(u"Odor", u"The air is very fresh, but carries no odors.")
        self.SetDesc(u"Sound", u"I can’t hear anything.  The silence is deafening.")
        self.SetDesc(u"Sky", u"The ceiling is the same rock that forms the cave walls.")
        self.SetDesc(u"Ground", u"The floor is rocky and somewhat rough.")
        self.HasWall = TRUE


#=========================================================================
#                               Lit Cavern Class
#=========================================================================

# A cavern that's lit. No other differences from ClassCavern. You might be
# wondering why we bothered creating this class when only a single property
# has changed.
#
# The reason is convenience. There are probably a dozen lit rooms inside
# the caverns, this class lets us define them easily. Since the idea is
# to make writing the game as easy as possible, convenience becomes more
# than a luxury, it becomes a valuable tool.

class ClassLitCavern(ClassCavern):
    """Class for a basic cavern 'room' that has light."""

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.IsLit = TRUE


#===========================================================================
#                              Class Cliff Room
#===========================================================================

# This is just an outside room that's adjacent to one of the cliff's that
# completely enclose the valley. Notice we have a different default map and
# we've set the HasCliff property to true.

class ClassCliffRoom(ClassOutside):
    """Class for an outdoor 'room' alongside the cliff."""


    #------------
    # Default Map
    #------------

    DefaultMap = {North:      u"There is a cliff there.",
                  Northeast:  u"There is a cliff there.",
                  East:       u"There is a cliff there.",
                  Southeast:  u"There is a cliff there.",
                  South:      u"There is a cliff there.",
                  Southwest:  u"There is a cliff there.",
                  West:       u"There is a cliff there.",
                  Northwest:  u"There is a cliff there.",
                  Up:         u"The cliffs are unclimbable.",
                  Down:       u"There’s no way down.",
                  Upstream:   u"There’s no stream here.",
                  Downstream: u"There’s no stream here.",
                  In:         u"There’s nothing here to enter.",
                  Out:        u"There’s nothing here to exit."}


    def SetMyProperties(self):
        """Sets default instance properties"""
        self.HasCliff = TRUE
        self.HasWall = FALSE

        self.SetDesc(u"Ground", u"""
                              The ground is rocky and stony, with liberal
                              amounts of dirt showing. Not at all inviting,
                              but nothing unusual for the base of a cliff.
                              """)

        self.SetDesc(u"Sky", u"""
                           Most of the sky is cut off by the cliffs and the
                           trees, but what you can see is blue with a few
                           fluffy white clounds. Good weather to be OUT of
                           this valley, hmm?
                           """)


#===========================================================================
#                               Valley Wall Class
#===========================================================================

# This class is an "abstract" one, in other words, it's not intended that
# any objects be created from it, it's only purpose is to become the parent
# of other classes. Not only does it save you coding effort, it also conserves
# memory, always a desirable goal.

class ClassValleyWall(ClassCliffRoom):


    #------------
    # Default Map
    #------------

    DefaultMap = {North:      u"There is a cliff there.",
                  Northeast:  u"There is a cliff there.",
                  East:       u"There is a cliff there.",
                  Southeast:  u"There is a cliff there.",
                  South:      u"There is a cliff there.",
                  Southwest:  u"There is a cliff there.",
                  West:       u"There is a cliff there.",
                  Northwest:  u"There is a cliff there.",
                  Up:         u"The cliffs are unclimbable.",
                  Down:       u"Not without mining tools, friend.",
                  Upstream:   u"There’s no stream here.",
                  Downstream: u"There’s no stream here.",
                  In:         u"There’s nothing here to enter.",
                  Out:        u"There’s nothing here to exit."}


    def SetMyProperties(self):
        """Sets default instance properties"""
        self.SetDesc(u"Odor", u"The air carries the sharp reek of dust.")
        self.SetDesc(u"Sound", u"You can hear the wind whispering around the cliff tops.")


#===========================================================================
#                           North Valley Wall Class
#===========================================================================

class ClassNorthValleyWall(ClassValleyWall):

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.NamePhrase = u"North Valley Wall"

        self.SetDesc(u"L", u"""
                         You are standing before the north wall of the valley.
                         Behind you (to the south) the forest stands silent and
                         dim. The valley walls stretch out of sight to either
                         side.
                         """)


#===========================================================================
#                              South Valley Wall Class
#===========================================================================

# This class is an "abstract" one, in other words, it's not intended that
# any objects be created from it, it's only purpose is to become the parent
# of other classes.
#
# Abstract classes can be handy if you have two classes that share a great
# many properties and/or methods, but need unique properties of their own.
#
# Not only does it save you coding effort, it also conserves memory, always
# a desirable goal.

class ClassSouthValleyWall(ClassValleyWall):

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.NamePhrase = u"South Valley Wall"

        self.SetDesc(u"L", u"""
                         You are standing before the south wall of the valley.
                         Behind you (to the north) the forest stands silent and
                         dim. The valley walls stretch out of sight to either
                         side.
                         """)


#===========================================================================
#                                Forest Class
#===========================================================================

# This is deep trackless pine forest, a sort of maze without walls. There
# are a great many rooms of this class, and it's also used to create a sub
# class called ClassForestPath.

class ClassForest(ClassOutside):
    """Class for forests."""


    DefaultMap = {North:      u"The trees are too close together in that direction.",
                  Northeast:  u"The trees are too close together in that direction.",
                  East:       u"The trees are too close together in that direction.",
                  Southeast:  u"The trees are too close together in that direction.",
                  South:      u"The trees are too close together in that direction.",
                  Southwest:  u"The trees are too close together in that direction.",
                  West:       u"The trees are too close together in that direction.",
                  Northwest:  u"The trees are too close together in that direction.",
                  Up:         u"There are no climbable trees here.",
                  Down:       u"There’s no passage into the ground. Sorry.",
                  Upstream:   u"There’s no stream here.",
                  Downstream: u"There’s no stream here.",
                  In:         u"There’s nothing here to enter.",
                  Out:        u"There’s nothing here to exit."}

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.HasForest = TRUE
        self.HasPineTree = TRUE
        self.HasGround = FALSE
        self.NamePhrase = u"Deep In Forest"

        self.SetDesc(u"L", u"""
                         You are standing in the middle of trackless pine
                         forest. Trees stretch in all directions around you,
                         out of sight. There are no paths.
                         """)

        self.SetDesc(u"Odor", u"""
                            The air smells pleasantly of pine trees and just a
                            hint of dampness.
                            """)

        self.SetDesc(u"Sound", u"""
                             There is no sound. The forest is completely
                             silent.
                             """)

        self.SetDesc(u"Ground", u"""
                              A thick coating of pine needles covers the ground
                              and deadens your footfalls. That might be one
                              reason the forest is so quiet.
                              """)

        self.SetDesc(u"Sky", u"""
                           The trees grow so thickly you can’t see the sky.
                           The light that manages to filter through the trees
                           is dim, like twilight.
                           """)



#===========================================================================
#                                 Forest Path Class
#===========================================================================

# This class defines all rooms that contain the forest path. This allows
# us to define the path as a floating object, like the pine tree. It
# also gives us a couple of ways to let the wolf wander the forest without
# appearing on the path. (The forest path is magical, it bars the wolf).


class ClassForestPath(ClassForest):
    """Class for forest path."""

    def SetMyProperties(self):
        """Sets default instance properties"""
        self.HasForestPath = TRUE




#***************************************************************************
#                R O O M S    ( L E V E L   0 - S u r f a c e )
#***************************************************************************


# Rooms are places for the player to visit. Unlike most of what we've seen
# so far, instantiation plays a larger role in distinguishing rooms,
# especially maps.
#
# Rooms are first arranged by level (dungeon level), and within level
# alphabetically by name. The one exception is that the room StartCliff
# (the starting location) is defined first, to make it easy to find.
#
# It doesn't matter what order you define your rooms in, but we have so
# many in Thief's Quest we chose this method to make rooms easier to find.



#===========================================================================
#                           Starting Cliff (Room #1)
#===========================================================================

# This is the first room the player will see. The game takes place in a
# valley completely surrounded by unclimbable cliffs. This gives a logical
# reason for the player not to be able to leave the valley.
#
# Note the use of a {} expression in the SetDesc("Sound" …) method (the
# last one defined for this object).

StartCliff = ClassCliffRoom()

StartCliff.CliffMessageIsVisible = TRUE
StartCliff.HasForestPath = TRUE
StartCliff.HasGround = FALSE
StartCliff.HasPineTree = TRUE
StartCliff.NamePhrase = u"At ›Start‹"

StartCliff.SetDesc(u"L", u"""
                       You are standing in a small clearing in a pine forest.
                       Behind you (to the west) is a cliff stretching upward
                       at least two thousand feet. About a third of the way up
                       you can plainly see the word »Start« carved in letters
                       fifty feet high.  The cliff is slightly hollowed out
                       so that it seems to menace you like a crashing wave of
                       granite.  To the north and south you can see trackless
                       pine forest. To the east a faint trail leads away from
                       the cliff and deeper into the forest.
                       """)

StartCliff.SetDesc(u"Odor", u"There’s a faint whiff of pine needles.")

StartCliff.SetDesc(u"Sound", u"""
                           {SCase(You())} can hear the wind sighing
                           faintly in the trees.
                           """)

StartCliff.SetDesc(u"Ground", u"""
                            A thick coating of pine needles covers the ground
                            and deadens your footfalls. That might be one
                            reason the forest is so quiet.
                            """)


#===========================================================================
#                            A 3 Way Path (Room #8)
#===========================================================================

# An easy room, however there's a subtle twist. To get here you travel
# south from the 4 way intersection, but to get back there you have to go
# *west* …
#
# As everyone knows forest paths are never straight …

A3WayPath = ClassForestPath()

A3WayPath.NamePhrase = u"A 3 Way Intersection"

A3WayPath.SetDesc(u"L", u"""
                      You are in the middle of a fork in the path.  A faint
                      trail leads east and upward, the path you are on
                      continues south, and back toward the west.
                      """)



#===========================================================================
#                       A 3 Way Path 2 (Room #15)
#===========================================================================

# Just another T in the path.

A3WayPath2 = ClassForestPath()

A3WayPath2.NamePhrase = u"A 3 Way Intersection"

A3WayPath2.SetDesc(u"L", u"""
                       You are on an east/west forest path at the point where
                       it joins a path going south. To the east you can see
                       light, as though the forest were ending.
                       """)


#===========================================================================
#                             A 4 Way Path (Room #4)
#===========================================================================

# This is the crossing of the two major paths in the forest. Notice we have
# to define a new a new class since the SoundDesc() method is no longer
# simply reading text from the Descriptions dictionary.

class ClassA4WayPath(ClassForestPath):

    #------------------
    # Sound Description
    #------------------

    def SoundDesc(self):

        #----------------------
        # Store Possible Sounds
        #----------------------

        # Silence holds the sound description when the dryad isn't at the maple
        # stand, Singing holds the sound description if she is.

        Silence = u"You hear nothing. The silence is deafening."

        Singing = u"""
                  From the north you can hear what sounds like a woman singing.
                  It’s very faint, and might be nothing but a trick of the
                  wind.
                  """

        #-------------------------
        # Is Dryad at maple stand?
        #-------------------------

        if Dryad.Where() == MapleStand:
            return Singing
        else:
            return Silence



A4WayPath = ClassA4WayPath()

A4WayPath.NamePhrase = u"Crossroads"

A4WayPath.SetDesc(u"L", u"""
                      You are standing on the forest path. The path continues
                      east here but another path crosses your path at this
                      point, leading north and south. The air is cool and
                      fragrant with pine scent.
                      """)


#===========================================================================
#                                Beech Copse (Room #10)
#===========================================================================

# Nothing special here, but it does contain the only tree in the whole
# forest the player can climb. If they dare …

BeechCopse = ClassOutside()

BeechCopse.HasBeechTree = TRUE
BeechCopse.HasForestPath = TRUE
BeechCopse.NamePhrase = u"Beech Copse"

BeechCopse.SetDesc(u"L", u"""
                       You are in a copse of beech trees. Unlike most of the
                       pine forest that you’ve seen, these trees are more
                       widely spread, allowing more light to penetrate. Their
                       limbs start close to the ground, some not more than five
                       feet up. Under the trees are years of accumulated fallen
                       leaves, making a rich mulch. The only path out of the
                       copse leads to the northwest.
                       """)

BeechCopse.SetDesc(u"Odor", u"You can smell the faint but sharp odor of leaf mulch.")
BeechCopse.SetDesc(u"Sound", u"The air is cheerful with birdsong.")

BeechCopse.SetDesc(u"Sky", u"""
                         Even though the trees are more widely spread, their
                         canopy blocks out the sky.
                         """)

BeechCopse.SetDesc(u"Ground", u"""
                            The leaf mulch is damp, indicating it must trap a lot
                            of rainfall.
                            """)


#===========================================================================
#                            Birch Grove (Room #16)
#===========================================================================

# The birch grove is an important place. It can heal the player, raise his
# level (making him tougher and a better fighter), it can neutralize venom
# from various monsters.


BirchGrove = ClassOutside()
BirchGrove.NamePhrase = u"Birch Grove"

BirchGrove.SetDesc(u"L", u"""
                       You are in a grove of silvery birch trees. The air here
                       is filled with birdsong, and the grove is bright with
                       afternoon sunlight.  This grove fills you with a sense
                       of peace and tranquility.  Here, you sense, you are
                       safe. This would be a good place to rest.  The only path
                       exits the grove to the northwest.
                       """)

BirchGrove.SetDesc(u"Odor", u"""
                          You can smell a faint tartness in the air, like rare
                          perfume.
                          """)

BirchGrove.SetDesc(u"Sound", u"""
                           You hear birdsong of surpassing loveliness. Tears
                           spring to your eyes, you feel like bursting into
                           song yourself.
                           """)

BirchGrove.SetDesc(u"Sky", u"""
                         This is the only part of the forest that lets you catch
                         even a glimpse of the sky. You can see bits of blue and
                         white through the tree tops. It isn’t much, but it
                         lifts your spirits enormously.
                         """)

BirchGrove.SetDesc(u"Ground", u"""
                            Unlike other parts of the forest, the leaves here
                            are quite dry, in fact, they collect in piles that
                            would make ideal sleeping as long as it didn’t rain.
                            """)


#===========================================================================
#                            Bottom Of Cliff (Room #36)
#===========================================================================

# An open invitation to a few hours of restful rock climbing …

BottomOfCliff = ClassCliffRoom()

BottomOfCliff.HasMound = TRUE
BottomOfCliff.NamePhrase = u"Bottom Of Cliff"

BottomOfCliff.SetDesc(u"L", u"""
                          You are standing between the mound and the eastern
                          cliff. To the west a hole leads into the mound. To
                          the north you can see forest, to the south the
                          valley wall stretches out of sight. The cliff here
                          looks climbable.
                          """)

BottomOfCliff.SetDesc(u"Sound", u"You can hear the wind roaring above you.")


#===========================================================================
#                            Brenin (Room #9)
#===========================================================================

# Brenin is the huge oak tree that serves as a landmark and it's where the
# druid hangs out.

Brenin = ClassOutside()

Brenin.HasCliff = TRUE
Brenin.NamePhrase = u"Brenin"
Brenin.NoExit = u"The valley wall bars further progress in that direction."

Brenin.SetDesc(u"L", u"""
                   You are standing under an incredible tree. It rears above
                   you, at least five hundred feet tall. Its branches start
                   fifty feet from the ground and stretch a hundred feet from
                   trunk to tip. Laying around the base of the tree are acorns
                   the size of apples. Mistletoe hangs in great bunches from
                   the tree’s massive trunk. The valley wall rises to the
                   west. The only trail exits to the south.
                   """)

Brenin.SetDesc(u"Odor", u"The very air is redolent with the smell of ancient days.")
Brenin.SetDesc(u"Sound", u"You can hear animals moving around in the tree branches.")


#===========================================================================
#                              Clearing (Room #20)
#===========================================================================

# The front porch to the hermit's cave.

Clearing = ClassOutside()

Clearing.HasMound = TRUE
Clearing.HasStream = TRUE
Clearing.NamePhrase = u"Clearing"

Clearing.SetDesc(u"L", u"""
                     You are standing in a clearing before a mound. There is a
                     small pool of clear water here, fed by a tiny stream. The
                     stream tinkles merrily over its bed. To the north and south
                     the forest broods menacingly. To the west is a tall hill with
                     a path leading upwards the summit. To the east is what appears
                     to be a massive mound of rock, easily fifty feet high and
                     hundreds of feet long. It appears that if you really wanted
                     to you could reach the top, although it would be a hard climb.
                     In the face of the mound is a large opening, it appears to be
                     a cavern. Somehow, although it sounds silly, you feel as
                     though you have returned home.
                     """)

Clearing.SetDesc(u"Odor", u"""
                        Now that you concentrate you can smell the faintest whiff
                        of freshly baked cookies!
                        """)

Clearing.SetDesc(u"Sound", u"You can hear the stream tinkling over its bed.")


#===========================================================================
#                                 Deep Forest
#===========================================================================

# This is the first of many deep forest rooms (there are about 8). They
# form a maze of sorts, without walls and without making the player feel
#  they're in a maze. Notice how we use the "forest" room to define them?
#
# Only the maps (defined after all rooms) are different.

DeepForest =  ClassForest()     # Room 2
DeepForest2 = ClassForest()     # Room 3
DeepForest3 = ClassForest()     # Room 18
DeepForest4 = ClassForest()     # Room 21
DeepForest5 = ClassForest()     # Room 27
DeepForest6 = ClassForest()     # Room 28
DeepForest7 = ClassForest()     # Room 34


#===========================================================================
#                            Dungeon Entrance (Room 22)
#===========================================================================

# The dungeon entrance is part of an elaborate hoax. Study the room
# carefully. Notice anything unusual? Hint, the Enter direction is *NOT*
# a room, it's a door …

DungeonEntrance = ClassOutside()
DungeonEntrance.NamePhrase = u"Sandy Depression"
DungeonEntrance.Value = 5

DungeonEntrance.SetDesc(u"L", u"""
                            You are standing in a sandy depression about fifty feet in
                            diameter. In the center of this shallow pit you can see a cement
                            cube about 8 feet on a side. On the north wall of the cube is a
                            massive steel door. On the door is a weathered note stencilled in
                            peeling orange paint. By the door is a peg.
                            """)

DungeonEntrance.SetDesc(u"Odor", u"You smell hot metal and dust.")
DungeonEntrance.SetDesc(u"Sound", u"You can hear a faint sound behind the door.")


#===========================================================================
#                            East Ledge (Room #38)
#===========================================================================

# The ledge provides a tease to make the player think it might be a way out.

EastLedge = ClassCliffRoom()
EastLedge.NamePhrase = u"East Ledge"

EastLedge.NoExit = u"""
                   Considering the fact that you’re about two hundred feet above the ground I
                   really would reconsider.
                   """

EastLedge.SetDesc(u"L", u"""
                      You have managed to reach a broad ledge and are now resting with your back
                      against the cliff, looking westward across the length of the valley.  No
                      other ledges are available around you, although you can try to continue
                      your climb.
                      """)

EastLedge.SetDesc(u"Sound", u"Just the wind moaning mournfully. Suits your mood perfectly.")
EastLedge.SetDesc(u"Odor", u"Nothing in particular assaults your olfactory sense at the moment.")


#===========================================================================
#                            Forest Cave (Room #26)
#===========================================================================

# A small taste of caving …

ForestCave = ClassLitCavern()
ForestCave.NamePhrase = u"Cave"
ForestCave.NoExit = u"The cave walls have no openings."

ForestCave.SetDesc(u"L", u"""
                       You are in a small cave just below the forest floor. The walls are
                       rough.  Above you light streams into the cave from the hole in the
                       cave’s ceiling.
                       """)

ForestCave.SetDesc(u"Odor", u"You can smell long ages of decayed leaves and damp mustiness.")

ForestCave.SetDesc(u"Sound", u"""
                           You can hear the wind whistling across the cave’s entrance, making
                           an eerie, haunting melody.
                           """)


#===========================================================================
#                        Forest With Cave (Room #25)
#===========================================================================

# Just a trick to get the player's hopes up …

ForestWithCave = ClassForest()
ForestWithCave.NamePhrase = u"Rocky Forest"

ForestWithCave.SetDesc(u"L", u"""
                           You are standing in an area of the forest that is much rougher than
                           other parts. Outcroppings of rough grey rock abound. At your feet
                           is a dark hole about three feet across. Peering into it reveals
                           only darkness. There are no paths in this part of the forest,
                           indeed movement in any direction will be difficult because of the
                           rocks.
                           """)

ForestWithCave.SetDesc(u"Sound", u"You can hear a faint but spine chilling whistling noise.")


#===========================================================================
#                     Further up a tree (Room #13)
#===========================================================================

# The player's climbed the beech tree to the second level.

FurtherUpATree = ClassOutside()
FurtherUpATree.HasBeechTree = TRUE
FurtherUpATree.NamePhrase = u"Further Up A Tree"

FurtherUpATree.NoExit = u"""
                        Considering the fact that you’re about forty feet above the ground I
                        really would reconsider.
                        """

FurtherUpATree.SetDesc(u"L", u"""
                           You are further up a beech tree. The trunk here is thinner, but
                           the foliage is even thicker. Each time you move the tree sways
                           alarmingly under your weight. You should seriously consider
                           climbing down now. I really don’t recommend trying to climb any
                           further.
                           """)

FurtherUpATree.SetDesc(u"Sound", u"""
                               You can still hear birds chirping, and the wind in the leaves,
                               but there’s also another sound, coming from the trunk, a sort
                               of creaking noise, it’s especially loud if you make a sudden
                               movement, and then you can also hear a kind of popping sound.
                               """)


#===========================================================================
#                            Gypsum Cave (Room #31)
#===========================================================================

# We want a cavern with light, so we use the Lit_Cavern class. If you scroll
# down to the map for the Gypsum cave you'll see only two

GypsumCave = ClassLitCavern()
GypsumCave.NamePhrase = u"Gypsum Cave"

GypsumCave.SetDesc(u"L", u"""
                       The walls of this cavern are coated with white crystals that reflect
                       the sunlight in brilliant flashes of light. The cave extends a long
                       way north and south, but there is only one opening, a dark passage on
                       the east wall burrowing deeper into the mound. The floor is covered
                       with white powder, which you are careful not to disturb as you crunch
                       around the cavern, exploring. On the west wall is an opening leading
                       back to the clearing.
                       """)

GypsumCave.SetDesc(u"Odor", u"The air reeks with the sour smell of gypsum.")


#===========================================================================
#                         Gypsum Passage (Room #32)
#===========================================================================

# Here's the first example of a real cave.

GypsumPassage = ClassCavern()
GypsumPassage.NamePhrase = u"Y Intersection"

GypsumPassage.SetDesc(u"L", u"""
                          You are in a rough Y intersection of passages, one running northeast,
                          one south, and one west.
                          """)

GypsumPassage.SetDesc(u"Odor", u"""
                             The gypsum odor here is noticable, but not nearly as strong as in
                             the main cave.
                             """)


#===========================================================================
#                            Hermit Cave (Room #33)
#===========================================================================

# This is where the player's hoard is located (along with a handy hermit accountant!)

HermitCave = ClassLitCavern()
HermitCave.NamePhrase = u"Egg-shaped Cavern"

HermitCave.SetDesc(u"L", u"""
                       You are in a large round cavern. The exit is on the south wall. In the
                       middle of the room is a small pool of water. The walls of this cavern
                       are smooth and the whole thing reminds you of an egg. In the ceiling are
                       a couple of small holes, enough to give a dim twilight gloom. Although
                       you are somewhat impressed with the way a single beam of light from the
                       ceiling causes the pool of water to shimmer eerily.
                       """)


#===========================================================================
#                                Hill (Room #17)
#===========================================================================

# Possibly this is the first open area the player's found in the gloom of
# the forest. It offers a fair vantage point for some of the surrounding
#  forest.

Hill = ClassOutside()
Hill.NamePhrase = u"Hill"

Hill.SetDesc(u"L", u"""
                 You are standing on the top of a hill. Around you long grass waves slowly in
                 the gentle wind. Behind you (to the west) the path disappears into the pine
                 forest. To the north and south the forest stretches below you to the distant
                 valley walls. Below you to the east is a clearing with a pool of water.
                 """)

Hill.SetDesc(u"Sound", u"""
                     You can hear water tinkling faintly in the stream that feeds the pool
                     below you.
                     """)


#===========================================================================
#                                Maple Stand (Room #6)
#===========================================================================

# Like many of the non-forest rooms this one has most of its properties
# defined directly.

MapleStand = ClassOutside()
MapleStand.HasForestPath = TRUE
MapleStand.NamePhrase = u"Maple Stand"

MapleStand.SetDesc(u"L", u"""
                       You are in a stand of maple trees.  Although it was early spring when
                       you were transported to the valley, these trees are showing fall
                       colors. A path exits to the south.
                       """)

MapleStand.SetDesc(u"Odor", u"""
                          You can smell damp leaves.  The air is cool like fall and a
                          crispness tickles your nose.
                          """)

MapleStand.SetDesc(u"Sound", u"You can hear the sound of crickets chirping.")


#===========================================================================
#                               North Valley Walls
#===========================================================================

# Like the deep Forest there are several (5) North walls, all pretty much
# the same.

NorthWall1 = ClassNorthValleyWall()     # Room 7
NorthWall2 = ClassNorthValleyWall()     # Room 19
NorthWall3 = ClassNorthValleyWall()     # Room 23
NorthWall4 = ClassNorthValleyWall()     # Room 24
NorthWall5 = ClassNorthValleyWall()     # Room 35


#===========================================================================
#                            Northern Path (Room #5)
#===========================================================================

# This leads to the maple-stand from the 4 way intersection (crossroads). Note we define it as
# a class because it has a complex SoundDesc() method that the Dictionary Descriptions service
# can't deal with. Notice also the LDesc method DOES use the service. This illustrates that you
# can mix and match sensory methods as needed.

class ClassNorthPath(ClassForestPath):


    #----------
    # SoundDesc
    #----------

    def SoundDesc(self):
        """Returns string description of sound in room"""

        #--------------
        # Record Sounds
        #--------------

        # Silence holds the sound description when the dryad isn't at the maple
        # stand, Singing holds the sound description if she is.

        Silence = u"You hear nothing. The silence is deafening."

        Singing = u"""
                  From the north you can hear a woman singing. Her voice is a golden harp that
                  sets your imagination soaring. But there’s also something about it that makes
                  you uneasy. Try as you might you simply can’t put your finger on it. Although
                  the words come to you plainly the language is strange, one like you’ve never
                  heard before, nor imagined would come from a human throat.
                  """

        #-------------------------
        # Is Dryad at maple stand?
        #-------------------------

        if Dryad.Where() == MapleStand:
            return Singing
        else:
            return Silence

NorthPath = ClassNorthPath()
NorthPath.NamePhrase = u"Northern Path"

NorthPath.SetDesc(u"L", u"""
                      You are on the northern path.  The forest around you is dim and cool. The
                      path runs north to south. To either side the trees press closely, as
                      though guarding against your intrusion.
                      """)


#===========================================================================
#                               South Valley Walls
#===========================================================================

# The south wall is shorter, but pretty much like the north wall.

SouthWall1 = ClassSouthValleyWall()     # Room 11
SouthWall2 = ClassSouthValleyWall()     # Room 29
SouthWall3 = ClassSouthValleyWall()     # Room 37


#===========================================================================
#                        Top East Ledge (Room #39)
#===========================================================================

# The view is nice … and provides some landmarks to orient the player. As an added bonus
# the room's worth 2 points.

TopEastLedge = ClassCliffRoom()
TopEastLedge.CliffMessageIsVisible = TRUE
TopEastLedge.NamePhrase = u"Top Ledge"

TopEastLedge.NoExit = u"""
                      Considering the fact that you’re about five hundred feet above the
                      ground I really would reconsider.
                      """

TopEastLedge.Value = 2

TopEastLedge.SetDesc(u"L", u"""
                          You have reached the topmost ledge on the eastern valley wall.
                          Above you the cliff bulges outward, preventing further climbing.
                          Cursing in frustrated disappointment you rest your back against the
                          narrow ledge and catch your breath. From this vantage point you can
                          see the entire valley. Far to the west you can make out the word
                          ›Start‹ carved on the west valley wall, where you entered this
                          cursed valley. In the southwestern corner of the valley you can
                          see a gigantic oak tree, half the height of the cliffs surrounding
                          the valley. The tree towers over the surrounding pine forest as
                          though it were the only tree in a field of dark green grass. Far
                          below, you can make out the pool in the clearing before the mound.
                          From this vantage point the mound looks almost like a fat snake.
                          Content to rest for a while, you close your eyes and contemplate
                          the nasty curses magicians lay on thieves like yourself.
                          """)

TopEastLedge.SetDesc(u"Odor", u"You smell nothing in the chill wind.")

TopEastLedge.SetDesc(u"Sound", u"""
                             You can hear nothing but the ever present wind as it roars past
                             like some ethereal waterfall.
                             """)


#===========================================================================
#                        Top Of The Mound (Room #30)
#===========================================================================

# The mound is a good vantage point, and worth a single point for scoring.

TopOfMound = ClassOutside()
TopOfMound.NamePhrase = u"Top Of Mound"
TopOfMound.Value = 1

TopOfMound.SetDesc(u"L", u"""
                       You are standing on top of the massive mound of rock. This vantage
                       point gives you a reasonable overview of the valley. To the east you
                       can see the east valley wall, and a set of ledges extending upward.
                       Cracks appear to connect the ledges, perhaps providing a way out. To
                       the north and south the forest stretches unbroken to the valley
                       walls. To the northwest of the clearing you can make out a break
                       in the trees, although no details are visible at this distance.
                       """)

TopOfMound.SetDesc(u"Odor", u"""
                          Now that you concentrate you can smell the faintest whiff of
                          freshly baked cookies!
                          """)

TopOfMound.SetDesc(u"Sound", u"""
                           You can hear water tinkling faintly in the stream that feeds the
                           pool below you.
                           """)


#===========================================================================
#                            Tree Top (Room #14)
#===========================================================================

# The player's at the top of the beech tree now. We also give him 5 points
# for discovering the place.

TreeTop = ClassOutside()
TreeTop.HasBeechTree = TRUE
TreeTop.CliffMessageIsVisible = TRUE
TreeTop.NamePhrase = u"Tree Top"

TreeTop.NoExit = u"That first step’s a looooong way down.  Why don’t you climb down first?"

TreeTop.Value = 5

TreeTop.SetDesc(u"L", u"""
                     You are nestled (very carefully) in the top of a beech tree. The trunk
                     is less than a foot thick at this point, and the tree lurches violently
                     with even your slightest movement. The wind is quite strong here,
                     plucking boldly at your clothes. Aside from that, you’re pretty safe.
                     And the view is terrific, from this lofty perch you can see the entire
                     valley. To the south, very near, you can see the valley wall. To the
                     west, not too far away, you can see a tremendously tall oak tree, the
                     biggest one you’ve ever seen. To the north the pine forest stretches
                     all the way to the north valley wall, with only one small break that
                     might be a clearing. To the northwest you can see the word "Start"
                     engraved on the west valley wall, where you entered this nightmare.
                     You curse your greed again, and promise yourself that no matter how
                     tempting, you’ll never steal from another wizard as long as you live.
                     To the northeast you can see a bare hill top and near it the glint of
                     open water. Staring intently you can make out what look like ledges on
                     the east valley wall. A way out, perhaps?
                     """)

TreeTop.SetDesc(u"Odor", u"""
                       The wind brings you an unsettling series of smells, pine fragrance,
                       the smell of dust, damp leaves, the foul odor of rotting flesh, and
                       many others. You shiver as you realize this vale is enchanted, and
                       might well harbor magical beasts. What horrors are you likely to
                       encounter in this unnatural place?
                       """)

TreeTop.SetDesc(u"Sound", u"""
                        You can hear the wind roaring through the tree tops. It’s loud enough
                        to drown out all other noises. Your perch sways gently as the wind
                        roars past.
                        """)


#===========================================================================
#                                Up A Tree (Room #12)
#===========================================================================

# The first level of the tree being climbed in the beech copse.

UpATree = ClassOutside()
UpATree.HasBeechTree = TRUE
UpATree.NamePhrase = u"Up A Tree"
UpATree.NoExit = u"You can’t go that way.  You’re in a tree, remember?"

UpATree.SetDesc(u"L", u"""
                    You are in the lower branches of a beech tree. The thick foliage blocks
                    out your vision in all directions. The trunk here is quite thick and
                    sturdy. In fact, your present perch is quite comfortable.
                    """)

UpATree.SetDesc(u"Sound", u"""
                        You can hear birds chirping and the wind whispering through the leaves.
                        It’s quite a soothing sound, almost enough to make you want to go to
                        sleep.
                        """)


#*********************************************************************
#                              T H I N G S
#*********************************************************************

# Things, like rooms, are actually objects in the programming sense.
# They are either tools, treasures, or scenery. These objects are ones
# the player will interact with directly.
#
# A tree, an acorn, a person, a sword, a ring—these are all things.



#====================================================================
#                                   Druid's Robe
#====================================================================

# The druid's robe is scenery, it doesn't appear in room descriptions.
# The other interesting thing about it is the Location property, the
# robe returns the Druid's location (which, since the player will
# never get their hands on it is natural enough).

class ClassRobe(ClassScenery):
    def Where(self): return Druid.Where()

Robe = ClassRobe(u"robe", u"brown,man’s,man's,his,druid’s,druid's")
Robe.StartingLocation = Brenin

Robe.SetDesc(u"Feel", u"""
                    He doesn’t look as though he’d appreciate your
                    pawing his robe.
                    """)

Robe.SetDesc(u"L", u"""
                 It looks to be brown homespun, something a monk would
                 wear. Not very valuable at all. It has long flowing
                 sleeves and a cowl. In some ways (except for the
                 color, material, and cowl) it reminds you of the
                 robe the wizard was wearing when he caught you.
                 """)

Robe.SetDesc(u"Odor", u"Any odor the robe might have is overwhelmed by his own pungent odor.")

Robe.SetDesc(u"Taste", u"""
                     Do you really feel like licking odorous homespun?
                     I sure don’t!
                     """)


#=====================================================================
#                                   Druid
#=====================================================================

# The druid is another cameo actor, and a non-combatant.  If spoken to
# he will give the player the mandala and instructions on its use. He
# then disappears forever.

class ClassDruid(ClassTQActor):
    """Druid Cameo Actor"""

    #------
    # ADesc
    #------

    def ADesc(self): return u"him"

    #-----------
    # FeelDesc()
    #-----------

    def FeelDesc(self):
        return u"""
               He doesn’t look as though he’d appreciate your pawing
               him.
               """

    #-----------
    # HereDesc()
    #-----------

    def HereDesc(self):
        return u"""
               A robed man stands observing you. A cowl hides his
               face. His hands are hidden in the robe’s sleeves.
               """

    #------------
    # HelloDesc()
    #------------

    def HelloDesc(self):

        #------------------
        # Make Druid Vanish
        #------------------

        # Move the druid into None and give the player the mandala

        self.MoveInto(None)
        Global.Player.Enter(Mandala)

        #--------------
        # Give the Clue
        #--------------

        return u"""
               The man bows to you, and says: ~i »I am Amak, keeper of
               the ancient places.  Welcome, bold adventurer.  Behold
               the mandala, the sacred circle of the druids.  Take it,
               and let it be your shield and your sword in the places
               of the dark.  To summon its aid, cry aloud the word
               ›Nirna‹, but do so only in dire need, for the mandala
               is a sacred object, and not for profane use.« ~l He hands
               you a small crystal disk, divided into four quarters.
               Bowing, the man turns and walks away into the forest.
               """


    #--------
    # LDesc()
    #--------

    def LDesc(self):
        Text = u"""
               There’s not much to see, just an average size man in a
               brown cowled robe. You can’t see his face, hands or
               feet.
               """

        if CarefullyAdverb.Applies() or CloselyAdverb.Applies():
            Text = Text + u"""
                           Your trained eye notes that his body stance seems wrong
                          for the humble robe he’s wearing, something tells you
                          he’d be more at home in a merchant house than this odd
                          forest.
                          """
            if Rock in P.CA().Contents:
                self.Alerted = TRUE
                Text = Text + u"""
                               The man seems to be peering toward a bulge in your
                               pocket—the rock you found perhaps? ~i »Don’t win this
                               damnable game.« ~l he whispers urgently. ~i »We’re all
                               trapped here. Help us!« ~l Looking around the man
                               bears an uncanny resemblence to a thief expecting
                               the city watch to show up any second. ~i »I’ve said
                               too much. But for all our sakes: DON’T WIN
                               the game!« ~l With that cryptic utterance
                               he resumes his act of calm indifference.
                               """

        return Text


    #-----------
    # OdorDesc()
    #-----------

    def OdorDesc(self):
        return u"""
               Other than the fact that he’s long overdue for a bath,
               you smell nothing unusual about him.
               """

    #------------
    # SoundDesc()
    #------------

    def SoundDesc(self): return u"He’s standing quietly."

    #-------
    # Take()
    #-------

    def Take(self,Multiple=FALSE):
        Complain(self.TakeDesc())

    #-----------
    # TakeDesc()
    #-----------

    def TakeDesc(self):
        return u"""
               The man strikes you suddenly, with enough force to
               knock you back. You aren’t injured, but the warning is
               obvious.
               """

    #------------
    # TasteDesc()
    #------------

    def TasteDesc(self): return u"I don’t think so!!!!!"

    #----------
    # TheDesc()
    #----------

    def TheDesc(self): return u"him"


Druid = ClassDruid(u"man,druid,monk", u"robed,brown,cowled,holy")

Druid.IsHim = TRUE
Druid.StartingLocation = Brenin


#=====================================================================
#                                   Jackalope
#=====================================================================

# The Jackalope is another cameo actor, and a non-combatant.
# He follows the player around.

class ClassJackalope(ClassTQActor):
    """Jackalope Cameo Actor"""

    def SetMyProperties(self):
        self.Value = 5

    #------
    # ADesc
    #------

    def ADesc(self): return u"it"

    #-----------
    # FeelDesc()
    #-----------

    def FeelDesc(self):
        return u"""
            You’re already wearing stovepipes on your legs because the jackalope
            is such a dangerous creature. Are you really sure you want to touch
            it? I wouldn’t if I were you, it’s got really really sharp teeth!
            """

    #-----------
    # HereDesc()
    #-----------

    def HereDesc(self):
        return u"""
            A fearsome critter is here with you. It somehow looks like a
            crossbreed between a jackrabbit and an antelope.
            """

    #------------
    # HelloDesc()
    #------------

    def HelloDesc(self):

        #-----------------------------------------------------
        # Give the Clue and start following the player if:
        #  - the player greets it or talks to it,
        #  - AND he has the mandala with him :-)
        # Accomplishing this is worth 5 points.
        #-----------------------------------------------------

        if Mandala in P.CA().Contents:
            self.Follow = TRUE

            # only add the score once
            if not self.Alerted:
                self.Alerted = TRUE
                IncrementScore(self.Value)

            Text = u"""
                The mandala in your pocket starts getting warm. Astonished, you
                take it out and see it emit a fascinating golden glow. You’re
                still puzzled as the small rabbit-like creature suddenly throws
                back its antlers, looks up to you, and—completely
                unexpected—starts talking: ~i »I’m Jørge, the Jaunty Jackalope.
                People call me a fabled and ancious creature, but as you can see
                I’m still pretty much alive. Actually, I’m seeking for a mate,
                but since we can only breed during heavy thunderstorms, you can
                imagine how lonely I am. So if you keep me entertained with a
                little whiskey from time to time, I might well become your
                friend and help you with your quest.« ~l
                """
        else:
            Text = u"""
                There seems some hope still … Even though you are a thief, it
                seems there is at least some decent behavior left in you. I
                mean, prowling through the wilderness and greeting each and
                every creature you meet on the way …
                """

        return Text

    #--------
    # LDesc()
    #--------

    def LDesc(self):
        Text = u"""
            There is a jackalope here, a fearsome little creature with soft
            and silvery fur, kinda antelope horns on its head and very sharp
            teeth. It stands about one foot high, not counting the antlers,
            that is.
            """

        if CarefullyAdverb.Applies() or CloselyAdverb.Applies():
            Text = Text + u"""
                From a book you once stole, you distinctly seem to remember
                that they were known in ancient times and nowadays believed
                extinct. Upon seeing you, the jackalope snarls at you"""
            if Mandala in P.CA().Contents:
                self.Alerted = TRUE
                Text = Text + u"""
                    and utters in an almost human voice: ~i »Name’s Jørge, got
                    some whiskey?« ~l
                    """
            Text = Text + u"."

        return Text


    #-----------
    # OdorDesc()
    #-----------

    def OdorDesc(self):
        return u"""
            Smelling a jackalope brings you in dangerous vicinity of its teeth,
            which is not recommended until you’re sure it is your friend.
            Anyhow, it smells a little like a rabbit that has played too long
            in damp rotting leaves on the forest floor.
            """

    #------------
    # SoundDesc()
    #------------

    def SoundDesc(self):
        return u"""
            It looks at you fiercely with bloodshot eyes and snarls ~i »Better you behave!« ~l
            """

    #-------
    # Take()
    #-------

    def Take(self, Multiple=FALSE):
        Complain(self.TakeDesc())

    #-----------
    # TakeDesc()
    #-----------

    def TakeDesc(self):
        Text = u"""
            No, no, no! The fearsome little critter snarled, jumped at you
            and gave you a painful bite! OUCH!
            """

        if Mandala in P.CA().Contents:
            Text = Text + u"""
                You feel your magic mandala getting hot and hear a faint
                whisper: ~i ›Get it what it wants and it might make friends
                with you—and may actually be of help‹. ~l
                """
        return Text

    #------------
    # TasteDesc()
    #------------

    def TasteDesc(self): return u"""
        You must be out of your mind … more likely the jackalope will taste YOU!
        """

    #----------
    # TheDesc()
    #----------

    def TheDesc(self): return u"it"


Jackalope = ClassJackalope(u"jørge,jackalope,critter", u"jaunty,ancious,fearsome")

Jackalope.StartingLocation = Clearing
Jackalope.Follow = TRUE


#====================================================================
#                                   Dryad's Dress
#====================================================================

# The dryad's dress is scenery, it doesn't appear in room
# descriptions. The other interesting thing about it is the Where()
# method, the dress returns the Dryad's location (which, since the
# player will never get their hands on it is natural enough).

class ClassDress(ClassScenery):
    def Where(self): return Dryad.Where()

Dress = ClassDress(u"dress", u"woman’s,woman's,dryad’s,dryad's")
Dress.AdjectivePhrase = u""
Dress.StartingLocation = MapleStand


Dress.SetDesc(u"Feel", u"""
                     She’s 30 feet away, and doesn’t look as though
                     she’d appreciate your pawing her dress.
                     """)

Dress.SetDesc(u"L", u"""
                 From this distance it’s hard to tell, but you’re
                 almost certain her dress is made of REAL maple
                 leaves, sown together in some way. Why the dead
                 leaves (which are red and gold) don’t crumble into
                 dust is a mystery. Why she’s wearing such a bizarre
                 garment is an even bigger mystery …
                 """)

Dress.SetDesc(u"Odor", u"Any odor the dress might have is overwhelmed by her perfume.")

Dress.SetDesc(u"Taste", u"""
                      She’s 30 feet away! Besides, do you really feel
                      like licking dead leaves? I sure don’t!
                      """)


#===========================================================================
#                                   Dryad
#===========================================================================


# The dryad looks like a red-haired woman. Observant players may note
# that her hair has golden highlights, or that her dress has strange
# leaf-like patterns on it, but that's all. If they try to take or
# attack her she disappears without warning them about the wolf or
# the druid.
#
# That's her only real purpose, other than to delight the player and
# provide a minor mystery for atmosphere.


class ClassDryad(ClassTQActor):
    def SetMyProperties(self):
        self.Value = 2

    def ADesc(self): return u"her"
    def FeelDesc(self): return u"She’s 30 feet away, and doesn’t look as though she’d appreciate your pawing her."
    def HereDesc(self): return u"A small red haired woman is watching you from behind a tree."


    def HelloDesc(self):

        #------------------
        # Make Dryad Vanish
        #------------------

        # Move the dryad into None and give the player two points for
        # gaining the clue.

        self.MoveInto(None)
        IncrementScore(self.Value)

        #--------------
        # Give the Clue
        #--------------


        # This clue is actually a cornecopia of clues. In order: the
        # silver branch (and the birch grove) are protection from the
        # wolf hiding in the forest, Brenin and the Druid, the crystal
        # mandala. An obtuse reference to the giant spider and how to
        # kill it (bright light focused through the mandala).

        # The second clues: Don't rely on the text as printed, listen,
        # sniff, taste, and feel for clues to survive. And finally
        # the whole speech should convince the player that he's just
        # had a supernatural encounter …

        Text = u"""
               The woman steps from behind the tree and raises one
               hand in greeting. Before you can say anything more,
               she begins to speak, her voice like a golden bell:
               ~i »Beware, human! Silver leaves guard ye well, for danger
               lurks, concealed in pleasant fragrances. Seek ye the
               ancient tree and its guardian, then win from him the
               sacred circle. Light shall be thy guide and thy guard
               for the dark has fangs. Heed me if thou wouldst live.« ~l ~p

               She studies you for a moment and adds ~i »Seek me anon,
               mortal. Be chary of what thou dost believe in this
               place. Thine eyes may not be thy surest sentinel, spurn
               not the lessons of the owl, the wolf, and the wise
               serpent, for what humankind has forgotten, they have
               remembered.« ~l ~p
               """

        if Rock in Global.Player.Contents:
            self.Alerted = TRUE
            Text = Text + u"""
                          Her voice suddenly changes, still lovely but definitely
                          human. ~i »Don’t be stone blind, thief. And listen for
                          me.« ~l
                          """

        Text = Text + u"""
                      Without warning the woman then turns and fades into the
                      trees, almost as though she had never been. You could
                      almost swear she faded INTO the tree she’d been leaning
                      against.
                      """

        return Text


    def LDesc(Self):
        return u"""
               The woman is quite beautiful, but there’s something eldritch about her that sends
               chills up and down your spine. And yet it’s nothing obvious. Her skin is nut brown,
               her hair is flaming red with golden highlights. Her eyes are brilliant green,
               visible in spite of the distance between the two of you. If you saw her in a city
               you’d call her an exotic beauty. But here and now there’s something more … Her
               dress is somewhat unusual, a pattern of leaves in red and gold, but again nothing
               that would explain your instinctive belief that there’s more than meets the eye
               here.
               """

    def OdorDesc(self):
        return u"""
               Although she’s 30 feet away you can detect the faint scent of her perfume, a scent
               that evokes visions of wild things slipping through the trees. You can feel the
               hairs on the back of your neck standing on end. No perfume you ever heard of can
               do that!
               """


    def SoundDesc(self):
        return u"""
               She stopped singing when you entered the stand of maples,
               and is now simply standing and watching you quietly.
               """


    def Take(self,Multiple=FALSE):
        """Take self"""
        Complain(self.TakeDesc())
        self.MoveInto(None)


    def TakeDesc(self): return u"""
                               The woman gasps, startled. Then she
                               dodges away, into the trees and out of
                               sight. For a moment you could swear she
                               dodged INTO the tree!
                               """
    def TasteDesc(self): return u"She’s 30 feet away!"
    def TheDesc(self): return u"her"

Dryad = ClassDryad(u"woman,dryad,hers", u"red,haired,small")

Dryad.IsHer = TRUE
Dryad.StartingLocation = MapleStand


#===========================================================================
#                          Thief's Quest Player
#===========================================================================

# This class extends the Player class from Universe, mainly adding sensory
# descriptions.

class ClassTQPlayer(ClassPlayer):


    #----------
    # Feel Desc
    #----------

    def FeelDesc(self): return u"""
                               You DON’T feel acres of rippling muscles … you’re a
                               thief, not a hero, after all …
                               """

    #-----------
    # OdorDesc()
    #-----------

    def OdorDesc(self): return u"""
                               You’re a bit ripe, about two months overdue for
                               your yearly bath …
                               """
    #------------
    # SoundDesc()
    #------------

    def SoundDesc(self): return u"""
                                You are silent (After all, you ARE a thief, right?)
                                """
    #------------
    # TasteDesc()
    #------------

    def TasteDesc(self): return u"""
                                You (perhaps wisely) decide against trying to
                                taste yourself.
                                """

#------------
# Redefine Me
#------------

TQMe = ClassTQPlayer(u"me,myself")
TQMe.Alerted = FALSE

Global.Player = TQMe




#----------------------------------------------------------------------
#                               Crystal Mandala
#----------------------------------------------------------------------

Mandala = ClassItem(u"mandala,circle", u"crystal,quartered")

Mandala.Bulk = 1
Mandala.StartingLocation = None
Mandala.Value = 60
Mandala.Weight = 1

Mandala.SetDesc(u"Feel", u"""
                       The mandala is cool and smooth to the touch, it weighs
                       a few ounces but has a curiously solid feel to it.
                       """)

Mandala.SetDesc(u"L", u"""
                    The mandala is a flat circle of cut crystal about 3 inches
                    in diameter. It’s thicker in the middle than at the edges,
                    and is divided into 4 quarters by a 4 pointed star somehow
                    embedded into the crystal. It’s very beautiful and
                    obviously valuable as well.
                    """)


Mandala.SetDesc(u"Odor", u"The mandala has no odor.")
Mandala.SetDesc(u"Taste", u"The mandala doesn’t have a taste.")


#=====================================================================
#                                    Rock
#=====================================================================


# This rock serves two purposes, one for the player and one for the
# game author.
#
# Since this is the first item players see, they're going to think
# it's important, especially since it emits a green flash when taken.
#
# It actually does contain a cryptic, creepy clue but is otherwise a red herring,
# doing absolutely nothing. You can throw it but it isn't a weapon, nor will it
# damage anything.
#
# For the developer it shows how to define a minimal object. Notice
# we haven't defined any of the major descriptions. This is to show
# you what happens when the default values are used.


Rock = ClassItem(u"rock,stone,words", u"small,gray,grey,illegible,tiny,scratched")
Rock.StartingLocation = StartCliff
Rock.Bulk = 5
Rock.Weight = 10

Rock.SetDesc(u"Feel", u"""
                    It weighs about a pound, and is smooth like a rock from a
                    stream, but not polished. It’s a typical rock.
                    """)

Rock.SetDesc(u"Take", u"""
                    The rock emits a bright green flash when you pick it up,
                    but does nothing else remarkable.
                    """)

Rock.SetDesc(u"Taste", u"""
                     Yep. Tastes like a rock.
                     """)

Rock.SetDesc(u"Read", u"""
                    In tiny, almost illegible, scratched letters the words read:
                    ~i »Help us! We’re all still here!« ~l
                    """)

Rock.SetDesc(u"L", u"""
                 Upon cursory examination the rock appears to be nothing but a
                 typical rock, smooth as though from a stream, but otherwise
                 just a small gray rock. {Choose(CarefullyAdverb.Applies() or
                 CloselyAdverb.Applies(), u" However when you examine the rock
                 more carefully you notice some tiny words scratched on the
                 rock’s underside.", u"")}
                 """)




#=====================================================================
#                                    Acorn
#=====================================================================

# The acorn is just a scenery prop, it does nothing except let the player
# interact with the acorns at Brenin.

Acorn = ClassScenery(u"acorn,acorns", u"large,huge,enormous,big")
Acorn.StartingLocation = Brenin
Acorn.Article = u"an"

Acorn.SetDesc(u"L", u"The acorns are huge, but otherwise unremarkable.")

Acorn.SetDesc(u"Feel", u"""
                     It weighs about a pound but except for its large size and weight feels
                     like a normal acorn.
                     """)

Acorn.SetDesc(u"Odor", u"It smells like any other acorn")

Acorn.SetDesc(u"Take", u"""
                     The acorns are unremarkable, except in size. After examining one you
                     realize its uselessness and drop it.
                     """)

Acorn.SetDesc(u"Taste", u"""
                      The acorn’s shell is way too tough to bite thru, and licking it merely
                      leaves a slightly bitter taste in your mouth.
                      """)

Global.Acorn = Acorn



#===========================================================================
#                                Beech Birds
#===========================================================================

BeechBird = ClassScenery(u"bird,birds", u"singing")
BeechBird.StartingLocation = BeechCopse

BeechBird.SetDesc(u"Feel", u"""
                         The birds are hidden in the trees, you can’t see them,
                         much less touch them. (As if a bird would willingly
                         let you touch it anyway.)
                         """)

BeechBird.SetDesc(u"L", u"""
                      You can’t see the birds, only hear them.
                      """)

BeechBird.SetDesc(u"Odor", u"The birds are hidden in the trees, you can’t smell them.")

BeechBird.SetDesc(u"Sound", u"""
                          {Choose(BirchGrove.Visited, u"The birdsong is cheerful but
                          not as lovely as in the birch grove.", u"The birdsong is
                          cheerful, although you can’t identify the kinds of
                          birds singing.")}
                          """)

BeechBird.SetDesc(u"Take", u"""
                         There aren’t any birds in sight, only in hearing.
                         """)

BeechBird.SetDesc(u"Taste", u"""
                          You want to lick a bird? Ycch. Besides, all the
                          birds are hidden in the trees, you can see any. Of
                          course no bird would let you get that close anyway.
                          """)


#===========================================================================
#                                Birch Birds
#===========================================================================

BirchBird = ClassScenery(u"bird,birds", u"singing")
BirchBird.StartingLocation = BirchGrove

BirchBird.SetDesc(u"Feel", u"""
                         The birds are hidden in the trees, you can’t see them,
                         much less touch them. (As if a bird would willingly
                         let you touch it anyway)
                         """)

BirchBird.SetDesc(u"L", u"""
                      You can’t see the birds, only hear them.
                      """)

BirchBird.SetDesc(u"Odor", u"The birds are hidden in the trees, you can’t smell them.")

BirchBird.SetDesc(u"Sound", u"""
                          {Choose(BirchGrove.Visited, u"The birdsong is lovely, much
                          prettier than the birds in the beech copse.", u"The
                          birdsong brings tears to your eyes. You’ve never heard
                          birds with such sweet song, nor even heard of any.")}
                          """)

BirchBird.SetDesc(u"Take", u"""
                         There aren’t any birds in sight, only in hearing.
                         """)

BirchBird.SetDesc(u"Taste", u"""
                          You want to lick a bird? Ycch. Besides, all the birds
                          are hidden in the trees, you can see any. Of course
                          no bird would let you get that close anyway.
                          """)



#===========================================================================
#                               Blockhouse
#===========================================================================

# The blockhouse is the dungeon's main entrance, it appears here to handle
# player interaction with it.

class ClassBlockhouse(ClassScenery):
    """Class for Blockhouse Modifications"""
    def ReadDesc(self): return BlockhouseNote.ReadDesc()

Blockhouse = ClassBlockhouse(u"blockhouse,cube,bunker", u"cement,concrete,gray,grey")
Blockhouse.StartingLocation = DungeonEntrance

Blockhouse.SetDesc(u"Feel", u"It feels like sun-warmed concrete to your cautious touch.")

Blockhouse.SetDesc(u"L", u"""
                       The blockhouse is a large featureless cube
                       about 8 feet on a side, made of gray cement or
                       concrete. There’s a massive steel door on one
                       side, with a sign stenciled in peeling orange
                       paint. There’s a peg by the door.
                       """)

Blockhouse.SetDesc(u"Odor", u"It smells musty, like hot concrete.")
Blockhouse.SetDesc(u"Take", u"""
                          I may not have made myself clear. The
                          blockhouse is 8 feet on a side, and probably
                          weighs more in tons than you weigh in
                          pounds. Let us also not forget that
                          buildings are generally firmly attached to
                          their foundations. In other words, it isn’t
                          going anywhere!
                          """)

Blockhouse.SetDesc(u"Taste", u"Blech! It tastes like dirty, weathered cement!")


#===========================================================================
#                              Blockhouse Note
#===========================================================================

# This is the note painted on the blockhouse door. Notice we explicitly set
# the note's AdjectivePhrase to "" (an empty string) to give the game a
# more natural way to refer to the note.

class ClassBlockhouseNote(ClassScenery):
    """Class for Blockhouse Note Modifications"""
    def ReadDesc(self):
        return u"""
               The sign says, ~i »Hi. Unauthorized personal stay out.
               This means you, bozo. Oh, yes. Beware of the griffon.
               Have a nice day.« ~l
               """

    def SDesc(self): return u"note"

BlockhouseNote = ClassBlockhouseNote(u"note,sign,message,text,words", u"painted,orange,peeling")
BlockhouseNote.AdjectivePhrase = u""
BlockhouseNote.StartingLocation = DungeonEntrance
BlockhouseNote.ParserFavors = TRUE

BlockhouseNote.SetDesc(u"Feel", u"It’s peeling, rough orange paint.")

BlockhouseNote.SetDesc(u"L", u"""
                           The note is in large block letters
                           stenciled on the door in peeling orange
                           paint, it’s obvious the note was painted a
                           long time ago. {BlockhouseNote.ReadDesc()}
                           """)

BlockhouseNote.SetDesc(u"Odor", u"It doesn’t have much of a smell.")

BlockhouseNote.SetDesc(u"Take", u"""
                              To take the note you’d have to take the
                              door, the note is painted on the door.
                              """)

BlockhouseNote.SetDesc(u"Taste", u"You want me to lick old paint? I don’t think so …")


#===========================================================================
#                               Blockhouse Peg
#===========================================================================

# This is the peg the keys hang from.

BlockhousePeg = ClassShelf(u"peg", u"wooden,hard,sturdy")
BlockhousePeg.StartingLocation = DungeonEntrance

BlockhousePeg.SetDesc(u"Feel", u"It’s smooth hard wood.")

BlockhousePeg.SetDesc(u"L", u"""
                          The peg is wood, weathered by sun and wind,
                          but very sturdy. It’s obviously a place to
                          hang a keyring.
                          """)

BlockhousePeg.SetDesc(u"Odor", u"""
                             It doesn’t have much of a smell, maybe
                             the faintest hint of sour tang, not
                             unexpected from weathered wood.
                             """)

BlockhousePeg.SetDesc(u"Take", u"""
                             The peg is far too well anchored to take.
                             Besides, it’s pretty obvious the peg is
                             just to hang keys from. Letting your
                             larcenous instincts run wild again?
                             """)

BlockhousePeg.SetDesc(u"Taste", u"""
                              You want me to lick a weathered wooden
                              peg? I don’t think so …
                              """)



#===========================================================================
#                                Birch Leaves
#===========================================================================

BirchLeaf = ClassScenery(u"leaf,leaves,mulch", u"birch,green,dead,rich,brown,black")
BirchLeaf.StartingLocation = BirchGrove

BirchLeaf.SetDesc(u"Feel", u"""
                         The leaves feel like typical leaves, the dead
                         ones are damp and crumbly, the live ones feel
                         like leaves.
                         """)

BirchLeaf.SetDesc(u"L", u"""
                      They’re about two inches long and arrowhead
                      shaped. The live ones are light green, the dead
                      ones are brown or black.
                      """)

BirchLeaf.SetDesc(u"Odor", u"The leaves smell kind of spicy.")
BirchLeaf.SetDesc(u"Sound", u"""
                          The leaves themselves are silent, tho there’s a kind of
                          sighing noise when the wind stirs them.
                          """)

BirchLeaf.SetDesc(u"Take", u"""
                         You could easily take hundreds of the things,
                         but they aren’t worth anything, so why bother?
                         """)

BirchLeaf.SetDesc(u"Taste", u"""
                          It tastes odd, kind of minty but not quite.
                          You spit it out, worried about poisoning
                          yourself.
                          """)


#===========================================================================
#                                Birch Tree
#===========================================================================

BirchTree = ClassScenery(u"tree", u"birch")
BirchTree.StartingLocation = BirchGrove

BirchTree.SetDesc(u"Feel", u"The bark is smooth.")

BirchTree.SetDesc(u"L", u"""
                      It’s a typical birch tree, with arrow-head
                      shaped light green leaves and smooth bark, just
                      like the dozens of others in the grove.
                      """)

BirchTree.SetDesc(u"Odor", u"It doesn’t have much of an odor, very treelike, actually.")

BirchTree.SetDesc(u"Sound", u"""
                          Other than a slight rustling noise when wind
                          moves through its leaves the tree makes no
                          noise at all.
                          """)

BirchTree.SetDesc(u"Take", u"""
                         The tree is rooted firmly in the ground.
                         Besides even if you could cut it down (which,
                         lacking an axe, you can’t) it’s far too large
                         to lift.
                         """)

BirchTree.SetDesc(u"Taste", u"I draw the line at licking trees, thank you very much.")




#===========================================================================
#                                  Clearing Pool
#===========================================================================

# This is the pool in the clearing. Notice the explicit removal of the
# AdjectivePhrase by setting it to "" (an empty string).

ClearingPool = ClassScenery(u"pool", u"cold,small,clear")
ClearingPool.AdjectivePhrase = u""
ClearingPool.StartingLocation = Clearing

ClearingPool.SetDesc(u"Feel", u"The water in the pool is extremely cold, almost like snowmelt.")

ClearingPool.SetDesc(u"L", u"""
                         Although the pool is small and clear, it is
                         extremely deep, almost like a well. The
                         bottom is shadowed, you can’t make out any
                         details.
                         """)

ClearingPool.SetDesc(u"Odor", u"The pool smells like clean water. It’s certainly drinkable.")
ClearingPool.SetDesc(u"Take", u"You don’t have anything meant to carry water.")

ClearingPool.SetDesc(u"Taste", u"""
                             The water tastes strongly of minerals,
                             but is not unpleasant. It is extremely
                             cold.
                             """)


#-----------------
# Hilltop Clearing
#-----------------

HilltopClearing = ClassScenery(u"clearing")
HilltopClearing.AdjectivePhrase = u""
HilltopClearing.StartingLocation = Hill

HilltopClearing.SetDesc(u"Feel", u"How exactly does one feel a clearing?")

HilltopClearing.SetDesc(u"L", u"""
                            The clearing is quite large, at least two hundred feet
                            across, roughly circular. It contains a pool and ends
                            at the foot of a large rock mound to the east. Pine
                            forest surrounds it to the north and south. It looks
                            awfully familiar some how …
                          """)


HilltopClearing.SetDesc(u"Odor", u"{Hill.OdorDesc()}")
HilltopClearing.SetDesc(u"Take", u"Take a clearing? Riiiiggghhhtttt.")
HilltopClearing.SetDesc(u"Taste", u"Um, are you sure the stress hasn’t unhinged your reason?")
HilltopClearing.SetDesc(u"Sound", u"{Hill.SoundDesc()}")


#---------------
# Mound Clearing
#---------------

MoundClearing = ClassScenery(u"clearing")
MoundClearing.AdjectivePhrase = u""
MoundClearing.StartingLocation = Clearing

MoundClearing.SetDesc(u"Feel", u"How exactly does one feel a clearing?")

MoundClearing.SetDesc(u"L", u"""
                          The clearing is quite large, at least two hundred feet
                          across, roughly circular with the hill to the west and the
                          mound to the east. Pine forest surrounds everything else
                          There’s a path climbing the hill to the west. In spite
                          of the fact you’ve never been here before you can’t
                          shake the feeling you’ve been here before …
                          """)


MoundClearing.SetDesc(u"Odor", u"{Clearing.OdorDesc()}")
MoundClearing.SetDesc(u"Take", u"Take a clearing? Riiiiggghhhtttt.")
MoundClearing.SetDesc(u"Taste", u"Um, are you sure the stress hasn’t unhinged your reason?")
MoundClearing.SetDesc(u"Sound", u"{Clearing.SoundDesc()}")


#---------------------
# Start Cliff Clearing
#---------------------

StartCliffClearing = ClassScenery(u"clearing")
StartCliffClearing.AdjectivePhrase = u""
StartCliffClearing.StartingLocation = StartCliff

StartCliffClearing.SetDesc(u"Feel", u"How exactly does one feel a clearing?")

StartCliffClearing.SetDesc(u"L", u"""
                               The clearing is about 30 feet across, roughly
                               a half-circle with the cliff at the western edge
                               and pine forest everywhere else. A path
                               disappears into the forest on the eastern edge.
                               """)


StartCliffClearing.SetDesc(u"Odor", u"{StartCliff.OdorDesc()}")
StartCliffClearing.SetDesc(u"Take", u"Take a clearing? Riiiiggghhhtttt.")
StartCliffClearing.SetDesc(u"Taste", u"Um, are you sure the stress hasn’t unhinged your reason?")
StartCliffClearing.SetDesc(u"Sound", u"{StartCliff.SoundDesc()}")





#===========================================================================
#                                Maple Leaves
#===========================================================================

MapleLeaf = ClassScenery(u"leaf,leaves", u"maple,red,gold,yellow,dead")
MapleLeaf.StartingLocation = MapleStand

MapleLeaf.SetDesc(u"Feel", u"""
                         The leaves feel like typical fallen leaves,
                         the ones on top are crumbly, the ones
                         underneath are damp and crumbly.
                         """)

MapleLeaf.SetDesc(u"L", u"""
                      They’re about four inches long and vaguely
                      pitchfork shaped. The ones on the tree are red
                      and gold, the dead ones are red, gold, brown or
                      black.
                      """)

MapleLeaf.SetDesc(u"Odor", u"""
                         The leaves are pretty much odorless, maybe a
                         slight sour whiff but you can’t be sure.
                         """)

MapleLeaf.SetDesc(u"Sound", u"""
                          Did you really expect a maple leaf to make
                          any noise?
                          """)

MapleLeaf.SetDesc(u"Take", u"""
                         You could easily take hundreds of the things,
                         but they aren’t worth anything, so why bother?
                         """)

MapleLeaf.SetDesc(u"Taste", u"""
                          It tastes about like what you’d expect a
                          leaf to taste like. You spit it out in
                          disgust.
                          """)


#===========================================================================
#                                Maple Sap
#===========================================================================

MapleSap = ClassScenery(u"sap,syrup", u"maple")
MapleSap.StartingLocation = MapleStand

MapleSap.SetDesc(u"Feel", u"There’s no sap on any of the trees.")
MapleSap.SetDesc(u"L", u"None of the trees has any sap on the bark.")
MapleSap.SetDesc(u"Odor", u"None of the trees has any sap on the bark.")
MapleSap.SetDesc(u"Sound", u"""
                            Yeah, sure. These are the Magic Maple Trees
                            that sing along while they work for you
                            and produce syrup, right? You’re even
                            crazier than I am!
                            """)
MapleSap.SetDesc(u"Take", u"None of the trees has any sap on the bark.")

MapleSap.SetDesc(u"Taste", u"""
                         Although you’ve heard how sweet maple syrup is, none
                         of these trees has any sap on the bark.
                          """)


#===========================================================================
#                                Maple Tree
#===========================================================================

MapleTree = ClassScenery(u"tree,trees", u"maple")
MapleTree.StartingLocation = MapleStand

MapleTree.SetDesc(u"Feel", u"The bark is typical tree bark.")

MapleTree.SetDesc(u"L", u"""
                      It’s a typical maple tree, with red and gold
                      leaves and smooth brown bark, just like the
                      dozens of others in the stand. You seem to
                      remember people make syrup from the sap, but you
                      have only the vaguest notion of how it’s done.
                      Another thing, these trees are showing fall
                      colors, but it was spring when you tried to rob
                      the wizard’s tower.
                      """)

MapleTree.SetDesc(u"Odor", u"It smells like any other tree.")

MapleTree.SetDesc(u"Sound", u"""
                          Other than a slight rustling noise when wind moves through its
                          leaves the tree makes no noise at all.
                          """)

MapleTree.SetDesc(u"Take", u"""
                         The tree is rooted firmly in the ground.
                         Besides even if you could cut it down (which,
                         lacking an axe, you can’t) it’s far too large
                         to lift.
                         """)

MapleTree.SetDesc(u"Taste", u"What? The TREE? I’d go for some tasty maple syrup, though.")



#=====================================================================
#                                    Mistletoe
#=====================================================================

# The mistletoe is just a scenery prop, it does nothing except let the player
# interact with it at Brenin. Notice we specifically set the AdjectivePhrase
# to "" (an empty string) so that the game will refer to the mistletoe more
# naturally.

Mistletoe = ClassScenery(u"mistletoe", u"dark,green,hanging,bunches")
Mistletoe.AdjectivePhrase = u""
Mistletoe.StartingLocation = Brenin
Mistletoe.Article = u"the"

Mistletoe.SetDesc(u"L", u"""
                       The mistletoe hangs everywhere, in huge
                       bunches, often brushing the ground (which
                       considering the lowest branches are 50 feet up
                       is pretty impressive). And NO, there’s no one
                       climbing around in the tree and cutting his fingers
                       on a golden sickle …
                       """)

Mistletoe.SetDesc(u"Feel", u"""
                          The mistletoe feels slightly oily, but
                          otherwise completely normal—except for its
                          size, of course.
                          """)

Mistletoe.SetDesc(u"Odor", u"The mistletoe has a slight acrid odor.")

Mistletoe.SetDesc(u"Sound", u"""
                           The mistletoe rustles in the breeze,
                           almost sounding as though it were
                           whispering. Very unnerving, now that your
                           attention has been drawn to it.
                           """)

Mistletoe.SetDesc(u"Take", u"""
                          A vague memory prods you as you start to
                          take the plant. Something about desecrating
                          ancient places. Uneasy you let your hand
                          fall without taking the mistletoe. The
                          stillness you hadn’t consciously noted ends
                          as you turn away. You shudder as you
                          contemplate the fate of those who defile
                          holy places.
                          """)

Mistletoe.SetDesc(u"Taste", u"""
                           You spit out the single twig you nibbled,
                           finding it quite the most bitter thing
                           you’ve ever tasted!
                           """)



#===========================================================================
#                                Oak Tree
#===========================================================================

# Notice how we create a class simply to override the SoundDesc()
# method.

class ClassOakTree(ClassScenery):
    def SetMyProperties(self):
        ClassScenery.SetMyProperties(self)

    def SoundDesc(self):
        if P.CA().Remembers(Dryad):
            IncrementScore(self.Value)
            self.Value=0
            Text = u"""
                   The wind in the tree’s branches isn’t whispering,
                   it’s SINGING with a woman’s glorious golden voice.
                   In fact, it reminds you of the woman you saw in the
                   maple stand. The longer you listen, the surer you
                   become that it IS the woman from the maple stand …
                   """
            if Dryad.Alerted:
                Text = Text + u"""
                              In the liquid flow of a language you don’t
                              understand a few recognizable words seem to appear
                              randomly, although if you weren’t listening
                              so intently they’d be easy to miss. ›Dream‹,
                              ›deceit‹, ›years‹, ›hope‹, ›inside‹ and ›charm‹ are
                              the ones you’re more or less sure of.
                              """

            return Text
        else:
            return u"""
                   The wind in the tree’s branches isn’t whispering,
                   it’s SINGING with a woman’s glorious golden
                   voice. The words aren’t in any language you
                   recognize, but conjure swirling images of
                   scarlet and saffron light that dance inside your
                   head …
                   """

OakTree = ClassOakTree(u"tree", u"oak")
OakTree.StartingLocation = Brenin
OakTree.Value = 10

OakTree.SetDesc(u"Feel", u"""
                       The tree seems to tingle under your fingertips,
                       you can sense the life of the tree flowing
                       under your hand like some vast ocean swell.
                       The sensation is so disconcerting you jerk your
                       hand away. You promise yourself to be more
                       cautious about what you touch in the future.
                       """)

OakTree.SetDesc(u"L", u"""
                    An incredible tree! It rears above you, at least
                    five hundred feet tall. The branches start fifty
                    feet from the ground and stretch a hundred feet
                    from trunk to tip. The trunk of the tree must be
                    at least 75 feet thick although it appears slender
                    in proportion.
                    """)

OakTree.SetDesc(u"Odor", u"""
                       It has no real smell (no more so than any other
                       tree), except you get the impression that this
                       tree is old, on the order of thousands of
                       years. Why it should smell old is something
                       you’d rather not think about right now …
                       """)

OakTree.SetDesc(u"Take", u"""
                       I’m not even going to dignify that with a
                       snide remark.
                       """)

OakTree.SetDesc(u"Taste", u"Oh, come ON. I draw the line at licking tree bark!")




#===========================================================================
#                                Beech Leaves
#===========================================================================

BeechLeaf = ClassLandmark(u"leaf,leaves,mulch", u"beech,green,dead,rich,brown,black")
BeechLeaf.Landmark = u"BeechTree"

BeechLeaf.SetDesc(u"Feel", u"""
                         The leaves feel like typical leaves, the dead ones are
                         damp and crumbly, the live ones feel like leaves.
                         """)

BeechLeaf.SetDesc(u"L", u"""
                      They’re about two inches long and arrowhead shaped. The
                      live ones are green, the dead ones are brown or black.
                      """)

BeechLeaf.SetDesc(u"Odor", u"The leaves smell kind of spicy.")
BeechLeaf.SetDesc(u"Sound", u"Did you really expect a beech leaf to make any noise?")

BeechLeaf.SetDesc(u"Take", u"""
                         You could easily take hundreds of the things, but they
                         aren’t worth anything, so why bother?
                         """)

BeechLeaf.SetDesc(u"Taste", u"They have kind of a minty flavor, quite pleasant, actually.")


#===========================================================================
#                                Beech Tree
#===========================================================================

BeechTree = ClassLandmark(u"tree", u"beech")
BeechTree.Landmark = u"BeechTree"

BeechTree.SetDesc(u"Feel", u"The bark is smooth.")

BeechTree.SetDesc(u"L", u"""
                      It’s a typical beech tree, with arrow-head shaped green leaves and
                      smooth bark, just like the dozens of others in the copse.
                      """)

BeechTree.SetDesc(u"Odor", u"It doesn’t have much of an odor, very treelike, actually.")

BeechTree.SetDesc(u"Sound", u"""
                          Other than a slight rustling noise when wind moves through its
                          leaves the tree makes no noise at all.
                          """)

BeechTree.SetDesc(u"Take", u"""
                         The tree is rooted firmly in the ground. Besides even if you could
                         cut it down (which, lacking an axe, you can’t) it’s far too large
                         to lift.
                         """)

BeechTree.SetDesc(u"Taste", u"I draw the line at licking trees, thank you very much.")



#===========================================================================
#                                   Cliff
#===========================================================================

# The cliff "floats" around. Any room that has the HasCliff set to
# true will let the cliff appear in that room. Also notice the
# ReadDesc, it allows the "Start" word to be seen from selected
# locations.

class ClassCliff(ClassLandmark):
    """Class to define 'floating' cliff special behaviors"""

    def ReadDesc(self):
        if self.Where().CliffMessageIsVisible:
            return u"The cliff has a single (50 foot tall) word: ›Start‹."
        else:
            return u"There’s no writing on the cliff here."


Cliff = ClassCliff(u"cliff,wall", u"granite,unclimbable,valley")
Cliff.Landmark = u"Cliff"
Cliff.StartingLocation = StartCliff
Cliff.ParserFavors = TRUE

Cliff.SetDesc(u"Feel", u"It feels like sun-warmed granite to your cautious touch.")
Cliff.SetDesc(u"L", u"It’s your typical 2,000 foot unclimbable (granite) cliff.")

Cliff.SetDesc(u"Odor", u"""
                     Pressing your nose up against the cliff you take
                     a deep whiff. Yep. Absolutely unmistakable. It
                     smells like every granite cliff you’ve ever
                     encountered in your spotted career.
                     """)

Cliff.SetDesc(u"Take", u"""
                     I’m sorry? Did you just ask to take a 2,000 foot
                     tall cliff, which I might add, stretches in
                     either direction totally out of sight? That
                     cliff? Idiot.
                     """)

Cliff.SetDesc(u"Taste", u"Not with MY tongue!")


#===========================================================================
#                                  Forest Floor
#===========================================================================

ForestFloor = ClassLandmark(u"ground,floor,mulch,dirt")
ForestFloor.Landmark = u"PineTree"

ForestFloor.SetDesc(u"Feel", u"""
                           The ground is dirt covered with a combination of
                           green and brown pine needles to a depth of an inch
                           or so. It’s kind of wet and messy, as though this
                           mulch traps rainfall.
                           """)

ForestFloor.SetDesc(u"L", u"{P.CA().Where().GroundDesc()}")

ForestFloor.SetDesc(u"Odor", u"""
                           The mulch covering the ground doesn’t smell nearly
                           as nice as the trees themselves, a very earthy
                           odor, wet and with just a touch of mold.
                           """)

ForestFloor.SetDesc(u"Sound", u"""
                            The ground isn’t making any noise, further when you
                            walk on it the mulch tends to deaden the sound of
                            your footsteps.
                            """)

ForestFloor.SetDesc(u"Take", u"You must be joking.")

ForestFloor.SetDesc(u"Taste", u"""
                            Ycch! Who knows how many animals have been along
                            here recently, leaving deposits, if you know what
                            I mean? There’s NO way I’m putting that in MY
                            mouth!
                            """)




#===========================================================================
#                                   Mound
#===========================================================================

# The mound is present in two areas, the clearing and at the bottom of the
# cliff on the east side of the valley.

Mound = ClassLandmark(u"mound", u"rocky,massive,stone,sandstone,snake")
Mound.Landmark = u"Mound"
Mound.StartingLocation = Clearing

Mound.SetDesc(u"Feel", u"""
                     It feels like sun-warmed rock to your touch. Lots
                     of handholds and a rough texture that would make
                     it easy to climb.
                     """)

Mound.SetDesc(u"L", u"""
                  It’s a large rocky mound, actually more like a
                  miniature hill, shaped like a fat snake.
                  """)

Mound.SetDesc(u"Odor", u"""
                    It smells sandy, which makes sense because the
                    rock is made of sandstone.
                    """)

Mound.SetDesc(u"Take", u"""
                     I’m sorry? Did you just ask to take a small
                     HILL? A MASSIVE mound of rock? Geez!
                     """)

Mound.SetDesc(u"Taste", u"Grit and dirt. Ptui!")



#===========================================================================
#                                Path In Forest
#===========================================================================

PathInForest = ClassLandmark(u"path,trail,track", u"faint,game")
PathInForest.Landmark = u"ForestPath"

PathInForest.SetDesc(u"Feel", u"""
                            Stooping down to feel the path you notice
                            a few other details. The path itself is
                            just a game trail worn by the passage of
                            animals, there are a number of smudges
                            and scuffs, but being city-born all you
                            can tell is they’re probably the remains
                            of the prints of animals who used the
                            path some time in the past. The only real
                            clue this is a path is that the pine
                            needles have been pushed to the path’s
                            edges by the passage of feet, hooves,
                            paws, or what have you.
                            """)

PathInForest.SetDesc(u"L", u"""
                         It’s a typical game trail, faint and winding
                         avoiding trees. Given your limited experience
                         on the subject it seems much like any other
                         game trail.
                         """)

PathInForest.SetDesc(u"Odor", u"""
                            If you insist. Sigh. It smells of dirt,
                            old pine needles, and dampness. Pretty
                            much as you expected.
                            """)

PathInForest.SetDesc(u"Sound", u"""
                             What, you’re trying to eavesdrop on
                             earthworms? The path itself is silent.
                             """)

PathInForest.SetDesc(u"Take", u"""
                            Look, it’s a game trail, all right? Part
                            of the ground. It’s not like you can dig
                            it up and tuck it in your pocket now is
                            it?
                            """)

PathInForest.SetDesc(u"Taste", u"""
                             Does the phrase »not bloody likely« ring
                             any bells?
                             """)



#===========================================================================
#                                Pine Cone
#===========================================================================

PineCone = ClassLandmark(u"cone,cones", u"pine")
PineCone.Landmark=u"PineTree"

PineCone.SetDesc(u"Feel", u"You don’t see any.")
PineCone.SetDesc(u"L", u"You don’t see any.")
PineCone.SetDesc(u"Odor", u"You don’t see any.")
PineCone.SetDesc(u"Sound", u"You don’t see any.")
PineCone.SetDesc(u"Take", u"You don’t see any.")
PineCone.SetDesc(u"Taste", u"You don’t see any.")

#===========================================================================
#                                Pine Tree
#===========================================================================

PineTree = ClassLandmark(u"forest", u"pine")
PineTree.Landmark = u"PineTree"

PineTree.SetDesc(u"Feel", u"You might touch one tree but not the whole forest!")

PineTree.SetDesc(u"L", u"""
                     There’s an almost palpable sense of menace in the forest.
                     Perhaps its the way the trees crowd closely together,
                     blocking your line of sight. Or it could be the eerie
                     silence under those trees. Even you know that a silent
                     forest is not a good thing, city-bred though you be.
                     """)

PineTree.SetDesc(u"Odor", u"""
                        It smells like any other pine forest. Very pleasant,
                        actually.
                        """)

PineTree.SetDesc(u"Sound", u"""
                         Other than a slight hissing noise when wind moves
                         through the needles there is no noise at all. It
                         sends chills down your spine.
                         """)

PineTree.SetDesc(u"Take", u"Take a whole forest? Who are you, Paul Bunyan?")
PineTree.SetDesc(u"Taste", u"One tree, maybe. Not a whole forest!")


#===========================================================================
#                                Pine Needle
#===========================================================================

PineNeedle = ClassLandmark(u"needle,needles,leaf,leaves", u"pine")
PineNeedle.Landmark=u"PineTree"

PineNeedle.SetDesc(u"Feel", u"""
                          The pine needles feel slightly slippery.
                          Remember, pine needles are just a kind of
                          leaf.
                          """)

PineNeedle.SetDesc(u"L", u"""
                       They are about an inch long and slender, green
                       when on the tree and brown once the tree sheds
                       them. They grow in thick bunches on every
                       branch. You’ve seen pine trees before, right?
                       """)

PineNeedle.SetDesc(u"Odor", u"""
                          A single needle doesn’t have much of an
                          odor, but a whole branch of the things
                          gives the typical pine fragrence that pine
                          trees are famous for.
                          """)

PineNeedle.SetDesc(u"Sound", u"""
                           Did you really expect a pine needle to make
                           any noise?
                           """)

PineNeedle.SetDesc(u"Take", u"""
                          You could take hundreds of the things, but
                          they aren’t worth anything.
                          """)

PineNeedle.SetDesc(u"Taste", u"""
                           It tastes about like what you’d expect a
                           pine needle to taste like. You spit it out
                           in disgust.
                           """)


#===========================================================================
#                                Pine Resin
#===========================================================================

PineResin = ClassLandmark(u"resin,sap", u"pine,amber,dark,hardened")
PineResin.Landmark = u"PineTree"

PineResin.SetDesc(u"Feel", u"""
                         The resin is hard and smooth, and firmly
                         embedded in the trunk.
                         """)

PineResin.SetDesc(u"L", u"""
                      A sort of dark amber color, the resin is nothing
                      more than hardened pine tree sap. Although, as
                      you examine it closely you notice it seems to
                      occur in groups of 4 vertical stripes, always
                      together. Moving to another tree that has resin
                      on it (not all of them do) you see the same
                      pattern. Such patterns don’t occur naturally …
                      """)

PineResin.SetDesc(u"Odor", u"The pine resin is odorless.")

PineResin.SetDesc(u"Sound", u"""
                          Did you really expect hardened tree sap to
                          make a noise?
                          """)

PineResin.SetDesc(u"Take", u"""
                         You can’t, the resin is rock hard and firmly
                         embedded in the trunk.
                         """)

PineResin.SetDesc(u"Taste", u"The resin has a slightly sweet taste.")


#===========================================================================
#                                Pine Tree
#===========================================================================

PineTree = ClassLandmark(u"tree,trees", u"pine")
PineTree.Landmark = u"PineTree"

PineTree.SetDesc(u"Feel", u"The bark is rough.")

PineTree.SetDesc(u"L", u"""
                     It’s a typical pine tree, with green needles and rough
                     brown bark, just like the thousands of others in the
                     forest. There is lots of resin on the trunk, but nothing
                     unusual.
                     """)

PineTree.SetDesc(u"Odor", u"""
                        It smells like any other pine tree. (You were
                        expecting maybe roses?)
                        """)

PineTree.SetDesc(u"Sound", u"""
                         Other than a slight hissing noise when wind moves
                         through its needles the tree makes no noise at all.
                         """)

PineTree.SetDesc(u"Take",u"""
                        The tree is rooted firmly in the ground. Besides even
                        if you could cut it down (which, lacking an axe, you
                        can’t) it’s far too large to lift.
                        """)

PineTree.SetDesc(u"Taste", u"Not with MY tongue!")



#===========================================================================
#                                Stream
#===========================================================================

# The stream, in case the player wants to interact with it. Note this is a
# floating object, notice the Where() method. Also notice we explicitly
# remove the AdjectivePhrase

Stream = ClassLandmark(u"stream,creek,rivulet,water", u"cold,tiny")
Stream.AdjectivePhrase = u""
Stream.Landmark = u"Stream"

Stream.SetDesc(u"Feel", u"""
                      The water in the stream is extremely cold,
                      almost like snowmelt.
                      """)

Stream.SetDesc(u"L", u"""
                   The stream is shallow, not more than a foot deep,
                   running over a rocky bed.
                   """)

Stream.SetDesc(u"Odor", u"""
                      The stream smells like a stream—damp, slightly
                      mossy with an overtone of frogs. You know, a
                      typical stream.
                      """)

Stream.SetDesc(u"Sound", u"""
                       The stream makes a tinkling noise as it
                       passes over very shallow (1 inch deep) parts
                       of its bed. At no point does the stream exceed
                       a foot in depth.
                       """)

Stream.SetDesc(u"Take", u"You don’t have anything meant to carry water.")

Stream.SetDesc(u"Taste", u"""
                       The water tastes strongly of minerals, but is
                       not unpleasant. It is extremely cold.
                       """)







#***************************************************************************
#                                M A P S
#***************************************************************************

# Here's another work around. Because of Python's interpreted nature,
# every object placed in a map dictionary must already be defined.
# Thus we have to add maps AFTER all the rooms they refer to have
# been defined.
#
# It's annoying, but not impossible.


StartCliff.Map = {North:     DeepForest,
                  Northeast: DeepForest,
                  East:      A4WayPath,
                  Southeast: DeepForest2,
                  South:     DeepForest2,
                  Up: u"""
                      The cliff offers no handholds and to your experienced
                      eye appears totally unclimbable.
                      """,
                  Down: u"It appears we’re fresh out of holes to climb down.",
                  Cliff: u"""
                         The cliff offers no handholds and to your experienced
                         eye appears totally unclimbable.
                         """}

A3WayPath.Map = {North:     DeepForest2,
                 Northeast: DeepForest2,
                 East:      BeechCopse,
                 Southeast: DeepForest2,
                 South:     Brenin,
                 Southwest: DeepForest2,
                 West:      A4WayPath,
                 Northwest: DeepForest2}

A3WayPath2.Map = {North:    DeepForest,
                 Northeast: DeepForest,
                 East:      Hill,
                 Southeast: DeepForest2,
                 South:     BirchGrove,
                 Southwest: DeepForest2,
                 West:      A4WayPath,
                 Northwest: DeepForest}

A4WayPath.Map = {North:     NorthPath,
                 Northeast: DeepForest,
                 East:      A3WayPath2,
                 Southeast: DeepForest2,
                 South:     A3WayPath,
                 Southwest: DeepForest2,
                 West:      StartCliff,
                 Northwest: DeepForest}

BeechCopse.Map = {North:     DeepForest2,
                  Northeast: DeepForest2,
                  East:      DeepForest6,
                  Southeast: SouthWall1,
                  South:     SouthWall1,
                  Southwest: SouthWall1,
                  West:      DeepForest2,
                  Northwest: A3WayPath,
                  Up:        UpATree,
                  BeechTree: UpATree,
                  Down:      u"The ground is in the way."}

BirchGrove.Map = {North:     DeepForest2,
                  Northeast: DeepForest2,
                  East:      DeepForest2,
                  Southeast: DeepForest2,
                  South:     DeepForest2,
                  Southwest: DeepForest2,
                  West:      DeepForest2,
                  Northwest: A3WayPath2,
                  Up:        u"There are no climbable trees here.",
                  Down:      u"You can not go down."}

BottomOfCliff.Map = {North:     DeepForest7,
                     South:     SouthWall3,
                     Southwest: SouthWall3,
                     West:      GypsumPassage,
                     Northwest: DeepForest7,
                     Up:        EastLedge,
                     Mound:     TopOfMound,
                     Down:      u"It appears we’re fresh out of holes to climb down."}

Brenin.Map = {North:     DeepForest2,
              Northeast: DeepForest2,
              East:      DeepForest2,
              Southeast: DeepForest2,
              South:     A3WayPath,
              Southwest: Brenin.NoExit,
              West:      Brenin.NoExit,
              Northwest: Brenin.NoExit,
              Up:        u"""
                         The nearest branch is fifty feet above you, and the
                         gnarled trunk is far too thick and slippery to
                         permit climbing. The mistletoe festooning the
                         branches is too fragile to bear your weight, even
                         though it nearly touches the ground in places.
                         """,
              Down:      u"There are no caverns here."}

Clearing.Map = {North:     DeepForest4,
                Northeast: DeepForest4,
                East:      GypsumCave,
                Southeast: DeepForest5,
                South:     DeepForest5,
                Southwest: ForestWithCave,
                West:      Hill,
                Northwest: DeepForest4,
                Up:        TopOfMound,
                Mound:     TopOfMound}

DeepForest.Map = {North:     DeepForest3,
                  Northeast: DeepForest5,
                  East:      DeepForest5,
                  Southeast: DeepForest2,
                  South:     DeepForest2,
                  Southwest: DeepForest2,
                  West:      DeepForest,
                  Northwest: DeepForest}

DeepForest2.Map = {North:     DeepForest,
                   Northeast: DeepForest,
                   East:      DeepForest5,
                   Southeast: BirchGrove,
                   South:     BeechCopse,
                   Southwest: DeepForest6,
                   West:      DeepForest2,
                   Northwest: DeepForest2}

DeepForest3.Map = {North:     NorthWall2,
                   Northeast: NorthWall2,
                   East:      DeepForest4,
                   Southeast: DeepForest,
                   South:     DeepForest,
                   Southwest: DeepForest,
                   West:      MapleStand,
                   Northwest: NorthWall2}

DeepForest4.Map = {North:     NorthWall4,
                   Northeast: NorthWall4,
                   East:      DeepForest4,
                   Southeast: DeepForest7,
                   South:     Clearing,
                   Southwest: Clearing,
                   West:      DeepForest3,
                   Northwest: DungeonEntrance}

DeepForest5.Map = {North:     DeepForest4,
                   Northeast: TopOfMound,
                   East:      BottomOfCliff,
                   Southeast: SouthWall3,
                   South:     DeepForest6,
                   Southwest: DeepForest6,
                   West:      DeepForest2,
                   Northwest: ForestWithCave}

DeepForest6.Map = {North:     ForestWithCave,
                   Northeast: DeepForest5,
                   East:      DeepForest5,
                   Southeast: SouthWall2,
                   South:     SouthWall2,
                   Southwest: SouthWall2,
                   West:      BeechCopse,
                   Northwest: DeepForest2}

DeepForest7.Map = {North:     NorthWall5,
                   Northeast: NorthWall5,
                   East:      BottomOfCliff,
                   Southeast: BottomOfCliff,
                   South:     BottomOfCliff,
                   Southwest: DeepForest4,
                   West:      DeepForest4,
                   Northwest: NorthWall5}

DungeonEntrance.Map = {North:     NorthWall3,
                       Northeast: NorthWall3,
                       East:      DeepForest4,
                       Southeast: DeepForest4,
                       South:     DeepForest,
                       Southwest: DeepForest,
                       West:      DeepForest3,
                       Northwest: NorthWall3,
                       Down:      u"""
                                  The sand in the depression is fairly loose,
                                  but digging downward (even if you  had a
                                  shovel) is likely to be pointless.
                                  """,
                       Up:        u"The blockhouse isn’t climbable.",
                       In:        u"""
                                  The blockhouse door is locked. As you
                                  attempt to enter a deep booming voice says
                                  ~i »Dungeon under construction, no
                                  admittance!« ~l
                                  """}

EastLedge.Map = {North:     u"The ledge disappears after only a few feet.",
                 South:     u"The ledge disappears after only a few feet.",
                 Southwest: EastLedge.NoExit,
                 West:      EastLedge.NoExit,
                 Northwest: EastLedge.NoExit,
                 Up:        TopEastLedge,
                 Down:      BottomOfCliff}

ForestCave.Map = {North:     ForestCave.NoExit,
                  Northeast: ForestCave.NoExit,
                  East:      ForestCave.NoExit,
                  Southeast: ForestCave.NoExit,
                  South:     ForestCave.NoExit,
                  Southwest: ForestCave.NoExit,
                  West:      ForestCave.NoExit,
                  Northwest: ForestCave.NoExit,
                  Up:        ForestWithCave,
                  Down:      u"There are no openings in the cave’s floor."}

ForestWithCave.Map = {North:     DeepForest2,
                      Northeast: DeepForest5,
                      East:      DeepForest5,
                      Southeast: DeepForest5,
                      South:     DeepForest6,
                      Southwest: DeepForest2,
                      West:      DeepForest2,
                      Northwest: DeepForest2,
                      Down:      ForestCave}

FurtherUpATree.Map = {North:     FurtherUpATree.NoExit,
                      Northeast: FurtherUpATree.NoExit,
                      East:      FurtherUpATree.NoExit,
                      Southeast: FurtherUpATree.NoExit,
                      South:     FurtherUpATree.NoExit,
                      Southwest: FurtherUpATree.NoExit,
                      West:      FurtherUpATree.NoExit,
                      Northwest: FurtherUpATree.NoExit,
                      Up:        TreeTop,
                      BeechTree: TreeTop,
                      Down:      UpATree}

GypsumCave.Map = {East: GypsumPassage,
                  West: Clearing}

GypsumPassage.Map = {Northeast: HermitCave,
                     South:     BottomOfCliff,
                     West:      GypsumCave}

HermitCave.Map = {South: GypsumCave}

Hill.Map = {North:     DeepForest,
            Northeast: DeepForest,
            East:      Clearing,
            Southeast: DeepForest2,
            South:     DeepForest2,
            Southwest: DeepForest2,
            West:      A3WayPath2,
            Northwest: DeepForest,
            Up:        u"You are on the TOP of a hill, remember?",
            Down:      Clearing}

MapleStand.Map = {North:     NorthWall1,
                  Northeast: DeepForest,
                  East:      DeepForest3,
                  Southeast: DeepForest,
                  South:     NorthPath,
                  Southwest: DeepForest,
                  West:      DeepForest,
                  Northwest: DeepForest,
                  Up:        u"The trees here are not climbable.",
                  Down:      u"There’s no way to go down."}

NorthWall1.Map = {East:      NorthWall2,
                  Southeast: MapleStand,
                  South:     MapleStand,
                  Southwest: MapleStand}

NorthWall2.Map = {East:      NorthWall3,
                  Southeast: DeepForest3,
                  South:     DeepForest3,
                  Southwest: DeepForest3,
                  West:      NorthWall1}

NorthWall3.Map = {East:      NorthWall4,
                  Southeast: DungeonEntrance,
                  South:     DungeonEntrance,
                  Southwest: DungeonEntrance,
                  West:      NorthWall2}

NorthWall4.Map = {East:      NorthWall5,
                  Southeast: DeepForest4,
                  South:     DeepForest4,
                  Southwest: DeepForest4,
                  West:      NorthWall3}

NorthWall5.Map = {East:      BottomOfCliff,
                  Southeast: DeepForest7,
                  South:     DeepForest7,
                  Southwest: DeepForest7,
                  West:      NorthWall4}

NorthPath.Map = {North:     MapleStand,
                 Northeast: DeepForest,
                 East:      DeepForest,
                 Southeast: DeepForest,
                 South:     A4WayPath,
                 Southwest: DeepForest,
                 West:      DeepForest,
                 Northwest: DeepForest}

SouthWall1.Map = {East:      SouthWall2,
                  Northeast: BeechCopse,
                  North:     BeechCopse,
                  Northwest: BeechCopse,
                  West:      BeechCopse}

SouthWall2.Map = {East:      SouthWall3,
                  Northeast: DeepForest6,
                  North:     DeepForest6,
                  Northwest: DeepForest6,
                  West:      SouthWall1}

SouthWall3.Map = {Northeast: BottomOfCliff,
                  North:     DeepForest5,
                  Northwest: DeepForest5,
                  West:      SouthWall2}

TopEastLedge.Map = {North:     u"The ledge disappears after only a few feet.",
                    South:     u"The ledge disappears after only a few feet.",
                    Southwest: TopEastLedge.NoExit,
                    West:      TopEastLedge.NoExit,
                    Northwest: TopEastLedge.NoExit,
                    Up:        u"""
                               The cliff bulges outward above you, preventing
                               further climbing.
                               """,
                    Down:      EastLedge}

TopOfMound.Map = {North:     DeepForest7,
                  Northeast: DeepForest7,
                  East:      BottomOfCliff,
                  Southeast: DeepForest5,
                  South:     DeepForest5,
                  Southwest: DeepForest5,
                  West:      Clearing,
                  Northwest: DeepForest4,
                  Up:        u"TOP of the mound, remember?",
                  Down:      u"Down in which (of many possible) directions?"}

TreeTop.Map = {North:     TreeTop.NoExit,
               Northeast: TreeTop.NoExit,
               East:      TreeTop.NoExit,
               Southeast: TreeTop.NoExit,
               South:     TreeTop.NoExit,
               Southwest: TreeTop.NoExit,
               West:      TreeTop.NoExit,
               Northwest: TreeTop.NoExit,
               Up:        u"""
                          In case you had forgotten, you’re in a tree TOP,
                          remember?  The only way up is with wings.
                          """,
               BeechTree: u"""
                          In case you had forgotten, you’re in a tree TOP,
                          remember?  The only way up is with wings.
                          """,
               Down:      FurtherUpATree}

UpATree.Map = {North:     UpATree.NoExit,
               Northeast: UpATree.NoExit,
               East:      UpATree.NoExit,
               Southeast: UpATree.NoExit,
               South:     UpATree.NoExit,
               Southwest: UpATree.NoExit,
               West:      UpATree.NoExit,
               Northwest: UpATree.NoExit,
               Up:        FurtherUpATree,
               BeechTree: FurtherUpATree,
               Down:      BeechCopse}


#*********************************************************************
#                   End of Thief's Quest Game Library
#*********************************************************************
