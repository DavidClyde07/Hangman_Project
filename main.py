####################################################################################
'''Exploring the python PyGame module by creating a simple hangman game.'''
####################################################################################

import pygame
import math
import random

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
hangman_status = 0 #tracks the player status hence which image to draw
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

RADIUS, GAP = 20, 15

letters = []
x_start = round((WIDTH - (RADIUS*2 + GAP) * 13 ) / 2 )
y_start = 400 
A = 65 #ASCII code for the letter A

words = ["HANGMAN", "DEVELOPER", "GEOMATICS", ]  #List to store the word to be guessed
secret_word = random.choice(words)
guessed = [] #List to store the gussed letters

#Creating a font for the letters, comicsans is the font and 40 is the font size
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)
TITLE = "DEVELOPER HANGMAN!"

for i in range(26):
  x = x_start + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
  y = y_start + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x,y, chr(A + i), True]) #cast chr to get the ASCII charater with the code A+i, as i increments you get B , C etc...


####################################################################################
'''Draw function '''
####################################################################################

def draw() :

  window.fill(WHITE)
  #Draw title 
  text = TITLE_FONT.render(TITLE, 1, BLACK)
  window.blit(text, (WIDTH/2 - text.get_width()/2 , 20 ))

  #Drawing a word to be guessed
  display_word = ""

  for letter in secret_word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "
  text = WORD_FONT.render(display_word, 1, BLACK)
  window.blit(text, (400,200) )

  #Drawing buttons
  for letter in letters :
    x , y, ltr, visible  = letter #Unpacking letter. Recall each element in looks like [x,y, A+i, visible boolean]
    if visible:
      #drawing each cicle. parameters are where, color, start pos, radius, line weight
      pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3) 
      text = LETTER_FONT.render(ltr, 1, BLACK)
      window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  
  
  window.blit(images[hangman_status], (100,150))
  pygame.display.update()

####################################################################################
'''Display Message function '''
####################################################################################

def display_message(message):
  pygame.time.delay(1000) #1 sec delay so user can see what happened
  window.fill(WHITE)
  text = WORD_FONT.render(message, 1, BLACK)
  window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(3000)#3 sec delay so user can read the end message before the game terminates.
  
###################################################################################
'''Setting up game loop to handel running of the game'''
###################################################################################


def main():

  global hangman_status
  FPS = 50 #Game will run at 50 frames per sec, Constant Variable
  run = True 
  clock = pygame.time.Clock()
  
  while run:
    clock.tick(FPS)
    
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
          x,y,ltr,visible = letter
          if visible:
            distance = math.sqrt((x-x_mouse)**2 + (y-y_mouse)**2)
            #when a letter is clicked make it disappear by setting visible boolean to False
            if distance < RADIUS:
              letter[3] = False
              guessed.append(ltr)

              if ltr not in secret_word:
                hangman_status += 1
    
    draw()
    
    won = True
    for letter in secret_word:
      if letter not in guessed:
        won = False
        break
    
    if won:
      display_message("You WON!!!")
      break

    if hangman_status == 6:
      display_message("You LOST!!!")  
      break


main()
pygame.quit()