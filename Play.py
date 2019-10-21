 #Imports
import pygame
import random
from pygame import *



#Screen Dimensions

WIN_WIDTH = 786
WIN_HEIGHT = 600
HALF_WIDTH = int(WIN_WIDTH / 4)
HALF_HEIGHT = int(WIN_HEIGHT / 4)

#Screen Defaults

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

#Init, Create Screen
pygame.init()
screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

##############Drawing Code##############

#Load Megaman Sprite Sheet
spritesheet = pygame.image.load("Media/Graphics/cia.png")

character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-1,-3889))
character = pygame.transform.scale(character,(19     *4,22*4))
character=pygame.transform.flip(character,True,False)
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
standleft = stage

character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-167,-3887))
character=pygame.transform.flip(character,True,False)
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
blinkleft = stage

standloopleft = [standleft, blinkleft]

character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-1,-3889))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
standright = stage

character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-167,-3887))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
blinkright = stage

standloopright = [standright, blinkright]

character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-20,-4123))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
stepright = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-2,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright1 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-200,-4125))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright2 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-390,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright3 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-587,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright4 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-782,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright5 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-979,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright6 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-1173,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright7 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-1367,-4125))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright8 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-2,-4328))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright9 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-200,-4328))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright10 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-390,-4328))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright11 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-587,-4328))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
runright12 = stage


walkloopright = [stepright, runright1, runright2, runright3,runright4, runright5,runright6,runright7,runright8,runright9,runright10,runright11,runright12]


#dance sprites

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-10,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d1 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-178,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d2 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-341,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d3 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-511,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d4 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-682,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d5 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-853,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d6 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1022,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d7 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1173,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d8 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1357,-6617))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d9 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-7,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d10 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-184,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d11 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-345,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d12 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-510,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d13 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-681,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d14 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-852,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d15 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1026,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d16 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1194,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d17 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1355,-6862))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d18 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-8,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d19 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-176,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d20 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-349,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d21 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-517,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d22 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-680,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d23 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-850,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d24 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1020,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d25 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1192,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d26 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1363,-7107))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d27 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-4,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d28 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-177,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d29 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-345,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d30 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-519,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d31 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-689,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d32 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-859,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d33 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1024,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d34 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1191,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d35 = stage


character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1360,-7349))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d36 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-6,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d37 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-175,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d38 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-351,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d39 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-521,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d40 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-683,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d41 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-852,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d42 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1020,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d43 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1194,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d44 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1358,-7594))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d45 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-3,-7834))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d46 = stage
character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-174,-7834))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d47 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-350,-7834))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d48 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-355,-8571))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d49 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-519,-8571))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d50 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-689,-8571))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d51 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-860,-8571))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d52 = stage

character = Surface((151,234),pygame.SRCALPHA)
character.blit(spritesheet,(-1025,-8571))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
d53 = stage





dloop=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d18,d28,d29,d30,d31,d32,d33,d34,d35,d36,d37,d38,d39,d40,d41,d42,d43,d44,d45,d46,d47,d48,d36,d37,d38,d39,d40,d41,d42,d43,d44,d45,d46,d47,d48,d49,d50,d51,d52,d53,d53,d53,d53,d53,d53]


walkloopleft = [pygame.transform.flip(walkloopright[0],True,False),pygame.transform.flip(walkloopright[1],True,False), pygame.transform.flip(walkloopright[2],True,False), pygame.transform.flip(walkloopright[3],True,False), pygame.transform.flip(walkloopright[4],True,False), pygame.transform.flip(walkloopright[5],True,False), pygame.transform.flip(walkloopright[6],True,False), pygame.transform.flip(walkloopright[7],True,False), pygame.transform.flip(walkloopright[8],True,False), pygame.transform.flip(walkloopright[9],True,False), pygame.transform.flip(walkloopright[10],True,False), pygame.transform.flip(walkloopright[11],True,False), pygame.transform.flip(walkloopright[12],True,False)]

character = Surface((130,205),pygame.SRCALPHA)
character.blit(spritesheet,(-1,-22))
character = pygame.transform.scale(character,(15*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(108,0))
fallright = stage
  
fallleft=pygame.transform.flip(fallright,True,False)


character = Surface((167,201),pygame.SRCALPHA)
character.blit(spritesheet,(-20,-4555))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
stepright = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-2,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright1 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-200,-4555))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright2 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-390,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright3 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-587,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright4 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-782,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright5 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-979,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright6 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-1173,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright7 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-1367,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright8 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-2,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright9 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-200,-4555))
character = pygame.transform.scale(character,(19*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright10 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-390,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright11 = stage

character = Surface((190,204),pygame.SRCALPHA)
character.blit(spritesheet,(-1-587,-4555))
character = pygame.transform.scale(character,(25*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
srunright12 = stage

character = Surface((149,195),pygame.SRCALPHA)
character.blit(spritesheet,(-79,-639))
character = pygame.transform.scale(character,(15*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(108,0))
shootrightstand=stage


shootrightstandloop =[srunright3]#chk this

character = Surface((29,22),pygame.SRCALPHA)
character.blit(spritesheet,(-206,-96))
character = pygame.transform.scale(character, (29*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun1 = stage

character = Surface((26,22),pygame.SRCALPHA)
character.blit(spritesheet,(-239,-96))
character = pygame.transform.scale(character, (26*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun2 = stage

character = Surface((30,24),pygame.SRCALPHA)
character.blit(spritesheet,(-268,-96))
character = pygame.transform.scale(character, (30*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
shootrightrun3 = stage



shootrightrunloop = [srunright1,srunright1, srunright2, srunright3,srunright4, srunright5,srunright6,srunright7,srunright8,srunright9,srunright10,srunright11,srunright12]



shootleftstandloop = [pygame.transform.flip(srunright1,True,False)]

shootleftrunloop = [pygame.transform.flip(shootrightrunloop[0],True,False),pygame.transform.flip(shootrightrunloop[1],True,False), pygame.transform.flip(shootrightrunloop[2],True,False), pygame.transform.flip(shootrightrunloop[3],True,False), pygame.transform.flip(shootrightrunloop[4],True,False), pygame.transform.flip(shootrightrunloop[5],True,False), pygame.transform.flip(shootrightrunloop[6],True,False), pygame.transform.flip(shootrightrunloop[7],True,False), pygame.transform.flip(shootrightrunloop[8],True,False), pygame.transform.flip(shootrightrunloop[9],True,False), pygame.transform.flip(shootrightrunloop[10],True,False), pygame.transform.flip(shootrightrunloop[11],True,False), pygame.transform.flip(shootrightrunloop[12],True,False)]

shootleftstand=pygame.transform.flip(shootrightstand,True,False)










shootfallleft = fallleft





shootfallright = fallright








character = Surface((119,215),pygame.SRCALPHA)
character.blit(spritesheet,(-33,-9116))
character = pygame.transform.scale(character, (15*4,22*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
takedamageright = stage

takedamagerightair = takedamageright

takedamageleft=pygame.transform.flip(takedamageright,True,False)
takedamageleftair=pygame.transform.flip(takedamagerightair,True,False)

#Load Buster Shots Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/bustershots2.png")

character = Surface((12,13),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-80))
character = pygame.transform.scale(character, (25*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(40,0))
bustershot1 = stage

character = Surface((36,20),pygame.SRCALPHA)
character.blit(spritesheet,(-77,-12))
character = pygame.transform.scale(character, (21*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershotm24 = stage

character = Surface((13,13),pygame.SRCALPHA)
character.blit(spritesheet,(-94,-80))
character = pygame.transform.scale(character, (13*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershot3 = stage

character = Surface((19,13),pygame.SRCALPHA)
character.blit(spritesheet,(-113,-80))
character = pygame.transform.scale(character, (19*6,13*6))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
bustershot4 = stage

#Load SMB Enemies Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/bubblebobble.png")

character = Surface((14,16),pygame.SRCALPHA)
character.blit(spritesheet,(-6,-5))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaleft = stage

character = Surface((14,16),pygame.SRCALPHA)
character.blit(spritesheet,(-26,-5))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaright = stage



goombawalk = [goombaleft, goombaright]

spritesheet = pygame.image.load("Media/Graphics/Backgrounds/ghost.png")

character = Surface((102,100),pygame.SRCALPHA)
character.blit(spritesheet,(-322,-240))
character=pygame.transform.flip(character,True,False)
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
ghostleft = stage

character = Surface((102,100),pygame.SRCALPHA)
character.blit(spritesheet,(-799,-240))
character=pygame.transform.flip(character,True,False)
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
ghostright = stage

ghostwalk = [ghostleft, ghostright]

spritesheet = pygame.image.load("Media/Graphics/Backgrounds/cockroach.png")

character = Surface((227,110),pygame.SRCALPHA)
character.blit(spritesheet,(-87,-32))
character=pygame.transform.flip(character,True,False)
character = pygame.transform.scale(character, (50*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
cockroachleft = stage

character = Surface((246,109),pygame.SRCALPHA)
character.blit(spritesheet,(-71,-371))
character=pygame.transform.flip(character,True,False)
character = pygame.transform.scale(character, (50*4,30*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
cockroachright = stage

cockroachwalk = [cockroachleft, cockroachright]
#Load Explosion Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/explosion.png")

explodex = 68
explodey = -6

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-117))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode1 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-181))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode2 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-245))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode3 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-309))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode4 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-373))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode5 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-437))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode6 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-502))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode7 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-566))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode8 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-631))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode9 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-696))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode10 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-760))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-761))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-826))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode12 = stage

explosion = [explode1,explode2,explode3,explode4,explode5,explode6,explode7,explode8,explode9,explode10,explode11,explode12]

#Load Bubble Bobble Enemies Sprite Sheet

#spritesheet = pygame.image.load("Media/Graphics/ant.png")

character = pygame.image.load("Media/Graphics/Backgrounds/ant1.png").convert_alpha()
character = pygame.transform.scale(character, (66*3,64*3))
toasterwalk1 = character

character = pygame.image.load("Media/Graphics/Backgrounds/ant2.png").convert_alpha()
character = pygame.transform.scale(character, (66*3,64*3))
toasterwalk2 = character

toasterwalkloop = [toasterwalk1,toasterwalk2]


#Load Item Sprite Sheet

spritesheet = pygame.image.load("Media/Graphics/item.png")

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-4))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe1 = stage

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-66))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe2 = stage

character = Surface((78,59),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-128))
character = pygame.transform.scale(character, (78*3,59*3))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,0))
itemframe3 = stage

itemloop = [itemframe1, itemframe2, itemframe3]

character=pygame.image.load("Media/Graphics/Backgrounds/thompson.png").convert_alpha()
character = pygame.transform.scale(character,(43*3,17*3))

thompson = character

character = pygame.image.load("Media/Graphics/rol.png").convert_alpha()
character = pygame.transform.scale(character, (87*3,50*3))

rol=character

character = pygame.image.load("Media/Graphics/vss.png").convert_alpha()
character = pygame.transform.scale(character, (87*3,37*3))
#stage = Surface((93*3,71*3),pygame.SRCALPHA)
#stage.blit(character,(130,0))
#vss = stage



vss=character
inconvo=False
press=1
#roomchatid=0  #chking in which room currently u can start conversation
m24=True

########################################
#global variable to check conditions all over program
havezuzu=False
havehappy=False
cockroachstates="cant atk"
vssstates="cant atk"
rolstates="cant atk"
musicplaying='none'

invincible=False
convoid=0#to chk which conversain will happed


#Main Function


def main():

    global inconvo,press,m24,havezuzu,vssstates,invincible,convoid,havehappy
    #Create clock, set caption
    timer = pygame.time.Clock()
    pygame.display.set_caption("Use arrows to move!")

    #Create Game
    game = Game()

    #Create Player
    player = Player(game)

    #Create Display
    display = Display("")

    #Create level
    room = Rooms(game,player)
    

    #Main Loop
    while 1:
        timer.tick(60)
        
        if game.screenfocus=="Checkpoint":
            changemusic('teleport',False)
           
            game.screenfocus="Game"
            game.projectilegroup.empty()
            game.entities.empty()
            game.playerentity.empty()
            player = Player(game)
            display = Display("")
            room = Rooms(game,player)
            tocheckpoint=RoomExit(room,256,56,32,80,game.checkpoint,"checkpoint")
            print(game.checkpoint)
            tocheckpoint.changeroom()
        if game.screenfocus == "Title":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))
            game.title.update()
            

        if game.screenfocus == "Game":
            game.camera.update(game.camerafocus)
            player.update()
    
            for e in game.entities:
                    screen.blit(e.image, game.camera.apply(e))
            for e in game.exitgroup:
                screen.blit(e.image, game.camera.apply(e))
            for e in game.itemgroup:
                e.update()
                screen.blit(e.image, game.camera.apply(e))
            for e in game.playerentity:
                screen.blit(e.image, game.camera.apply(e))
            for e in game.projectilegroup:
                e.update(game.platforms)
                screen.blit(e.image, game.camera.apply(e))
            for e in game.enemygroup:
                e.update(game.platforms,game.projectilegroup)
                screen.blit(e.image, game.camera.apply(e))
            #for e in game.detectablegroup:
            #    screen.blit(e.image, game.camera.apply(e))

            


            if inconvo:
                bg = pygame.image.load("Media/Graphics/Backgrounds/chat.png").convert_alpha()
                bg=pygame.transform.scale(bg,(680,240))
                screen.blit(bg,(0,0))

                temp=conversation(convoid)
                if temp==1:
                    
                    press=1
                    inconvo=False
                        
                        
                #for e in pygame.event.get():
                    #if e.type == QUIT: raise SystemExit("QUIT")
                    #if e.type == KEYDOWN and e.key == K_ESCAPE:
                        #raise SystemExit("ESCAPE")
                    #if e.type == KEYDOWN and e.key == K_SPACE:
                        #inconvo=False
            if not inconvo:
                display.update(player.lifetotal[player.currentlifetotal])
                screen.blit(display.image,(96,0))
                if player.longjumpcooldown==400:

                    
                    font=pygame.font.Font(None, 60)
                    text=font.render("b",1,(0,0,255))
                    screen.blit(text,(60,0))
                    #pygame.display.update()



                if player.m24cooldown>=300:
                    font=pygame.font.Font(None, 60)
                    text=font.render("m",1,(0,255,0))
                    screen.blit(text,(20,0))
                

            #Uncomment To View Objects Detectable Area
            #for e in game.detectablegroup: screen.blit(e.image, game.camera.apply(e))
           

        if game.screenfocus == "Game Over":
            #for e in game.titlegroup: screen.blit(e.image,(0,0))
            #for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))
            inconvo=False
            press=1
            #roomchatid=0  #chking in which room currently u can start conversation
            m24=False

            ########################################
            #global variable to check conditions all over program
            havezuzu=False
            havehappy=False
            cockroachstates="cant atk"
            vssstates="cant atk"
            rolstates="cant atk"

            invincible=False
            convoid=0#to chk whi
            pygame.time.delay(1000)
            game = Game()

            #Create Player
            player = Player(game)

            #Create Display
            display = Display("")

            #Create level
            room = Rooms(game,player)

        if game.screenfocus == "Level Complete":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))

        if game.screenfocus == "Pause Menu":
            for e in game.titlegroup: screen.blit(e.image,(0,0))
            for e in game.menugroup: screen.blit(e.image,(e.rect.x,e.rect.y))
            game.pausemenu.update()

        pygame.display.update()
        

class Game(object):
    def __init__(self):
        #Create Sprite Groups
        self.entities = pygame.sprite.Group()
        self.playerentity = pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemygroup = pygame.sprite.Group()
        self.exitgroup = pygame.sprite.Group()
        self.newlevelgroup=pygame.sprite.Group
        self.menugroup = pygame.sprite.Group()
        self.titlegroup = pygame.sprite.Group()
        self.detectablegroup = pygame.sprite.Group()
        self.itemgroup = pygame.sprite.Group()
        self.msggroup=[]
        self.trapgroup=pygame.sprite.Group()
        #Create Camera
        self.camera = ""
        self.camerafocus = ""
        #Create Platforms
        self.platforms = []
        #invisible blocks that will cause conversation in game
        self.convoblock=[]
        #Create Screen Focus
        self.screenfocus = "Title"
        
        #Create Title
        self.title = Title(self)
        #Create Gameover
        self.gameover = GameOver(self)
        #Create Level Complete
        self.levelcomplete = LevelComplete(self)
        #Create Pause Menu
        self.pausemenu = PauseMenu(self)
        #creating checkpoint
        self.checkpoint=0
    def makecheckpoint(self,value):
        self.checkpoint=value
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y, w, h,chatid=0):
        Entity.__init__(self)
        self.rect = Rect(x*3,y*3,w*3,h*3)
        self.chatid=chatid
    def update(self):
        pass
        
class Player(Entity):
    def __init__(self, game):
        Entity.__init__(self)
        #Add Player to Game
        self.icounter=0 #invincible counter
        self.game = game
        self.game.playerentity.add(self)
        #Set Player Velocities
        self.xvel = 0
        self.yvel = 0
        #Set Player Offsets
        self.xoffset = -128
        self.yoffset = 0
        #cooldown
        self.longjumpcooldown=0
        self.m24cooldown=0

        #Counters
        self.walkcounter = 0
        self.standcounter = 0
        self.attackcounter = 0
        self.takedamagecounter = 0
        self.dancecounter=0
        self.d=pygame.mixer.Sound('Media/Music/bts.ogg')
        self.counter=0
        #States
        #abilities
        self.longjump=False
        self.m24=False
        self.dance=False




        self.collideright = False
        self.onGround = True
        self.airborne = False
        self.faceright = True
        self.takingdamage = False
        self.attacking = False
        self.moving = False
        #Create Player Sprite
        self.image = Surface((300, 150),pygame.SRCALPHA)
        self.rect = Rect(0, 0, 300, 150)
        #Create Player Detectable Area
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(0, 0, 80, 90)
        self.detectable.image = Surface((80,90))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        self.game.detectablegroup.add(self.detectable)
        #Life Meter
        self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll"]
        self.currentlifetotal = 9
        #Inputs
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.space = False       
    def startingposition(self,x,y):
        self.rect = Rect(x, y, 300, 150)
        self.detectable.rect = Rect(x, y, 80, 90)

    def inputhandler(self):
        
            for e in pygame.event.get():
                if not inconvo:
                
                    if e.type == QUIT: raise SystemExit("QUIT")
                    if e.type == KEYDOWN and e.key == K_ESCAPE:
                        raise SystemExit("ESCAPE")
                    if e.type == KEYDOWN and e.key == K_UP and not self.dance:
                        self.up = True
                    if e.type == KEYDOWN and e.key == K_DOWN :
                        self.down = True
                    if e.type == KEYDOWN and e.key == K_LEFT and not self.dance:
                        self.left = True
                    if e.type == KEYDOWN and e.key == K_RIGHT and not self.dance:
                        self.right = True
                    if e.type == KEYDOWN and e.key == K_SPACE and not self.dance:
                        self.space = True
                        changemusic('bullet',False)
                    if e.type == KEYDOWN and e.key == K_b  and havehappy:
                        self.longjump=True
                        self.up=True
                    if e.type == KEYDOWN and e.key == K_m  and m24:
                        
                        self.m24=True
                    if e.type == KEYDOWN and e.key == K_d:
                        
                        self.dance=True

                    if e.type == KEYDOWN and e.key == K_RETURN:
                        self.game.pausemenu.createpausemenu()
                        self.game.screenfocus = "Pause Menu"
                if e.type == KEYUP and e.key == K_SPACE:
                    self.space = False    
                if e.type == KEYUP and e.key == K_UP:
                    self.up = False

                if e.type == KEYUP and e.key == K_b and havehappy:
                        self.longjump=False 
                        self.up=False
                if e.type == KEYUP and e.key == K_d:
                        
                        self.dance=False
                        self.dancecounter=0
                        self.d.stop()
                if e.type == KEYUP and e.key == K_m and m24:
                    self.m24=False
                if e.type == KEYUP and e.key == K_DOWN:
                    self.down = False
                    self.dancecounter=0
                if e.type == KEYUP and e.key == K_RIGHT:
                    self.right = False
                    self.counter = 0
                if e.type == KEYUP and e.key == K_LEFT:
                    self.left = False
                    self.counter = 0

    def update(self):
        #cooldown counter
        if havehappy:
            self.longjumpcooldown+=1
        if self.longjumpcooldown>=400:
            self.longjumpcooldown=400
        if m24:
            self.m24cooldown+=1
            if self.m24cooldown>=400:
                self.m24cooldown=400

          
        
                

        self.inputhandler()
        
        #Apply Inputs

        if self.up:
            if self.onGround:
                if self.longjump:
                     if self.longjumpcooldown>=400:
                            self.yvel=-22.6
                            self.longjumpcooldown=0
                else:
                    self.yvel -= 10.6
            # Only jump if on the ground
        if self.down and self.airborne:
            self.yvel=self.yvel+5.6
            # Does nothing
        if self.left:
            self.faceright = False
            if self.takingdamage == False:
                self.xvel = -8
                self.moving = True
            # Move if not taking damage
        if self.right:
            self.faceright = True
            if self.takingdamage == False:
                self.xvel = 8
                self.moving = True
            # Move if not taking damage
        if self.space:
            projectile = Projectile(self,self.game)
            self.game.projectilegroup.add(projectile)
            self.space = False
            self.attacking = True
            #Create projectile on space
        if self.m24:
            if self.m24cooldown>=300:
                changemusic('m24',False)
                projectile = Projectile(self,self.game,"m24")
                self.game.projectilegroup.add(projectile)
                self.m24 = False
                self.attacking = True


                self.m24cooldown=0
            
            #Create projectile on space
        

        #Apply States 
        if self.yvel < 0: self.airborne = True
            #Player is moving up
        if self.yvel > 1.2: self.airborne = True
            #Player is falling
        if self.onGround == True:
            if self.up == True:
                self.airborne == True
            else:
                self.airborne = False
            #Still airborne while pressing up
        if not self.onGround:
            self.yvel += 0.3
            #Apply gravity
            if self.yvel > 100:
                self.yvel = 100
                #Max falling speed
        if not(self.left or self.right):
            if not self.takingdamage:
                self.moving = False
                self.xvel = 0
            #Stop player if not taking damage
        if self.takingdamage:
            if self.collideright:
                self.xvel = -8
            else:
                self.xvel = 8
            #Move player if taking damage
        if self.attackcounter > 8:
            self.attacking = False
            self.attackcounter = 0
            self.standcounter = 0
            #Stop attacking after 9 updates
        if self.takedamagecounter > 13:
            self.takingdamage = False
            self.takedamagecounter = 0
            #Player stops taking damage after 14 updates
        

        #Increase or Reset Counters
        if self.attacking: self.attackcounter = self.attackcounter + 1
        if self.takingdamage: self.takedamagecounter = self.takedamagecounter + 1
        if not self.moving: self.standcounter = 0

        #Collisions
        self.detectable.rect.left += self.xvel
        self.collide(self.xvel, 0)
        self.detectable.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel)

        #Offsets
        
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        if inconvo and not (self.airborne):
            pygame.time.delay(200) # if i dont add not airbornecondotion than when player interacts with convo block while in air than player will feel like laggy in air
            
        #moving to checkpoint
     


        
        #Animate
        self.animate()

    def collide(self, xvel, yvel):
        global invincible,press,convoid,m24,vssstates,havehappy,havezuzu
        global inconvo

        if convoid>=10 and inconvo:
            self.right=False
            self.left=False
            self.up=False
            self.counter = 0
     
        
        if invincible: self.icounter+=1
        if self.icounter>=100:
           
            self.icounter=0
            invincible=False
        #collide with convo block
        for c in self.game.convoblock:
            if pygame.sprite.collide_rect(self.detectable,c):
                if c.chatid==1:
                    if not musicplaying=='pubg':changemusic('pubg',True)
                self.game.projectilegroup.empty()
                self.right=False
                self.left=False
                self.up=False
                self.counter = 0
                inconvo=True   
                press=1
                convoid=c.chatid     
                self.game.convoblock.remove(c)
                
                
                

               
            
                 


        #Collide Platforms
        for p in self.game.platforms:
            if pygame.sprite.collide_rect(self.detectable, p):
                if xvel > 0:
                    self.detectable.rect.right = p.rect.left
                if xvel < 0:
                    self.detectable.rect.left = p.rect.right
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom

        #Collide Enemies
        for e in self.game.enemygroup:
            if pygame.sprite.collide_rect(self.detectable, e.detectable):
                leftdifference = self.detectable.rect.right - e.detectable.rect.left
                rightdifference = self.detectable.rect.left - e.detectable.rect.right
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                if e.type=="rol":
                    self.currentlifetotal=1

                if not invincible:
                    self.takingdamage = True
                    self.currentlifetotal = self.currentlifetotal - 1
                    changemusic('female'+str(random.randint(1,4))+'',False)
                    invincible=True
                
                if self.currentlifetotal<=0 and vssstates=="can atk" and e.type=="vss":
                    self.game.makecheckpoint(7)
                    self.game.screenfocus="Checkpoint"
                    self.d.stop() #stops music of dance

                    self.kill()
                    return

                elif self.currentlifetotal <= 0 and self.game.checkpoint>0:
                        self.game.screenfocus="Checkpoint"
                        self.d.stop() #stops music of dance
                        
                        

                elif self.game.checkpoint==0 and self.currentlifetotal<=0:
                    self.game.screenfocus = "Game Over"
                    self.d.stop() #stops music of dance
                if e.type=="ghost":
                    self.game.enemygroup.remove(e) #remove ghost after hit


                    #self.game.gameover.creategameover()
                    #self.game.screenfocus = "Game Over"
                    #self.currentlifetotal = 0

        #Collide Items
        for i in self.game.itemgroup:
                if i.type=="zuzu":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        havezuzu=True
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        text("YOU GOT SPIRIT OF zuzu....",0,"red",55)
                        pygame.time.delay(1000)
                elif i.type=="checkpoint":
                    if pygame.sprite.collide_rect(self.detectable,i.detectable):
                            self.currentlifetotal=9
                           
                            self.game.makecheckpoint(i.id)


                elif i.type=="m24":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        m24=True
                        self.m24cooldown=400
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        convoid=13
                        inconvo=True
                elif i.type=="happy":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable) and rolstates=="defeat":
                        havehappy=True
                        self.longjumpcooldown=400
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        convoid=12
                        inconvo=True
                elif i.type=="bd":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        
                    
                        self.game.itemgroup.remove(i)
                        
                        inconvo=True
                        convoid=11
                     
                    #self.game.levelcomplete.createlevelcomplete()
                    #self.game.screenfocus = "Level Complete"
        #collide projectile
        for e in self.game.projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, e):
                leftdifference = self.detectable.rect.right - e.detectable.rect.left
                rightdifference = self.detectable.rect.left - e.detectable.rect.right
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                if not invincible:
                    changemusic('female'+str(random.randint(1,4 ))  +'',False)
                    self.game.projectilegroup.remove(e)
                    self.takingdamage = True
                    self.currentlifetotal = self.currentlifetotal - e.damage
                    invincible=True
                if self.currentlifetotal<=0 and vssstates=="can atk" and e.type=="vss":
                    self.game.makecheckpoint(7)
                    self.game.screenfocus="Checkpoint"
                    vssstates="can dmg"
                    self.kill()
                    return
                           
                    self.game.makecheckpoint(7)
                elif self.currentlifetotal <= 0 and self.game.checkpoint>0:

                    self.game.screenfocus="Checkpoint"
                    self.kill()
                    
                    
                elif self.game.checkpoint==0 and self.currentlifetotal<=0:
                    self.game.screenfocus = "Game Over"

                    #self.game.gameover.creategameover()
                    #self.game.screenfocus = "Game Over"
                    #self.currentlifetotal = 0
        #collide Traps
        for t in self.game.trapgroup:
            if pygame.sprite.collide_rect(self.detectable, t):
                changemusic('yell',False)
                self.game.enemygroup.add(Goomba(self.rect.x+(350*3), 153, -14,"ghost"))
                
                self.game.trapgroup.remove(t)

        #collide msggroup
        for m in self.game.msggroup:
        	if pygame.sprite.collide_rect(self.detectable, m):
        		if m.chatid==1:
        			changemusic('10',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==2:
        			changemusic('20',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==3:
        			changemusic('30',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==4:
        			changemusic('40',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==5:
        			changemusic('5',False)
        			self.game.msggroup.remove(m)


        #Collide Exits
        for x in self.game.exitgroup:
            if pygame.sprite.collide_rect(self.detectable, x):
                if x.roomid==13:
                    if vssstates=="defeat":
                        self.yvel=0
                        self.xvel=0
                        x.changeroom()
                elif x.roomid==19:
                    if cockroachstates=="defeat":
                        self.yvel=0
                        self.xvel=0
                        x.changeroom()
                else:

                    self.yvel=0
                    self.xvel=0
                    x.changeroom()

        #checking checkpoint

    def animate(self):
        
        state = []
        state.append(self.airborne)
        state.append(self.moving)
        state.append(self.faceright)
        state.append(self.takingdamage)
        state.append(self.attacking)
        #Moving
        
        if state[1]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:

                if state[2]:
                    self.walkloop(walkloopright)
                else:
                    self.walkloop(walkloopleft)
        else:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:
                if self.dance:

                    self.danceloop(dloop)
                elif state[2]:
                    self.standloop(standloopright)
                else:
                    self.standloop(standloopleft)
        
        #Attacking
        if state[4]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(shootfallright)
                else:
                    self.updatecharacter(shootfallleft)
            else:
                if state[1]:
                    if state[2]:
                        self.walkloop(shootrightrunloop)
                    else:
                        self.walkloop(shootleftrunloop)
                else:
                    if state[2]:
                        self.updatecharacter(shootrightstand)
                    else:
                        self.updatecharacter(shootleftstand)

        #Hurt
        if state[3]:
            if state[2]:
                self.updatecharacter(takedamageright)
            else:
                self.updatecharacter(takedamageleft)

        

    #Standing Animation Loop    
    def standloop(self, loop):
        if self.standcounter == 0 or self.standcounter == 1:
            self.walkcounter = 0
            self.updatecharacter(loop[0])
        elif self.standcounter == 200: self.updatecharacter(loop[1])
        elif self.standcounter == 210:
            self.updatecharacter(loop[0])
            self.standcounter = 0
        self.standcounter = self.standcounter + 1

    #Walking Animation Loop
    def danceloop(self, loop):
        print(self.dancecounter)
        if self.dancecounter == 0 or self.dancecounter == 1:
            self.standcounter = 0
            self.counter=0
            self.d.stop()
            self.d.play()
            self.updatecharacter(loop[1])
        elif self.dancecounter==(5+(self.counter*9)):
            try:
                self.updatecharacter(loop[self.counter])
                self.counter+=1
            except IndexError:
                self.dancecounter=0
                self.counter=0
            
            
        elif self.dancecounter >= 995:
            self.updatecharacter(loop[1])
            self.dancecounter = 0
            self.counter=0
        self.dancecounter += 1

    def walkloop(self, loop):
        if self.walkcounter == 0 or self.walkcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[1])
        elif self.walkcounter == 5: self.updatecharacter(loop[1])
        elif self.walkcounter == 10: self.updatecharacter(loop[2])
        elif self.walkcounter == 15: self.updatecharacter(loop[3])
        elif self.walkcounter == 20: self.updatecharacter(loop[4])
        elif self.walkcounter == 25: self.updatecharacter(loop[5])
        elif self.walkcounter == 30: self.updatecharacter(loop[6])
        elif self.walkcounter == 35: self.updatecharacter(loop[7])
        elif self.walkcounter == 40: self.updatecharacter(loop[8])
        elif self.walkcounter == 45: self.updatecharacter(loop[9])
        elif self.walkcounter == 50: self.updatecharacter(loop[10])
        elif self.walkcounter == 55: self.updatecharacter(loop[11])
        elif self.walkcounter == 60: self.updatecharacter(loop[12])
        elif self.walkcounter == 65:
            self.updatecharacter(loop[1])
            self.walkcounter = 5
        self.walkcounter = self.walkcounter + 1

    #Update Current Frame
    def updatecharacter(self, ansurf): self.image = ansurf



class Projectile(Entity):
    def __init__(self, player,game,typee=0):
        Entity.__init__(self)
        self.xvel=15
        self.type=typee
        self.prange=500

        self.damage=1

        if typee=="m24":
            self.xvel=40
            self.prange=1000
            self.damage=4
        if typee=="vss":
            self.xvel=7
            self.prange=2000
            self.damage=2
        if typee=="thompson":
        	self.xvel=12
        	self.prange=400 
        	self.damage=1
        if typee=="rol":
        	self.xvel=12
        	self.prange=1000
        	self.damage=1
       	if typee=="rol2":
       		self.xvel=40
        	self.prange=400
        	self.damage=1
        self.detectable = pygame.sprite.Sprite()
        #Place Projectile Facing Right
        if player.faceright == True :
            self.xvel = self.xvel
            
            x = player.detectable.rect.right +10
            y = player.detectable.rect.top + 18 
            if self.type=="m24": self.image=bustershotm24
            else: self.image = bustershot1
            self.detectable.rect = Rect(x, y, 32, 32)
        #Place Projectile Facing Left
        elif player.faceright == False and not (self.type=="rol" or self.type=="rol2"):
            self.xvel = self.xvel * -1
            
            x = player.detectable.rect.left -70
            y = player.detectable.rect.top + 18
            if self.type=="m24":self.image = pygame.transform.flip(bustershotm24, True, False)
            else: self.image = pygame.transform.flip(bustershot1, True, False)
            self.detectable.rect = Rect(x, y, 32, 32)

        if self.type=="rol":
            self.xvel = self.xvel
            
            x = player.detectable.rect.right -60
            y = player.detectable.rect.top + random.randint(10*3,70*3) 
            self.image = ghostright
            self.detectable.rect = Rect(x, y, 32, 32)
        elif self.type=="rol2":
            self.xvel = self.xvel
            
            x = player.detectable.rect.right + 18
            y = player.detectable.rect.top -55
            self.image = ghostright
            self.detectable.rect = Rect(x, y, 32, 32)




        self.detectable.image = Surface((32,32))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        game.detectablegroup.add(self.detectable)
        self.image = pygame.transform.scale(self.image,(96,96))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
        
    def update(self, platforms):
        self.rect.left += self.xvel
        self.detectable.rect.left += self.xvel
        #removing projectile once range is gone
        if self.xvel>0:
            self.prange-=self.xvel
            if self.prange<=0:
                self.kill()
        elif self.xvel<=0:
            self.prange+=(self.xvel)#self.xvel already in negative
            if self.prange<=0:
                self.kill()

        #moving projectile in y axis
        '''self.rect.right+=self.y
        self.detectable.rect.right+=self.y'''
        self.collide(platforms)
    
    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self.detectable, p) and not (self.type=="rol" or self.type=="rol2"):
                self.kill()

class Rooms(object):
    def __init__(self,game,player):
        self.width = 0
        self.height = 0
        self.game = game
        self.player=player
        self.room1counter=0
        self.room6counter=0
        self.room4counter=0
        self.room7counter=0
        if self.game.checkpoint==0:
            self.createroom1("a")

        
    def dumpsprites(self):
        self.game.itemgroup.empty()
        self.game.enemygroup.empty()
        self.game.entities.empty()
        self.game.exitgroup.empty()
        self.game.platforms = []
    def resetcamera(self):
        total_level_width  = self.width*3
        total_level_height = self.height*3
        self.game.camera = Camera(complex_camera, total_level_width, total_level_height)
        self.game.camerafocus = self.player.detectable
    def setbackground(self, backgroundpath):
        self.dumpsprites()
        bg = Entity()
        bg.image = pygame.image.load(backgroundpath)
        self.width = bg.image.get_width()
        self.height = bg.image.get_height()
        bg.rect = Rect(0,0,self.width*3,self.height*3)
        bg.image = pygame.transform.scale(bg.image,(self.width*3,self.height*3))
        self.game.entities.add(bg)
        self.resetcamera()
    def createroom1(self, entrance):
        #global roomchatid
        
        if not musicplaying=='pubg':changemusic('pubg',True)

        #roomchatid=1
        self.room1counter+=1
        #Set Background
        self.setbackground("Media/Graphics/Backgrounds/room1.png")

        
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(160,318)
        elif entrance == "b": self.player.startingposition(2992,1086)
        elif entrance == "c": self.player.startingposition(954*3,94*3)

        #Set Up Enemies
        self.game.enemygroup.add(Goomba(294, 320, -2))
        #self.game.enemygroup.add(Toaster(868, 1016, 200, -2))
        #self.game.enemygroup.add(Toaster(1672, 1209, 600, -2))
        #self.game.enemygroup.add(Toaster(1868, 1209, 600, -2))
        #self.game.enemygroup.add(Goomba(2868, 1109, -2))

        #Set Up Platforms
        self.game.platforms.append(Platform(48,424,976,40))
        self.game.platforms.append(Platform(0,0,48,468))
        self.game.platforms.append(Platform(48,136,32,16))
        self.game.platforms.append(Platform(128,200,128,16))
        self.game.platforms.append(Platform(64,264,48,16))
        self.game.platforms.append(Platform(80,328,112,16))
        self.game.platforms.append(Platform(224,360,80,16))
        self.game.platforms.append(Platform(896,392,128,32))
        self.game.platforms.append(Platform(928,280,96,48))
        self.game.platforms.append(Platform(1026,393,64,32))
        self.game.platforms.append(Platform(44,27,1024,9))
        self.game.platforms.append(Platform(838,38,185,35))
        self.game.platforms.append(Platform(804,137,224,97))
        self.game.platforms.append(Platform(819,238,207,45))
        

        
        #convo block
        if not havezuzu and self.room1counter<=1:
            self.game.convoblock.append(Platform(48,136,124,23,1))

        #roomchatid=1


        #Set Up Exits
        
        self.game.exitgroup.add(RoomExit(self,1025,328,40,64,3,"a"))
        self.game.exitgroup.add(RoomExit(self,1025,71,40,64,11,"b"))
        
    def createroom2(self, entrance):
        global press
        press=1
        #roomchatid=2
        if not musicplaying=='pubg':changemusic('pubg',True)
       
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room2.png")

        #Set Up Player
        if entrance == "a": self.player.startingposition(0,366)
        if entrance == "checkpoint": self.player.startingposition(124*3,130*3)
        #Set Up Platforms
        self.game.platforms.append(Platform(0,152,48,72))
        self.game.platforms.append(Platform(48,168,48,56))
        self.game.platforms.append(Platform(96,184,64,40))
        self.game.platforms.append(Platform(160,168,48,56))
        self.game.platforms.append(Platform(208,152,48,72))
        self.game.platforms.append(Platform(224,88,32,64))
        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))
        self.game.platforms.append(Platform(0,0,48,88))

        #convo block
        
        if not m24:self.game.convoblock.append(Platform(131,147,12,23,2))


        #item
        self.game.itemgroup.add(Item(46,109,"checkpoint",2)) # 2 will b use to create room 2

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-32,88,32,64,3,"b"))

    def createroom3(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room3.png")
        if not musicplaying=='pubg':changemusic('pubg',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(8,1086)
        elif entrance == "b": self.player.startingposition(680,2622)
        elif entrance == "c": self.player.startingposition(8,2622)
        elif entrance == "d": self.player.startingposition(688,318)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,0,32,328))
        self.game.platforms.append(Platform(32,0,192,24))
        self.game.platforms.append(Platform(224,0,32,72)) 
        self.game.platforms.append(Platform(112,24,32,64))
        self.game.platforms.append(Platform(32,24,16,16))
        self.game.platforms.append(Platform(96,24,16,16))
        self.game.platforms.append(Platform(144,24,16,16))
        self.game.platforms.append(Platform(208,24,16,16))
        self.game.platforms.append(Platform(112,200,32,288))
        self.game.platforms.append(Platform(144,328,32,16))
        self.game.platforms.append(Platform(144,456,32,16))
        self.game.platforms.append(Platform(224,136,32,704))
        self.game.platforms.append(Platform(192,136,32,16))
        self.game.platforms.append(Platform(192,264,32,16))
        self.game.platforms.append(Platform(192,392,32,16))
        self.game.platforms.append(Platform(192,520,32,16))
        self.game.platforms.append(Platform(112,584,64,16))
        self.game.platforms.append(Platform(0,392,32,448))
        self.game.platforms.append(Platform(32,392,32,16))
        self.game.platforms.append(Platform(32,648,32,16))
        self.game.platforms.append(Platform(32,776,32,16))
        self.game.platforms.append(Platform(112,712,32,432))
        self.game.platforms.append(Platform(144,712,32,16))
        self.game.platforms.append(Platform(80,840,32,16))
        self.game.platforms.append(Platform(80,968,32,16))
        self.game.platforms.append(Platform(80,1096,32,16))
        self.game.platforms.append(Platform(144,1096,32,16))
        self.game.platforms.append(Platform(0,904,32,336))
        self.game.platforms.append(Platform(32,904,32,16))
        self.game.platforms.append(Platform(32,1032,32,16))
        self.game.platforms.append(Platform(32,1160,32,72))
        self.game.platforms.append(Platform(64,1192,32,40))
        self.game.platforms.append(Platform(96,1224,64,8))
        self.game.platforms.append(Platform(160,1192,32,40))
        self.game.platforms.append(Platform(192,1160,32,80))
        self.game.platforms.append(Platform(224,904,32,336))
        self.game.platforms.append(Platform(192,904,32,16))
        self.game.platforms.append(Platform(256,904,32,24))
        self.game.platforms.append(Platform(-32,904,32,16))
        self.game.platforms.append(Platform(-32,392,32,16))
        self.game.platforms.append(Platform(256,136,32,16))

        #Set Up Enemies
        self.game.enemygroup.add(Goomba(360, 520, 2))
        
        #set up block unless condition
        if not havezuzu:
            self.game.platforms.append(Platform(222,66,37,70))
        
       
        
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-40,328,40,64,1,"b"))
        self.game.exitgroup.add(RoomExit(self,256,840,32,64,2,"a"))
        self.game.exitgroup.add(RoomExit(self,-32,840,32,64,4,"a"))
        self.game.exitgroup.add(RoomExit(self,256,72,32,64,6,"a"))

    def createroom4(self,entrance):
        self.room4counter+=1

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room4.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(672,318)

        #Set Up Platforms
        self.game.platforms.append(Platform(48,168,160,40))
        self.game.platforms.append(Platform(0,0,48,208))
        self.game.platforms.append(Platform(48,0,160,24)) 
        self.game.platforms.append(Platform(208,0,48,56))
        self.game.platforms.append(Platform(208,136,48,72))
        self.game.platforms.append(Platform(256,136,32,16))


        #enemy


        #ITEM
        if not havezuzu:
            self.game.itemgroup.add(Item(110,135,"zuzu"))

            #convoblock
            self.game.convoblock.append(Platform(223,118,20,20,3))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,256,56,32,80,3,"c"))

    def createroom5(self, entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room2.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(0,366)
        
        #Set Up Platforms
        self.game.platforms.append(Platform(0,152,48,72))
        self.game.platforms.append(Platform(48,168,48,56))
        self.game.platforms.append(Platform(96,184,64,40))
        self.game.platforms.append(Platform(160,168,48,56))
        self.game.platforms.append(Platform(208,152,48,72))
        self.game.platforms.append(Platform(224,88,32,64))
        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))
        self.game.platforms.append(Platform(0,0,48,88))
        
        #Set Up Items
        #self.game.itemgroup.add(Item(46,109))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-32,88,32,64,3,"d"))
        self.game.exitgroup.add(RoomExit(self,46,109,20,20,6,"e"))

    def createroom6(self,entrance):
        self.room6counter+=1
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/boss1.png")
        if not vssstates=="cant atk":
            changemusic('boss',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(10,178)
        
        #Set Up Platforms
        self.game.platforms.append(Platform(0,207,1017,35))
        self.game.platforms.append(Platform(1,1,5,210))
        self.game.platforms.append(Platform(1005,94,16,115))
        self.game.platforms.append(Platform(985,11,30,80))
        self.game.platforms.append(Platform(600,11,290,30))

        
        
        #Set Up Items
        #convo block
        if vssstates =="cant atk":

            self.game.convoblock.append(Platform(756,110,22,197,4))
        if m24 and not vssstates =="defeat":
        	self.game.convoblock.append(Platform(10,178,22,22,14))

        #enemy
        self.game.enemygroup.add(boss(900*3, 130*3, 200, -2,self.game))

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,968,187,35,17,13,"a"))
    def createroom7(self,entrance):
        self.room7counter+=1

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room4.png")
        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(122*3,131*3)
        if entrance == "checkpoint": self.player.startingposition(122*3,131*3)

        #Set Up Platforms
        self.game.platforms.append(Platform(48,168,160,40))
        self.game.platforms.append(Platform(0,0,48,208))
        self.game.platforms.append(Platform(48,0,160,24)) 
        self.game.platforms.append(Platform(208,0,48,56))
        self.game.platforms.append(Platform(208,136,48,72))
        self.game.platforms.append(Platform(256,136,32,16))


        #convo block

        if not m24 and self.room7counter<=1: self.game.convoblock.append(Platform(108,111,38,51,6))

        #ITEM
        self.game.itemgroup.add(Item(46,115,"checkpoint",7))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,256,56,32,80,8,"a"))

    def createroom8(self,entrance):
        
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room8.png")

        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(30*3,105*3)
        if entrance == "b": self.player.startingposition(30*3,363*3)

        #Set Up Platforms83
        self.game.platforms.append(Platform(0,35,30,40))
        self.game.platforms.append(Platform(29,21,255,15))
        self.game.platforms.append(Platform(0,137,57,14)) 
        self.game.platforms.append(Platform(110,35,31,57))
        self.game.platforms.append(Platform(112,200,35,19))
        self.game.platforms.append(Platform(256,136,32,16))

        self.game.platforms.append(Platform(223,42,33,414))
        self.game.platforms.append(Platform(187,264,32,18))
        self.game.platforms.append(Platform(106,327,34,18)) 
        self.game.platforms.append(Platform(186,391,38,55))
        self.game.platforms.append(Platform(63,425,131,35))
        self.game.platforms.append(Platform(2,394,60,70))
        self.game.platforms.append(Platform(0,151,25,179))


        #enemy
        self.game.enemygroup.add(Toaster(136, 180, 22, -2))
        self.game.enemygroup.add(Goomba(470, 399, -2))
        
        #ITEM
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-35,71,32,64,7,"a"))
        self.game.exitgroup.add(RoomExit(self,-35,328,32,64,9,"a"))


    def createroom9(self,entrance):
        

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room9.png")

        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(462*3,361*3)
        if entrance == "b": self.player.startingposition(44*3,360*3)

        #Set Up Platforms83
        self.game.platforms.append(Platform(450,394,51,16))
        self.game.platforms.append(Platform(485,0,25,329))
        self.game.platforms.append(Platform(412,330,32,17)) 
        self.game.platforms.append(Platform(370,457,115,23))
        self.game.platforms.append(Platform(480,409,21,296))
        self.game.platforms.append(Platform(223,150,68,439))

        self.game.platforms.append(Platform(293,525,77,20))
        self.game.platforms.append(Platform(447,650,36,70))
        self.game.platforms.append(Platform(65,684,384,31)) 
        self.game.platforms.append(Platform(189,650,100,38))
        self.game.platforms.append(Platform(364,588,42,21))
        self.game.platforms.append(Platform(0,404,32,309))
        self.game.platforms.append(Platform(37,650,27,57))

        self.game.platforms.append(Platform(295,267,109,21))
        self.game.platforms.append(Platform(322,204,159,18))
        self.game.platforms.append(Platform(193,138,256,18))
        self.game.platforms.append(Platform(145,28,18,17))
        self.game.platforms.append(Platform(209,28,18,17))
        self.game.platforms.append(Platform(289,28,18,17))
        self.game.platforms.append(Platform(354,28,18,17))
        self.game.platforms.append(Platform(403,28,18,17))
        self.game.platforms.append(Platform(32,28,18,17))
        self.game.platforms.append(Platform(97,28,18,17))

        self.game.platforms.append(Platform(0,0,482,23))
        self.game.platforms.append(Platform(111,24,34,64))
        self.game.platforms.append(Platform(368,24,34,64))

        self.game.platforms.append(Platform(225,26,64,48))
        self.game.platforms.append(Platform(0,0,32,329))


        self.game.platforms.append(Platform(34,202,114,14))
        self.game.platforms.append(Platform(197,266,28,17))
        self.game.platforms.append(Platform(114,330,112,17))
        self.game.platforms.append(Platform(0,394,111,18))


        #enemy
        self.game.enemygroup.add(Toaster(467, 440, 110, -2))
        self.game.enemygroup.add(Toaster(436, 310, 22, -2))
        self.game.enemygroup.add(Toaster(385, 246, 106, -3))
        self.game.enemygroup.add(Toaster(463, 180, 150, -2))
        self.game.enemygroup.add(Toaster(431, 118, 254, -2))
        self.game.enemygroup.add(Toaster(362, 118, 170, -3))
        self.game.enemygroup.add(Toaster(255, 118, 60, -2))

        self.game.enemygroup.add(Toaster(364, 517-16, 70, -2))

        self.game.enemygroup.add(Toaster(432, 681-16, 150, -2))
        self.game.enemygroup.add(Toaster(300, 681-16, 150, 2))
        self.game.enemygroup.add(Toaster(173, 681-16, 110, -2))
        self.game.enemygroup.add(Toaster(120, 681-16, 60, 3))

        #self.game.enemygroup.add(Toaster(214, 266-20, 25, -2))
        self.game.enemygroup.add(Toaster(215, 330-20, 100, -3))

       


        #ITEM
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,500,330,10,63,8,"b"))
        self.game.exitgroup.add(RoomExit(self,-35,329,32,64,10,"a"))


    def createroom10(self,entrance):
   

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room10.png")

        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(220*3,100*3)
        if entrance == "b": self.player.startingposition(27*3,100 *3)

        #Set Up Platforms83
        self.game.platforms.append(Platform(0,136,255,78))
        self.game.platforms.append(Platform(0,0,66,70))
        self.game.platforms.append(Platform(224,0,29,70)) 
        self.game.platforms.append(Platform(62,0,166,35))
        

        #enemy
        self.game.enemygroup.add(Toaster(13, 135-20, 190, 15))
        #self.game.enemygroup.add(Goomba(470, 399, -2))
        
        #ITEM
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,0,71,5,66,11,"a"))
        self.game.exitgroup.add(RoomExit(self,260,70,14,70,9,"b"))

    def createroom11(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room11.png")

        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(228*3,100*3)
        elif entrance == "b": self.player.startingposition(50*3,100*3)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,0 ,294,1))
        self.game.platforms.append(Platform(0,134,250,34))
        


        #enemy


        #ITEM
        if not m24:
            self.game.itemgroup.add(Item(122,110,"m24"))

            #convoblock
            #self.game.convoblock.append(Platform(223,118,20,20,3))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,256,130,32,80,10,"b"))
        self.game.exitgroup.add(RoomExit(self,-30,0,5,150,1,"c"))

    def createroom12(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room11.png")

        if not musicplaying=="lavender":
            changemusic('lavender',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(228*3,100*3)
        elif entrance == "b": self.player.startingposition(50*3,100*3)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,0 ,294,1))
        self.game.platforms.append(Platform(0,134,250,34))
        


        #enemy


        #ITEM
        if not m24:
            self.game.itemgroup.add(Item(122,120,"m24"))

            #convoblock
            #self.game.convoblock.append(Platform(223,118,20,20,3))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,256,130,32,80,10,"b"))
        self.game.exitgroup.add(RoomExit(self,-30,0,5,150,1,"c"))

    def createroom13(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room13.png")
        if not musicplaying=="pubg":
            changemusic('pubg',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(45*3,105*3)
        elif entrance == "b": self.player.startingposition(	1113*3,112*3)
        elif entrance == "checkpoint": self.player.startingposition(	350*3,140 *3)

        #Set Up Platforms
        self.game.platforms.append(Platform(1,1 ,72,80))
        self.game.platforms.append(Platform(63,1,226,44))
        
        self.game.platforms.append(Platform(284,1 ,14,68))
        self.game.platforms.append(Platform(556,1 ,14,68))
        self.game.platforms.append(Platform(301,1,853,16))
        
        self.game.platforms.append(Platform(1,146 ,75,59))
        self.game.platforms.append(Platform(72,191,1093,9))
        
        self.game.platforms.append(Platform(1067,145 ,94,45))
        self.game.platforms.append(Platform(1134,7,32,70))


        self.game.platforms.append(Platform(0,74,2,75))

        #convo block
        self.game.convoblock.append(Platform(163,138,43,54,16))
        
        
        #item
        self.game.itemgroup.add(Item(350,142,"checkpoint",13))

        #enemy
        self.game.trapgroup.add(Platform(557,150,35,37))



        #self.game.enemygroup.add(Goomba(249, 178, -2))

        #ITEM
       

            #convoblock
            #self.game.convoblock.append(Platform(223,118,20,20,3))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,1155,82,6,73,14,"a"))
        


    def createroom14(self,entrance):


        if not musicplaying=="pubg":
            changemusic('pubg',True)

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room14.png")
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(46*3,602*3)
        elif entrance == "b": self.player.startingposition(1485*3,100*3)

        #Set Up Platforms
        self.game.platforms.append(Platform(0,646 ,63,42))
        self.game.platforms.append(Platform(56,663,38,30))
        self.game.platforms.append(Platform(70,678 ,1468,25))
        self.game.platforms.append(Platform(0,508,29,70))
        self.game.platforms.append(Platform(126,508,31,70))
        self.game.platforms.append(Platform(26,506 ,103,27))
        self.game.platforms.append(Platform(157,509,1128,9))
        self.game.platforms.append(Platform(1246,389 ,63,220))
        self.game.platforms.append(Platform(1472,550,33,11))
        self.game.platforms.append(Platform(1393,613 ,28,11))
        self.game.platforms.append(Platform(1502,319,34,356))
        
        self.game.platforms.append(Platform(1472,421,33,11))
        self.game.platforms.append(Platform(1393,485 ,28,11))
        self.game.platforms.append(Platform(1246,247,97,74))
        self.game.platforms.append(Platform(1393,357 ,28,11))
        self.game.platforms.append(Platform(1470,248,64,75))
        self.game.platforms.append(Platform(1295,247 ,204,23))
        self.game.platforms.append(Platform(1199,386,158,14))
        self.game.platforms.append(Platform(1168,406 ,34,40))
        self.game.platforms.append(Platform(697,405,213,14))
        self.game.platforms.append(Platform(1,390 ,396,47))
        self.game.platforms.append(Platform(400,421,813,19))
        self.game.platforms.append(Platform(0,0 ,32,400))
        self.game.platforms.append(Platform(25,325,109,16))
        
        self.game.platforms.append(Platform(194,259,129,21))
        self.game.platforms.append(Platform(316,134 ,29,190))
        self.game.platforms.append(Platform(29,196,77,47))
        self.game.platforms.append(Platform(70,198,70,15))
        self.game.platforms.append(Platform(188,130 ,130,16))
        self.game.platforms.append(Platform(228,150,95,31))

        self.game.platforms.append(Platform(352,267,27,24))
        self.game.platforms.append(Platform(447,267,27,24))
        self.game.platforms.append(Platform(542,267,27,24))
        self.game.platforms.append(Platform(640,267,27,24))
        self.game.platforms.append(Platform(734,267,27,24))
        self.game.platforms.append(Platform(833,267,27,24))
        self.game.platforms.append(Platform(925,267,27,24))
        self.game.platforms.append(Platform(1021,267,27,24))
        self.game.platforms.append(Platform(1118,267,27,24))
        self.game.platforms.append(Platform(1215,267,27,24))

        self.game.platforms.append(Platform(352,13,27,24))
        self.game.platforms.append(Platform(447,13,27,24))
        self.game.platforms.append(Platform(542,13,27,24))
        self.game.platforms.append(Platform(640,13,27,24))
        self.game.platforms.append(Platform(734,13,27,24))
        self.game.platforms.append(Platform(833,13,27,24))
        self.game.platforms.append(Platform(925,13,27,24))
        self.game.platforms.append(Platform(1021,13,27,24))
        self.game.platforms.append(Platform(1118,13,27,24))
        self.game.platforms.append(Platform(1215,13,27,24))

        self.game.platforms.append(Platform(343,240,907,21))
        self.game.platforms.append(Platform(322,132,59,44))
        self.game.platforms.append(Platform(378,151,36,38))
        self.game.platforms.append(Platform(410,167,33,26))
        self.game.platforms.append(Platform(445,179,1015,53))
        self.game.platforms.append(Platform(1153,165,33,26))
        self.game.platforms.append(Platform(1182,147,315,37))
        self.game.platforms.append(Platform(1212,131,98,20))
        self.game.platforms.append(Platform(1470,130,64,27))
        self.game.platforms.append(Platform(30,1,1504,16))
        self.game.platforms.append(Platform(317,1,32,65))
        self.game.platforms.append(Platform(1248,1,33,65))

        self.game.platforms.append(Platform(1208,12,31,22))
        self.game.platforms.append(Platform(1473,12,31,22))
        self.game.platforms.append(Platform(1504,6,35,63))
        

        #enemy
        self.game.enemygroup.add(Goomba(548, 386, 2))
        self.game.enemygroup.add(Goomba(467, 386, -3))
        self.game.enemygroup.add(Goomba(361, 111, 0))
        self.game.enemygroup.add(Goomba(1394, 112, 8))
        #self.game.enemygroup.add(Goomba(673, 136, 2))
        self.game.trapgroup.add(Platform(375, 93, 27,37))

        self.game.enemygroup.add(Toaster(1414, 596, 10, -2))
        self.game.enemygroup.add(Toaster(1475, 403, 10, 2))

        self.game.enemygroup.add(boss(1002*3, 660*3, 0, -2,self.game,"thompson"))
        self.game.enemygroup.add(boss(210*3, 90*3, 0, -2,self.game,"thompson"))

        #ITEM

            #convoblock
            #self.game.convoblock.append(Platform(223,118,20,20,3))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,1532,65,5,71,15,"a"))
        self.game.exitgroup.add(RoomExit(self,0,576,1,72,13,"b"))

    def createroom15(self,entrance):

        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room15.png")
        if not musicplaying=="pubg":
            changemusic('pubg',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(23*3,67*3)
        elif entrance == "b": self.player.startingposition(	220*3,320*3)
        elif entrance == "c": self.player.startingposition(	44*3,349*3)
        elif entrance == "d": self.player.startingposition(	220*3,63*3)

        #Set Up Platforms
        self.game.platforms.append(Platform(1,1 ,30,30))
        self.game.platforms.append(Platform(225,1 ,30,30))
        self.game.platforms.append(Platform(1,98,27,175))
        
        self.game.platforms.append(Platform(224,98 ,98,191))
        self.game.platforms.append(Platform(224,354 ,30,70))
        self.game.platforms.append(Platform(1,384,237,54))
        
        self.game.platforms.append(Platform(30,113 ,32,17))
        self.game.platforms.append(Platform(193,113 ,32,17))
        self.game.platforms.append(Platform(30,241 ,32,17))
        self.game.platforms.append(Platform(193,241 ,32,17))
        self.game.platforms.append(Platform(26,0 ,215,2))

        #block
        if not havehappy: self.game.platforms.append(Platform(251,31 ,4,68))
        
        
        
        #item
        #self.game.itemgroup.add(Item(350,142,"checkpoint",13))

        #enemy
        #self.game.trapgroup.add(Platform(557,150,35,37))



        #self.game.enemygroup.add(Goomba(249, 178, -2))

        #ITEM
       

            #convoblock
        if not havehappy : self.game.convoblock.append(Platform(35,95,19,15,7))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,0,31,2,73,14,"b"))
        self.game.exitgroup.add(RoomExit(self,253,289,5,66,16,"a"))
        self.game.exitgroup.add(RoomExit(self,1,273,1,118,17,"a"))
        self.game.exitgroup.add(RoomExit(self,254,32,1,71,18,"a"))

    def createroom16(self, entrance):

    	
       
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room2.png")

        if not musicplaying=="pubg":
            changemusic('pubg',True)



        #Set Up Player
        if entrance == "a": self.player.startingposition(0,366)
        if entrance == "checkpoint": self.player.startingposition(124*3,130*3)
        #Set Up Platforms
        self.game.platforms.append(Platform(0,152,48,72))
        self.game.platforms.append(Platform(48,168,48,56))
        self.game.platforms.append(Platform(96,184,64,40))
        self.game.platforms.append(Platform(160,168,48,56))
        self.game.platforms.append(Platform(208,152,48,72))
        self.game.platforms.append(Platform(224,88,32,64))
        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))
        self.game.platforms.append(Platform(0,0,48,88))

        #convo block
        
     

        #item
        self.game.itemgroup.add(Item(46,109,"checkpoint",16)) # 16 will b use to create room 2

        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,-32,88,32,64,15,"b"))

    
    def createroom17(self,entrance):

        global HALF_WIDTH,HALF_HEIGHT
        HALF_WIDTH = int(WIN_WIDTH / 1.5)
        HALF_HEIGHT = int(WIN_HEIGHT / 1.5)
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room17.png")
        if rolstates=="can atk":
            changemusic('boss',True)
        
        #Set Up Player
        if entrance == "a": self.player.startingposition(1660*3,471*3)
        

        #Set Up Platforms
        self.game.platforms.append(Platform(1660,-30 ,35,460))
        self.game.platforms.append(Platform(1658,505 ,35,194))
        self.game.platforms.append(Platform(1594,522,80,8))
        
        self.game.platforms.append(Platform(1466,522 ,65,8))
        self.game.platforms.append(Platform(1357,522 ,65,8))
        self.game.platforms.append(Platform(1211,521 ,98,11))
        self.game.platforms.append(Platform(1066,520,86,11))
        
        self.game.platforms.append(Platform(1515,1 ,134,153))
        self.game.platforms.append(Platform(1,667 ,1686,32))
        self.game.platforms.append(Platform(190,598 ,37,78))
        self.game.platforms.append(Platform(285,607 ,43,63))
        self.game.platforms.append(Platform(475,607 ,43,63))
        self.game.platforms.append(Platform(572,607 ,43,63))
        self.game.platforms.append(Platform(869,607 ,43,63))
        self.game.platforms.append(Platform(1050,607 ,43,63))
        self.game.platforms.append(Platform(761,623 ,46,47))
        self.game.platforms.append(Platform(1144,637 ,46,25))
        self.game.platforms.append(Platform(955,575 ,46,90))
        self.game.platforms.append(Platform(667,590 ,46,76))

        self.game.platforms.append(Platform(38,551 ,32,17))
        self.game.platforms.append(Platform(0,0 ,39,667))
        self.game.platforms.append(Platform(39,1 ,802,64))
        self.game.platforms.append(Platform(40,110 ,228,36))
        self.game.platforms.append(Platform(185,143 ,46,71))
        self.game.platforms.append(Platform(377,572 ,46,85))
        self.game.platforms.append(Platform(94,648 ,46,18))

        #block
        #if not havehappy: self.game.platforms.append(Platform(251,31 ,4,68))
        
        
        
        #item
        self.game.itemgroup.add(Item(60,620,"happy"))

        #enemy
        self.game.enemygroup.add(boss(95*3, 580*3, 200, -2,self.game,"rol"))



        #self.game.enemygroup.add(Goomba(249, 178, -2))

        #ITEM
       

            #convoblock
        if rolstates=="cant atk": self.game.convoblock.append(Platform(235,251,29,397,8))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,1695,425,18,88,15,"c"))    	

    def createroom18(self, entrance):


        
       
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room18.png")

        if cockroachstates=="can atk":
            changemusic('boss',True)

        #Set Up Player
        if entrance == "a": self.player.startingposition(26*3,100*3)
        
        #Set Up Platforms
        self.game.platforms.append(Platform(50,0,712,39))
        self.game.platforms.append(Platform(0,0,29,70))
        self.game.platforms.append(Platform(31,0,38,52))
        self.game.platforms.append(Platform(0,131,29,63))
        self.game.platforms.append(Platform(29,152,33,41))
        self.game.platforms.append(Platform(60,168,700,49))
        self.game.platforms.append(Platform(705,154,60,25))
        self.game.platforms.append(Platform(736,138,30,20))
        self.game.platforms.append(Platform(702,0,57,51))
        self.game.platforms.append(Platform(735,52,35,19))
        self.game.platforms.append(Platform(762,68,1,72))
        self.game.platforms.append(Platform(29,136,33,16))
        self.game.platforms.append(Platform(701,136,37,17))

        #convo block
        
        if cockroachstates=="cant atk": self.game.convoblock.append(Platform(25,98,58,79,9))

        #boss
        self.game.enemygroup.add(Goomba(632, 110,0 ,"cockroach"))
        #Set Up Exits
        self.game.exitgroup.add(RoomExit(self,0,62,1,78,15,"d"))    
        self.game.exitgroup.add(RoomExit(self,755,68,1,72,19,"a"))    
    def createroom19(self, entrance):


        
       
        #Set Up Background
        self.setbackground("Media/Graphics/Backgrounds/room19.png")

        if not musicplaying=="end":
            changemusic('end',True)

        #Set Up Player
        if entrance == "a": self.player.startingposition(41*3,157*3)
        
        #Set Up Platforms
        self.game.platforms.append(Platform(0,194,58,82))
        self.game.platforms.append(Platform(56,210,34,24))
        self.game.platforms.append(Platform(79,228,3755,40))
        self.game.platforms.append(Platform(1,57,3837,35))
        self.game.platforms.append(Platform(0,116,23,12))
        self.game.platforms.append(Platform(219,130,32,10))
        self.game.platforms.append(Platform(442,130,32,10))
        self.game.platforms.append(Platform(664,130,32,10))
        self.game.platforms.append(Platform(892,130,32,10))
        self.game.platforms.append(Platform(1113,130,32,10))
        self.game.platforms.append(Platform(1561,130,32,10))
        self.game.platforms.append(Platform(1785,130,32,10))
        self.game.platforms.append(Platform(2010,130,32,10))
        self.game.platforms.append(Platform(2236,130,32,10))
        self.game.platforms.append(Platform(2458,130,32,10))
        self.game.platforms.append(Platform(2680,130,32,10))
        self.game.platforms.append(Platform(2906,130,32,10))
        self.game.platforms.append(Platform(3130,130,32,10))
        self.game.platforms.append(Platform(3353,130,32,10))
        self.game.platforms.append(Platform(3575,130,32,10))
        self.game.platforms.append(Platform(3803,130,32,10))


        self.game.platforms.append(Platform(208,0,48,88))
        self.game.platforms.append(Platform(160,0,48,72))
        self.game.platforms.append(Platform(96,0,64,56))
        self.game.platforms.append(Platform(48,0,48,72))

        self.game.platforms.append(Platform(3739,210,94,40))

        self.game.platforms.append(Platform(3772,194,60,19))
        self.game.platforms.append(Platform(0,112,2,96))
        self.game.platforms.append(Platform(3830,124,2,96))

        #msg group
        self.game.msggroup.append(Platform(267,86,58,147,1))
        self.game.msggroup.append(Platform(1448,86,58,147,2))
        self.game.msggroup.append(Platform(1912,86,58,147,3))
        self.game.msggroup.append(Platform(2479,86,58,147,4))
        self.game.msggroup.append(Platform(3500,86,58,147,5))
        

        #convo block
        self.game.convoblock.append(Platform(197,111,51,126,15))
     

        #item
        self.game.itemgroup.add(Item(3795,168,"bd")) # 16 will b use to create room 2

        #Set Up Exits
        #self.game.exitgroup.add(RoomExit(self,-32,88,32,64,15,"b"))


class RoomExit(Entity):
    def __init__(self, room, x, y, w, h, roomid, entrance):
        Entity.__init__(self)
        self.image = Surface((w*3, h*3))
        self.image.fill(Color("Blue"))
        self.rect = Rect(x*3, y*3, w*3, h*3)
        self.room = room
        self.roomid = roomid
        self.entrance = entrance
    def changeroom(self):
        global HALF_WIDTH,HALF_HEIGHT
        HALF_WIDTH = int(WIN_WIDTH / 4)
        HALF_HEIGHT = int(WIN_HEIGHT / 4)

        self.room.game.convoblock.clear()
        self.room.game.projectilegroup.empty()

        if self.roomid == 1: self.room.createroom1(self.entrance)
        if self.roomid == 2: self.room.createroom2(self.entrance)
        if self.roomid == 3: self.room.createroom3(self.entrance)
        if self.roomid == 4: self.room.createroom4(self.entrance)
        if self.roomid == 5: self.room.createroom5(self.entrance)
        if self.roomid == 6: self.room.createroom6(self.entrance)
        if self.roomid == 7: self.room.createroom7(self.entrance)
        if self.roomid == 8: self.room.createroom8(self.entrance)
        if self.roomid == 9: self.room.createroom9(self.entrance)
        if self.roomid == 10: self.room.createroom10(self.entrance)
        if self.roomid == 11: self.room.createroom11(self.entrance)
        if self.roomid == 12: self.room.createroom12(self.entrance)
        if self.roomid == 13: self.room.createroom13(self.entrance)
        if self.roomid == 14: self.room.createroom14(self.entrance)
        if self.roomid == 15: self.room.createroom15(self.entrance)
        if self.roomid == 16: self.room.createroom16(self.entrance)
        if self.roomid == 17: self.room.createroom17(self.entrance)
        if self.roomid == 18: self.room.createroom18(self.entrance)
        if self.roomid == 19: self.room.createroom19(self.entrance)
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Goomba(Entity):
    def __init__(self, x, y, xvel,type=0):
        Entity.__init__(self)
        #health
        x-x*3
        y=y*3

        self.type=type

        if self.type=="ghost":
            self.currentlifetotal=1
        elif self.type=="cockroach":
            self.currentlifetotal=110
            self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll","llllllllll","lllllllllll","llllllllllll","lllllllllllll","llllllllllllll","lllllllllllllll","llllllllllllllll","lllllllllllllllll","llllllllllllllllll","lllllllllllllllllll","llllllllllllllllllll","lllllllllllllllllllll","llllllllllllllllllllll"]    
        else:
            self.currentlifetotal=3
        #Set Velocities
        self.xvel = xvel
        self.yvel = 0
        #States
        self.onGround = False
        self.airborne = True
        self.destroyed = False
        #Offsets
        self.xoffset = -130
        self.yoffset = -30
        #Counter
        self.counter = 0
        #Create Sprite Image
        self.image = Surface((300, 450), pygame.SRCALPHA)
        if self.type=="ghost":
            self.image=ghostleft
        elif self.type=="cockroach":
            self.image=cockroachleft
        else:
            self.image = goombaleft
        self.rect = Rect(x, y, 300, 450)
        #Create Detectable
        self.detectable = pygame.sprite.Sprite()
        if self.type=="cockroach":
            self.detectable.rect = Rect(x, y, 50*4,30*4)
            self.detectable.image = Surface((50*4,30*4))
        else:
            self.detectable.rect = Rect(x, y, 64,64)
            self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):

        if  self.type=="cockroach":
            font=pygame.font.Font(None, 70)
            text=font.render(self.lifetotal[(int(self.currentlifetotal/5))],1,(255,255,0))
            screen.blit(text,(500,0))
        #Move
        if self.yvel < 0: self.airborne = True
        if self.onGround == True: self.airborne = False
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 1.2: self.airborne = True
            if self.yvel > 100: self.yvel = 100

        if cockroachstates=="can atk" and self.xvel==0:
        	self.xvel=-15

        
        

        
        #Collisions
        self.detectable.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, projectilegroup)
        self.detectable.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel, platforms, projectilegroup)

        #Apply Offsets
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Platforms
        global inconvo,cockroachstates,convoid
        for p in platforms:

            
            if pygame.sprite.collide_rect(self.detectable, p):
                
                  
                if xvel > 0:
                    self.detectable.rect.right = p.rect.left
                    self.xvel = self.xvel * -1
                    if self.type=="ghost":
                        self.kill()
                    elif self.type=="cockroach":
                        self.xvel=random.randint(15,33)* -1
                if xvel < 0:
        
                    self.detectable.rect.left = p.rect.right
                    self.xvel = self.xvel * -1
                    if self.type=="ghost":
                        self.kill()
                    elif self.type=="cockroach":
                        self.xvel=random.randint(15,33)
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j) and not self.destroyed and self.type=="cockroach":
                changemusic('hit',False)
                projectilegroup.remove(j)
                self.currentlifetotal-=j.damage
                if self.currentlifetotal<=0:
                    self.xvel = 0
                    self.destroyed = True
                    cockroachstates="defeat"
                    inconvo=True
                    convoid=10
            elif pygame.sprite.collide_rect(self.detectable, j) and not self.destroyed:
                changemusic('hit',False)
                projectilegroup.remove(j)
                self.currentlifetotal-=j.damage
                if self.currentlifetotal<=0:
                    self.xvel = 0
                    self.destroyed = True

    #Animate
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            if self.type=="ghost":
                self.walkloop(ghostwalk)
            if self.type=="cockroach":
                self.walkloop(cockroachwalk)
            else:
                self.walkloop(goombawalk)

    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10: 
            if self.xvel<0 :
            	self.updatecharacter(loop[0])
            else:self.updatecharacter(pygame.transform.flip(loop[0], True, False))

        elif self.counter == 20:
            if self.xvel<0:self.updatecharacter(loop[1])
            else:self.updatecharacter(pygame.transform.flip(loop[1], True, False))
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0: self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 1
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf
        
class Toaster(Entity):
    def __init__(self, x, y, track, xvel,type=0):
        Entity.__init__(self)
        #Set Velocities
        x=x*3
        y=y*3
        track=track*3

        self.type=0
        self.xvel = xvel
        self.yvel = 0
        #States
        self.destroyed = False
        self.faceright = False
        self.onGround = False
        self.airborne = True
        #Offests
        self.xoffset = -130
        self.yoffset = 0
        #Counter
        self.counter = 0
        #Configure Track
        if xvel > 0:
            self.min = x
            self.max = x + track
        elif xvel < 0:
            self.max = x
            self.min = x - track
        #Create Sprite Image
        self.image = Surface((300, 650), pygame.SRCALPHA)
        self.image = toasterwalk1
        self.rect = Rect(x, y, 300, 650)
        #Create Dectectable
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x, y, 64,150)
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):
        #Move
        if self.xvel > 0: self.faceright = True
        if self.xvel < 0: self.faceright = False
        self.detectable.rect.left += self.xvel
        if self.detectable.rect.left == self.max: self.xvel = -abs(self.xvel)
        if self.detectable.rect.left == self.min: self.xvel = abs(self.xvel)
        self.detectable.rect.top += self.yvel

        #Collisions
        self.collide(0, self.yvel, platforms, projectilegroup)
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j) and not self.destroyed:
                changemusic('hit',False)
                projectilegroup.remove(j)
                self.destroyed = True
                self.counter = 0
                self.xvel = 0

    #Animate          
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            self.walkloop(toasterwalkloop)
    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10:
            self.updatecharacter(loop[0])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[0], True, False))
        elif self.counter == 20:
            self.updatecharacter(loop[1])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[1], True, False))
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0:
            self.yoffset = -30
            self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 20
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf

class boss(Entity):
    def __init__(self, x, y, track, xvel,game,type="vss"):
        Entity.__init__(self)
        
        self.type=type
        if self.type=="vss":
            self.currentlifetotal=9
        elif self.type=="rol":
            self.currentlifetotal=90
        elif self.type=="thompson":
            self.currentlifetotal=1
        else:
            self.currentlifetotal=9
        #Set Velocities
        self.game=game
        self.pcounter=0
        self.xvel = xvel
        self.yvel = -2
        self.move=-0.3
        #States
        self.destroyed = False
        self.faceright = False
        self.onGround = False
        self.airborne = True
        #Offests
        self.xoffset = -130
        self.yoffset = 0

        
        if self.type=="vss":
            self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll"]
        if self.type=="rol":
            self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll","llllllllll","lllllllllll","llllllllllll","lllllllllllll","llllllllllllll","lllllllllllllll","llllllllllllllll","lllllllllllllllll","llllllllllllllllll"]     
        #Counter
        self.counter = 0
        #Configure Track
        if xvel > 0:
            self.min = x
            self.max = x + track
        elif xvel < 0:
            self.max = x
            self.min = x - track
        #Create Sprite Image
        if self.type=="thompson":
            self.image = Surface((300, 450), pygame.SRCALPHA)
            self.image = thompson
            self.rect = Rect(x, y, 43*3,17*3)
            

        elif self.type=="rol":
            self.image = Surface((300, 450), pygame.SRCALPHA)
            self.image = rol
            self.rect = Rect(x, y, (39)*3,40*3)
            print("yo boy")
        elif self.type=="vss":
            self.image = Surface((300, 450), pygame.SRCALPHA)
            self.image = vss
            self.rect = Rect(x, y, 87*3,37*3)

        #Create Dectectable
        self.detectable = pygame.sprite.Sprite()
        
        if self.type=="thompson":
            self.detectable.rect = Rect(x, y, 43*3,17*3)
            self.detectable.image = Surface((32,32))
        
        elif self.type=="rol":
            self.detectable.rect = Rect(x, y, 39*3,40*3)
            self.detectable.image = Surface((64,64))
        else:

            self.detectable.rect = Rect(x, y, 87*3,37*3)
            self.detectable.image = Surface((64,64))

            
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):
        if not inconvo and not vssstates=="defeat" and self.type=="vss":
            font=pygame.font.Font(None, 150)
            text=font.render(self.lifetotal[self.currentlifetotal],1,(210,105,30))
            screen.blit(text,(500,0))
            
        if  self.type=="rol":
            font=pygame.font.Font(None, 70)
            text=font.render(self.lifetotal[(int(self.currentlifetotal/5))],1,(0,250,0))
            screen.blit(text,(500,0))
        #Move
       
        self.pcounter=self.pcounter+1
        '''if self.xvel > 0: self.faceright = False #not making boss turn arounnd unlike toaster
        if self.xvel < 0: self.faceright = False
        self.detectable.rect.left += self.xvel
        if self.detectable.rect.left == self.max: self.xvel = -abs(self.xvel)
        if self.detectable.rect.left == self.min: self.xvel = abs(self.xvel)'''
        if not vssstates =="cant atk" and self.type=="vss":
            self.yvel+=self.move
            self.detectable.rect.top += self.yvel
        
        #Collisions
        self.collide(0, self.yvel, platforms, projectilegroup)
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #shoot projectiles
        
        if self.pcounter==random.randint(1,2)or self.pcounter==random.randint(40,41):
            if not vssstates=="cant atk" and self.type=="vss":
                projectile = Projectile(self,self.game,"vss")
                self.game.projectilegroup.add(projectile)
                changemusic('vss',False)
            elif self.type=="thompson":
                projectile = Projectile(self,self.game,"thompson")
                self.game.projectilegroup.add(projectile)
            elif self.type=="rol" and not rolstates=="cant atk":
                projectile = Projectile(self,self.game,"rol")

                self.game.projectilegroup.add(projectile)
                
                	
        elif self.pcounter==80:
            if  not rolstates=="cant atk":
            	projectile = Projectile(self,self.game,"rol2")
                
            	self.game.projectilegroup.add(projectile)
            self.pcounter=0


        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Projectiles
        global vssstates,convoid,inconvo,rolstates
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j) and not self.destroyed and not (j.type=="rol" or j.type=="rol2"):
                projectilegroup.remove(j)
                if self.type=="vss":
                    if j.type=="m24":
                        changemusic('hit',False)
                        self.currentlifetotal-=j.damage
                        self.counter = 0
                        if self.currentlifetotal<=0:
                            self.destroyed = True
                            self.yvel=0
                            self.onGround=True
                            self.airborne=False
                            vssstates="defeat"
                            convoid=5
                            inconvo=True
                            self.game.projectilegroup.empty()
                elif self.type=="rol":
                    changemusic('hit',False)
                    if j.type=="m24":
                        self.currentlifetotal-=j.damage+2
                        self.counter = 0
                        if self.currentlifetotal<=0:
                            self.destroyed = True
                            rolstates="defeat"
                         
                            self.game.projectilegroup.empty()
                    else:
                        changemusic('hit',False)
                        self.currentlifetotal-=j.damage
                        self.counter = 0
                        if self.currentlifetotal<=0:
                            self.game.projectilegroup.empty()
                            self.destroyed = True
                            rolstates="defeat"
                            

                else:
                    self.currentlifetotal-=j.damage
                    self.counter = 0
                    if self.currentlifetotal<=0:
                        self.destroyed = True
                self.xvel = 0 
        #with platform
        for p in platforms:
            if pygame.sprite.collide_rect(self.detectable, p) and not  self.type=="rol":
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.move = -0.3
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom
                    self.move = 0.3

    #Animate          
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
        	if self.type=="thompson":
        		self.walkloop(thompson)
        	elif self.type=="rol":
        		self.walkloop(rol)
        	else:
        		self.walkloop(vss)
    #Walk Loop Animation
    def walkloop(self,loop):
        if self.counter == 10:
            self.updatecharacter(loop)
            #if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop, True, False))
        elif self.counter == 20:
            self.updatecharacter(loop)
            #if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop, True, False))
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0:
            self.yoffset = -30
            self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 5
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf

class Item(Entity):
    def __init__(self, x, y,type,id=0):
        Entity.__init__(self)
        self.id=id #this id willl b used to match with checkpoint and use as roomid
        self.notimage=False # to remove image once aquired
        self.type=type

        # images and variables acording to diffrent items
        if self.type=="zuzu":
            self.image =pygame.image.load("Media/Graphics/Backgrounds/dog.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(25*3,25*3))

            
        elif self.type=="checkpoint":
            self.image=itemframe1        

        elif self.type=="m24":
            self.image =pygame.image.load("Media/Graphics/Backgrounds/m24.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40*3,30*3))

        elif self.type=="happy":
            self.image =pygame.image.load("Media/Graphics/Backgrounds/cat.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(25*3,25*3))
        elif self.type=="bd":
            self.image =pygame.image.load("Media/Graphics/Backgrounds/bd.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(25*3,25*3))


        self.rect = Rect(x*3,y*3,78*3,59*3)
        self.counter = 0
        self.detectable = pygame.sprite.Sprite()
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x*3, y*3, 64,64)

        if type=="checkpoint":
            self.detectable.rect.x = self.detectable.rect.x + 190
            self.detectable.rect.y = self.detectable.rect.y + 60
        else:
            self.detectable.rect.x = self.detectable.rect.x + 0
            self.detectable.rect.y = self.detectable.rect.y + 0
    def noimage(self):
        self.notimage=True
           
    def update(self):
        if not self.notimage:
            if self.type=="checkpoint":
                if self.counter == 0: self.image = itemloop[0]
                if self.counter == 10: self.image = itemloop[1]
                if self.counter == 20:
                    self.image = itemloop[2]
                    self.counter = 0
                self.counter = self.counter + 1
        else:
            self.image=pygame.image.load("Media/Graphics/Backgrounds/transparent.png").convert_alpha()

class PauseMenu(object):
    def __init__(self,game):
        self.game = game
    def createpausemenu(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Paused", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 290
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.game.screenfocus = "Game"

    def update(self):
        self.inputhandler()

class LevelComplete(object):
    def __init__(self,game):
        self.game = game
    def createlevelcomplete(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Level Complete", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 200
        ss.rect.y = 400
        self.game.menugroup.add(ss)
        
class GameOver(object):
    def __init__(self,game):
        self.game = game
    def creategameover(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Game Over", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 240
        ss.rect.y = 400
        self.game.menugroup.add(ss)

    
class Title(object):
    def __init__(self,game):
        self.game = game
        self.counter = 0
        self.createtitle()
    def createtitle(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit("ESCAPE")
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()
        #Animate Title Screen

        if not musicplaying =='title':changemusic('title',True)

        if self.counter == 100:
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Starring cia", 1, (255, 255, 255))
            ss.rect = Rect(280,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = standleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 300:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("press space", 1, (255, 255, 255))
            ss.rect = Rect(260,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = goombaleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        
        self.counter = self.counter + 1

def conversation(idd):
    global press,vssstates,inconvo,rolstates,cockroachstates

    inconvo=True
    



    if idd==1:

            
            
            if press==1:
                text("press space to shoot") 
            elif press==2:
                text("Arrow keys to move")
                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
            
            
                
    elif idd==2:

            
            
            if press==1:
                text("[This is check point]")
                
            elif press==2:
                text("ur health will also be restored here")
                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_SPACE:
                    press+=1
            
            
    elif idd==3:

            if press==1:
                text("I have Been waiting for u Cia")
                
            elif press==2:
                text("i am the spirit of zuzu. ")
                
                
                
            elif press==3:
                text("someone put a spell on u when u were sleeping and now u",)
                text("are trapped in this world",1)
            elif press==4:
                text("to get out of here u need a SPECIAL ITEM.")
                text("take me and ill help u get out of here.",2)
            elif press>=5:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_SPACE:
                    press+=1
                    return 0                
    elif idd==4:

            if press==1:
                text("VSS: MUHAHAHAHAHAHA")
                
                
            elif press==2:
                text("VSS: we finally meet cia.")
                text("to move forward u must defeat me first.",1)
                text("BUT I WILL NEVER LET YOU PASS",2)
                                
            elif press==3:
                text("VSS: I WILL TAKE REVENGE OF EVERY TIME U IGNORED ME")
            elif press==4:
                text("zuzu: this is bad, i know this boss, ur normal atks wont work")
                text(" on him. u need special atk to damage this boss cia",1)
            elif press==5:
                text("VSS: YOU WILL NEVER GET PASS ME!!!!!!!")
            elif press>=6:
                vssstates="can atk"
                changemusic('boss',True)
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_SPACE:
                    press+=1
                    return 0        

    elif idd==5:

            
            
            if press==1:
                text("VSS: UGH..........") 
            elif press==2:
                text("VSS: all i ever wanted ....")
                
            elif press==3:
                text("was to be picked by u once.............")
            elif press==4:
                text("just...once.............")
                
            elif press==5:
                text("zuzu: u did it! lets move ahead")
            elif press>=6:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break

    elif idd==6:

            
            
            if press==1:
                text("zuzu: u cant kill that boss with regular atks.") 
                text("u need special atk",1)
            elif press==2:
                text("zuzu. i used last of my power to teleport u out of there")
                
            elif press==3:
                text("u need to find a way to kill that boss ")
                
            elif press>=4:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
    

    elif idd==7:

            
            
            if press==1:
                text("zuzu: ur almost at the end cia") 
                
            elif press==2:
                text("zuzu: at top left is the final boss who put a curse on u")
                text("but to enter that room u need SPIRIT OF HAPPY",1)
                
            elif press==3:
                text("at bottom right is checkpoint which u should go first because")
                text("at bottom left is the boss guarding SPIRIT OF HAPPY.",1)
                text("which mi8 b dificult",2)
                pygame.time.delay(600)
                
            elif press>=4:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
                
    elif idd==8:

            
            
            if press==1:
                text("Roley: CIA!!!") 
                
            elif press==2:
                text("Roley: u attention seeker b*tch ill ILL KILL U RIGHT HERE")

                
            elif press>=3:
                rolstates="can atk"
                changemusic('boss',True)
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break


    elif idd==9:

            
            
            if press==1:
                text("cockroach: So  u made it till here huh") 
                
            elif press==2:
                text("zuzu: ur the one who trapped cia here?")
                    
            elif press==3:
                text("cockroach: Yes i did")
                 
            elif press==4:
                text("cockroach : i got lost once and got into her room.")
                text("when she found out she tried to find and remove me",1)    
                text("i had to kill her so i can take over that place",2)    
                text("so i put a curse on her and trapped her mind here",3) 

            elif press==5:
                text("cockroach: do u wanna know how i put a curse on u cia?")   
            elif press==6:
                text("cockroach: when u were sleeping at night i climbed on ur bed")   
            elif press==7:
                text("cockroach: and i crawled ur arm and work my way to ur face")   
            elif press==8:
                text("cockroach: and than i got to ur ear and entered ur ear")   

            elif press==9:
                text("cockroach: MUHAHAHAHAHAHA!!!!")
            elif press==10:
                text("cockroach: than i put curse on ur brain")

            elif press==11:
                text("cockroach: to get out u need to kill me first here")

            elif press==12:
                text("cockroach: goodluck because that will NEVER HAPPEN")
            elif press==13:
                text("cockroach: ONCE I KILL U HERE ILL BRING MY BOYS IN UR")
                text(" HOUSE AND WE WILL EAT UR FLESH FOR YEARS ",1)
                text(" MUHAHAHAHAHAHAAHAHAAH!!!!!",2)
      
                

                
            elif press>=14:
                cockroachstates="can atk"
                changemusic('boss',True)
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break

    elif idd==10:

            
            
            if press==1:
                text("zuzu: U DID IT U CAN GO HOME NOW") 
                
            elif press==2:
                text("next room has that special item which once u take it will")
                text("be end of this journey",1)
                text("farewell cia and feed me later ok?!",2)

                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break

    elif idd==11:

            
            
            if press==1:
            	text("Bilal:HAPPY BIRTHDAY!!!!!",0,"blue")
                        
                
            elif press==2:
                text("well game will end now thnx for playinn. bye",1,"blue") 

                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break

    elif idd==12:

            
            
            if press==1:
            	text("u got spirit of happy",0,"blue")
                        
                
            elif press==2:
                text("u can now do long jump by press b button") 
            elif press==3:
                text("it has some cooldown, when cooldown is up itll show on")
            elif press==4:
                text("top left of screen")

                
            elif press>=5:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break

    elif idd==13:

            
            
            if press==1:
            	text("u got spirit of m24",0,"blue")
                        
                
            elif press==2:
                text("u can do m24 atk by pressing m button but has cooldown") 
            elif press==3:
                text("when cooldown is up itll show on top left of screen")

            elif press==4:
                text("m24 bullet has 5 times more dmg than normal bullet")    
            elif press==4:
                text(" and is the only bullet than can hurt Vss")

                
            elif press>=5:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
                
                    

    elif idd==14:

            
            
            if press==1:
            	text("zuzu : Remember vss can only be damages by m24 projectile")
                        
                
            elif press==2:
                text("u can use m24 projectile by pressing m") 
            

                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
    elif idd==15:

            
            
            if press==1:
            	text("Bilal: well cia this is it thnx for playing")
                        
                
            elif press==2:
                text("i wish i could make game longer but that all the time i had")     
            elif press==3:
                text("i never made a game so this was my first game and it was") 
                text("one of most challenging things to do for me since i had",1 )
                text("no idea how to start",2 )     
            elif press==4:
                text("u did gave me a gift 3 years ago which was drawing of me")
                text("back than i didnt had much to make as gift. i cant draw but",1)
                text("now i can do this atleast",2)


            elif press==5:
                text("and since ur here means i kinda was successful in this gift")     
            elif press==6:
                text("really hoping u didnt had much issue while playing")     
            elif press==7:
                text("and sorry cause i did added stuff that u dont like and")     
                text("i hope i didnt over do it",1)     
            elif press==8:
                text("well this is it walk the final path of game ") 
            

                
            elif press>=9:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
                
                    
    
    elif idd==16:

            
            
            if press==1:
            	text("zuzu : did u know u can dance by holding d button?")
                        
                
            elif press==2:
                text("try it hold d button") 
            

                
            elif press>=3:
                return 1
            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and (e.key == K_SPACE or e.key==K_RETURN):
                    press+=1
                    break
                    

                
        
    

def text(msg,y=0,color=0,size=30):

    

    font=pygame.font.SysFont('comicsans',size)
    if color=="red":
        text=font.render(msg,1,(255,0,0))
    else:
        text=font.render(msg,1,(255,255,255))
    screen.blit(text,(36,38+(y*20)))
    pygame.display.update()


def changemusic(name,music):#if music true if sound than false
	global musicplaying
	if music:
		m=pygame.mixer.music.load('Media/Music/'+name+'.mp3')
		pygame.mixer.music.set_volume(0.3 )
		pygame.mixer.music.play(-1)
		musicplaying=name
	else:
		sound=pygame.mixer.Sound('Media/Music/'+name+'.ogg') 

		sound.play()	


class Display(Entity):
    def __init__(self, string):
        Entity.__init__(self)
        self.font = pygame.font.Font(None, 80)
        self.image = self.font.render(string, 1, (255, 0, 0))
    def update(self, string):
        self.image = self.font.render(string, 1, (255, 0, 0))

if __name__ == "__main__":
    main()
