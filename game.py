import pygame as pg


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


def menu():
    print("Меню:")
    print("1. Играть")
    print("2. Правила")
    print("3. Выход")


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
