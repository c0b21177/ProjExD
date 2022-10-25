import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    tori_sfc = pg.image.load("fig/9.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    font = pg.font.Font(None, 80)

    bomb_sfc = pg.image.load("bomb01.png")
    bomb_sfc = pg.transform.rotozoom(bomb_sfc, 0, 0.1)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = random.randint(10,300), random.randint(10,890)

    power_sfc = pg.Surface((350, 50))
    power_rct = power_sfc.get_rect()
    power_rct.center = 1375, 75

    vx = vy = 4
    powerx = 350
    powery = 50

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(power_sfc, power_rct)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        pg.draw.rect(scrn_sfc, (0, 255, 0), (1200, 50, powerx, powery))
        text = font.render("stamina", True, (0,0,0))
        scrn_sfc.blit(text,[1200,50])
        bomb_rct.move_ip(vx,vy)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LEFT]:
            tori_rct.centerx -= 1
            if key_lst[pg.K_LSHIFT] and powerx >= 0:
                tori_rct.centerx -= 2
                powerx -= 0.5
            if not key_lst[pg.K_LSHIFT] and powerx <= 350:
                powerx += 0.1
        elif key_lst[pg.K_RIGHT]:
            tori_rct.centerx += 1
            if key_lst[pg.K_LSHIFT] and powerx >= 0:
                tori_rct.centerx += 2
                powerx -= 0.5
            if not key_lst[pg.K_LSHIFT] and powerx <= 350:
                powerx += 0.1
        elif key_lst[pg.K_UP]:
            tori_rct.centery -= 1
            if key_lst[pg.K_LSHIFT] and powerx >= 0:
                tori_rct.centery -= 2
                powerx -= 0.5
            if not key_lst[pg.K_LSHIFT] and powerx <= 350:
                powerx += 0.1
        elif key_lst[pg.K_DOWN]:
            tori_rct.centery += 1
            if key_lst[pg.K_LSHIFT] and powerx >= 0:
                tori_rct.centery += 2
                powerx -= 0.5
            if not key_lst[pg.K_LSHIFT] and powerx <= 350:
                powerx += 0.1
        else:
            powerx += 0.5
            

        if tori_rct.left < 0 :
            tori_rct.move_ip(2, 0)
        if tori_rct.right > 1600:
            tori_rct.move_ip(-2, 0)
        if tori_rct.top < 0:
            tori_rct.move_ip(0, 2)
        if tori_rct.bottom > 900:
            tori_rct.move_ip(0, -2)
            

        if bomb_rct.left < -22 or bomb_rct.right > 1622:
            vx = -vx
        if bomb_rct.top < -20 or bomb_rct.bottom > 920:
            vy = -vy

        if tori_rct.colliderect(bomb_rct):
            return

        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
    
    
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()