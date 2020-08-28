import pygame
import time
pygame.init()

################################################################################
winHeight = 512; winWidth = winHeight
herox = 128; heroy = 0
vel = 12
walkCount = 0
up = False
down = False
left = False
right = False
################################################################################

win = pygame.display.set_mode((winHeight,winWidth))
frame1 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f1.png").convert(), (64,64))
frame2 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f2.png").convert(), (64,64))
frame3 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f1.png").convert(), (64,64))
frame4 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f4.png").convert(), (64,64))
bframe1 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/b1.png").convert(), (64,64))
bframe2 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/b2.png").convert(), (64,64))
bframe3 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/b3.png").convert(), (64,64))
bframe4 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/b4.png").convert(), (64,64))
lframe1 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/l1.png").convert(), (64,64))
lframe2 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/l2.png").convert(), (64,64))
lframe3 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/l3.png").convert(), (64,64))
lframe4 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/l4.png").convert(), (64,64))
rframe1 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/r1.png").convert(), (64,64))
rframe2 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/r2.png").convert(), (64,64))
rframe3 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/r3.png").convert(), (64,64))
rframe4 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/r4.png").convert(), (64,64))
currentFrame = frame1
walkDown = [frame2,frame3,frame4, frame1]
walkUp = [bframe2,bframe3,bframe4,bframe1]
walkLeft = [lframe2,lframe3,lframe4,lframe1]
walkRight = [rframe2,rframe3,rframe4,rframe1]

def makeBorder():
    global heroy
    global herox
    if heroy >= (512-64):
        heroy = (512-64)
    if heroy <= 0:
        heroy = 0
    if herox <=(0-12):
        herox = (0-12)
    if herox >= (winWidth-52):
        herox = (winWidth-52)

def redrawGameWindow():
    global walkCount
    global currentFrame
    win.fill((20,170,80))
    if walkCount +1 >= 5:
        walkCount = 0

    if down:
        win.blit(walkDown[walkCount],(herox,heroy))
        walkCount += 1
        currentFrame = frame1
    elif up:
        win.blit(walkUp[walkCount],(herox,heroy))
        walkCount += 1
        currentFrame = bframe1
    elif left:
        win.blit(walkLeft[walkCount],(herox,heroy))
        walkCount += 1
        currentFrame = lframe1
    elif right:
        win.blit(walkRight[walkCount],(herox,heroy))
        walkCount += 1
        currentFrame = rframe1
    else:
        win.blit(currentFrame,(herox,heroy))

    pygame.display.update()

actual_frame = frame1
run = True
while run:

    pygame.time.delay(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        heroy += vel
        down = True
        up = False
        left = False
        right = False
        if keys[pygame.K_LEFT]:
            herox -= vel//2
        elif keys[pygame.K_RIGHT]:
            herox += vel//2
    elif keys[pygame.K_UP]:
        heroy-= vel
        down = False
        up = True
        left = False
        right = False
        if keys[pygame.K_RIGHT]:
            herox += vel//2
        elif keys[pygame.K_LEFT]:
            herox -= vel//2
    elif keys[pygame.K_LEFT]:
        herox -= vel
        down = False
        up = False
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        herox += vel
        down = False
        up = False
        left = False
        right = True

    else:
        down = False
        up = False
        left = False
        right = False
        walkCount = 0

    makeBorder()
    redrawGameWindow()
