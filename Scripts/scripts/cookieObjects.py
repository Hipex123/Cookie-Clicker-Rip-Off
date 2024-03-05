import pygame
from dataCookie import *
from cookieImg import *


pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)

class Building:
    def __init__(self, cps, cost, picture: pygame.Surface, name, discription, owned):
        self.cps = cps
        self.cost = cost
        self.baseCost = cost
        self.picture = picture
        self.name = name
        self.discription = discription
        self.owned = owned

        self.Text = fonts[2].render(f"{cost}", True, (255, 255, 255))

    def buy(self):
        global cookies
        global Cps
        global buyBuilding
        

        cookies -= self.cost
        Cps += self.cps
        self.owned += 1
        self.cost = round(self.baseCost * pow(1.15, self.owned))
        pygame.mixer.Sound.play(buyBuilding)
        return Cps


    def info(self, font: pygame.font, x,y):
        discription = font.render(self.discription, True, (180, 180, 180))
        owned = font.render(f"Owned: {self.owned}", True, (180, 180, 180))
        discriptionTwo = font.render(f"That guy makes {self.cps} cookie per second.", True, (180, 180, 180))
        discriptionThree = font.render(f"And all of them make {self.owned * self.cps} cookie per second.", True, (180, 180, 180))

        screen.blit(discription, (x,y))
        screen.blit(owned, (x+20,y+30))
        screen.blit(discriptionTwo, (x-67,y+90))
        screen.blit(discriptionThree, (x-67,y+110))

    def infoSet(self, filePath, y1, y2, y3, y4, x):
        screen.blit(gold, (1250, y1))
        screen.blit(draw(300, 150, 255, 50,50,50), (1260, y2))

        if self.name != "Dad":
            screen.blit(setImage(filePath, 120, 100), (1245, y3))
        self.info(fonts[3], x, y4)
    
    def updateText(self, cookies):
        self.Text = fonts[2].render(f"{self.cost}", True, (255, 255, 255))

        if self.cost > cookies:
            self.picture.set_alpha(150)
            self.Text.set_alpha(150)
        else:
            self.picture.set_alpha(255)
            self.Text.set_alpha(255)

class Achievment:
    def __init__(self, picture: pygame.Surface, name, discription, condition , texture: pygame.Surface, building: Building = None):
        self.picture = picture
        self.condition = condition
        self.build = building
        self.valid = True
        global fonts

        self.nm = fonts[4].render(name, True, (255, 255, 255))
        self.disc = fonts[1].render(discription, True, (255, 255, 255))

        self.nm.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
        self.disc.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def check(self):
        global cookies
        global currentTime

        if cookies >= self.condition and self.valid:
            screen.blit(draw(350, 160, 255, 50, 50, 50), (790, 840))
            screen.blit(frame, (790, 840))
            screen.blit(self.picture, (770, 830))
            screen.blit(self.nm, (890, 870))
            screen.blit(self.disc, (815, 940))
            return True

    def checkBuilding(self):
        global currentTime
        
        if self.build.owned >= self.condition and self.valid:
            screen.blit(draw(350, 160, 255, 50, 50, 50), (790, 840))
            screen.blit(frame, (790, 840))
            screen.blit(self.picture, (790, 850))
            screen.blit(self.nm, (890, 870))
            screen.blit(self.disc, (815, 960))
            return True

class Upgrade:
    def __init__(self, name, discription, picture: pygame.Surface, condition, upgrade, cost,build: Building, texture: pygame.Surface):
        self.name = name
        self.picture = picture
        self.condition = condition
        self.upgrade = upgrade
        self.cost = cost
        self.build = build
        self.valid = True
        self.shown = False


        self.picture = pygame.transform.smoothscale(self.picture, (100,90))

        self.frameRect = frame2.get_rect()
        self.frameRect.width = 100
        self.frameRect.height = 101
        self.frameRect.x = 1605
        self.frameRect.y = 26

        self.nm = fonts[4].render(name, True, (255, 255, 255))
        self.disc = fonts[5].render(discription, True, (255, 255, 255))
        self.cst = fonts[4].render(f"{self.cost}", True, (255, 255, 255))
        
        self.nm.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
        self.disc.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
        self.cst.blit(texture, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def check(self):
        if self.condition <= self.build.owned and self.valid:
            screen.blit(draw(100, 101, 255, 50, 50, 50), (1605, 26))
            screen.blit(frame2, (1605, 26))
            if self.name != "More milk":
                screen.blit(self.picture, (1605, 30))
            
            self.shown = True

    def info(self):
        screen.blit(draw(300, 200, 255, 0, 0, 0), (1620, 27))

        screen.blit(self.nm, (1710, 27))
        screen.blit(self.disc, (1710, 55))
        screen.blit(priceCookie, (1710, 75))
        screen.blit(self.cst, (1735, 75))

    def bought(self):
        global Cps
        self.build.cps *= 2
        Cps += (self.build.cps*self.build.owned)/2
        return Cps

#buildings
whatB = Building(2, 5, what, "What", "Normal guy who bakes cookies.", 0)
twentyOneB = Building(3, 10, twentyOne, "21", "Not a child labor. He is 21.", 0)
skullB = Building(8, 110, skull, "Skull", "Nah bro fr fr.", 0)
nabruB = Building(47, 1200, nabru, "Nabru", "You know him.", 0)
manB = Building(260, 13000, man, "Man", "Gets people to bake cookeis.", 0)
dadB = Building(1400, 140000, dad, "Dad", "Got the milk.", 0)
everyoneB = Building(7800, 200000, everyone, "Everyone", "Everyone bakes cookies.", 0)
dontHurtB = Building(44000, 330000, dontHurt, "Dont hurt me", "No more laziness.", 0)
sigmaB = Building(260000, 75000000, sigma, "Sigma", "Gets alphas to make cookies.", 0)
steveB = Building(1600000, 99000000, steve, "Steve", "He is steve.", 0)

buildings = [whatB, twentyOneB, skullB, nabruB, manB, dadB, everyoneB, dontHurtB, sigmaB, steveB]
#achivements
achiOne = Achievment(achi_01, "Jesse we need to cook", "Beak 1 cookie.", 1, textureGold)
achiTwo = Achievment(achi_02, "Baking bread", "Beak 1000 cookies.", 1000, textureGold)
achiThree = Achievment(achi_03, "Baking cookie", "Beak 100 Thousand cookies.", 100000, textureGold)
achiFour = Achievment(achi_04, "You actually playing?", "Beak 1 Million cookies.", 1000000, textureGold)
achiFive = Achievment(achi_05, "Okay now you can go", "Beak 100 Million cookies.", 100000000, textureGold)
achiSix = Achievment(achi_06, "What did I say?", "Beak 1 Billion cookies.", 1000000000, textureGold)
achiSeven = Achievment(achi_07, "Go play MC or smth", "Beak 100 Billion cookies.", 100000000000, textureGold)
achiEight = Achievment(achi_08, "Happy now?", "Beak 1 Trillion cookies.", 1000000000000, textureGold)
achiNine = Achievment(achi_09, "Here is a golden star *", "Beak 100 Trillion cookies.", 100000000000000, textureGold)
achiTen = Achievment(achi_10, "Get a life", "Beak 1 Quadrillion cookies.", 1000000000000000, textureGold)
achiEleven = Achievment(achi_11, "Nobody will see this", "Beak 100 Quadrillion cookies.", 100000000000000000, textureGold)
achiTwelve = Achievment(achi_12, "Why?", "Beak 1 Quintillion cookies.", 1000000000000000000, textureGold)
#section2achivements

achiBOne = Achievment(setImage("whatIcon.png", 120, 100), "What?", "Own What?", 1, textureGold, whatB)
achiBTwo = Achievment(setImage("_twentyOneIcon.png", 120, 100), "Child labor", "Own 21", 1, textureGold, twentyOneB)
achiBThree = Achievment(setImage("skullIcon.png", 120, 100), "Man he is dead", "Own Skull", 1, textureGold, skullB)
achiBFour = Achievment(setImage("_nabruIcon.png", 120, 100), "Why is he here again?", "Own...", 1, textureGold, nabruB)
achiBFive = Achievment(setImage("manIcon.png", 120, 100), "He rises", "Own Moustache Man", 1, textureGold, manB)
achiBSeven = Achievment(setImage("everyOneIcon.png", 120, 100), "One mind", "Own everyone", 1, textureGold, everyoneB)
achiBEight = Achievment(setImage("dontHurtIcon.png", 120, 100), "Just dont hurt him", "Own that guy", 1, textureGold, dontHurtB)
achiBNine = Achievment(setImage("sigmaIcon.png", 120, 100), "Omega", "Own sigma", 1, textureGold, sigmaB)
achiBTen = Achievment(setImage("steveIcon.png", 130, 110), "Conqueror", "Own steve", 1, textureGold, steveB)

achiBEleven = Achievment(setImage("whatIcon.png", 120, 100), "What?????...", "Own 100 What?", 100, textureGold, whatB)
achiBTwelve = Achievment(setImage("_twentyOneIcon.png", 120, 100), "Thats messed up", "Own 100 21", 100, textureGold, twentyOneB)
achiBThirteen = Achievment(setImage("skullIcon.png", 120, 100), "Spam", "Own 100 Skull", 100, textureGold, skullB)
achiBFourteen = Achievment(setImage("_nabruIcon.png", 120, 100), "Nightmare", "Own 100...", 100, textureGold, nabruB)
achiBFiveteen = Achievment(setImage("manIcon.png", 120, 100), "Nobody is safe", "Own 100 Moustache Men", 100, textureGold, manB)
achiBSeventeen = Achievment(setImage("everyOneIcon.png", 120, 100), "Multiverse", "Own 100 everyone", 100, textureGold, everyoneB)
achiBEighteen = Achievment(setImage("dontHurtIcon.png", 120, 100), "Havent hurt him? Good", "Own 100 guys", 100, textureGold, dontHurtB)
achiBNineteen = Achievment(setImage("sigmaIcon.png", 120, 100), "Impossible", "Own 100 sigmas", 100, textureGold, sigmaB)
achiBTwenty = Achievment(setImage("steveIcon.png", 130, 110), "2B2T", "Own 100 steves", 100, textureGold, steveB)

whatUp = Upgrade("Questions", "All What? are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 100,whatB, textureRuby)
twentyOneUp = Upgrade("Necrophilia", "All twentyOnes are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 1100,twentyOneB, textureRuby)
skullUp = Upgrade("Necro", "All skulls are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 1000,skullB, textureRuby)
nabruUp = Upgrade("Piece of cake", "All dudes are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 12_000,nabruB, textureRuby)
manUp = Upgrade("No idea", "All men are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 1_300_00,manB, textureRuby)
dadUp = Upgrade("More milk", "All dads are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 1_400_000,dadB, textureRuby)
EveryOneUp = Upgrade("Zaza", "All everyone are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 20_000_000,everyoneB, textureRuby)
dontHurtUp = Upgrade("Hurt him", "All guys are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 330_000_000,dontHurtB, textureRuby)
sigmaUp = Upgrade("Omega", "All sigmas are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 5_100_000_000,sigmaB, textureRuby)
steveUp = Upgrade("Getting upgrade", "All steves are 2x efficient.", setImage("whatIcon.png", 50, 50), 25, 2, 75_000_000_000,steveB, textureRuby)