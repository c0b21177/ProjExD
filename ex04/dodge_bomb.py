import pygame as pg
import sys
import random

x, y = random.randint(10,1590), random.randint(10,890)

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    tori_sfc = pg.image.load("fig/9.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900 ,400
    draw_sfc = pg.Surface((20,20))
    draw_sfc.set_colorkey((0,0,0))
    pg.draw.circle(draw_sfc, (255,0,0), (10,10), 10)
    draw_rct = draw_sfc.get_rect()
    draw_rct.centerx, draw_rct.centery = x,y
    vx = vy = 1


    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(draw_sfc, draw_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        draw_rct.move_ip(vx,vy)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LEFT]:
           tori_rct.centerx -= 1
        if key_lst[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_lst[pg.K_UP]:
            tori_rct.centery -= 1
        if key_lst[pg.K_DOWN]:
            tori_rct.centery += 1

        if tori_rct.left < 0 :
            tori_rct.move_ip(1, 0)
        if tori_rct.right > 1600:
            tori_rct.move_ip(-1, 0)
        if tori_rct.top < 0:
            tori_rct.move_ip(0, 1)
        if tori_rct.bottom > 900:
            tori_rct.move_ip(0, -1)
            

        if draw_rct.left < 0 or draw_rct.right > 1600:
            vx = -vx
        if draw_rct.top < 0 or draw_rct.bottom > 900:
            vy = -vy

        if tori_rct.colliderect(draw_rct):
            return

        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
    
    
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()