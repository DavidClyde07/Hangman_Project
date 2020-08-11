####################################################################################
'''Exploring the python PyGame module by creating a simple hangman game.'''
####################################################################################

import pygame
import math


pygame.init()  #Initializing the pygame module

####################################################################################
'''Setting up the game display window'''
####################################################################################

#Variable for the display, NOTE these are constants 
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT)) #set_mode method defines dispaly dimensions

pygame.display.set_caption("Lets Play Hangman!!!")

###################################################################################
''' Loading In Images''' 
###################################################################################

#storing images in a list

images = []
#loop to populate list with the images
for i in range(7):
  each_image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(each_image)


####################################################################################
'''Game Variables'''
####################################################################################
hangman_status = 1 #tracks the player status hence which image to draw
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

RADIUS, GAP = 20, 15

letters = []
x_start = round((WIDTH - (RADIUS*2 + GAP) * 13 ) / 2 )
y_start = 400 

for i in range(26):
  x = x_start + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
  y = y_start + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x,y])





####################################################################################
'''Draw function '''
####################################################################################

def draw() :

  window.fill(WHITE)

  for letter in letters :
    x , y  = letter #Unpacking letter. Recall each element in looks like [x,y]
    #drawing each cicle parameters are where, color, start pos, radius, line weight
    pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3) 


  window.blit(images[hangman_status], (100,150))
  pygame.display.update()





###################################################################################
'''Setting up game loop to handel running of the game'''
###################################################################################
FPS = 50 #Game will run at 50 frames per sec, Constant Variable
run = True 
clock = pygame.time.Clock()

while run:
  clock.tick(FPS)
  draw()

  #Loop to handle game events
  for event in pygame.event.get():
    #Handle quiting
    if event.type == pygame.QUIT:
      run = False
    #Handel mouse clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos() #Note pygame coord sys starts at top left
      print(pos)


pygame.quit()