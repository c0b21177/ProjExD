import pygame as pg
import sys
from random import randint

class Screen():
    def __init__(self, title, wdhi, bgi):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wdhi)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgi)
        self.bgi_rct = self.bgi_sfc.get_rect()
        self.bgy = 0
        self.scroll = 3
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, (0,self.bgy))
        self.sfc.blit(self.bgi_sfc, (0, self.bgy - self.bgi_rct.height))
    
    def update(self):
        self.bgy = (self.bgy + self.scroll) % self.bgi_rct.height
        

class Bird():
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, png, zoom, cent):
        sfc = pg.image.load(png)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = sfc.get_rect()
        self.rct.center = cent

    def blit(self, scrn:Screen):
        scrn.sfc.blit(self.sfc, self.rct)

    def update(self, scrn:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scrn.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scrn)

class Enemy():
    def __init__(self, png, zoom, speed, scrn:Screen):
        sfc = pg.image.load(png)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(50, scrn.rct.width-50)
        self.rct.centery = 50
        self.vx, self.vy = speed
    
    def blit(self, scrn:Screen):
        scrn.sfc.blit(self.sfc, self.rct)

    def update(self, scrn:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scrn.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scrn)
    
class Shot():
    def __init__(self, png, zoom, speed, centerx, centery):
        sfc = pg.image.load(png)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = centerx
        self.rct.centery = centery
        self.bx, self.by = speed
    
    def blit(self, scrn:Screen):
        scrn.sfc.blit(self.sfc, self.rct)

    def update(self, scrn:Screen):
        self.rct.move_ip(self.bx, self.by)
        self.blit(scrn)

def check_bound(obj_rct, scrn_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scrn_rct.left or scrn_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def main():
    scrn = Screen("シューティングゲーム", (700,900), "bg_sky.jpg")
    tori = Bird("superman.png", 2.0, (350, 800))
    teki = Enemy("UFO.png", 0.1, (+1, 0), scrn)
    clock = pg.time.Clock()
    a = False
    
    while True: 
        scrn.blit()
        scrn.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    a = True
                    gun = Shot("bullet.png", 0.02, (0,-2), tori.rct.centerx-5, tori.rct.centery)
                    gun2 = Shot("bullet.png", 0.02, (0,-2), tori.rct.centerx+15, tori.rct.centery)
        
        tori.update(scrn) 
        teki.update(scrn)
        if a == True:
            gun.update(scrn)
            gun2.update(scrn)

        if tori.rct.colliderect(teki.rct):
            return
            

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() 
    main()    
    pg.quit() 
    sys.exit()
