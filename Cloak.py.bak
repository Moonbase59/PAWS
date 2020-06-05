# -*- coding: utf-8 -*-

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                                 Cloak Of Darkness                             #
#                              Created by Roger Firth                           #
#                     Implemented by Neil Cerutti (c) 1999-2002                 #
#                 Updated for PAWS 2.1 by Matthias C. Hormann 2016              #
#                                                                               #
# The C="""...""" statements scattered throughout this source code are actually #
# a work-around for Python's lack of block comments. Notepad++ can only fold    #
# block comments, not a series of comment lines. Using C="""...""" doesn't      #
# increase PAWS memory footprint, although it does have a tiny impact           #
# on loading time.                                                              #
#                                                                               #
C="""
  Although a tiny game, (3 rooms, 3 objects) the real point of this game is
  to be a Rosetta Stone for interactive fiction. At the Cloak Of Darkness
  website (http://www.firthworks.com/roger/cloak/index.html) the game is
  available in 20 different authoring languages to show a prospective author
  how a language "feels".                                                                      #

  This file follows PAWS Style Guidelines and is annotated for study by
  novice game authors. Therefore it's VERY verbose, with tons of comments
  about even the smallest detail--far too bulky for the Cloak Website. The
  file called CloakRS.py (Rosetta Stone) is the one on the Cloak website. It
  has far fewer comments, so if you want a bare bones sample, look there.
  CloakRS.py is also included as part of the PAWS download.

  This version also dispenses with the end game wrap up, simplifying things.

  Created by: Roger Firth                                                       #
  Originally Implemented by: Neil Cerutti                                       #
  Originally Implemented on: 09/24/2000                                         #
  Refactored By: Roger Plowman
  Refactored On: 12/14/2007
  Refactored By: Matthias C. Hormann
  Refactored On: 2016-11-16
  """
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
#********************************************************************************

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

#*******************************************************************************
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

Game.Author = u"Roger Firth (implemented by Neil Cerutti)"
Game.Copyright = u"1999-2000"
Game.Name = u"Cloak of Darkness"
Game.Version = u"1.5"

Game.IntroText = u"""
                 Hurrying through the rainswept November night, you’re glad
                 to see the bright lights of the Opera House. It’s
                 surprising that there aren’t more people about, but, hey,
                 what do you expect from a cheap demo game? ~p
                 """

#*******************************************************************************
#                  G A M E   S E T U P   /   W R A P U P
#
C="""
  Every game you write has to have a "user set up". This is where you can do
  anything special needed to set up your game. Fortunately, very few games
  need anything unusual in terms of setup, so you can copy the setup from
  one game to another.

  The only thing you have to do is change the name of your setup function,
  and change the StartingLocation to the room the player starts in.

  """

def CloakUserSetUpGame():
    Global.Production = FALSE
    P.AP().CurrentActor = Global.Player
    P.CA().StartingLocation = Foyer

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

Engine.UserSetUpGame = CloakUserSetUpGame   # Always copy this line

#*******************************************************************************
#                            R O O M   B L U E P R I N T S
#
C="""
  Python requires every object you create have a blueprint. Python calls
  that blueprint a "class". The word class comes from the ivory tower
  computer scientists who created the idea of objects in the first place. So
  don't worry about it, just remember "class = blueprint".

  The advantage of using classes (blueprints) to create objects should be
  obvious. Create a single blueprint and you can use that blueprint to
  create not just one object, but many different objects.

  In a game as small as this one it's hard to see why blueprints (classes)
  give you an advantage. Consider this. There are 4 rooms in Cloak, the
  Foyer, the Bar, the Cloakroom and the special Nowhere room.

  But there are only 3 room blueprints. The Foyer and the Cloakroom both use
  the MakeCODRoom blueprint. That's because while obviously very different,
  both rooms also have a lot in common. Blueprints (classes) let you
  leverage what's common between objects to your advantage. The larger your
  game, the larger the advantage becomes.
  """

class MakeCODRoom(ServiceDictDescription, ClassRoom):
    """
    This is a "doc string". A doc string is like a comment, but has the
    added advantage that Python can automatically collect and print the
    doc strings, helping you create automatic documentation. As a second
    advantage doc strings vanish along with the rest of the class when you
    fold the file using Notepad++.

    Now let's talk about this class. We're going to use it to create the
    rooms in Cloak. Notice that there are two other classes (blueprints)
    used to start this class: ServiceDictDescription and ClassRoom.

    That brings up an important point. Blueprints almost always start from
    other blueprints. That means whatever those two classes can do,
    MakeCODRoom can ALSO do--without you coding a thing!

    In other words, MakeCODRoom will ADD functionality on top of whatever
    functionality it inherited from ServiceDictDescription and ClassRoom.
    """
    def SetMyProperties(self):
        """
        This method allows you to change properties you inherited from other
        classes, or create new properties. In this case we inherited IsLit
        from ClassRoom. But IsLit is normally FALSE--in other words rooms
        are dark.

        Obviously, we want rooms lit unless we specifically say otherwise.
        """
        self.IsLit = TRUE

    def FeelDesc(self):
        """
        We inherited this method from ServiceDictDescription, but we
        actually want the one from ClassRoom instead. The code below lets
        us call FeelDesc() from ClassRoom, and that gives us the description
        we want.
        """

        return ClassRoom.FeelDesc(self)

class MakeBar(MakeCODRoom):
    """
    We're basing the bar blueprint on the MakeCODRoom blueprint (class,
    remember class = blueprint).

    By doing that we gain all the capabilities of MakeCODRoom for free. All
    this blueprint adds is a way to turn the lights on and off.
    """

    def SetIsLit(self, LightStatus):
        """
        This method sets IsLit for the room to whatever LightStatus is.
        LightStatus will either be TRUE or FALSE, depending on where the
        cloak is. We'll talk about this method more when we actually call
        it.
        """

        self.IsLit = LightStatus
        return ""

class MakeNowhere(MakeCODRoom):
    """
    This blueprint will be used to create the Nowhere room. Like MakeBar
    this blueprint starts with the MakeCODRoom blueprint (class). All we
    need to do is change the Enter method.
    """

    def Enter(self, Object):
        """
        The Enter method of a room checks to see if the object trying to
        enter the room is allowed to. If entry is allowed the method returns
        SUCCESS, if entry is not allowed it returns FAILURE.

        In this case we ALWAYS return FAILURE. The Complain() function
        prints the complaint to the screen but then returns FAILURE, so
        Enter() passes that failure back to the parser.

        If the bar is lit the complaint is the only thing that happens, but
        if the bar is NOT lit (is dark) we add 1 to the Trampled property
        of the sawdust, and give a different complaint.
        """

        if Bar.IsLit:
            return Complain(u"There’s no exit in that direction.")
        else:
            Sawdust.Trampled += 1
            return Complain(u"Blundering around in the dark isn’t a good idea.")


#*******************************************************************************
#                         T H I N G   B L U E P R I N T S
#
C="""
  As you'd expect, things use blueprints just like rooms do--and for exactly
  the same reason. In a small game like Cloak there are as many blueprints
  as there are things--but the larger the game, the larger the gain.
  """

class MakeCloak(ClassItem):
    """
    ClassItem is used to create objects that the player can pick up, drop,
    and carry--just like the cloak. The problem is, we don't want the
    player to drop the cloak. So we change the way drop works for MakeCloak.
    """
    def Drop(self, Multiple=FALSE):
        """We simply return a complaint, and the drop doesn't happen."""
        return Complain(u"""
                        This isn’t the best place to leave a smart cloak
                        lying around.
                        """)

class MakeHook(ServiceActivation, ClassShelf):
    """
    Blueprint for the hook. A shelf is any object that can have other
    objects put on it. Normally you'd think of a shelf--but a hook works
    exactly the same way for cloak, right?

    We just need to change the Enter method to turn the lights on in the
    bar.
    """

    def Enter(self, Object):
        """
        Turn on the light in the Bar when player puts the cloak on the hook.
        """
        if Object == Cloak: Bar.SetIsLit(TRUE)
        return ClassShelf.Enter(self, Object)

class MakeSawdust(ClassScenery):
    """
    The sawdust is scenery--a thing that the player can't take. But we also
    need to add some things to make the sawdust work like we need it to.
    """
    def SetMyProperties(self):
        """
        Add the Trampled property to track how much the player tramped
        around the bar in the dark.
        """

        self.Trampled = 0

    def ReadDesc(self):
        """
        Reading the message ends the game, one way or another. That's why
        we set the Global.GameState to FINISHED. Once this method ends
        the game ends.
        """

        #-------------
        # End The Game
        #-------------

        # Global GameState is normally RUNNING. Changing it to FINISHED signals
        # the engine that the game is over.

        Global.GameState = FINISHED

        #--------------
        # Trampled < 2?
        #--------------

        # If Trampled is less than 2 return the winning message.

        if self.Trampled < 2: return u"""
                                     The message, neatly marked in the
                                     sawdust, reads...

                                     ~p *** You have won. *** ~p
                                     """
        #----------------------
        # Return Losing Message
        #----------------------

        # By reaching this point we know Trampled is 2 or more, so the player
        # lost. Return the losing message. We could have used an ELSE clause on
        # the IF test above to return the losing message, but this is yet another
        # example of KISS--keeping it simple, Sam. :)
        #
        # IF tests are a break of the reader's concentration. IF ELSE tests are
        # even worse. Since there was no real need for ELSE, we didn't use it.
        # And made the program simpler to follow.

        return u"""
               The message has been carelessly trampled, making it
               difficult to read. You can just distinguish the words...

               ~p *** You have lost. *** ~p
               """
#*******************************************************************************
#                               M A K E   R O O M S
#
C="""
  In this section we finally start MAKING rooms! Up to now we've just been
  drawing blueprints, so to speak. But in this section we make the rooms the
  player will travel through.
  """

#--- Foyer

C="""
  The first line makes the Foyer object. Notice how naturally it reads?
  That's why we named the blueprint (the class) the way we did.

  NamePhrase is the name of the room. The SetDesc() method takes two
  arguments, the "L" (for long description) and the actual long description.
  """

Foyer = MakeCODRoom()
Foyer.NamePhrase = u"Foyer of the Opera House"
Foyer.SetDesc(u"L",u"""
                  You are standing in a spacious hall, splendidly decorated
                  in red and gold, with glittering chandeliers overhead. The
                  entrance from the street is to the north, and there are
                  doorways south and west.
                  """)

#--- Cloakroom

C="""
  The cloakroom is created the same way as the Foyer, using the same
  properties. The only difference is the text used! This demonstrates how
  useful the blueprint approach is. Imagine now if you had a hundred rooms
  to create?
  """

Cloakroom = MakeCODRoom()
Cloakroom.NamePhrase = u"Cloakroom"
Cloakroom.SetDesc(u"L",u"""
                      The walls of this small room were clearly once lined
                      with hooks, though now only one remains. The exit is a
                      door to the east.
                      """)

#--- Bar

C="""
  The bar is very similar, even though it uses a slightly different
  blueprint. One interesting item is the floor description (the 4'th line).
  Notice the curly braces? PAWS will read between the curly braces and
  replace the CBE (Curly Brace Expression) with the calculated value. In
  this case reading the floor of the bar does EXACTLY the same thing as
  reading the message directly!

  CBE's are an extremely useful technique and very simple to use.
  """

Bar = MakeBar()
Bar.NamePhrase = u"Foyer Bar"
Bar.IsLit = FALSE
Bar.SetDesc(u"Floor",u"{Sawdust.ReadDesc()}")
Bar.SetDesc(u"L",u"""
                The bar, much rougher than you expected after the opulence of the
                northern foyer, is completely empty. There seems to be some sort
                of message scrawled in the sawdust on the floor.
                """)

#--- Nowhere Room

C="""
  Since the Nowhere room is never actually entered, it doesn't need a long
  description, just a name.
  """

Nowhere = MakeNowhere()
Nowhere.NamePhrase = u"Nowhere Room"

#*******************************************************************************
#                                   M A K E   T H I N G S
#
C="""
  These are the things the player will interact with. But we're actually
  making them here, not just drawing blueprints.
  """

#--- Cloak

C="""
  Note there's a new wrinkle. When we made rooms there was nothing between
  the parentheses. But when you make a thing you need to specify two
  different groups of words between the parentheses. Each group of words is
  in quotes, with commas between them.

  The first group of words are nouns that describe the thing. "Cloak" in
  this case. The second group of words are adjectives describing the thing.
  We need the adjectives in case the player says something like "get black
  cloak".

  Also notice the CBE in the Take discription, this turns OFF the light in
  the bar--but since SetIsLit returns "", all the player sees is "Taken".
  """

Cloak = MakeCloak(u"cloak",u"velvet,black,satin,dark,handsome")
Cloak.StartingLocation = Global.Player
Cloak.Bulk = 1
Cloak.Weight = 10
Cloak.SetDesc(u"Take", u"{Bar.SetIsLit(FALSE)}Taken.")
Cloak.SetDesc(u"L", u"""
                   A handsome cloak, of velvet trimmed with satin, and
                   slightly spattered with raindrops. Its blackness is so
                   deep that it almost seems to suck light from the room.
                   """)

#--- Hook

C="""
  Same arrangement we saw when making the cloak, you need both nouns and
  adjectives, a long description, and so on. Notice there's a property
  called StartingLocation. This is the room the hook will be found in when
  the game starts.

  Also notice the CBE in the long description. The Choose() function returns
  TRUE if the cloak is in the hook's contents. In other words, hanging on
  the hook. Notice how the long description changes naturally?
  """

Hook = MakeHook(u"hook,peg",u"small,brass")
Hook.MaxBulk = 1
Hook.MaxWeight = 10
Hook.StartingLocation = Cloakroom
Hook.ActivateSpontaneousPhrase = u"I don’t know how to do that."
Hook.ActivatePassivePhrase = u"I don’t know how to do that."
Hook.SetDesc(u"Take", u"The hook is screwed to the wall.")
Hook.SetDesc(u"L", u"""
                  It’s just a small brass hook,
                  {Choose (Cloak in Self().Contents,
                           u" with a cloak hanging on it.",
                           u" screwed to the wall.")}
                  """)


#--- Sawdust

C="""
  There's a CBE in the long description but by now that's old news. The
  ParserFavors property is new, and will take a little explaining. Simply
  put, it means if two objects have the same name in the same place, the
  Sawdust will win.

  There's a floor (actually ground) object that's defined by Universe that
  is normally where the player is (it moves with the player). That lets the
  player say things like "look at floor".

  But the parser can confuse the floor and the sawdust under unusual
  circumstances. When that happens the ParserFavors property insures the
  Sawdust is picked instead of the ground.
  """

Sawdust = MakeSawdust(u"message,sawdust,floor")
Sawdust.SetDesc(u"L", u"{Self().ReadDesc()}")
Sawdust.ParserFavors = TRUE
Sawdust.StartingLocation = Bar

#*******************************************************************************
#                                      M A P S
#
C="""
  Maps have to be defined last because Python requires you define things
  before you use them. By putting the maps as the last part of the file
  we're making sure all rooms have already been created.

  Notice only the directions actually used are defined. If you don't define
  a direction PAWS will provide an appropriate complaint.
  """

Foyer.Map = {North: u"""
                    You’ve only just arrived and besides, the weather
                    outside seems to be getting worse.
                    """,
             South: Bar,
             West:  Cloakroom}

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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                       End Of Cloak Of Darkness Game                           #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
