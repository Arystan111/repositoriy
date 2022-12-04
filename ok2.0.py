import pygame as pg
from random import *

pg.init()
W = 400
H = 400
RED = (255, 0, 0)
f = 42
k = 14
sc = pg.display.set_mode((W, H))
win = pg.display.set_mode((400, 400))
background_color = (255, 255, 255)
color = (64, 64, 64)
img = pg.image.load('Оранжевая машинка2.png')



clock = pg.time.Clock()
FPS = 110


s = 0
fp = 100





class Game_sprite(pg.sprite.Sprite):
    def __init__(self, x, filename, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)


def menu_def():
    sc.blit(menu.image, menu.rect)
    play = sc.blit(btn_start.image, btn_start.rect)
    stop = sc.blit(btn_stop.image, btn_stop.rect)
    pg.display.update()



    

sprts = pg.sprite.Group()
user_car = pg.sprite.Group()
green_left = pg.sprite.Group()
green_right = pg.sprite.Group()
road_group = pg.sprite.Group()
menu_group = pg.sprite.Group()
play_group = pg.sprite.Group()
stop_group = pg.sprite.Group()

menu = Game_sprite(200, 'Menu.png', menu_group)
btn_start = Game_sprite(200, 'btn_play.png', play_group)
btn_stop = Game_sprite(200, 'btn_exit.png', stop_group)
car1 = Game_sprite(60, 'Оранжевая машинка2.png', user_car)
let = Game_sprite(randint(100, 300), 'let3.png', sprts)
gr_left = Game_sprite(33, 'gr.png', green_left)
gr_right = Game_sprite(367, 'gr.png', green_right)



car1.rect.y = 200
car1.rect.x = 100
gr_left.rect.y = 0
gr_right.rect.y = 0
menu.rect.y = 0
btn_start.rect.y = 150
btn_stop.rect.y = 250




game = True
game_over = 0

sc.blit(menu.image, menu.rect)
play = sc.blit(btn_start.image, btn_start.rect)
stop = sc.blit(btn_stop.image, btn_stop.rect)
pg.display.update()



while game:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    score = pg.font.Font(None, 46)
    text_score = score.render(str(s), 1, (255, 255, 255))
    per = pg.font.Font(None, 18)
    text_per = per.render(str(fp), 1, (255, 255, 255))


    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                pos = i.pos
                if play.collidepoint(pos):
                    game_over = 1
                    let.rect.y = 0
                    pg.display.update()
                elif stop.collidepoint(pos):
                    game = False

    if game_over == 1:
        if keys[pg.K_LEFT]:
            car1.rect.x = car1.rect.x - 3
        elif keys[pg.K_RIGHT]:
            car1.rect.x = car1.rect.x + 3
        elif keys[pg.K_DOWN]:
            car1.rect.y = car1.rect.y + 3
        elif keys[pg.K_UP]:
            car1.rect.y = car1.rect.y - 3


        sc.blit(gr_left.image, gr_left.rect)
        sc.blit(gr_right.image, gr_right.rect)
        sc.blit(car1.image, car1.rect)
        sc.blit(let.image, let.rect)



        pg.display.update()
        car1.update()

    if let.rect.y < H:
        let.rect.y = let.rect.y + randint(1, 3)
    else:
        let = Game_sprite(randint(100, 300), 'let3.png', sprts)
        let.rect.y = 0
        s = s+1
        text_score = score.render(str(s), 1, (255,255,255))




    if pg.sprite.spritecollideany(car1, sprts):
        game_over = 0
        menu_def()

    if pg.sprite.spritecollideany(car1, green_left):
        game_over = 0
        menu_def()


    if pg.sprite.spritecollideany(car1, green_right):
        game_over = 0
        menu_def()


    pg.display.update()
