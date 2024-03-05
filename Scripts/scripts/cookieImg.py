import pygame
pygame.init()
from cookieDef import *
from dataCookie import *

background = setImage("cookieBG.png", 1950,1010)
bigCookie = setImage("cookie.png", bigCookieW,bigCookieH)
priceCookie = setImage("cookie.png", 20,20)
cookie = setImage("cookie.png", 50,50)
plank = setImage("woodenPlank.png", 180,1200)
milk = setImage("milk.png", 1074,700)
gold = setImage("gold.png", 320,170)
#buildings
what = setImage("what.png", 340,210)
twentyOne = setImage("_twentyOne.png", 340,210)
skull = setImage("skull.png", 340,210)
nabru = setImage("_nabru.png", 340, 210)
man = setImage("man.png", 340, 210)
dad = setImage("dad.png", 340, 210)
everyone = setImage("everyone.png", 340, 210)
dontHurt = setImage("dontHurt.png", 340, 210)
sigma = setImage("sigma.png", 340, 210)
steve = setImage("steve.png", 340, 210)

#achivements/upgrades
frame = setImage("_achievFrame.png", 360, 170)
frame2 = setImage("_achievFrame.png", 100, 101)
#_cookie
achi_01 = setImage("Cookie_achiev_01.png", 140, 100)
achi_02 = setImage("Cookie_achiev_02.png", 140, 100)
achi_03 = setImage("Cookie_achiev_03.png", 140, 100)
achi_04 = setImage("Cookie_achiev_04.png", 140, 100)
achi_05 = setImage("Cookie_achiev_05.png", 100, 70)
achi_06 = setImage("Cookie_achiev_06.png", 100, 70)
achi_07 = setImage("Cookie_achiev_07.png", 100, 70)
achi_08 = setImage("Cookie_achiev_08.png", 100, 70)
achi_09 = setImage("Cookie_achiev_09.png", 100, 70)
achi_10 = setImage("Cookie_achiev_10.png", 100, 70)
achi_11 = setImage("Cookie_achiev_11.png", 100, 70)
achi_12 = setImage("Cookie_achiev_12.png", 100, 70)

# OTHER
rPlank = setImage("woodenPlank.png", 180,336)
rPlank = pygame.transform.rotate(rPlank, 90)

rPlankT = setImage("woodenPlank.png", 180,1139)
rPlankT = pygame.transform.rotate(rPlankT, 90)


#TEXTURES
#deafult
textureImage = pygame.image.load(texturePath1)

textureSurface = pygame.Surface(textureImage.get_size())
textureSurface.blit(textureImage, (0,0))
#gold
textureImageGold = pygame.image.load(texturePath2)

textureGold = pygame.Surface(textureImageGold.get_size())
textureGold.blit(textureImageGold, (0,0))

#ruby
textureImageRuby = pygame.image.load(texturePath3)

textureRuby = pygame.Surface(textureImageRuby.get_size())
textureRuby.blit(textureImageRuby, (0,0))