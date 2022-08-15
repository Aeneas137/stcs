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

C_GRAY=(200,200,200)

gui=None
guiwin_debug=None
guiwin_ship=None
guiimg_ship=None
guitxt_debug=None
guibtn_debug_circles=None
guibtn_debug_labels=None

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
    
#
# Initialize the GUI
#
def init_gui():
    global gui
    global guiwin_debug
    global guiwin_ship
    global guiimg_ship
    global guitxt_debug
    global guibtn_debug_circles
    global guibtn_debug_labels
    
    gui = pygame_gui.UIManager((SCREENW,SCREENH))

    #build the debug window
    w,h = 500,300
    x = SCREENW-w
    y = SCREENH-h
    guiwin_debug = pygame_gui.elements.ui_window.UIWindow(
        rect=pygame.Rect((x,y),(w,h)),
        window_display_title="DEBUG OUTPUT",
        element_id="guiwin_debug",
        manager=gui
    )
    guitxt_debug = pygame_gui.elements.ui_text_box.UITextBox(
        relative_rect=pygame.Rect((0,0),(w-10,200)),
        html_text="",
        container=guiwin_debug,
        manager=gui
    )
    guibtn_debug_circles = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((0, 200), (120, 40)), 
        text='Circles On', 
        container=guiwin_debug,
        manager=gui
    )
    guibtn_debug_labels = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((125, 200), (120, 40)), 
        text='Labels On', 
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
    t=""
    for s in sizes: 
        t += str(s) + ", "
    print(t)

    print("Display modes:")
    modes=pygame.display.list_modes(depth=0, flags=pygame.FULLSCREEN, display=0)
    t=""
    for m in modes:
        #ignore oversize modes > desktop
        if (m[0] <= info.current_w and m[1] <= info.current_h):
            t += "("+ str(m[0]) + "x" + str(m[1]) + "), "
    print(t)

    SCREENW=1920
    SCREENH=1200

#
#
#
def print_debug_info(target):
    global fonts
    
    debugx=SCREENW-200
    debugy=SCREENH-100
    nl=16

    if guibtn_debug_circles.text == "Circles On":
        hexmap.draw_circles(target)
    
    if guibtn_debug_labels.text == "Labels On":
        hexmap.draw_labels(target, fonts)
    
    s = "Ship: " + str(ship.rect.left) + "," + str(ship.rect.top) + \
        " (" + str(ship.rect.centerx) + "," + str(ship.rect.centery) + ")"
    print_text(backbuffer, fonts, debugx, debugy, s, C_GRAY)
    s += "<br>"

    mouse = pygame.mouse.get_pos()
    x,y=mouse
    s += "Mouse: " + str(x) + "," + str(y) 
    s += "<br>"
    print_text(backbuffer, fonts, debugx, debugy, s, C_GRAY)

    index,center = hexmap.get_hex_at(mouse)
    posx,posy = center
    indx,indy = index
    #hex-grid 'Y' starts at 1 instead of 0 (based on the FASA hex map)
    s += "Hex: " + str(indx)+"," + str(indy+1) + " at " + str((posx,posy))
    s += "<br>"

    guitxt_debug.html_text = s
    guitxt_debug.rebuild()


    if indx>-1:
        hexmap.draw_hex(target, (255,0,0), radius=80, position=center, width=8)
        

"""
Ship data for now will include starbases, etc.
must define the xml structure first!
"""
def load_ship(filename):
    global ship
    
    ship = Ship()
    ship.load_specs("ship_excelsior.xml")
    print(str(ship.specs))
    
    ship.load_top("fed_enterprise_b_512.png")
    ship.load_side("fed_enterprise_b_side_512.png")
    ship.rect.centerx = 170
    ship.rect.centery = 159
    
    ship.build_details_window(gui)
    

"""
"""
def load_hexmap(filename):
    #define the xml structure first!
    load_ship("ship.xml")
    

"""
main engine start       
"""
init_game()
init_gui()
load_hexmap("map.xml")



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

        #send events to GUI
        gui.process_events(event)
        
        #handle all gui buttons
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
        
            #debug circles toggle
            if event.ui_element == guibtn_debug_circles:
                if guibtn_debug_circles.text=='Circles On':
                    guibtn_debug_circles.set_text('Circles Off')
                else:
                    guibtn_debug_circles.set_text('Circles On')

            #debug labels toggle
            if event.ui_element == guibtn_debug_labels:
                if guibtn_debug_labels.text=='Labels On':
                    guibtn_debug_labels.set_text('Labels Off')
                else:
                    guibtn_debug_labels.set_text('Labels On')

    #handle input events
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

    #let the GUI perform updates
    gui.update(time_delta)
    
    #clear the background
    backbuffer.fill((20,20,20))
    

    hexmap.draw(backbuffer, (200,200,200))
    
    ship.draw(backbuffer)
   
    print_debug_info(backbuffer)
    
    gui.draw_ui(backbuffer)


    #draw the back buffer
    screen.blit(backbuffer, (0,0))

    pygame.display.update()
    
pygame.quit()

"""
msgbox = pygame_gui.windows.ui_message_window.UIMessageWindow(
    rect=pygame.Rect((500,500),(200,160)),
    html_message="Debug circles toggled",
    manager=gui,
    window_title="Debug Toggle"
)
"""
