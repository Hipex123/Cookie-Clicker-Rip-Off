import pygame, random, sys, os
from dataCookie import *
from cookieImg import *
from cookieDef import *
from cookieRects import *
from cookieObjects import *

try:
    pygame.init()
    pygame.mixer.pre_init(44100,16,2,4096)

except pygame.error as error:
    print("An error occurred while initializing pygame:", error)
except Exception as error:
    print("An unexpected error occurred:", error)


#COLLECTIONS

rects = [whatRect, twentyOneRect, skullRect, nabruRect, manRect, dadRect, everyoneRect, dontHurtRect, sigmaRect, steveRect]

achievments = [achiOne, achiTwo, achiThree, achiFour, achiFive, achiSix, achiSeven, achiEight, achiTen, achiEleven, achiTwelve,]

achievmentBuildings = [achiBOne, achiBTwo, achiBThree, achiBFour, achiBFive, achiBSeven, achiBEight, achiBNine, achiBTen,
                       achiBEleven, achiBTwelve, achiBThirteen, achiBFourteen, achiBFiveteen, achiBSeventeen, achiBEighteen,
                        achiBNineteen, achiBTwenty]


upgrades = [whatUp, twentyOneUp, skullUp, nabruUp, manUp, dadUp, EveryOneUp, dontHurtUp, sigmaUp, steveUp]

infoSetUps = [["whatIcon.png", 160, 170, 170, 190, 1340],
                 ["_twentyOneIcon.png", 230, 240, 230, 250, 1340],
                 ["skullIcon.png", 320, 330, 310, 340, 1340],
                 ["_nabruIcon.png", 410, 420, 420, 430, 1330],
                 ["manIcon.png", 490, 500, 490, 510, 1330],
                 ["_twentyOneIcon.png", 570, 580, 580, 590, 1330],
                 ["everyoneIcon.png", 650, 660, 660, 670, 1330],
                 ["dontHurtIcon.png", 730, 740, 740, 750, 1330],
                 ["sigmaIcon.png", 810, 820, 820, 830, 1330],
                 ["steveIcon.png", 840, 850, 850, 860, 1330]]


costTextPos = [(1755,198), (1756,280), (1755,364), (1755,449), (1755,534), (1755,619), (1755,701), (1755,783), (1756,870), (1753,953)]
buildPos = [(1590,100), (1590,184), (1590,268), (1590,352), (1590,436), (1590,520), (1590,604), (1590,688), (1590,772), (1590,856)]


#MAIN LOOP
while running:
    pygame.display.set_caption(f"{cookies} Cookies - Cookie Clicker")
    #SET UP
    screen.blit(background, (0, 0))

    cookieText = fonts[0].render(f"{cookies} cookies", True, (255, 255, 255))
    cookieTextTwo = fonts[1].render(f"{Cps} cookies per second", True, (255, 255, 255))
    

    for building in buildings:
        building.updateText(cookies)

    bigCookieClick = fonts[1].render(f"{cookiesClicks} cookies", True, (255, 255, 255))


    cookieText.blit(textureSurface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
    cookieTextTwo.blit(textureSurface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    #EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if cookieRect.collidepoint(pygame.mouse.get_pos()):
                x,y = pygame.mouse.get_pos()
                x-=15
                y-=15
                cookies+=cookiesClicks
                clickText.append((x, y, clickTextAlpha))
                #screen.blit(bigCookieClick, pygame.mouse.get_pos())
                bigCookie = setImage("cookieTwo.png", bigCookieW,bigCookieH)
                pygame.mixer.Sound.play(cookieClickTwo)
                pygame.mixer.Sound.play(cookieClickThree)
                #bigCookie = pygame.transform.scale(bigCookie, (bigCookieW-5, bigCookieH-5))
                #bigCookie = pygame.transform.scale(bigCookie, (bigCookieW+5, bigCookieH+5))

            for rect, building in zip(rects, buildings):
                if rect.collidepoint(pygame.mouse.get_pos()):
                    if cookies >= building.cost:
                        Cps = building.buy()

            for upgrade in upgrades:
                if upgrade.frameRect.collidepoint(pygame.mouse.get_pos()) and upgrade.cost <= cookies and upgrade.valid:
                    upgrade.valid = False

                    upgrade.shown = False
                    cookies -= upgrade.cost
                    Cps = upgrade.bought()
                    break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if cookieRect.collidepoint(pygame.mouse.get_pos()):
                bigCookie = setImage("cookie.png", bigCookieW,bigCookieH)


    #IF BUILDINGS

    for rect, building, infoSetUp in zip(rects, buildings, infoSetUps):
        if rect.collidepoint(pygame.mouse.get_pos()):
            filePath, y1, y2, y3, y4, x1 = infoSetUp
            building.infoSet(filePath, y1, y2, y3, y4, x1)


    #IF UPGRADES
    for upgrade in upgrades:
        if upgrade.frameRect.collidepoint(pygame.mouse.get_pos()) and upgrade.shown:
            upgrade.info()
    #TIME
    currentTime = pygame.time.get_ticks()

    if currentTime >= gameSecond:
        cookies += Cps
        gameSecond = currentTime + 1000

    if currentTime >= nextTime:
        xCookie = random.randint(20, 420)
        yCookie = -40
        smallCookies.append((xCookie, yCookie, cookieVelocety))
        nextTime = currentTime + random.randint(1000,5000)

    updateCookies = []
    for smallCookie in smallCookies:
        xCookie, yCookie, cookieVelocety = smallCookie

        yCookie += cookieVelocety

        if yCookie < 700:
            updateCookies.append((xCookie, yCookie, cookieVelocety))
    
    smallCookies = updateCookies

    updateClickText = []
    for text in clickText:
        xText, yText, alphaText = text

        alphaText -= 10
        yText -= 1
        bigCookieClick.set_alpha(alphaText)

        if alphaText > 0:
            updateClickText.append((xText, yText, alphaText))

    clickText = updateClickText

    #achievments

    for achievment in achievments:
        if achievment.check():
            if currentTime >= destroyTime:
                achievment.valid = False
                destroyTime = currentTime+destroyTime

    for achievment in achievmentBuildings:
        if achievment.checkBuilding():
            if currentTime >= destroyTime:
                achievment.valid = False
                destroyTime = currentTime+destroyTime

    #DISPLAY
    for smallCookie in smallCookies:
        xCookie, yCookie, cookieVelocety = smallCookie
        screen.blit(cookie, (xCookie, yCookie))

    screen.blit(bigCookie, cookieRect)

    screen.blit(cookieText, (170,130))
    screen.blit(cookieTextTwo, (140,170))

    screen.blit(plank, (400,-40))
    screen.blit(plank, (1500,-40))
    screen.blit(milk, (-289,500))

    screen.blit(draw(320,1310, 180, 100, 100, 100), (1604,-298))

    screen.blit(rPlank, (1593,50))
    screen.blit(rPlank, (1593,918))
    screen.blit(rPlankT, (470,50))

    #buildings
    for building, pos in zip(buildings, buildPos):
        screen.blit(building.picture, pos)

    for building, pos in zip(buildings, costTextPos):
        screen.blit(building.Text, pos)

    for text in clickText:
        xText, yText, alphaText = text
        
        screen.blit(bigCookieClick, (xText, yText))
    
    for upgrade in upgrades:
        upgrade.check()
    #END OF LOOP
    pygame.display.update()
    clock.tick(60)

#END
pygame.quit()
sys.exit()