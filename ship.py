"""
FASA Star Trek Tactical Starship Combat Simulator (TSCS)

Ship module
The goal is to use a pair of high-res ship images and prepare them as needed for use
in the game. Only one frame of the top view is needed for in-game rendering, and the
side view is for the ship detail "screens". 

The Ship class pre-renders the hex angles (60 degrees per turn) for quicker rendering.

Keep in mind this is a turn-based game so framerate is not extremely important. 
However, we'll try to be as efficient as possible anyway.

Ship art should be a high-res 512px image and will be scaled as needed.

The ship specifications should be loaded from a data file. Currently just showing design info.

***NOTE***
In the FASA ship recognition books, the first column of data (Mk I) will be closer to the
original specs of a ship in the TV series/films. The additional model columns were invented
by FASA to bring ships forward in time to the film-era or the TNG-era (see the dates).
So, it's better to use the Mk I column because later models are OP.
If you WANT to add a later model, add the model to the classname, e.g. Constellation Mk II.

"""

import pygame
import pygame_gui
import json
from xml.etree import ElementTree as et

class Specs(object):
    def __init__(self):
        self.classname = ""
        self.hulltype = ""

    def load(self,filename):
        #load from specs file
        print("Parsing file: " + filename + "...")

        with open(filename, "r") as read_file:
            data = json.load(read_file)
        
        self.classname = data["classname"]
        self.hulltype = data["hulltype"]
        
    def save(self,filename):
        #save to specs file
        print("Saving file: " + filename + "...")
        with open(filename, "w") as write_file:
            json.dump(self, write_file)

    def __str__(self):
        s = "classname=" + self.classname + "\n"
        s+= "hulltype=" + self.hulltype + "\n"
        return s
    
#
# Ship class
#
class Ship(object):
    def __init__(self):
        #super(Ship,self).__init__()
        self.dir = 0
        self.scale = 0.25
        self.image_top=None
        self.rect=None
        self.gui=None
        #this stores the 6 pre-rotated 'hex' images
        self.rotimglist = []

        self.specs = Specs()

    """
    These properties could have been put into MyLibrary.Sprite, but I opted
    instead to make this class more self contained since it has already veered
    away from being strictly about the ship 'Sprite'. Instead, think of this 
    class as a 'miniature' used on the hex map combined with the player's
    ship 'data sheet'.
    """
    #x property from topleft
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    x = property(_getx,_setx)

    #y property from topleft
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    y = property(_gety,_sety)

    #position property returns the topleft
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos  
    position = property(_getpos,_setpos)
    
    #centerx position based on center of the image rect
    def _getcenterx(self): return self.rect.centerx
    def _setcenterx(self,value): self.rect.centerx = value
    centerx = property(_getcenterx,_setcenterx)
    
    #centery position based on center of the image rect
    def _getcentery(self): return self.rect.centery
    def _setcentery(self,value): self.rect.centery = value
    centery = property(_getcentery,_setcentery)
    

    def __str__(self):
        return str(self.rect)
        
    def load_specs(self,filename):
        self.specs.load(filename)
        
    def load_top(self, filename):
        self.image_top = pygame.image.load(filename).convert_alpha()
        self.image_top.set_colorkey((0,0,0,255))
        self.rect = self.image_top.get_rect()
        #print("\nShip constructor:")
        #create 6 hex-oriented rotation images
        for angle in range(0,6):
            #clockwise is negative
            tempimg = pygame.transform.rotozoom(self.image_top, angle*-60, self.scale)
            tempimg.set_colorkey((0,0,0,255))
            #remove extra space around sprite pixels
            minrect = tempimg.get_bounding_rect()
            #pygame.draw.rect(tempimg, (255,255,255), minrect, 1)
            minimg = pygame.Surface((minrect.width,minrect.height))
            #grab the minimal image
            minimg.blit(tempimg, minrect)
            #print("Rotated Image " + str(angle) + ": " + str(tempimg.get_size()) + ", Minrect: " + str(minrect))
            #add to the list
            self.rotimglist.append(tempimg)

    def load_side(self, filename):
        #side view image used in tactical screen
        self.image_side = pygame.image.load(filename).convert_alpha()
        self.image_side.set_colorkey((0,0,0,255))
    

    #draw rotated image based on hex dir (0-5, 0=up)
    #position is based on the center point
    def draw(self, target):
        img = self.rotimglist[self.dir]
        r = img.get_rect()
        r.centerx = self.rect.centerx
        r.centery = self.rect.centery
        target.blit(img, r)
        
    #draw the side view image based at the center point
    def draw_sideview(self, target, position):
        rect = self.image_side.get_rect()
        rect.center = position
        target.blit(self.image_side, target)
        
    def build_details_window(self,gui):
        self.gui=gui
        window_pos=(500,100)
        window_size=(600,800)
        guiwin_ship = pygame_gui.elements.ui_window.UIWindow(
            rect=pygame.Rect(window_pos,window_size),
            window_display_title = self.specs.classname + " Class " + self.specs.hulltype,
            element_id="guiwin_ship",
            manager=self.gui
        )

        """
        #ship name label
        guilbl_name = pygame_gui.elements.ui_label.UILabel(
            relative_rect=pygame.Rect(0,0,guiwin_ship.rect.width,20),
            text="Excelsior Class XII-XIV Battleship",
            container=guiwin_ship,
            manager=self.gui
        )
        """
    
        #ship top image rendered left
        s = pygame.transform.rotozoom(self.image_top, 90, 1.0).convert_alpha()
        r = s.get_rect()
        w,h = r.width,r.height
        guiimg_ship = pygame_gui.elements.ui_image.UIImage(
            relative_rect=pygame.Rect((20,0),(w,h)),
            image_surface=s,
            container=guiwin_ship,
            manager=self.gui
        )

        #ship side image
        r=self.image_side.get_rect()
        w,h = r.width,r.height
        guiimg_ship_side = pygame_gui.elements.ui_image.UIImage(
            relative_rect=pygame.Rect((10,200),(w,h)),
            image_surface=self.image_side,
            container=guiwin_ship,
            manager=self.gui
        )

        #specifications
        #obviously this needs to pull actual ship data from a file...
        #just testing the look & feel here for now...
        
        s = "Superstructure Points..............<b>" + "42" + "</b><br>"
        s+= "Damage Chart.......................<b>" + "C" + "</b><br>"
        s+= "Size L/W/H (meters)................<b>" + "467 / 186 / 78" + "</b><br>"
        s+= "Weight (metric tons)...............<b>" + "243,610" + "</b><br>"
        s+= "Crew...............................<b>" + "800" + "</b><br>"
        s+= "Total Power Units Available........<b>" + "116" + "</b><br>"
        s+= "Movement Point Ratio...............<b>" + "6/1" + "</b><br>"
        s+= "Warp Engine Type...................<b>" + "FTWA (x2)" + "</b><br>"
        s+= "  Power Units Available............<b>" + "38" + "</b><br>"
        s+= "  Stress Charts....................<b>" + "D/F" + "</b><br>"
        s+= "  Maximum Safe Cruising Speed......<b>" + "Warp 12" + "</b><br>"
        s+= "  Emergency Speed..................<b>" + "Warp 14" + "</b><br>"
        s+= "Impulse Engine Type................<b>" + "FIG-3" + "</b><br>"
        s+= "  Power Units Available............<b>" + "40" + "</b><br>"
        s+= "Beam Weapon Type...................<b>" + "FH-11 (x10)" + "</b><br>"
        s+= "  Fore Firing Arcs.................<b>" + "2 / 2 / 2" + "</b><br>"
        s+= "  Aft Firing Arcs..................<b>" + "2 / 0 / 2" + "</b><br>"
        s+= "  Firing Chart.....................<b>" + "Y" + "</b><br>"
        s+= "  Maximum Power....................<b>" + "10" + "</b><br>"
        s+= "  Damage Modifiers" + "<br>"
        s+= "    +3.............................<b>" + "1-10" + "</b><br>"
        s+= "    +2.............................<b>" + "11-17" + "</b><br>"
        s+= "    +1.............................<b>" + "18-24" + "</b><br>"
        s+= "Beam Weapon Type...................<b>" + "FH-5 (x8)<br>"
        s+= "  Fore Firing Arcs.................<b>" + "2 / 0 / 2" + "</b><br>"
        s+= "  Aft Firing Arcs..................<b>" + "2 / 0 / 2" + "</b><br>"
        s+= "  Firing Chart.....................<b>" + "R" + "</b><br>"
        s+= "  Maximum Power....................<b>" + "4" + "</b><br>"
        s+= "  Damage Modifiers" + "<br>"
        s+= "    +3.............................<b>" + "0-0" + "</b><br>"
        s+= "    +2.............................<b>" + "1-8" + "</b><br>"
        s+= "    +1.............................<b>" + "9-16" + "</b><br>"
        s+= "Missile Weapon Type................<b>" + "FP-4 (x6></b><br>"
        s+= "  Fore Firing Arcs.................<b>" + "1 / 1 / 1" + "</b><br>"
        s+= "  Aft Firing Arcs..................<b>" + "1 / 1 / 1" + "</b><br>"
        s+= "  Firing Chart.....................<b>" + "S" + "</b><br>"
        s+= "  Power To Arm.....................<b>" + "1" + "</b><br>"
        s+= "  Damage...........................<b>" + "20" + "</b><br>"
        s+= "Deflector Shield Type..............<b>" + "FSS" + "</b><br>"
        s+= "  Shield Point Ratio...............<b>" + "1/4" + "</b><br>"
        s+= "  Maximum Shield Power.............<b>" + "20" + "</b><br>"
        s+= "Combat Efficiency" + "<br>"
        s+= "  D / WDF..........................<b>" + "198 / 182" + "</b><br>"
        
        r = guiwin_ship.rect
        guitxt_ship = pygame_gui.elements.ui_text_box.UITextBox(
            relative_rect=pygame.Rect(10,300,r.width-50,400),
            html_text="",
            container=guiwin_ship,
            manager=gui
        )
        guitxt_ship.html_text = s
        guitxt_ship.rebuild()
        
        
    
