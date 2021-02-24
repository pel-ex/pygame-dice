import pygame
import time
import random
from sys import exit

pygame.init()
pygame.display.set_caption('Dice')
programIcon = pygame.image.load('icon.jpg')

pygame.display.set_icon(programIcon)

size = 500                      # window size
spsz = size//10                 # spot size
m = int(size/2)                 # mid-point of dice (or die?)
l=t=int(size/4)                 # location of left and top spots
r=b=size-l                      # location of right and bottom spots
rolling = 12                    # times that dice rolls before stopping
diecol = (255,255,127)          # die colour
spotcol = (0,127,127)           # spot colour
 
d = pygame.display.set_mode((size, size))
d.fill(diecol)
pygame.display.set_caption("Dice Simulator")
 
for i in range(rolling):
    n=random.randint(1,6)
    d.fill(diecol)                          # clear previous spots
    if n % 2 == 1:
        pygame.draw.circle(d,spotcol,(m,m),spsz)  # middle spot
    if n==2 or n==3 or n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,b),spsz)  # left bottom
        pygame.draw.circle(d,spotcol,(r,t),spsz)  # right top
    if n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,t),spsz)  # left top
        pygame.draw.circle(d,spotcol,(r,b),spsz)  # right bottom
    if n==6:
        pygame.draw.circle(d,spotcol,(m,b),spsz)  # middle bottom
        pygame.draw.circle(d,spotcol,(m,t),spsz)  # middle top
 
    pygame.display.flip()
    time.sleep(0.2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.quit()
pygame.quit()
exit()
