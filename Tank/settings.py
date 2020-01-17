import pygame
from os import path
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

largo = 1024 #32
alto = 576  #18
tile = 32
gridlargo = int(alto / tile)
gridalto = int(largo / tile)

pygame.mixer.init()

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
Background = BLACK
wa = pygame.image.load(path.join(img_dir, "1.png"))
shield = pygame.image.load(path.join(img_dir, "Shield.png"))
S = pygame.image.load(path.join(img_dir, "s.png"))
bullet = pygame.image.load(path.join(img_dir, "BulletIcon.png"))
tar = pygame.image.load(path.join(img_dir, "target.png"))
Backgroundim = pygame.image.load(path.join(img_dir, "Ground.jpg"))
playerimg1 = pygame.image.load(path.join(img_dir, "tank.png"))
playerimg2 = pygame.image.load(path.join(img_dir, "tank2.png"))
shootsnd = pygame.mixer.Sound(path.join(snd_dir, "shoot.wav"))
avanzarsnd = pygame.mixer.Sound(path.join(snd_dir, "avanzar.wav"))
explosionsnd = pygame.mixer.Sound(path.join(snd_dir, "explosion.wav"))