import time, pygame, random, sys, webbrowser # import necessary modules
from pygame.locals import *

""" 
Welcome to my snake game:
This game write with python and pygame module
Also you want to run this game first you should install some modules that are import block
time, random and sys modules included in python

to install modules with console or terminal first of all you must install pip command
If pip not exist in your computer you shoul reinstall python with pip command or modify your python

to install modules with pip: 
to install pygame    : pip install pygame
to install webbrowser: pip install webbrowser


This game write by Ömer Faruk ÖZKAN
"""



# write function
def write(text, x, y):
    black = pygame.Color(0, 0, 0)
    font = pygame.font.SysFont('monaco', 18, bold = False, italic = False) # text font
    text = font.render(text, True, black)
    m_screen.blit(text, [x, y])



# terminate function
def terminate():
    pygame.quit() # exiting pygame
    sys.exit() # close black terminal




# blast function
b = []
def blast(w, h):
    blast = pygame.image.load('image/game_screen/snake/explosed-sprite.png')
    width, height = blast.get_size()
    for i in range(int(width/w)):
        b.append(blast.subsurface((i * w, 0, w, h)))


# set cursor
cursor = pygame.image.load('image/cursor/cursor.png')
def cursor_set():
    m_screen.blit(cursor, pygame.mouse.get_pos())
    pygame.mouse.set_visible(False)



# Colors
red = pygame.Color(255, 10, 10) # gameover
green = pygame.Color(100, 255, 70) # background
game_orange = pygame.Color(255, 178, 102)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0) # score
blue = pygame.Color(58, 78, 131) # snake
grey = pygame.Color(250, 250, 250) #Score
white = pygame.Color(255, 255, 255) # white



# fps controller
fpsController = pygame.time.Clock()



# High Score
first_nick = ''
first_score = int()
second_nick = ''
second_score = int()
third_nick = ''
third_score = int()
# high score files
f_n = open('score/nick/first.txt', 'r')
f_s = open('score/score/first.txt', 'r')
s_n = open('score/nick/second.txt', 'r')
s_s = open('score/score/second.txt', 'r')
t_n = open('score/nick/third.txt', 'r')
t_s = open('score/score/third.txt', 'r')

first_nick = f_n.read()
first_score = f_s.read()
second_nick = s_n.read()
second_score = s_s.read()
third_nick = t_n.read()
third_score = t_s.read()
f_n.close()
f_s.close()
s_n.close()
s_s.close()
t_n.close()
t_s.close()

def write_score(nick_score, score_x, score_y):
    s_white = pygame.Color(255, 255, 255)
    s_font = pygame.font.SysFont('monaco', 22, bold = False, italic = False) # text font
    nick_score = s_font.render(nick_score, True, s_white)
    m_screen.blit(nick_score, [score_x, score_y])


# options value
mute = False # mute/unmute control  
velocity = 10
speed = 12
s_x = 720 # menu screen x
s_y = 460 # menu screen y
g_x = s_x
g_y = s_y
speed_level = 1 # 1: low 2: medium 3: fast
screen_size = 2 # default 720x460
food_bar = 1 # default 1 peach
BG_color = 1 # 1: light 2: medium 3: dark
mute_bar = 1 # 1: unmute 2: mute
food = pygame.image # game food image
color = pygame.Color # game bg color
color = green # default color
# initialize pygame module
pygame.init()




#set up window caption
pygame.display.set_icon(pygame.image.load('image/Caption/gameicon.png')) # icon
pygame.display.set_caption('Snake Game!') # caption text




# set up screen
m_screen = pygame.display.set_mode([s_x, s_y]) # menu
pygame.display.flip()





#<---------- IMAGE LOAD ---------->

# opening screen
open_BG = pygame.image.load('image/open_screen/BG.png')
press = pygame.image.load('image/open_screen/press.png')
text_logo = pygame.image.load('image/open_screen/logo.png')
t1 = pygame.image.load('image/open_screen/1.png')
t2 = pygame.image.load('image/open_screen/2.png')
t3 = pygame.image.load('image/open_screen/3.png')


#_______________________________________ snake images _______________________________________________
head = [pygame.image.load('image/game_screen/snake/head1.png'), pygame.image.load('image/game_screen/snake/head2.png'), pygame.image.load('image/game_screen/snake/head3.png'), pygame.image.load('image/game_screen/snake/head4.png')]
tail = [pygame.image.load('image/game_screen/snake/tail1.png'), pygame.image.load('image/game_screen/snake/tail2.png'), pygame.image.load('image/game_screen/snake/tail3.png'), pygame.image.load('image/game_screen/snake/tail4.png')]


#--------------------------------------------- enemy images ---------------------------------------------------
e_down = [pygame.image.load('image/enemy/down/d1.png'), pygame.image.load('image/enemy/down/d2.png'), pygame.image.load('image/enemy/down/d3.png'), pygame.image.load('image/enemy/down/d4.png'), pygame.image.load('image/enemy/down/d5.png'), pygame.image.load('image/enemy/down/d6.png'), pygame.image.load('image/enemy/down/d7.png'), pygame.image.load('image/enemy/down/d8.png'), pygame.image.load('image/enemy/down/d9.png'), pygame.image.load('image/enemy/down/d10.png'), pygame.image.load('image/enemy/down/d11.png'), pygame.image.load('image/enemy/down/d12.png')]
e_up = [pygame.image.load('image/enemy/up/u1.png'), pygame.image.load('image/enemy/up/u2.png'), pygame.image.load('image/enemy/up/u3.png'), pygame.image.load('image/enemy/up/u4.png'), pygame.image.load('image/enemy/up/u5.png'), pygame.image.load('image/enemy/up/u6.png'), pygame.image.load('image/enemy/up/u7.png'), pygame.image.load('image/enemy/up/u8.png'), pygame.image.load('image/enemy/up/u9.png'), pygame.image.load('image/enemy/up/u10.png'), pygame.image.load('image/enemy/up/u11.png'), pygame.image.load('image/enemy/up/u12.png')]
e_right = [pygame.image.load('image/enemy/right/r1.png'), pygame.image.load('image/enemy/right/r2.png'), pygame.image.load('image/enemy/right/r3.png'), pygame.image.load('image/enemy/right/r4.png'), pygame.image.load('image/enemy/right/r5.png'), pygame.image.load('image/enemy/right/r6.png'), pygame.image.load('image/enemy/right/r7.png'), pygame.image.load('image/enemy/right/r8.png'), pygame.image.load('image/enemy/right/r9.png'), pygame.image.load('image/enemy/right/r10.png'), pygame.image.load('image/enemy/right/r11.png'), pygame.image.load('image/enemy/right/r12.png')]
e_left = [pygame.image.load('image/enemy/left/l1.png'), pygame.image.load('image/enemy/left/l2.png'), pygame.image.load('image/enemy/left/l3.png'), pygame.image.load('image/enemy/left/l4.png'), pygame.image.load('image/enemy/left/l5.png'), pygame.image.load('image/enemy/left/l6.png'), pygame.image.load('image/enemy/left/l7.png'), pygame.image.load('image/enemy/left/l8.png'), pygame.image.load('image/enemy/left/l9.png'), pygame.image.load('image/enemy/left/l10.png'), pygame.image.load('image/enemy/left/l11.png'), pygame.image.load('image/enemy/left/l12.png')]
e_walkCount = 0


#-------------------------------------------- General İmage ---------------------------------------------------
button_n = pygame.image.load('image/Buttons/button1.png') # normal button
button_o = pygame.image.load('image/Buttons/button2.png') # mouse hover button
menu_n = pygame.image.load('image/P_screen/menu1.png') #home button normal
menu_o = pygame.image.load('image/P_screen/menu2.png') #home button hover
restart = pygame.image.load('image/Buttons/restart.png') # restart button
help_button = pygame.image.load('Help/help_button.png') # Help Button

#______________________________________ menu image load ________________________________________
m_BG = pygame.image.load_extended('image/M_screen/main_m/m_BG.png') # menu background image




#------------------------------------- social media icons ----------------------------------------
facebook = pygame.image.load('image/M_screen/links/facebook.png') # facebook icon
instagram = pygame.image.load('image/M_screen/links/instagram.png') # instagram icon
linkedin = pygame.image.load('image/M_screen/links/linkedin.png') # linked in icon
twitter = pygame.image.load('image/M_screen/links/twitter.png') # twitter icon
youtube = pygame.image.load('image/M_screen/links/youtube.png') # youtube icon


#------------------------------------------ play menu input --------------------------------------------------
play_BG = pygame.image.load_extended('image/P_screen/p_background.png') # play menu background
n_font = pygame.font.Font(None, 24) # nick font
nick_box = pygame.image.load('image/P_screen/nick_box.png') # nick_box image
nick = '' # user nick string
nickEnter = False
click = False
nick_loop = True
GO = True
# --------------------------------------   options menu images  ---------------------------------------------
o_BG = pygame.image.load('image/Option_screen/o_BG.png')
unmute = pygame.image.load('image/Option_screen/unmute.png')
nmute = pygame.image.load('image/Option_screen/mute.png')
peach1 = pygame.image.load('image/Option_screen/food/peach.png') # 1
berry1 = pygame.image.load('image/Option_screen/food/berry.png') # 2
cherry1 = pygame.image.load('image/Option_screen/food/cherry.png') # 3
grape1= pygame.image.load('image/Option_screen/food/grape.png') # 4
strawberry1 = pygame.image.load('image/Option_screen/food/strawberry.png') # 5
orange1 = pygame.image.load('image/Option_screen/food/orange.png') # 6


#--------------------------------------------- speed bar --------------------------------------------------------
slow = pygame.image.load('image/Option_screen/speed/slow.png')
medium = pygame.image.load('image/Option_screen/speed/medium.png')
fast = pygame.image.load('image/Option_screen/speed/fast.png')



#----------------------------------------- How to play menu image --------------------------------------------------
n_left = pygame.image.load('image/How_play_Screen/n_green_l.png')
n_right = pygame.image.load('image/How_play_Screen/n_green_r.png')
o_left = pygame.image.load('image/How_play_Screen/o_green_l.png')
o_right = pygame.image.load('image/How_play_Screen/o_green_r.png')
grey_left = pygame.image.load('image/How_play_Screen/grey_left.png')
grey_right = pygame.image.load('image/How_play_Screen/grey_right.png')
manual_BG = pygame.image.load('image/How_play_Screen/manual_BG.png')




#--------------------------------------------- manual text image -----------------------------------------------------
m1 = pygame.image.load('image/How_play_Screen/manual/manual_1.png')
m2 = pygame.image.load('image/How_play_Screen/manual/manual_2.png')


#<-------------------------------------------  Score menu image  --------------------------------------------------->
score_BG = pygame.image.load('image/Score_screen/score_screen.png') # score screen background
s_table = pygame.image.load('image/Score_screen/score.png') # score table
first = pygame.image.load('image/Score_screen/1.png')
second = pygame.image.load('image/Score_screen/2.png')
third = pygame.image.load('image/Score_screen/3.png')




#<------------------------------------------- food images ----------------------------------------------------->
peach = pygame.image.load('image/game_screen/food/peach.png') # 1
berry = pygame.image.load('image/game_screen/food/berry.png') # 2
cherry = pygame.image.load('image/game_screen/food/cherry.png') # 3
grape = pygame.image.load('image/game_screen/food/grape.png') # 4
strawberry = pygame.image.load('image/game_screen/food/strawberry.png') # 5
orange = pygame.image.load('image/game_screen/food/orange.png') # 6
food = peach # default food




#<--------------------------------------------  game sounds  ------------------------------------------------->
m_sound = {}
m_sound['switch'] = pygame.mixer.Sound('sounds/menu/button_switch.wav')
m_sound['click'] = pygame.mixer.Sound('sounds/menu/click.ogg')
m_sound['eat'] = pygame.mixer.Sound('sounds/playground/Eat.wav')
m_sound['crash'] = pygame.mixer.Sound('sounds/playground/none.wav')
m_sound['keydown'] = pygame.mixer.Sound('sounds/open/keydown.ogg')
open_sound = pygame.mixer.Sound('sounds/open/opening.ogg')
game_sound = pygame.mixer.Sound('sounds/playground/forest.wav')
logo_sound = pygame.mixer.Sound('sounds/open/game_logo.wav')


#------------------------------------------- game inputs and variables ---------------------------------------------
# variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
grass_1 = pygame.image.load('image/game_screen/grass/grass1.png')
grass_2 = pygame.image.load('image/game_screen/grass/grass2.png')
grass_3 = pygame.image.load('image/game_screen/grass/grass3.png')
grass_4 = pygame.image.load('image/game_screen/grass/grass4.png')
grass_x = (s_x / 10) 
grass_y = (s_y / 10) 
e_x = 360
e_y = 200
x_diff = 1
y_diff = 0 



#--------------------------------------------------- import variables ------------------------------------------
snakePos = [100,50]
snakeBody =[[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
changeto = direction
score = 0
velocit = 10
a = snakeBody[-1] # Tail
b = snakeBody[-2]


#_________________________________________ game functions ___________________________________________
def enemy_move(e_direction):
    global e_walkCount, e_x, e_y
    if e_walkCount + 1 >= 48:
        e_walkCount = 0
    if e_direction == 1 and e_x >= 2: # LEFT
        m_screen.blit(e_left[e_walkCount//4], (e_x, e_y))
        e_walkCount += 1
        e_x -= 10
    elif e_direction == 2 and e_x <= g_x -25: # RIGHT
        m_screen.blit(e_right[e_walkCount//4], (e_x, e_y))
        e_walkCount += 1
        e_x += 10
    elif e_direction == 3 and e_y >= 2: # UP
        m_screen.blit(e_up[e_walkCount//4], (e_x, e_y))
        e_walkCount += 1
        e_y -= 10
    elif e_direction == 4 and e_y <= g_y - 32: # DOWN
        m_screen.blit(e_down[e_walkCount//4], (e_x, e_y))
        e_walkCount += 1
        e_y += 10
    else:
        return enemy_move(random.randint(1, 5))




#------------------------------------------ show menu normal --------------------------------------------------
def normal_menu():
    m_screen.blit(button_n, (310, 120)) # Play
    m_screen.blit(button_n, (310, 170)) # Options
    m_screen.blit(button_n, (310, 220)) # How to Play
    m_screen.blit(button_n, (310, 270)) # High Score
    m_screen.blit(button_n, (310, 320)) # Quit
    # buttons texts
    write('Play', 345, 128) # play text
    write('Options', 333, 178) # options text
    write('How to Play', 326, 227) # How to Play text
    write('High Score', 328, 279) # High Score text
    write('Quit', 345, 328) # Quit 

#------------------------------------------------ SHOW SCORE ---------------------------------------------------
def show_Score(choice = 1):
    global score 
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}' .format(score), True, grey)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (g_x / 2, g_y / 3)
    m_screen.blit(Ssurf, Srect)

#-------------------------------------------------- game over -----------------------------------------------------
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, pygame.Color(200, 0, 0))
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 30)
    m_screen.fill((0, 0, 0))
    pygame.display.update()                                          

def opt(column, line):
    write('Screen Size:', 220, 130)
    write('FPS:', 220, 180)
    write('Fruit:', 220, 230)
    write('Bacground Color:', 220, 280)
    write('Sound:', 220, 330)
    if column == 1:
        if line == 1:
            # left
            m_screen.blit(o_left, (351, 126))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        elif line == 2:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(o_left, (351, 176))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        elif line == 3:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(o_left, (351, 226))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        elif line == 4:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(o_left, (351, 276))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        elif line == 5:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(o_left, (351, 326))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
    elif column == 2:
        if line == 1:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(o_right, (501, 126))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        if line == 2:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(o_right, (501, 176))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        if line == 3:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(o_right, (501, 226))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(n_right, (500, 325))
        if line == 4:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(o_right, (501, 276))
            m_screen.blit(n_right, (500, 325))
        if line == 5:
            # left
            m_screen.blit(n_left, (350, 125))
            m_screen.blit(n_left, (350, 175))
            m_screen.blit(n_left, (350, 225))
            m_screen.blit(n_left, (350, 275))
            m_screen.blit(n_left, (350, 325))
            # right
            m_screen.blit(n_right, (500, 125))
            m_screen.blit(n_right, (500, 175))
            m_screen.blit(n_right, (500, 225))
            m_screen.blit(n_right, (500, 275))
            m_screen.blit(o_right, (501, 326))
    else:
        # left
        m_screen.blit(n_left, (350, 125))
        m_screen.blit(n_left, (350, 175))
        m_screen.blit(n_left, (350, 225))
        m_screen.blit(n_left, (350, 275))
        m_screen.blit(n_left, (350, 325))
        # right
        m_screen.blit(n_right, (500, 125))
        m_screen.blit(n_right, (500, 175))
        m_screen.blit(n_right, (500, 225))
        m_screen.blit(n_right, (500, 275))
        m_screen.blit(n_right, (500, 325))


#<---------------------------------------------------First Screen------------------------------------------------>
# LOGO
op = True
r = 255
g = 255
b = 255
logo = pygame.image.load('image/Caption/gamelogo.png')
logo_sound.play()
pygame.time.delay(1800)

# Logo Start
while op:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            break
        op = False
    
    m_screen.fill(pygame.Color(r, g, b)) 
    cursor_set()  
    if r >= 40:
        m_screen.blit(logo, (200, 100))
        cursor_set()
    if r == 1 or g == 1 or b == 1:
        break
        op = False
    elif r > 0:
        r -= 1
        g -= 1
        b -= 1
    
    pygame.display.update()
    fpsController.tick(12) 
logo_sound.stop()
pygame.time.delay(1500)
python = pygame.image.load('image/Caption/python.png')




# PYTHON
op = True
r = 255
g = 255
b = 255
# python (logo) start
while op:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            break
        op = False
    m_screen.fill(pygame.Color(r, g, b))  
    cursor_set()

    if r >= 40:
        m_screen.blit(python, (0, 80))
        cursor_set()
    if r == 1 or g == 1 or b == 1:
        break
        op = False
    elif r > 0:
        r -= 5
        g -= 5
        b -= 5
    
    pygame.display.update() 

pygame.time.delay(1500)
powered = pygame.image.load('image/Caption/pygame_powered.png')




# PYGAME POWERED
op = True
r = 0
g = 0
b = 0
# pygame powered logo start
while op:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            break
        op = False
    m_screen.fill(pygame.Color(r, g, b))  
    cursor_set()
    if r >= 215:
        m_screen.blit(powered, (150, 120))
        cursor_set()
    if r == 254 or g == 254 or b == 254:
        break
        op = False
    elif r < 255:
        r += 1
        g += 1
        b += 1
    
    pygame.display.update()

pygame.time.delay(2000)
dice = pygame.image.load('image/Caption/dicelogo.png')





# DICE SOFTWARE LOGO
op = True
r = 255
g = 255
b = 255
# dice software start
while op:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            break
        op = False
    m_screen.fill(pygame.Color(r, g, b)) 

    if r >= 100:
        m_screen.blit(dice, (110, 100))
        logo_color = pygame.Color(100, 0, 100)
        logo_font = pygame.font.SysFont('monaco', 48, False, True)
        logo_text = logo_font.render('Dice Software', True, logo_color)
        m_screen.blit(logo_text, (320, 220))
        write('Presented..', 325, 260)
    if r == 1 or g == 1 or b == 1:
        break
        op = False
    elif r > 0:
        r -= 1
        g -= 1
        b -= 1
    cursor_set()
    pygame.display.update()
pygame.time.delay(1000)





# open screen
opening = True
open_sound.play()
while opening:
    clock = pygame.time.Clock()
    m_screen.blit(open_BG, (0, 0))
    m_screen.blit(press, (250, 400))
    m_screen.blit(text_logo, (200, 10))
    m_screen.blit(t1, (252, 280)) # create the floor
    m_screen.blit(t2, (320, 280)) # create the floor
    m_screen.blit(t3, (388, 280)) # create the floor 
    r1 = pygame.image.load('image/open_screen/snake/r1.png')
    m_screen.blit(r1, (252, 265))
    cursor_set()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            opening = False
            open_sound.stop()
            m_sound['keydown'].play()   
            break     
    pygame.display.update() 
#<----------------------------------------------First Screen Finish----------------------------------->




##################################### MENU ##################################### (Main Loop)
running = True
while running: 
    
    # menu screen
    # background colour and background
    m_screen.fill(pygame.Color(255, 255, 255))
    m_screen.blit(m_BG, (0, 0))
    cursor_set()
    # event   
    for event in pygame.event.get():

        # mouse movement
        mouse = pygame.mouse.get_pos()

        # mouse click
        m_click = pygame.mouse.get_pressed()
        
        # mouse action   
        if event.type == pygame.QUIT:
            terminate()




#####################################            PLAY            #####################################            
        elif mouse[1] >= 124 and mouse[1] <= 145 and mouse[0] >= 316 and mouse[0] <= 400: # if hover play button           
            
            m_screen.blit(button_o, (311, 121)) # hover play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # Quit
            m_screen.blit(help_button, (640, 380)) # help button
            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 346, 129) # hover play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit
            cursor_set()
            if m_click[0] == 1: # mouse click control
                if mute == True:
                    None
                else:
                    m_sound['click'].play() # play click sound
                play = True
                while play:
                    
                    m_screen.fill(pygame.Color(255, 255, 255))
                    m_screen.blit(play_BG, (0,0))
                    write('Play', 345, 32)

                    # nick block
                    m_screen.blit(nick_box, (330, 170)) # nick box
                    cursor_set()
                    # play menu events
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            play = False
                            terminate()
                        
                        # Mouse click
                        p_hover = pygame.mouse.get_pos() # play menu mouse movement
                        p_click = pygame.mouse.get_pressed() # play menu mouse click
                        if p_hover[0] >= 333 and p_hover[0] <= 475 and p_hover[1] >= 172 and p_hover[1] <= 203:
                            write('Play', 345, 32)


                            # nick block
                            write('Enter Your Nick:', 220, 177) # nick text
                            m_screen.blit(nick_box, (330, 170)) # nick box
                            if nickEnter == True:
                                nick_surface = n_font.render(nick, True, (white))
                                m_screen.blit(nick_surface, (335, 177))

                            
                            m_screen.blit(button_n, (320, 230)) # normal start button
                            write('START', 345, 237) # normal start text
                            m_screen.blit(menu_n, (325, 280)) # go home button hover 
                            write('Menu:', 280, 289) # go home text

                            if p_click[0] == 1:
                                
                                nick_loop = True
                                while nick_loop:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            terminate()
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_BACKSPACE:
                                                
                                                nick = nick[:-1]
                                            elif event.key == pygame.K_RETURN:
                                                if len(nick) <= 8 and len(nick) >= 4:
                                                    click = False
                                                    nickEnter = True
                                                    nick_loop = False
                                                else:
                                                    click = True
                                                    nick = ''
                                                    nick_loop = False
                                            elif len(nick) < 9:
                                                nick += event.unicode


                                    write('Play', 345, 32)
                                    # nick block
                                    write('Enter Your Nick:', 220, 177) # nick text
                                    m_screen.blit(nick_box, (330, 170)) # nick box
                                    
                                    m_screen.blit(button_n, (320, 230)) # normal start button
                                    write('START', 345, 237) # normal start text
                                    m_screen.blit(menu_n, (325, 280)) # go home button hover 
                                    write('Menu:', 280, 289) # go home text

                                    nick_surface = n_font.render(nick, True, (255, 255, 255))
                                    m_screen.blit(nick_surface, (335, 177))
                                    

                                    pygame.display.update()

                            if click == True:
                                red_color = pygame.Color(255, 0, 0)
                                error_font = pygame.font.SysFont('monaco', 14, bold = False, italic = False) # Error text font
                                error = error_font.render('Please enter your nick or enter your nick between 4-8', True, red_color)
                                m_screen.blit(error, (330, 210))
                                if nickEnter == True:
                                    nick_surface = n_font.render(nick, True, (white))
                                    m_screen.blit(nick_surface, (335, 177))

                            cursor_set()
                            pygame.display.update()
                            
                    
                        elif p_hover[0] >= 330 and p_hover[0] <= 350 and p_hover[1] >= 282 and p_hover[1] <= 305:
                            
                            write('Play', 345, 32)
                            # nick block
                            write('Enter Your Nick:', 220, 177) # nick text
                            m_screen.blit(nick_box, (330, 170)) # nick box
                            if nickEnter == True:
                                nick_surface = n_font.render(nick, True, (white))
                                m_screen.blit(nick_surface, (335, 177))
                            
                            m_screen.blit(button_n, (320, 230)) # normal start button
                            write('START', 345, 237) # normal start text
                            m_screen.blit(menu_o, (326, 281)) # go home button hover 
                            write('Menu:', 280, 289) # go home text

                            if click == True:
                                red_color = pygame.Color(255, 0, 0)
                                error_font = pygame.font.SysFont('monaco', 14, bold = False, italic = False) # Error text font
                                error = error_font.render('Please enter your nick or enter your nick between 4-8', True, red_color)
                                m_screen.blit(error, (330, 210))

                            cursor_set()
                            pygame.display.update()
                            if p_click[0] == 1: # go home click statement
                                pygame.display.set_mode((s_x, s_y))
                                if mute == True:
                                    None
                                else:
                                    m_sound['click'].play() # play click sound
                                click = False
                                play = False
                        elif p_hover[0] >= 325 and p_hover[0] <= 407 and p_hover[1] >= 235 and p_hover[1]  <= 259:
                            write('Play', 345, 32)
                            

                            # nick block
                            write('Enter Your Nick:', 220, 177) # nick text
                            m_screen.blit(nick_box, (330, 170)) # nick box
                            if nickEnter == True:
                                nick_surface = n_font.render(nick, True, (white))
                                m_screen.blit(nick_surface, (335, 177))
                            
                            m_screen.blit(button_o, (321, 231)) # hover start button
                            write('START', 346, 238) # hover start text 
                            m_screen.blit(menu_n, (325, 280)) # normal home button
                            write('Menu:', 280, 289) # home text

                            # click control
                            if click == True:
                                red_color = pygame.Color(255, 0, 0)
                                error_font = pygame.font.SysFont('monaco', 14, bold = False, italic = False) # Error text font
                                error = error_font.render('Please enter your nick or enter your nick between 4-8', True, red_color)
                                m_screen.blit(error, (330, 210))

                            cursor_set()
                            pygame.display.update()
                            if p_click[0] == 1 and nickEnter == False:
                                
                            
                                # nick block
                                
                                red_color = pygame.Color(255, 0, 0)
                                error_font = pygame.font.SysFont('monaco', 14, bold = False, italic = False) # Error text font
                                error = error_font.render('Please enter your nick or enter your nick between 4-8', True, red_color)
                                m_screen.blit(error, (330, 210))
                                if nickEnter == True:
                                    nick_surface = n_font.render(nick, True, (white))
                                    m_screen.blit(nick_surface, (335, 177))

                                click = True
                                cursor_set()
                                pygame.display.update()
                            
                            elif p_click[0] == 1 and nickEnter == True:
                                pygame.display.set_mode((g_x, g_y))
                                if mute == True:
                                    None
                                else:
                                    m_sound['click'].play() # play click sound

                                    if mute == True:
                                        None
                                    else:
                                        game_sound.play()
# <------------------------------------  GAME INSIDE --------------------------------------->
                                m_screen.fill(green)
                                start = True
                                x_diff = 2
                                pygame.display.update()
                                fpsController.tick(speed)
                                
                                
                                # screen size control
                                if screen_size == 1:
                                    g_x = 460
                                    g_y = 280
                                elif screen_size == 2:
                                    g_x = 720
                                    g_y = 460
                                elif screen_size == 3:
                                    g_x = 1080
                                    g_y = 720


                                # food control
                                if food_bar == 1:
                                    food = peach
                                elif food_bar == 2:
                                    food = berry
                                elif food_bar == 3:
                                    food = cherry
                                elif food_bar == 4:
                                    food = grape
                                elif food_bar == 5:
                                    food = strawberry
                                elif food_bar == 6:
                                    food = orange


                                # first food
                                foodPos = [random.randint(1, (g_x / 10)) * 10, random.randint(1, (g_y / 10)) * 10]
                                snakePos = [100,50]
                                snakeBody =[[100, 50], [90, 50], [80, 50]]
                                direction = 'RIGHT'
                                changeto = direction
                                score = 0
                                
                                #<--------------- Game Start --------------->                         
                                while start:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            terminate()
                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                                                changeto = 'RIGHT'
                                            if event.key == pygame.K_LEFT or event.key == ord('a'):
                                                changeto = 'LEFT'
                                            if event.key == pygame.K_UP or event.key == ord('w'):
                                                changeto = 'UP'
                                            if event.key == pygame.K_DOWN or event.key == ord('s'):
                                                changeto = 'DOWN'
                                    # validation of direction
                                    if changeto == 'RIGHT' and not direction == 'LEFT':
                                        direction = 'RIGHT'
                                    if changeto == 'LEFT' and not direction == 'RIGHT':
                                        direction = 'LEFT'
                                    if changeto == 'UP' and not direction == 'DOWN':
                                        direction = 'UP'
                                    if changeto == 'DOWN' and not direction == 'UP':
                                        direction = 'DOWN'
                                    if direction == 'RIGHT':
                                        snakePos[0] = snakePos [0] + 10
                                    if direction == 'LEFT':
                                        snakePos[0] -= 10
                                    if direction == 'UP':
                                        snakePos[1] -= 10
                                    if direction == 'DOWN':
                                        snakePos[1] += 10
                                    
                                    # snake body mechanism
                                    snakeBody.insert(0, list(snakePos))
                                    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[True]:                         
                                        m_sound['eat'].play()                                
                                        score += 15
                                        foodPos = [random.randint(1, ((g_x - 10) / 10)) * 10, random.randint(1, ((g_y - 10) / 10)) * 10]
        

                                    else:
                                        snakeBody.pop()
                                    
                                    # if the food generate in snake body generate again
                                    if foodPos in snakeBody:
                                        foodPos = [random.randint(1, ((g_x - 10) / 10)) * 10, random.randint(1, ((g_y - 10) / 10)) * 10]
                                        


                                    # gameplay background
                                    m_screen.fill(color)
                                    m_screen.blit(food, (foodPos[0], foodPos[1]))

                                    # ENEMY BLOCK
                                    enemy_move(x_diff)
                                    if y_diff <= 12:
                                        y_diff += 1
                                    else:
                                        y_diff = 0
                                        x_diff = random.randint(1, 4)                              
                                    # ENEMY BLOCK FINISH





                                    # draw snake
                                    for i in snakeBody:
                                        # HEAD
                                        if direction == 'LEFT':
                                            m_screen.blit(head[0], snakePos)
                                        elif direction == 'UP':
                                            m_screen.blit(head[2], snakePos)
                                        elif direction == 'RIGHT':
                                            m_screen.blit(head[3], snakePos)
                                        elif direction == 'DOWN':
                                            m_screen.blit(head[1], snakePos)

                                        #BODY
                                        m_screen.blit(pygame.image.load('image/game_screen/snake/body.png'), i)

                                    if snakePos[0] >= e_x and snakePos[0] <= e_x + 21 and snakePos[1] >= e_y and snakePos[1] <= e_y + 25:
                                        m_sound['crash'].play()
                                        GO = True
                                        while GO:    
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    terminate()
                                            go_hover = pygame.mouse.get_pos()
                                            go_click = pygame.mouse.get_pressed()
                                            if go_hover[0] >= ((g_x / 2) - 18) and go_hover[0] <= ((g_x / 2) + 8)  and go_hover[1] >= (g_y / 2)+ 32 and go_hover[1] <= (g_y / 2)+ 58:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_o, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                if go_click[0] == True:
                                                    if mute == True:
                                                        None
                                                    else:
                                                        m_sound['click'].play()
                                                    GO = False
                                                    start = False
                                                    nickEnter = False
                                                    nick = ''
                                                    pygame.display.set_mode((720, 460))
                                                cursor_set()
                                                pygame.display.update()
                                            else:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_n, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                cursor_set()
                                                pygame.display.update()


                                    
                                    
                                    
                                    # Draw Food
                                    m_screen.blit(food, (foodPos[0], foodPos[1]))


                                    # snake hits y axis wall
                                    if snakePos[0] > g_x - 5 or snakePos[0] < 0:
                                        m_sound['crash'].play()
                                        GO = True
                                        while GO:    
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    terminate()
                                            go_hover = pygame.mouse.get_pos()
                                            go_click = pygame.mouse.get_pressed()
                                            if go_hover[0] >= ((g_x / 2) - 18) and go_hover[0] <= ((g_x / 2) + 8)  and go_hover[1] >= (g_y / 2)+ 32 and go_hover[1] <= (g_y / 2)+ 58:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_o, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                if go_click[0] == True:
                                                    if mute == True:
                                                        None
                                                    else:
                                                        m_sound['click'].play()
                                                    GO = False
                                                    start = False
                                                    nickEnter = False
                                                    nick = ''
                                                    pygame.display.set_mode((720, 460))
                                                cursor_set()
                                                pygame.display.update()
                                            else:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_n, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                cursor_set()
                                                pygame.display.update()

                                    # snake hit x axis wall
                                    if snakePos[1] > g_y - 5 or snakePos[1] < 0:
                                        m_sound['crash'].play()
                                
                                        GO = True
                                        while GO:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    terminate()
                                            go_hover = pygame.mouse.get_pos()
                                            go_click = pygame.mouse.get_pressed()
                                            if go_hover[0] >= ((g_x / 2) - 18) and go_hover[0] <= ((g_x / 2) + 8)  and go_hover[1] >= (g_y / 2)+ 32 and go_hover[1] <= (g_y / 2)+ 58:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_o, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                if go_click[0] == True:
                                                    if mute == True:
                                                        None
                                                    else:
                                                        m_sound['click'].play()
                                                    GO = False
                                                    start = False
                                                    nickEnter = False
                                                    nick = ''
                                                    pygame.display.set_mode((720, 460))
                                                cursor_set()
                                                pygame.display.update()
                                            else:
                                                m_screen.fill(black)
                                                go_font = pygame.font.SysFont('monaco', 72)
                                                go_surf = go_font.render('Game Over!', True, red)
                                                go_rect = go_surf.get_rect()
                                                go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                m_screen.blit(go_surf, go_rect)
                                                show_Score(0)
                                                # menu button
                                                m_screen.blit(menu_n, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                cursor_set()
                                                pygame.display.update()



                                    
                                        

                                    # snake hit its body
                                    for block in snakeBody[1:]:
                                        if snakePos[0] == block[0] and snakePos[1] == block[1]:
                                            
                                            GO = True
                                            while GO:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        terminate()
                                                go_hover = pygame.mouse.get_pos()
                                                go_click = pygame.mouse.get_pressed()
                                                if go_hover[0] >= ((g_x / 2) - 18) and go_hover[0] <= ((g_x / 2) + 8)  and go_hover[1] >= (g_y / 2)+ 32 and go_hover[1] <= (g_y / 2)+ 58:
                                                    m_screen.fill(black)
                                                    go_font = pygame.font.SysFont('monaco', 72)
                                                    go_surf = go_font.render('Game Over!', True, red)
                                                    go_rect = go_surf.get_rect()
                                                    go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                    m_screen.blit(go_surf, go_rect)
                                                    show_Score(0)
                                                    # menu button
                                                    m_screen.blit(menu_o, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                    if go_click[0] == True:
                                                        if mute == True:
                                                            None
                                                        else:
                                                            m_sound['click'].play()
                                                    GO = False
                                                    start = False
                                                    nickEnter = False
                                                    nick = ''
                                                    pygame.display.set_mode((720, 460))
                                                    cursor_set()
                                                    pygame.display.update()
                                                else:
                                                    m_screen.fill(black)
                                                    go_font = pygame.font.SysFont('monaco', 72)
                                                    go_surf = go_font.render('Game Over!', True, red)
                                                    go_rect = go_surf.get_rect()
                                                    go_rect.midtop = ((g_x / 2), (g_y / 6))
                                                    m_screen.blit(go_surf, go_rect)
                                                    show_Score(0)
                                                    # menu button
                                                    m_screen.blit(menu_n, (((g_x / 2) - 20), (g_y / 2)+ 30))
                                                    cursor_set()
                                                    pygame.display.update()
                                                
                                            
                                        
                                    
                                    show_Score()
                                    pygame.display.flip()
                                    fpsController.tick(speed)
                                    

# <------------------------------------ GAME FINISH ----------------------------------------->
                        
                            

                        else:
                            write('Play', 345, 32)
                            
                            # nick block
                            write('Enter Your Nick:', 220, 177) # nick label
                            m_screen.blit(nick_box, (330, 170)) # nick box
                            if nickEnter == True:
                                nick_surface = n_font.render(nick, True, (white))
                                m_screen.blit(nick_surface, (335, 177))
                            
                            if click == True:
                                red_color = pygame.Color(255, 0, 0)
                                error_font = pygame.font.SysFont('monaco', 14, bold = False, italic = False) # Error text font
                                error = error_font.render('Please enter your nick or enter your nick between 4-8', True, red_color)
                                m_screen.blit(error, (330, 210))


                            m_screen.blit(button_n, (320, 230)) # normal start button
                            write('START', 345, 237) # start button
                            m_screen.blit(menu_n, (325, 280)) # menu normal button
                            write('Menu:', 280, 289) # menu button text
                            cursor_set()
                            pygame.display.update()
                            



#####################################         OPTIONS         #####################################
        elif mouse[1] >= 174 and mouse[1] <= 195 and mouse[0] >= 316 and mouse[0] <= 400: # if hover options button
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_o, (311, 171)) # hover options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # Quit
            m_screen.blit(help_button, (640, 380)) # help button
            

            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 334, 179) # hover options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit
            cursor_set()
            if m_click[0] == 1: # mouse click control
                if mute == True:
                    None
                else:
                    m_sound['click'].play() # play click sound
                option = True
                while option:
                    
                    m_screen.fill(pygame.Color(255, 255, 255))
                    m_screen.blit(o_BG, (0, 0))
                    write('Options', 332, 32)
                    cursor_set()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            option = False
                            terminate()
                        else:
                            o_hover = pygame.mouse.get_pos()
                            o_click = pygame.mouse.get_pressed()
                            cursor_set()
                            # Menu Hovered Options Menu
                            if o_hover[0] >= 85 and o_hover[0] <= 105 and o_hover[1] >= 345 and o_hover[1] <= 365:
                                m_screen.blit(menu_o, (81, 341)) # hover home button
                                opt(0, 0)
                                
                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                cursor_set()
                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    option = False
                                cursor_set()
                            # LEFT
                            # screen size left
                            elif o_hover[1] >= 128 and o_hover[1] <= 142 and o_hover[0] >= 352 and o_hover[0] <= 365:
                                opt(1, 1)
                                
                                # screen size
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if screen_size == 3:
                                        screen_size = 2
                                        g_x = 720
                                        g_y = 460
                                    elif screen_size == 2:
                                        screen_size = 1
                                        g_x = 460
                                        g_y = 280
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar


                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            
                            # FPS left
                            elif o_hover[1] >= 178 and o_hover[1] <= 192 and o_hover[0] >= 352 and o_hover[0] <= 365:
                                opt(1, 2)
                                
                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if speed_level == 3:
                                        speed_level = 2
                                        speed = 12
                                    elif speed_level == 2:
                                        speed_level = 1
                                        speed = 10

                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar


                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()

                            # Fruit left
                            elif o_hover[1] >= 228 and o_hover[1] <= 242 and o_hover[0] >= 352 and o_hover[0] <= 365:
                                opt(1, 3)
                                
                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar


                                # fruit
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if food_bar == 6:
                                        food_bar = 5
                                        food = strawberry
                                    elif food_bar == 5:
                                        food_bar = 4
                                        food = grape
                                    elif food_bar == 4:
                                        food_bar = 3
                                        food = cherry
                                    elif food_bar == 3:
                                        food_bar = 2
                                        food = berry
                                    elif food_bar == 2:
                                        food_bar = 1
                                        food = peach

                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    food = orange
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()

                            # BG Color left
                            elif o_hover[1] >= 278 and o_hover[1] <= 292 and o_hover[0] >= 352 and o_hover[0] <= 365:
                                opt(1, 4)
                                
                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar


                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if BG_color == 3:
                                        BG_color = 2
                                        color = game_orange
                                    elif BG_color == 2:
                                        BG_color = 1
                                        color = green


                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            
                            # Sound left
                            elif o_hover[1] >= 328 and o_hover[1] <= 342 and o_hover[0] >= 352 and o_hover[0] <= 365:
                                opt(1, 5)
                                
                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1: # LOW
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2: # MEDIUM
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3: # FAST
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 2:
                                    if o_click[0] == 1:
                                        if mute == True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        mute_bar = 1
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                    mute = False
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                    mute = True
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()

                            # RIGHT
                            # size right
                            elif o_hover[1] >= 128 and o_hover[1] <= 142 and o_hover[0] >= 503 and o_hover[0] <= 516:
                                opt(2, 1)
                                

                                # screen size
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if screen_size == 1:
                                        screen_size = 2
                                        g_x = 720
                                        g_y = 460
                                    elif screen_size == 2:
                                        screen_size = 3
                                        g_x = 1080
                                        g_y = 720

                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()

                            # FPS right
                            elif o_hover[1] >= 178 and o_hover[1] <= 192 and o_hover[0] >= 503 and o_hover[0] <= 516:
                                opt(2, 2)
                                

                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if speed_level == 1:
                                        speed_level = 2
                                        speed = 12
                                    elif speed_level == 2:
                                        speed_level = 3
                                        speed = 15

                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            # fruit right
                            elif o_hover[1] >= 228 and o_hover[1] <= 242 and o_hover[0] >= 503 and o_hover[0] <= 516:
                                opt(2, 3)
                                

                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if food_bar == 1:
                                        food_bar = 2
                                        food = berry
                                    elif food_bar == 2:
                                        food_bar = 3
                                        food = cherry
                                    elif food_bar == 3:
                                        food_bar = 4
                                        food = grape
                                    elif food_bar == 4:
                                        food_bar = 5
                                        food = strawberry
                                    elif food_bar == 5:
                                        food_bar = 6
                                        food = orange

                                if food_bar == 1:
                                    food = peach
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange
                                
                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            # BG color right
                            elif o_hover[1] >= 278 and o_hover[1] <= 292 and o_hover[0] >= 503 and o_hover[0] <= 516:
                                opt(2, 4)
                                

                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange

                                # BG color 
                                if o_click[0] == 1:
                                    if mute == True:
                                        None
                                    else:
                                        m_sound['click'].play()
                                    if BG_color == 1:
                                        BG_color = 2
                                        color = game_orange
                                    elif BG_color == 2:
                                        BG_color = 3
                                        color = yellow

                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            # sound right
                            elif o_hover[1] >= 328 and o_hover[1] <= 342 and o_hover[0] >= 503 and o_hover[0] <= 516:
                                opt(2, 5)
                                

                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # speed
                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange

                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)

                                # sound button
                                if mute_bar == 1:
                                    if o_click[0] == 1:
                                        if mute == True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        mute_bar = 2
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                    mute = False
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                    mute = True

                                
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            # Normal Options Menu
                            else:
                                opt(0, 0)
                

                                # screen size
                                if screen_size == 1:
                                    write('460 x 280', 410, 130) # small
                                elif screen_size == 2:
                                    write('720 x 460', 410, 130) # medium
                                elif screen_size == 3:
                                    write('1080 x 720', 410, 130) # screen size

                                # sound button
                                if mute_bar == 1:
                                    m_screen.blit(unmute, (425, 320))
                                elif mute_bar == 2:
                                    m_screen.blit(nmute, (425, 320))
                                
                                # speed
                                if speed_level == 1:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                elif speed_level == 2:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                elif speed_level == 3:
                                    m_screen.blit(slow, (400, 180)) # slow bar
                                    m_screen.blit(medium, (430, 170)) # medium bar
                                    m_screen.blit(fast, (460, 160)) # fast bar

                                # fruit
                                if food_bar == 1:
                                    m_screen.blit(peach1, (425, 220)) # peach
                                elif food_bar == 2:
                                    m_screen.blit(berry1, (425, 220)) # berry
                                elif food_bar == 3:
                                    m_screen.blit(cherry1, (425, 220)) # cherry
                                elif food_bar == 4:
                                    m_screen.blit(grape1, (425, 220)) # grape
                                elif food_bar == 5:
                                    m_screen.blit(strawberry1, (425, 220)) # strawberry
                                elif food_bar == 6:
                                    m_screen.blit(orange1, (425, 220)) # orange

                                # BG color 
                                if BG_color == 1:
                                    write('Green', 425, 280 )
                                elif BG_color == 2:
                                    write('Light Orange', 410, 280)
                                elif BG_color == 3:
                                    write('Yellow', 425, 280)


                                

                                # home button
                                m_screen.blit(menu_n, (80, 340)) # normal home button
                                cursor_set()
                            cursor_set()
                        pygame.display.update()




#####################################         HOW TO PLAY       #####################################
        elif mouse[1] >= 224 and mouse[1] <= 245 and mouse[0] >= 316 and mouse[0] <= 400: # if hover how to play button
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_o, (311, 221)) # hover how to play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # Quit
            m_screen.blit(help_button, (640, 380)) # help button
            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts 
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 327, 228) # hover how to play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit
            cursor_set()
            if m_click[0] == 1: # mouse click control
                if mute == True:
                    None
                else:
                    m_sound['click'].play() # play click sound
                manual = True
                manual_page = 0
                while manual:
                    
                    m_screen.fill(pygame.Color(255, 255, 255))
                    m_screen.blit(manual_BG, (0, 0))
                    write('How to Play', 324, 32)
                    cursor_set()

                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            manual = False
                            terminate()
                        else:
                            manual_hover = pygame.mouse.get_pos() # manual menu mouse movement
                            manual_click = pygame.mouse.get_pressed() # manual menu mouse click
                            cursor_set()
                            if manual_page == 0:
                                m_screen.blit(m1, (150, 100))
                                if manual_hover[0] >= 658 and manual_hover[0] <= 672 and manual_hover[1] >= 212 and manual_hover[1] <= 226:
                                    
                                    m_screen.blit(o_right, (656, 211))
                                    m_screen.blit(menu_n, (80, 340))
                                    cursor_set()
                                    if manual_click[0] == 1:
                                        if mute ==  True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        manual_page = 1
                                    cursor_set()
                                elif manual_hover[0] >= 85 and manual_hover[0] <= 105 and manual_hover[1] >= 345 and manual_hover[1] <= 365:
                                    
                                    m_screen.blit(menu_o, (81, 341)) # hover home button
                                    m_screen.blit(n_right, (655, 210))
                                    cursor_set()
                                    if manual_click[0] == 1:
                                        if mute == True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        manual = False
                                    cursor_set()
                                else:
                                    m_screen.blit(menu_n, (80, 340)) # normal home button
                                    m_screen.blit(n_right, (655, 210))
                                    cursor_set()
                            elif manual_page == 1:
                                m_screen.blit(m2, (150, 100))
                                if manual_hover[0] >= 48 and manual_hover[0] <= 61 and manual_hover[1] >= 212 and manual_hover[1] <= 226:
                                    m_screen.blit(o_left, (46, 211))
                                    m_screen.blit(menu_n, (80, 340)) # normal home button
                                    cursor_set()
                                    if manual_click[0] == 1:
                                        if mute == True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        manual_page = 0
                                    cursor_set()
                                elif manual_hover[0] >= 85 and manual_hover[0] <= 105 and manual_hover[1] >= 345 and manual_hover[1] <= 365: 
                                    
                                    m_screen.blit(menu_o, (81, 341)) # hover home button
                                    m_screen.blit(n_left, (45, 210))
                                    cursor_set()
                                    if manual_click[0] == 1:
                                        if mute == True:
                                            None
                                        else:
                                            m_sound['click'].play()
                                        manual = False
                                else:
                                    m_screen.blit(menu_n, (80, 340)) # normal home button
                                    m_screen.blit(n_left, (45, 210))
                                    cursor_set()
                                cursor_set()
                        pygame.display.update()
                

                            
#####################################      HİGH SCORE     #####################################
        elif mouse[1] >= 274 and mouse[1] <= 295 and mouse[0] >= 316 and mouse[0] <= 400: # if hover high score button
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_o, (311, 271)) # hover high score
            m_screen.blit(button_n, (310, 320)) # Quit
            m_screen.blit(help_button, (640, 380)) # help button
            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 329, 280) # hover high score text
            write('Quit', 345, 328) # Quit
            cursor_set()
            if m_click[0] == 1: # mouse click control
                if mute == True:
                    None
                else:
                    m_sound['click'].play() # play click sound
                score = True
                while score:
                    
                    m_screen.fill(pygame.Color(255, 255, 255))
                    m_screen.blit(score_BG, (0, 0))
                    write('High Score', 325, 32)
                    cursor_set()
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            play = False
                            terminate()

                        # mouse action
                        s_hover = pygame.mouse.get_pos() # score menu mouse movement
                        s_click = pygame.mouse.get_pressed() # score menu mouse click
                        if s_hover[0] >= 245 and s_hover[0] <= 265 and s_hover[1] >= 293 and s_hover[1] <= 315:
                            m_screen.blit(first, (240, 110))
                            
                            m_screen.blit(second, (240, 170))
                            m_screen.blit(third, (240, 230))
                            m_screen.blit(s_table, (300, 110))
                            m_screen.blit(s_table, (300, 170))
                            m_screen.blit(s_table, (300, 230))
                            write_score('test3', 315, 120)
                            write_score('3545', 360, 120)
                            write_score('test11', 315, 180)
                            write_score('2115', 360, 180)
                            write_score('test5', 315, 240)
                            write_score('730', 360, 240)
                            m_screen.blit(menu_o, (241, 291)) # hover home button
                            cursor_set()
                            if s_click[0] == 1:
                                if mute == True:
                                    None
                                else:
                                    m_sound['click'].play() # play click sound
                                score = False
                        else:
                            m_screen.blit(first, (240, 110))
                            m_screen.blit(second, (240, 170))
                            m_screen.blit(third, (240, 230))
                            m_screen.blit(s_table, (300, 110))
                            m_screen.blit(s_table, (300, 170))
                            m_screen.blit(s_table, (300, 230))
                            write_score('test3', 315, 120)
                            write_score('3545', 360, 120)
                            write_score('test11', 315, 180)
                            write_score('2115', 360, 180)
                            write_score('test5', 315, 240)
                            write_score('730', 360, 240)
                            m_screen.blit(menu_n, (240, 290)) # normal home button
                            cursor_set()
                        cursor_set()
                        pygame.display.update()




#####################################        QUIT       #####################################
        elif mouse[1] >= 324 and mouse[1] <= 345 and mouse[0] >= 316 and mouse[0] <= 400: # if hover quit button
            
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_o, (311, 321)) # hover quit
            m_screen.blit(help_button, (640, 380)) # help button
            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 346, 329) # hover quit text

            if m_click[0] == 1: # mouse click control
                pygame.time.wait(10)
                if mute == True:
                    None
                else:
                    m_sound['click'].play() # play click sound
                pygame.time.wait(10)
                running = False
                terminate()
            cursor_set()




        # <---------------------- HELP BUTTON ----------------------->    
        elif mouse[0] >= 641 and mouse[0] <= 663 and mouse[1] >= 381  and mouse[1] <= 403:
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # quit
            m_screen.blit(help_button, (640, 380)) # help button

            # social media buttons
            m_screen.blit(facebook, (250, 380)) # hover facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit 
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('help.html')
            cursor_set()


        # <---------------- HOVER SOCIAL MEDIA ------------------>
        # hover facebook
        elif mouse[0] >= 255 and mouse[0] <= 275 and mouse[1] >= 385 and mouse[1] <= 405:
            
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # quit
            m_screen.blit(help_button, (640, 380)) # help button

            # social media buttons
            m_screen.blit(facebook, (251, 381)) # hover facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # menu texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit 
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('https://www.facebook.com/omer.ozkan.92754397')
            cursor_set()



        # hover twitter
        elif mouse[0] >= 305 and mouse[0] <= 325 and mouse[1] >= 385 and mouse[1] <= 405:
            normal_menu()
            write('Main Menu', 324, 32)
            m_screen.blit(help_button, (640, 380)) # help button
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (301, 381)) # hover twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('https://twitter.com/104Zkan')
            cursor_set()
        # hover instagram
        elif mouse[0] >= 355 and mouse[0] <= 375 and mouse[1] >= 385 and mouse[1] <= 405:
            
            normal_menu()
            write('Main Menu', 324, 32)
            m_screen.blit(help_button, (640, 380)) # help button
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (351, 381)) # hover instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('https://www.instagram.com/omerozkan785')
            cursor_set()
        # hover linked in
        elif mouse[0] >= 405 and mouse[0] <= 425 and mouse[1] >= 385 and mouse[1] <= 405:
            
            normal_menu()
            write('Main Menu', 324, 32)
            m_screen.blit(help_button, (640, 380)) # help button
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (401, 381)) # hover linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('www.linkedin.com/in/o3omer')
            cursor_set()
        # hover youtube
        elif mouse[0] >= 455 and mouse[0] <= 475 and mouse[1] >= 385 and mouse[1] <= 405:
            
            normal_menu()
            write('Main Menu', 324, 32)
            m_screen.blit(help_button, (640, 380)) # help button
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (451, 381)) # youtube icon
            if m_click[0] == 1:
                if mute == True:
                    None
                else:
                    m_sound['click'].play()
                webbrowser.open('https://www.youtube.com/channel/UCnyGoEFzT0wybX8oA10gFaQ?view_as=subscriber')
            cursor_set()

#####################################        NORMAL MENU BLOCK        #####################################
        else: # The cursour not point any button
            
            # drawing buttons
            m_screen.blit(button_n, (310, 120)) # Play
            m_screen.blit(button_n, (310, 170)) # Options
            m_screen.blit(button_n, (310, 220)) # How to Play
            m_screen.blit(button_n, (310, 270)) # High Score
            m_screen.blit(button_n, (310, 320)) # Quit
            m_screen.blit(help_button, (640, 380)) # help button
            # social media icons
            m_screen.blit(facebook, (250, 380)) # facebook icon
            m_screen.blit(twitter, (300, 380)) # twitter icon
            m_screen.blit(instagram, (350, 380)) # instagram icon
            m_screen.blit(linkedin, (400, 380)) # linkedin icon
            m_screen.blit(youtube, (450, 380)) # youtube icon

            # buttons texts
            write('Main Menu', 324, 32)
            write('Play', 345, 128) # play text
            write('Options', 333, 178) # options text
            write('How to Play', 326, 227) # How to Play text
            write('High Score', 328, 279) # High Score text
            write('Quit', 345, 328) # Quit 
            cursor_set() 
        pygame.display.update()
        