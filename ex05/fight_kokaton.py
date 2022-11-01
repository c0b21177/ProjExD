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
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


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
        self.rct.centerx = randint(0, scrn.rct.width)
        self.rct.centery = randint(0, scrn.rct.height)
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
    def __init__(self, png, zoom, speed, cent):
        sfc = pg.image.load(png)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.centerx, self.rct.centery = cent
        self.bx, self.by = speed
    
    def blit(self, scrn:Screen):
        scrn.sfc.blit(self.sfc, scrn.rct)

    def update(self, scrn:Screen):
        self.rct.move_ip(self.bx, self.by)
        self.blit(scrn)



def check_bound(obj_rct, scrn_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scrn_rct.left or scrn_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    scrn = Screen("戦え！こうかとん", (1600,900), "space_bg.jpg")
    tori = Bird("fig/9.png", 2.0, (900, 400))
    teki = Enemy("UFO.png", 0.1, (+1, +1), scrn)
    teki2 = Enemy("UFO.png", 0.1, (-1, -1), scrn)
    teki3 = Enemy("UFO.png", 0.1, (-2, -1), scrn)
    

    clock = pg.time.Clock()
    while True: 
        scrn.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        tori.update(scrn)
        teki.update(scrn)
        teki2.update(scrn)
        teki3.update(scrn)
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_z]:
            gun = Shot("bullet.png", 0.05, (0, -1), (tori.rct.centerx, tori.rct.centery))
            gun.update(scrn)


        if tori.rct.colliderect(teki.rct):
            return

        if tori.rct.colliderect(teki2.rct):
            return

        if tori.rct.colliderect(teki3.rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() 
    main()    
    pg.quit() 
    sys.exit()
