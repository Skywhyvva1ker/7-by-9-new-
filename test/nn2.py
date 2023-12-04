import pygame

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Инициализация окна игры
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Игра на Pygame")

# Задержка перед обновлением экрана
clock = pygame.time.Clock()

# Флаг паузы
is_paused = False

# Главный игровой цикл
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка нажатия на клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Переключение флага паузы
                is_paused = not is_paused

    # Отображение текста "ПАУЗА" в центре экрана при паузе
    if is_paused:
        font = pygame.font.SysFont(None, 48)
        text = font.render("ПАУЗА", True, BLACK)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()