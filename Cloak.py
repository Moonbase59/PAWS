# -*- coding: utf-8 -*-

# COD version 1.3 modified slightly by Wolf to take advantage of new features
# available in PAWS version 1.3.
# Modified again by Matthias C. Hormann to be compatible with PAWS 2.1 (Unicode).

#=================
# Import Libraries
#=================

# import the engine and world library.

#from PAWS import *
#from Universe import *
# The ONLY change needed fpr PAWS 2.03:
from PAWS.Core import *
from PAWS.Universe import *


#==========
# Game data
#==========

# Set common game related information like who the author is, the game's
# copyright, name, and version. IntroText is the text that appears just before
# the player gives their first command.

Game.Author = u"Roger Firth (implemented by Neil Cerutti)"
Game.Copyright = u"1999-2002"
Game.Name = u"Cloak of Darkness"
Game.Version = u"1.3"

Game.IntroText = u"""
    Hurrying through the rainswept November night, you're glad to see the
    bright lights of the Opera House. It's surprising that there aren't more
    people about, but, hey, what do you expect from a cheap demo game? ~p
    """

#------------
# Game Set Up
#------------

# Always written by the author, the last chance to perform custom set up before
# the game begins. Normally it sets 3 things: whether the game is in production
# (all done and ready to play), which character the player will play, and where
# that character starts.

def CloakUserSetUpGame():
    Global.Production = FALSE
    P.AP().CurrentActor = Global.Player
    P.CA().StartingLocation = Foyer

#-------------
# Game Wrap Up
#-------------

# Always written by the author, this is the final chance to print text to the
# screen before the game ends.

def CloakPostGameWrapUp():
    if not Bar.Visited: return

    if Sawdust.TrampleState < 2:
        Say(u"~p *** You have won. *** ~p ")
    else:
        Say(u"~p *** You have lost. *** ~p ")

#---------------------------------------
# Hook Author's Set Up/Wrap Up To Engine
#---------------------------------------

# This is how you tell the PAWS engine to use your functions instead of the
# default ones (which don't do much).

Engine.UserSetUpGame = CloakUserSetUpGame
Engine.PostGameWrapUp = CloakPostGameWrapUp

#==============
# Rooms In Game
#==============

# There are 3 rooms in the game, the Foyer, the Bar, and the Cloakroom. A fourth
# "room" (Nowhere) is actually a way to create a room that complains, refuses
# entry, and tramples the message.

#--------------------------------------
# Blueprint for Cloak Of Darkness Rooms
#--------------------------------------

# Since all the rooms are pretty much the same, all rooms can be created
# from a single "blueprint", or a slightly modified version of the blueprint.
# Either way, this room blueprint does all the heavy lifting.

class ClassCODRoom(ServiceDictDescription, ClassRoom):
    """Blueprint for all rooms in game."""

    #-------------------
    # Set Default Values
    #-------------------

    # Any properties you set in SetMyProperties() will be inherited automatically
    # by rooms created from it. In this case the rooms will be lit by default.

    def SetMyProperties(self):
        self.IsLit = TRUE

    #-----------------
    # Feel Description
    #-----------------

    # This method lets us use the Feel method from ClassRoom, which is better
    # than the one from the description service ServiceDictDescription for this
    # game.

    def FeelDesc(self): return ClassRoom.FeelDesc(self)

#---------------
# Northern Foyer
#---------------

# All we have to do is create the room, then set the room's name and long
# description. All the other senses (sound, smell, taste, touch) already have
# reasonable defaults.

Foyer = ClassCODRoom()

Foyer.NamePhrase = u"Foyer of the Opera House"

Foyer.SetDesc(u"L", u"""
                  You are standing in a spacious hall, splendidly decorated in
                  red and gold, with glittering chandeliers overhead. The
                  entrance from the street is to the north, and there are
                  doorways south and west.
                  """)

#-----------
# Cloak Room
#-----------

Cloakroom = ClassCODRoom()

Cloakroom.NamePhrase = u"Cloakroom"

Cloakroom.SetDesc(u"L", u"""
                      The walls of this small room were clearly once lined with
                      hooks, though now only one remains. The exit is a door to
                      the east.
                      """)

#--------------
# Bar Blueprint
#--------------

# The bar is a little more complex, but we base the bar's blueprint on the
# ClassCODRoom and just add a new method to easily turn the lights on and off.

class ClassBar(ClassCODRoom):
    """Blueprint for bar, based on a regular COD room"""

    def SetIsLit(self, LightStatus):
        """
        Allows for easy changing of the Bar's IsLit property in CBEs. A routine
        called in a CBE must return a string.
        """

        self.IsLit = LightStatus

        return u""

#--------
# The Bar
#--------

# Like the Foyer and the Cloak Room we set the bar's name and long description
# but we also turn off the lights

Bar = ClassBar()

Bar.NamePhrase = u"Foyer Bar"

Bar.SetDesc(u"L", u"""
                The bar, much rougher than you expected after the opulence of the
                northern foyer, is completely empty. There seems to be some sort
                of message scrawled in the sawdust on the floor.
                """)

Bar.SetDesc(u"Floor", u"{Sawdust.ReadDesc()}")

Bar.IsLit = FALSE

#------------------
# Nowhere Blueprint
#------------------

# Based on the standard COD room blueprint, this room has a different Enter()
# method. It refuses to let the player enter the room, complains, and tramples
# the message.

class ClassNowhere(ClassCODRoom):
    def Enter(self, Object):
        Say(u"Blundering around in the dark isn't a good idea.")
        Sawdust.TrampleState = Sawdust.TrampleState + 2
        return FAILURE

#------------
# Create Room
#------------

# Notice the room doesn't need a long description because it will never
# let the player inside in the first place.

Nowhere = ClassNowhere()
Nowhere.NamePhrase = u"Nowhere Room"

#================
# Objects In Game
#================

# The game contains three objects, the cloak, the hook, and the message.

#----------------
# Cloak Blueprint
#----------------

# The cloak is pretty normal except you can't drop it anywhere. So we base the
# cloak blueprint on ClassItem blueprint (which is used for normal things the
# player can pick up) and just change the Drop() method.

class ClassCloak(ClassItem):
    def Drop(self, Multiple=FALSE):
        """You can't put the cloak anywhere but on the hook."""
        Say(u"This isn't the best place to leave a smart cloak lying around.")
        return FAILURE

#----------
# The Cloak
#----------

# When we create the cloak we tell PAWS what nouns will refer to the cloak, then
# what adjectives. We give it a starting location (the player) and set its bulk
# and weight, then set the long and take descriptions.
#
# Notice the curly brace expression? CBE's allow you to put code inside pieces of
# text to make them more flexible.

Cloak = ClassCloak(u"cloak", u"velvet,black,satin,dark,handsome")

Cloak.StartingLocation = Global.Player
Cloak.Bulk = 1
Cloak.Weight = 10

Cloak.SetDesc(u"L", u"""
                   A handsome cloak, of velvet trimmed with satin, and
                   slightly spattered with raindrops. Its blackness is so
                   deep that it almost seems to suck light from the room.
                   """)

Cloak.SetDesc(u"Take", u"{Bar.SetIsLit(FALSE)}Taken.")

#---------------------
# Brass Hook Blueprint
#---------------------

# The brass hook is a "shelf", a thing you can put other things on. It's ALSO a
# light switch IF the cloak is put on the hook. Notice once we deal with the
# light switch aspect we actually use the Enter() method from ClassShelf to do
# all the real work.

class ClassHook(ClassShelf):

    def Enter(self, Object):
        """Turn on the light in the Bar when player puts the cloak on the hook."""
        if Object == Cloak: Bar.SetIsLit(TRUE)
        return ClassShelf.Enter(self, Object)

#---------
# The Hook
#---------

# We create the hook, set the maximum bulk and weight it will hold, set its
# starting location, the complaint if the player tries to take it, and the
# long description. Notice the CBE in the long description.

Hook = ClassHook(u"hook,peg", u"small,brass")

Hook.MaxBulk = 1
Hook.MaxWeight = 10
Hook.StartingLocation = Cloakroom

Hook.SetDesc(u"Take", u"The hook is screwed to the wall.")

Hook.SetDesc(u"L", u"""
                  It's just a small brass hook,
                  {Choose (Cloak in Self().Contents,
                           u" with a cloak hanging on it.",
                           u" screwed to the wall.")}
                  """)

#--------------------------
# Sawdust Message Blueprint
#--------------------------

# The message is scenery--it won't be described as a seperate item unless the
# player specifically examines it. SetMyProperties() let's us add a TrampleState
# property.
#
# The ReadDesc() does more than simply return the message. It also signals the
# game is over so the natural game cycle will cause the game to end before the
# player can type in another command.

class ClassSawdust(ClassScenery):
    def SetMyProperties(self):
        self.TrampleState = 0

    def ReadDesc(self):
        Global.GameState = FINISHED
        if self.TrampleState < 2:
            return u"The message, neatly marked in the sawdust, reads …"
        else:
            return u"""The message has been carelessly trampled, making it
                   difficult to read. You can just distinguish the
                   words …
                   """

#--------------------
# The Sawdust Message
#--------------------

# All we need are the message long description (notice the CBE which takes the
# long description from the read description) and the message's starting location.

Sawdust = ClassSawdust(u"message,sawdust,floor")
Sawdust.SetDesc(u"L", u"{Self().ReadDesc()}")
Sawdust.ParserFavors = TRUE
Sawdust.StartingLocation = Bar

#--------
# The map
#--------

# Maps are defined last in PAWS because all rooms referenced on the map must
# already have been defined. We have maps for the 3 rooms the player can actually
# enter, the Nowhere room refuses the player entry but still provides a text
# message.
#
# Also notice we don't have to provide map directions for directions that aren't
# valid, the system takes care of that for you.

Foyer.Map = {North: u"""
                    You've only just arrived and besides, the weather
                    outside seems to be getting worse.
                    """,
             South: Bar,
             West: Cloakroom}

Cloakroom.Map = {East: Foyer}

Bar.Map = {North:      Foyer,
           Northeast:  Nowhere,
           East:       Nowhere,
           Southeast:  Nowhere,
           South:      Nowhere,
           Southwest:  Nowhere,
           West:       Nowhere,
           Northwest:  Nowhere,
           Up:         Nowhere,
           Down:       Nowhere,
           Upstream:   Nowhere,
           Downstream: Nowhere,
           In:         Nowhere,
           Out:        Nowhere}
