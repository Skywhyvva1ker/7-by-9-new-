import pygame as pg
import random
import time
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

card_width, card_height = GEOM['card']
icon_img = pg.image.load('GUI/other_img/icon.png')

pg.mixer.music.load(RSC['main_sound'])
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(-1)

display = pg.display.set_mode((width, height))
pg.display.set_icon(icon_img)

bg_color = RSC['img']['bg_color']
BLACK = RSC['img']['BLACK']
WHITE = RSC['img']['WHITE']

# Создание кнопок
button_font = pg.font.SysFont("Arial", 30)

# КНОПКА ИГРАТЬ
button_play = pg.Surface((200, 70))
button_play.fill(BLACK)
button_play_rect = button_play.get_rect(center=(width // 2, height // 2 - 150))
button_play_text = button_font.render("Играть", True, WHITE, BLACK)
button_play_text_rect = button_play_text.get_rect(center=button_play_rect.center)

# КНОПКА ПРАВИЛА
button_rules = pg.Surface((200, 70))
button_rules.fill(BLACK)
button_rules_rect = button_rules.get_rect(center=(width // 2, height // 2 - 50))
button_rules_text = button_font.render("Правила", True, WHITE, BLACK)
button_rules_text_rect = button_rules_text.get_rect(center=button_rules_rect.center)

# КНОПКА НАСТРОЙКИ
button_settings = pg.Surface((200, 70))
button_settings.fill(BLACK)
button_settings_rect = button_settings.get_rect(center=(width // 2, height // 2 + 50))
button_settings_text = button_font.render("Настройки", True, WHITE, BLACK)
button_settings_text_rect = button_settings_text.get_rect(center=button_settings_rect.center)

# КНОПКА ВЫХОД
button_exit = pg.Surface((200, 70))
button_exit.fill(BLACK)
button_exit_rect = button_exit.get_rect(center=(width // 2, height // 2 + 200))
button_exit_text = button_font.render("Выход", True, WHITE, BLACK)
button_exit_text_rect = button_exit_text.get_rect(center=button_exit_rect.center)

# КНОПКА ВКЛ/ВЫКЛ МУЗЫКИ
pause_music_button = pg.image.load("GUI/other_img/music_on.png")
pause_music_button_width = pause_music_button.get_width()
pause_music_button_height = pause_music_button.get_height()
pause_music_button_rect = pause_music_button.get_rect(bottomright=(screen.get_width() - 10, screen.get_height() - 10))

# КНОПКА BACK
back_button = pg.image.load("GUI/other_img/back.png")
back_button_width = back_button.get_width()
back_button_height = back_button.get_height()
back_button_rect = back_button.get_rect(bottomright=(screen.get_width() - 50, screen.get_height() - 10))

# КНОПКА ПАУЗЫ/ВОЗОБНОВЛЕНИЯ ИГРЫ
pause_button = pg.image.load("GUI/other_img/pause.png")
pause_button_width = pause_button.get_width()
pause_button_height = pause_button.get_height()
pause_button_rect = pause_button.get_rect(bottomright=(screen.get_width() - 10, screen.get_height() - 560))

pause_game = False
pause_music = False
current_player = None


def paused_music():
    global pause_music_button
    if pause_music:
        pause_music_button = pg.image.load("GUI/other_img/music_off.png")
        pg.mixer.music.pause()
    else:
        pause_music_button = pg.image.load("GUI/other_img/music_on.png")
        pg.mixer.music.play()


def choose_random_player():
    current_player = random.randint(1, Deck.num_players)
    print('Ходит игрок:', current_player)


# Определение шрифта и размера текста
font = pg.font.SysFont('Times New Roman', 22)
small_font = pg.font.SysFont('Times New Roman', 16)

# Определение текста
text1 = font.render('ПРАВИЛА НАСТОЛЬНОЙ ИГРЫ 7 НА 9', True, BLACK)
text2 = small_font.render('ОБ ИГРЕ', True, BLACK)
text3 = small_font.render('2-4 игрока. Тут все просто: есть карты, на них цифры.', True, BLACK)
text4 = small_font.render(
    'Нужно быстро считать и класть подходящую карту в центр стола.',
    True, BLACK)
text5 = small_font.render(
    'Очередности хода нет. Кто первым посчитал, кладёт карту.',
    True, BLACK)

# Определение позиции текста
text1_rect = text1.get_rect(center=(width // 2, int(height * 0.04)))
text2_rect = text2.get_rect(topleft=(int(width * 0.06), int(height * 0.07)))
text3_rect = text3.get_rect(topleft=(int(width * 0.03), int(height * 0.1)))
text4_rect = text4.get_rect(topleft=(int(width * 0.03), int(height * 0.13)))
text5_rect = text4.get_rect(topleft=(int(width * 0.03), int(height * 0.16)))


def rules_text_view():
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    screen.blit(text4, text4_rect)
    screen.blit(text5, text5_rect)


last_choice_time = time.time()


gameState = "главное меню"
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print('Выход из игры')

        if event.type == pg.MOUSEBUTTONDOWN:
            if gameState == "главное меню":
                if button_play_rect.collidepoint(event.pos):
                    Deck.num_players = 2
                    print("Кнопка 'Играть' нажата!")
                    gameState = "игра началась"
                    last_choice_time = 0
                    deck = Deck()
                    deck.num_players = 2
                    deck.deal_cards()
                    print(deck.DECK)
                    print(deck.table_card)
                    print(deck.player1_deck)
                    print(deck.player2_deck)
                elif button_rules_rect.collidepoint(event.pos):
                    gameState = "открыты правила"
                    print("Кнопка 'Правила' нажата!")
                elif button_settings_rect.collidepoint(event.pos):
                    gameState = "открыты настройки"
                    print("Кнопка 'Настройки' нажата!")
                elif pause_music_button_rect.collidepoint(event.pos):
                    pause_music = not pause_music
                    paused_music()
                elif pause_button_rect.collidepoint(event.pos):
                    print('пауза')
                elif button_exit_rect.collidepoint(event.pos):
                    running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if gameState == "игра началась":
                if pause_music_button_rect.collidepoint(event.pos):
                    pause_music = not pause_music
                    paused_music()

                elif back_button_rect.collidepoint(event.pos):
                    gameState = 'главное меню'

        if event.type == pg.MOUSEBUTTONDOWN:
            if gameState == "открыты правила":
                if pause_music_button_rect.collidepoint(event.pos):
                    pause_music = not pause_music
                    paused_music()

                elif back_button_rect.collidepoint(event.pos):
                    gameState = 'главное меню'

        if event.type == pg.MOUSEBUTTONDOWN:
            if gameState == "открыты настройки":
                if pause_music_button_rect.collidepoint(event.pos):
                    pause_music = not pause_music
                    paused_music()

                elif back_button_rect.collidepoint(event.pos):
                    gameState = 'главное меню'

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print("Кнопка 'Escape' нажата ")
                gameState = "главное меню"

            elif event.key == pg.K_q:
                running = False
                print('Выход из игры')

            # elif event.key == pg.K_r:
            #     if gameState == "игра началась":
            #         pause_game = not pause_game

    screen.fill(bg_color)

    if gameState == "главное меню":
        screen.blit(button_play, button_play_rect)
        screen.blit(button_play_text, button_play_text_rect)

        screen.blit(button_rules, button_rules_rect)
        screen.blit(button_rules_text, button_rules_text_rect)

        screen.blit(button_settings, button_settings_rect)
        screen.blit(button_settings_text, button_settings_text_rect)

        screen.blit(button_exit, button_exit_rect)
        screen.blit(button_exit_text, button_exit_text_rect)

        screen.blit(pause_music_button, pause_music_button_rect)

    elif gameState == "игра началась":
        screen.blit(pause_button, pause_button_rect)
        screen.blit(pause_music_button, pause_music_button_rect)
        screen.blit(back_button, back_button_rect)
        current_time = time.time()
        if current_time - last_choice_time >= 5 and gameState == "игра началась":
            # Выбираем случайное число
            choose_random_player()
            # Обновляем время последнего выбора
            last_choice_time = current_time

    elif gameState == "открыты правила":
        screen.blit(pause_music_button, pause_music_button_rect)
        screen.blit(back_button, back_button_rect)
        rules_text_view()

    elif gameState == "открыты настройки":
        screen.blit(pause_music_button, pause_music_button_rect)
        screen.blit(back_button, back_button_rect)

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
