import pygame
import time
pygame.init()

################################################################################
winHeight = 512; winWidth = winHeight
herox = 128; heroy = 0
vel = 8
################################################################################

win = pygame.display.set_mode((winHeight,winWidth))
frame1 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f1.png").convert(), (64,64))
frame2 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f2.png").convert(), (64,64))
frame3 = frame1
frame4 = pygame.transform.smoothscale(pygame.image.load("C:/python_projects/my_projects/animation-study/res/f4.png").convert(), (64,64))
walkDown = [frame1,frame2,frame3,frame4]
walkCount = 0



clock = pygame.time.Clock()
actual_frame = frame1

run = True
while run:
    pygame.time.delay(80)
    r = pygame.time.get_ticks()                        #second = 1000mileseconds
    r2 = int(r/125)                            #1000mileseconds/125 = 1/8 second
    win.fill((20,170,80))
    hero = win.blit(actual_frame,(herox, heroy))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if walkCount +1 >= 5:
        walkCount = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        heroy-=vel
        movement = True
    elif keys[pygame.K_DOWN]:
        heroy+=vel
        movement = True
    else:
        movement = False
        actual_frame = frame1
    while movement == True:
        if r2%2==0:
            actual_frame = frame2

        elif r2%2!=0:
            actual_frame = frame4
        break
    pygame.display.update()
