"""
FASA Star Trek Tactical Starship Combat Simulator (TSCS)

Requires:
    Python 3.10
    pygame 2.1
        pip install pygame
        https://www.pygame.org/docs/index.html
    pygame_gui 
        pip install pygame_gui -U
        https://pygame-gui.readthedocs.io/en/latest/modules.html
        
"""

import sys, time, random, math, pygame, pygame_gui
from pygame.locals import *
from MyLibrary import *
from hexmap import Hexmap
from ship import Ship

from pygame.locals import (
    K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,K_RETURN,K_SPACE,KEYDOWN,QUIT,
    K_a,K_s,K_d,K_f
)

#
# all globals must be pre-defined
#
SCREENW=0
SCREENH=0
running=False
screen=None
fontl=None
fonts=None
hexmap=None
ship=None

gui=None
guiwin_debug=None
guiwin_ship=None
guibtn_hello=None
guiimg_ship=None
guitxt_debug=None

#
# Initialization (be sure to call get_video_info() first)
#
def init_game():
    global screen, backbuffer, fontl, fonts, timer
    global hexmap, ship

    pygame.init()
    get_video_info()

    title = "FASA Starship Tactical Combat Simulator"
    pygame.display.set_caption(title + " (" + str(SCREENW) + "x" + str(SCREENH)+ ")")

    screen = pygame.display.set_mode(size=(SCREENW,SCREENH))
    #pygame.display.toggle_fullscreen()
    
    backbuffer = pygame.Surface((SCREENW,SCREENH))
    
    timer = pygame.time.Clock()

    #this avoids slow font scaling (add more if needed)
    fontl = pygame.font.SysFont('arial', size=24, bold=True)
    fonts = pygame.font.SysFont('arial', size=16, bold=False)

    pygame.mouse.set_visible(True)

    hexmap = Hexmap()
    hexmap.init(80)
    
    ship = Ship()
    ship.rect.centerx = 170
    ship.rect.centery = 159
    
#
# Initialize the GUI
#
def init_gui():
    global gui
    global guiwin_debug
    global guiwin_ship
    global guibtn_hello
    global guiimg_ship
    global guitxt_debug
    
    gui = pygame_gui.UIManager((SCREENW,SCREENH))

    guiwin_ship = pygame_gui.elements.ui_window.UIWindow(
        rect=pygame.Rect((500,500),(400,600)),
        window_display_title="Ship Details",
        element_id="guiwin_ship",
        manager=gui
    )

    guibtn_hello = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 400), (90, 40)), 
        text='Say Hello', 
        container=guiwin_ship,
        manager=gui
    )
    
    #imgrot = pygame.transform.rotozoom(ship.surf, 90, 0.5).convert_alpha()
    imgrot = ship.surf.convert_alpha()
    imgrot.set_colorkey((0,0,0,255))

    r=ship.surf.get_rect()
    s = pygame.Surface(r.size, pygame.SRCALPHA)
    pygame.draw.rect(s, (0,0,255,64), s.get_rect())
    s.blit(imgrot, (0,0))
    
    r = s.get_rect()
    w,h = r.width,r.height
    
    guiimg_ship = pygame_gui.elements.ui_image.UIImage(
        relative_rect=pygame.Rect((10,10),(w,h)),
        image_surface=s,
        container=guiwin_ship,
        manager=gui
    )
    
    w,h = 400,200
    x = SCREENW-w
    y = SCREENH-h
    guiwin_debug = pygame_gui.elements.ui_window.UIWindow(
        rect=pygame.Rect((x,y),(w,h)),
        window_display_title="DEBUG OUTPUT",
        element_id="guiwin_debug",
        manager=gui
    )
    
    guitxt_debug = pygame_gui.elements.ui_text_box.UITextBox(
        relative_rect=pygame.Rect((0,0),(400,200)),
        html_text="",
        container=guiwin_debug,
        manager=gui
    )



#
# Get display settings
#
def get_video_info():
    global SCREENW
    global SCREENH

    info=pygame.display.Info()
    print("Display: " + str(info.current_w) + "," + str(info.current_h) + "," + str(info.bitsize))
    
    print("Desktop modes:")
    sizes=pygame.display.get_desktop_sizes()
    for s in sizes: print(s)

    print("Display modes:")
    modes=pygame.display.list_modes(depth=0, flags=pygame.FULLSCREEN, display=0)
    for m in modes:
        #ignore oversize modes > desktop
        if (m[0] <= info.current_w and m[1] <= info.current_h):
            print(m)

    SCREENW=1920
    SCREENH=1200
   

#
#
#
def fontprint(target, text, pos, color=(200,200,200), center=False, background=None, font=fonts):
    x,y=pos
    surf = fonts.render(text, True, color, background)
    if center:
        r = surf.get_bounding_rect()
        x-=r.width/2
        y-=r.height/2
    target.blit(surf, (x,y))
    
#
#
#
def print_debug_info():
    global fonts
    
    debugx=SCREENW-200
    debugy=SCREENH-100
    nl=16

    hexmap.draw_circles(screen)
    hexmap.draw_labels(screen, fonts)
    
    s = "Ship: " + str(ship.rect.left) + "," + str(ship.rect.top) + \
        " (" + str(ship.rect.centerx) + "," + str(ship.rect.centery) + ")"
    #fontprint(screen, s, (debugx,debugy))
    #debugy+=nl
    s += "<br>"

    mouse = pygame.mouse.get_pos()
    x,y=mouse
    s += "Mouse: " + str(x) + "," + str(y) 
    s += "<br>"
    #fontprint(screen, s, (debugx,debugy))
    #debugy+=nl

    index,center = hexmap.get_hex_at(mouse)
    posx,posy = center
    indx,indy = index
    #hex-grid Y starts at 1 (based on the FASA hex map)
    s += "Hex: " + str(indx)+"," + str(indy+1) + " at " + str((posx,posy))
    s += "<br>"

    guitxt_debug.html_text = s
    guitxt_debug.rebuild()


    if indx>-1:
        hexmap.draw_hex(screen, (255,0,0), radius=80, position=center, width=8)
        

#
# main engine start       
#
init_game()
init_gui()

game_over = False
last_time = 0

inputdelay = 0
clock = pygame.time.Clock()

#main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: sys.exit()
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == guibtn_hello:
                print("Hello!")
                msgbox = pygame_gui.windows.ui_message_window.UIMessageWindow(
                    rect=pygame.Rect((500,500),(200,160)),
                    html_message="This is a message",
                    manager=gui,
                    window_title="Test Message"
                )

                
                
        gui.process_events(event)
        
    gui.update(time_delta)

    pressed_keys = pygame.key.get_pressed()
    if pygame.time.get_ticks() > inputdelay + 100:
        inputdelay = pygame.time.get_ticks()
        
        if pressed_keys[K_UP]:
            ship.rect.centery -= hexmap.hexsize*2
        if pressed_keys[K_DOWN]:
            ship.rect.centery += hexmap.hexsize*2

        if pressed_keys[K_LEFT]:
            hexmap.jumptoggle = hexmap.jumptoggle * -1
            ship.rect.centerx -= hexmap.hexsize
            ship.rect.centery -= hexmap.hexsize * hexmap.jumptoggle
        if pressed_keys[K_RIGHT]:
            hexmap.jumptoggle = hexmap.jumptoggle * -1
            ship.rect.centerx += hexmap.hexsize
            ship.rect.centery += hexmap.hexsize * hexmap.jumptoggle

        if pressed_keys[K_d]:
            ship.dir = ship.dir + 1
            if ship.dir > 5: ship.dir = 0
        if pressed_keys[K_a]:
            ship.dir = ship.dir - 1
            if ship.dir < 0: ship.dir = 5
    
    #clear the background
    backbuffer.fill((20,20,20))
    
    hexmap.draw(backbuffer, (200,200,200))
    
    ship.draw(backbuffer)
   
    print_debug_info()
    
    gui.draw_ui(backbuffer)


    #draw the back buffer
    screen.blit(backbuffer, (0,0))

    pygame.display.update()
    
pygame.quit()







    
