import pygame
import random
import os

pygame.init()

win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Falling Blocks")


script_dir = os.path.dirname('Obstacles')
rel_path = r"/Users/alecdewulf/Desktop/Falling-Blocks/Images"
abs_file_path = os.path.join(script_dir, rel_path)

# loading objects
current_file = "finalboulder.png"
boulderimg = pygame.image.load("finalboulder.png")
current_file = "betterball.png"
snowballimg = pygame.image.load("betterball.png")
current_file = "bestrock.png"
rockimg = pygame.image.load("bestrock.png")

rel_path = r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Powerups"
script_dir = os.path.dirname('Powerups')
abs_file_path = os.path.join(script_dir, rel_path)

# loading powerups
current_file = r"\resizedheart.png"
heartimg = pygame.image.load("resizedheart.png")
current_file = r"\bestgun.png"
gunimg = pygame.image.load(r"bestgun.png")
current_file = r'\better_small.png'
side_gun = pygame.image.load('better_small.png')

#loading background
abs_file_path = os.path.join('Backgrounds',r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Backgrounds")
bg = pygame.image.load("background.jpg")


rel_path = r"C:\Users\Owner\Desktop\Falling-Blocks\Images\Player"
script_dir = os.path.dirname('Player')
abs_file_path = os.path.join(script_dir, rel_path)

# character
char = pygame.image.load("standing.png")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load(r'R3.png'), pygame.image.load(r'R4.png'),\
             pygame.image.load(r'R5.png'), pygame.image.load(r'R6.png'), pygame.image.load( r'R7.png'), pygame.image.load(r'R8.png'), pygame.image.load( r'R9.png')]
walkLeft = [pygame.image.load( r'L1.png'), pygame.image.load( r'L2.png'), pygame.image.load( r'L3.png'), pygame.image.load( r'L4.png'),\
            pygame.image.load(r'L5.png'), pygame.image.load(r'L6.png'), pygame.image.load(r'L7.png'), pygame.image.load( r'L8.png'), pygame.image.load(r'L9.png')]



