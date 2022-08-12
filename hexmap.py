"""
FASA Star Trek Tactical Starship Combat Simulator (TSCS)

hexmap module

"""

import math
import pygame

def fontprint(target, font, text, pos, color):
    x,y=pos
    surf = font.render(text, True, color, None)
    #defaults to center=True for this module (for now)
    r = surf.get_bounding_rect()
    x-=r.width/2
    y-=r.height/2
    target.blit(surf, (x,y))

class Hexmap():
    def __init__(self): 
        super(Hexmap,self).__init__()
        self.jumptoggle = -1
        self.pi2 = math.pi * 2.0
        self.hexsize = 0

    def init(self, hexsize):
        self.hexsize = hexsize

        #create list of circles at hex locations (easier than hex-grid math)
        #each object in list contains (index,center) 
        #where index=hexmap x,y and center=screen x,y
        self.circles = []
        startx = self.hexsize+5
        starty = self.hexsize-5
        w = self.hexsize
        h = (self.hexsize-10)*2
        x = 0
        toggle=-1
        for x in range(0,15):
            px = startx+w*x
            for y in range(0,8):
                #store index and position of each hexagon in a list for easy lookup
                py = starty+h*y
                center=(px,py)
                index=(x,y)
                self.circles.append([index,center])
            toggle*=-1
            startx += int(self.hexsize / 2)
            starty += (self.hexsize-10) * toggle

    #
    #based on hexmap index, returns just the center position
    #
    def get_hex_center(self, index):
        #iterate hexmap circles
        for c in self.circles:
            index,center=c
            cx,cy=center
            x,y = index
            if x==cx and y==cy:
                return center
            
        return (-1,-1)
    
    
    #
    #searches circles list to find a circle containing x,y
    #returns hex index AND center position
    #
    def get_hex_at(self, pos):
        #iterate hexmap circles
        for c in self.circles:
            index,center=c
            d=int(math.dist(pos,center))
            if d < self.hexsize*0.8:
                return c
        return [(-1,-1),center]
    
    #
    #draws a single hexagon
    #for a filled hexagon, use width=0
    #
    def draw_hex(self, target, color, radius, position, width=1):
        vertices=6
        x, y = position
        pygame.draw.polygon(target, color, [
            (x + radius * math.cos(self.pi2 * i / vertices), y + radius * math.sin(self.pi2 * i / vertices))
            for i in range(vertices)
        ], width)
    
    #
    #draws a circle bounding the interior of the hexagon
    #mainly used for debugging the hexmap 
    #
    def draw_circles(self, target, color=(80,80,80), width=1):
        radius = int(self.hexsize*0.88)
        #iterate hexmap circles
        for c in self.circles:
            index,center=c
            pygame.draw.circle(target, color, center, radius, width)

    
    #
    #prints the index and position centered on each hexagon
    #(hex coords are q,r but since no hex math is being used, it doesn't matter)
    #
    def draw_labels(self, target, font, color=(150,150,150), showcenterlabel=False):
        #get font size (this is slow...)
        surf = font.render("ABC", True, (255,255,255), None)
        r = surf.get_bounding_rect()
        font_height=r.height+3

        #iterate hexmap circles
        for c in self.circles:
            index,center=c
            x,y=center
            indx,indy=index
            
            #print hexmap index (technically q,r but we're using distance instead)
            text = str('{:02d}'.format(indx)) + "-" + str('{:02d}'.format(indy+1))
            fontprint(target, font, text, (x,y), color)
            
            if showcenterlabel:
                #print hex center position in screen coords
                text = str(int(x))+","+str(int(y))
                fontprint(target, font, text, (x,y+font_height), color)
        

    #
    #draws all of the hexes in the hexmap
    #
    def draw(self, target, hex_color=(255,255,255)):
        #iterate hexmap circles
        for c in self.circles:
            index,center=c
            self.draw_hex(target, hex_color, self.hexsize, center, 2)

    