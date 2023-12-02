import pygame as pg
from card import Card
from deck import Deck
from hand_players import Hand_Players
from GUI.config import GEOM
from GUI.config import RSC
from game import *

pg.init()
width, height = GEOM['display']
screen = pg.display.set_mode((width, height))
pg.display.set_caption("7 НА 9")

icon_img = pg.image.load('GUI/other_img/icon.png')

pg.mixer.music.load("GUI/sounds/Free-Flow-Flava-This-Is-Japan.wav")
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(-1)

display = pg.display.set_mode((width, height))
pg.display.set_icon(icon_img)

bg_color = RSC['img']['bg_color']
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание кнопок
button_font = pg.font.SysFont("Arial", 30)

button_play = pg.Surface((200, 70))
button_play.fill(BLACK)
button_play_rect = button_play.get_rect(center=(width // 2, height // 2 - 150))
button_play_text = button_font.render("Играть", True, WHITE, BLACK)
button_play_text_rect = button_play_text.get_rect(center=button_play_rect.center)

button_rules = pg.Surface((200, 70))
button_rules.fill(BLACK)
button_rules_rect = button_rules.get_rect(center=(width // 2 , height // 2 - 50))
button_rules_text = button_font.render("Правила", True, WHITE, BLACK)
button_rules_text_rect = button_rules_text.get_rect(center=button_rules_rect.center)

button_settings = pg.Surface((200, 70))
button_settings.fill(BLACK)
button_settings_rect = button_settings.get_rect(center=(width // 2, height // 2 + 50))
button_settings_text = button_font.render("Настройки", True, WHITE, BLACK)
button_settings_text_rect = button_settings_text.get_rect(center=button_settings_rect.center)

button_exit = pg.Surface((200, 70))
button_exit.fill(BLACK)
button_exit_rect = button_exit.get_rect(center=(width // 2, height // 2 + 200))
button_exit_text = button_font.render("Выход", True, WHITE, BLACK)
button_exit_text_rect = button_exit_text.get_rect(center=button_exit_rect.center)

gameState = "главное меню"

card_width, card_height = GEOM['card']

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if gameState == "главное меню":
                if button_play_rect.collidepoint(event.pos):
                    Deck.num_players = 2
                    print("Кнопка 'Играть' нажата!")
                    gameState = "игра началась"
                    Deck = Deck()
                    print(Deck.DECK)
                    print(Deck.table_card)
                elif button_rules_rect.collidepoint(event.pos):
                    print("Кнопка 'Правила' нажата!")
                elif button_settings_rect.collidepoint(event.pos):
                    print("Кнопка 'Настройки' нажата!")
                elif button_exit_rect.collidepoint(event.pos):
                    running = False

    screen.fill(bg_color)

    if gameState == "главное меню":
        # Отображение кнопок
        screen.blit(button_play, button_play_rect)
        screen.blit(button_play_text, button_play_text_rect)

        screen.blit(button_rules, button_rules_rect)
        screen.blit(button_rules_text, button_rules_text_rect)

        screen.blit(button_settings, button_settings_rect)
        screen.blit(button_settings_text, button_settings_text_rect)

        screen.blit(button_exit, button_exit_rect)
        screen.blit(button_exit_text, button_exit_text_rect)
    elif gameState == "игра началась":
        print('')

    pg.display.flip()

pg.quit()


def rules():
    print('\nПРАВИЛА НАСТОЛЬНОЙ ИГРЫ 7 НА 9 \n')
    print("""ОБ ИГРЕ
    2-4 игрока
    Тут все просто: есть карты, на них цифры. 
Нужно быстро считать и класть подходящую карту в центр стола. 
Очередности хода нет. Кто первым посчитал, кладёт карту.\n """)
    print("""СОСТАВ
    73 карты с цифрами от 1 до 10.\n """)
    print("""ПОДГОТОВКА
    1. Перемешайте карты.
    2. Откройте первую карту и положите в центр стола. Это центральная стопка.
    3. Раздайте игрокам оставшиеся карты поровну. У каждого будет своя колода.\n """)
    print("""ХОД ИГРЫ   
    Раздающий говорит: 'Начали!' Посмотрите на карту в центре и посчитайте
какую карту нужно на неё положить. Берите карты по одной, пока не возьмете
подходящую. Взяли? Громко назовите большое число с этой карты и кладите её
в центр поверх первой. Теперь скорее считайте, что нужно положить на новую
карту и так далее.
В руке может быть сколько угодно карт.\n""")
    print("""КОНЕЦ ИГРЫ
    Когда ваша колода кончилась, а в руке осталась одна карта, положите её 
рубашкой вверх в центральную стопку. Неважно какое число изображено на
вашей карте. Крикните '7 на 9!'
Вы победили!\n""")
    print("""ЕСЛИ СУММА БОЛЬШЕ 10
    Вы посчитали и получили число больше 10? Вычтите из него 10.
Карту с этим числом и нужно класть в центр.
Например: 
    В центре лежит 9(+-3).
    Если прибавить 3, получится 12.
    Значит нужно класть карту с цифрой 2.
    Если вычитать, кладите 6, как обычно.\n""")
    print("""ЕСЛИ РАЗНОСТЬ МЕНЬШЕ 1
    Вы посчитали и получили число меньше 1? Прибавляйте 10
и кладите карту с этим числом.
Например:
    В центре лежит 1(+-2).
    Если вычесть 2, то получится -1.
    Значит, нужно класть карту с цифрой 9.
    Если прибавлять, кладите 3.\n""")
    print("""ЧТО ЕЩЁ НУЖНО ЗНАТЬ
    Вы можете класть несколько карт подряд, но нужно класть их по одной карте за раз.
Сразу стопку карт класть нельзя.
    Если сразу несколько человек кладут подходящую карту в центральную стопку,
побеждает тот, кто положил карту первым. Даже если он назвал число вторым.
Остальные забирают карты обратно в руки.
    Если вдруг ни у кого нет подходящей карты, хотя все карты уже в руках,
все игроки кладут свои карты на стол лицом вниз. Раздающий достает нижнюю
карту центральной стопки и кладет её наверх. Потом он говорит 'Начали!',
все берут свои карты и продолжают игру.
 """)

# num_players = 2
# def select_players():
#     global num_players
#     num_players = input("Введите количество игроков (2-4): ")
#     if num_players.isdigit():
#         num_players = int(num_players)
#         if num_players >= 2 and num_players <= 4:
#             print("Количество игроков выбрано:", num_players)
#         else:
#             print("Неверное количество игроков. Попробуйте еще раз.")
#             select_players()
#      else:
#         print("Неверный ввод. Попробуйте еще раз.")
#         select_players()