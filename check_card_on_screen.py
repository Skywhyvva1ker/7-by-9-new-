import pygame as pg


pg.init()

screen = pg.display.set_mode((800, 600))

card_images = {
    (1, 'green'): pg.image.load("GUI/card_img/1_green.png")
}
card = card_images[(1, 'green')]

GEOM = {
    'card': (100, 152)
}
card_width, card_height = GEOM['card']

center_x = (screen.get_width() - card_width) // 2
center_y = (screen.get_height() - card_height) // 2

while True:
    screen.blit(card, (center_x, center_y))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()

pg.quit()