import pygame as pg

RSC = {
    'title': '7 by 9',
    'FPS': 60,
    ''
    'img': {
        'bg_color': (84, 179, 179),
        'back': 'GUI/cad_img/card_background.png',
        'card': 'GUI/cad_img/{}.png',
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255)
    },
    'main_sound': "GUI/sounds/Free-Flow-Flava-This-Is-Japan.wav",
}

# info = pg.display.Info()
# width = info.current_w
# height = info.current_h - 65

GEOM = {
    'display': (800, 600),
    'card': (100, 152),
    'dx_card': 10,
    'dx_card_compact': 30,
    'xgap': 10,
    'ygap': 10,
}

card_images = {
    (1, 'orange'): pg.image.load("GUI/card_img/1_orange.png"),
    (2, 'orange'): pg.image.load("GUI/card_img/2_orange.png"),
    (3, 'orange'): pg.image.load("GUI/card_img/3_orange.png"),
    (4, 'orange'): pg.image.load("GUI/card_img/4_orange.png"),
    (5, 'orange'): pg.image.load("GUI/card_img/5_orange.png"),
    (6, 'orange'): pg.image.load("GUI/card_img/6_orange.png"),
    (7, 'orange'): pg.image.load("GUI/card_img/7_orange.png"),
    (8, 'orange'): pg.image.load("GUI/card_img/8_orange.png"),
    (9, 'orange'): pg.image.load("GUI/card_img/9_orange.png"),
    (10, 'orange'): pg.image.load("GUI/card_img/10_orange.png"),
    (1, 'blue'): pg.image.load("GUI/card_img/1_blue.png"),
    (2, 'blue'): pg.image.load("GUI/card_img/2_blue.png"),
    (3, 'blue'): pg.image.load("GUI/card_img/3_blue.png"),
    (4, 'blue'): pg.image.load("GUI/card_img/4_blue.png"),
    (5, 'blue'): pg.image.load("GUI/card_img/5_blue.png"),
    (6, 'blue'): pg.image.load("GUI/card_img/6_blue.png"),
    (7, 'blue'): pg.image.load("GUI/card_img/7_blue.png"),
    (8, 'blue'): pg.image.load("GUI/card_img/8_blue.png"),
    (9, 'blue'): pg.image.load("GUI/card_img/9_blue.png"),
    (10, 'blue'): pg.image.load("GUI/card_img/10_blue.png"),
    (1, 'green'): pg.image.load("GUI/card_img/1_green.png"),
    (2, 'green'): pg.image.load("GUI/card_img/2_green.png"),
    (3, 'green'): pg.image.load("GUI/card_img/3_green.png"),
    (4, 'green'): pg.image.load("GUI/card_img/4_green.png"),
    (5, 'green'): pg.image.load("GUI/card_img/5_green.png"),
    (6, 'green'): pg.image.load("GUI/card_img/6_green.png"),
    (7, 'green'): pg.image.load("GUI/card_img/7_green.png"),
    (8, 'green'): pg.image.load("GUI/card_img/8_green.png"),
    (9, 'green'): pg.image.load("GUI/card_img/9_green.png"),
    (10, 'green'): pg.image.load("GUI/card_img/10_green.png"),
}
