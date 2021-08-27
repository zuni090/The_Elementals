import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1368,700))

#back-img
back = pygame.image.load('game background.jpg')
screen.blit(back,(0,0))
# background music
mixer.music.load('Free_Pipe-Howl-Rumble-By-Transition_TRANE01048.wav')
mixer.music.play(-1)

pygame.font.init()
def abc():
    back = pygame.image.load('game background.jpg')
    screen.blit(back,(0,0))
    head = pygame.font.Font('freesansbold.ttf', 17)
    heading = pygame.font.Font('freesansbold.ttf', 30)
    under = pygame.font.Font('freesansbold.ttf', 15)
    instruction = pygame.font.Font('freesansbold.ttf', 17)
    first()
    second()
    third()

def first():
        a =  head.render("This Game has been developed using Python\tin Pycharm Community Edition 20.1", True, (128,128,128))
        screen.blit(a , (350, 80))

def second():
    b = heading.render("GAME CONTROL KEYS",True,(204,0,0))
    bb = under.render("=======================================",True,(204,0,0))
    screen.blit(b,(420,150))
    screen.blit(bb,(420,180))

def third():
    c = instruction.render("-> Use Arrow keys as prespective to move up , down , left and right .",True,(255,255,0))
    cc = instruction.render("-> Use Space Bar to shoot the bullet .",True,(255,255,0))
    screen.blit(c,(320,200))
    screen.blit(cc,(320,220))
    a1 = instruction.render("- This Game is based on Avatar type , and has 4 modes i.e EARTH , AIR , FIRE and WATER .",True,(255,255,0))
    a2 = instruction.render("- Each levels has its own function and difficulties , you have to kill all bots to clear level.",True, (255,255,0))
    a3 = instruction.render("- On collision with bot or bot's bullet, player ship will lose health . ",True,(255,255,0))
    a4 = instruction.render("- You have to kill the boss as well which appear at last in game to win the game .  ", True,(255, 255, 0))
    screen.blit(a1,(290,260))
    screen.blit(a2, (290,290))
    screen.blit(a3, (290,320))
    screen.blit(a4, (290, 350))

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

abc()
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game  = False

    pygame.display.update()
