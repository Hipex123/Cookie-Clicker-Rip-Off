import pygame, os, sys
pygame.init()

currendDir = os.path.dirname(sys.executable)
imagesFolder = os.path.abspath(os.path.join(currendDir, "..", "Images"))
soundsFolder = os.path.abspath(os.path.join(currendDir, "..", "Sounds"))

def setImage(fileName, width, height):
    imagePath = os.path.join(imagesFolder, fileName)
    Image = pygame.image.load(imagePath)
    Image = pygame.transform.scale(Image, (width,height))
    return Image

def setEffect(fileName, volume):
    soundPath = os.path.join(soundsFolder, fileName)
    fx = pygame.mixer.Sound(soundPath)
    pygame.mixer.Sound.set_volume(fx,volume)
    return fx

def draw(w,h,alpha,r,g,b):
    s = pygame.Surface((w,h))
    s.set_alpha(alpha)                
    s.fill((r,g,b))           
    return s

def replaceLine(lineNum, content):
    with open("DataUpdate.txt") as file:
        lines = file.readlines()
    
    lines[lineNum-1] = content + "\n"

    with open("DataUpdate.txt", "w") as file:
        for line in lines:
            file.write(line)