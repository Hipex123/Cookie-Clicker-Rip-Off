import pygame, random, os
from cookieDef import *
pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)

inFile = open("DataUpdate.txt", "w")
outFile = open("DataUpdate.txt", "r")

readFile = outFile.read().splitlines()


empty = True
running = True

width = 1200
height = 900

clock = pygame.time.Clock()

cookies = 0
Cps = 0
cookiesClicks = 1

bigCookieW = 300
bigCookieH = 300

currentTime = pygame.time.get_ticks()
gameSecond = 1000
nextTime = random.randint(500,5000)
destroyTime = 5000

smallCookies = []
cookieVelocety = 0.5

clickText = []
clickTextAlpha = 255

#MUSIC
musicPath = os.path.join(soundsFolder, "CookieClicker.mp3")
BGmusic = pygame.mixer.music.load(musicPath)

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#SOUND EFFECTS
cookieClickTwo = setEffect("clickb4.mp3", 0.1)
cookieClickThree = setEffect("clickb1.mp3", 0.1)

buyBuilding = setEffect("clickb1.mp3", 0.7)


screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
iconPath = os.path.join(imagesFolder, "cookie.png")
pygame.display.set_icon(pygame.image.load(iconPath))

fonts = [pygame.font.SysFont(None, 50), pygame.font.SysFont(None, 35), pygame.font.SysFont(None, 45),pygame.font.SysFont("inkfree", 16),
          pygame.font.SysFont(None, 33), pygame.font.SysFont(None, 22)]

#TEXTURE PATHS
texturePath1 = os.path.join(imagesFolder, "green-grunge.png")
texturePath2 = os.path.join(imagesFolder, "goldTexture.png")
texturePath3 = os.path.join(imagesFolder, "_rubyTexture.png")