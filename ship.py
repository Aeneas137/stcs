"""
FASA Star Trek Tactical Starship Combat Simulator (TSCS)

ship module

"""

import pygame

#
# Ship class
#
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship,self).__init__()
        self.dir = 0
        self.scale = 0.25
        self.surf = pygame.image.load("fed_enterprise.png").convert_alpha()
        self.surf.set_colorkey((0,0,0,255))
        self.rect = self.surf.get_rect()
        print("Ship constructor:")
        #create 6 hex-oriented rotation images
        self.rotimglist = []
        for angle in range(0,6):
            #clockwise is negative
            tempimg = pygame.transform.rotozoom(self.surf, angle*-60, self.scale)
            tempimg.set_colorkey((0,0,0,255))
            #remove extra space around sprite pixels
            minrect = tempimg.get_bounding_rect()
            #pygame.draw.rect(tempimg, (255,255,255), minrect, 1)
            minimg = pygame.Surface((minrect.width,minrect.height))
            #grab the minimal image
            minimg.blit(tempimg, minrect)
            print("Image " + str(angle) + ": " + str(tempimg.get_size()) + ", Minrect: " + str(minrect))
            #add to the list
            self.rotimglist.append(tempimg)

    #draw rotated image based on hex dir (0-5, 0=up)
    def draw(self, target):
        img = self.rotimglist[self.dir]
        r = img.get_rect()
        r.centerx = self.rect.centerx
        r.centery = self.rect.centery
        target.blit(img, r)

