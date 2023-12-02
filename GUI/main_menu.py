import pygame as pg
from game import *



pg.init()
info = pg.display.Info()
width = info.current_w
height = info.current_h - 65
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Моя игра")

# Цвета
bc_color = (84, 179, 179)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание кнопок
button_font = pg.font.SysFont("Arial", 30)

button_play = pg.Surface((200, 70))
button_play.fill(BLACK)
button_play_rect = button_play.get_rect(center=(width // 2, height // 2 - 100))
button_play_text = button_font.render("Играть", True, WHITE, BLACK)
button_play_text_rect = button_play_text.get_rect(center=button_play_rect.center)

button_rules = pg.Surface((200, 70))
button_rules.fill(BLACK)
button_rules_rect = button_rules.get_rect(center=(width // 2, height // 2))
button_rules_text = button_font.render("Правила", True, WHITE, BLACK)
button_rules_text_rect = button_rules_text.get_rect(center=button_rules_rect.center)

button_settings = pg.Surface((200, 70))
button_settings.fill(BLACK)
button_settings_rect = button_settings.get_rect(center=(width // 2, height // 2 + 100))
button_settings_text = button_font.render("Настройки", True, WHITE, BLACK)
button_settings_text_rect = button_settings_text.get_rect(center=button_settings_rect.center)

button_exit = pg.Surface((200, 70))
button_exit.fill(BLACK)
button_exit_rect = button_exit.get_rect(center=(width // 2, height // 2 + 200))
button_exit_text = button_font.render("Выход", True, WHITE, BLACK)
button_exit_text_rect = button_exit_text.get_rect(center=button_exit_rect.center)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if button_play_rect.collidepoint(event.pos):
                print("Кнопка 'Играть' нажата!")
            elif button_rules_rect.collidepoint(event.pos):
                print("Кнопка 'Правила' нажата!")
            elif button_settings_rect.collidepoint(event.pos):
                print("Кнопка 'Настройки' нажата!")
            elif button_exit_rect.collidepoint(event.pos):
                running = False

    screen.fill(bc_color)

    # Отображение кнопок
    screen.blit(button_play, button_play_rect)
    screen.blit(button_play_text, button_play_text_rect)

    screen.blit(button_rules, button_rules_rect)
    screen.blit(button_rules_text, button_rules_text_rect)

    screen.blit(button_settings, button_settings_rect)
    screen.blit(button_settings_text, button_settings_text_rect)

    screen.blit(button_exit, button_exit_rect)
    screen.blit(button_exit_text, button_exit_text_rect)

    pg.display.flip()

pg.quit()