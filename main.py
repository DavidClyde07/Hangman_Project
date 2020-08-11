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
A = 65 #ASCII code for the letter A

#Creating a font for the letters, comicsans is the font and 40 is the font size
LETTER_FONT = pygame.font.SysFont("comicsans", 40)


for i in range(26):
  x = x_start + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
  y = y_start + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x,y, chr(A + i)]) #cast chr to get the ASCII charater with the code A+i, as i increments you get B , C etc...





####################################################################################
'''Draw function '''
####################################################################################

def draw() :

  window.fill(WHITE)
  
  #Drawing buttons
  for letter in letters :
    x , y, ltr  = letter #Unpacking letter. Recall each element in looks like [x,y, A+i]
    #drawing each cicle parameters are where, color, start pos, radius, line weight
    pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3) 
    text = LETTER_FONT.render(ltr, 1, BLACK)
    window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  
  
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
      x_mouse, y_mouse = pygame.mouse.get_pos() #Note pygame coord sys starts at top left
      #print(pos)

      for letter in letters:
        x,y,ltr = letter
        distance = math.sqrt((x-x_mouse)**2 + (y-y_mouse)**2)
        if distance < RADIUS:
          print(ltr)


pygame.quit()