import pygame 
import random 

# Инициализация Pygame 
pygame.init() 

# Определение цветов 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 

# Определение параметров окна 
WIDTH, HEIGHT = 800, 600 
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Виселица") 

# Словарь слов 
words = ["автомобиль", "банан", "книга", "пицца", "программирование", "змея", "кот", "собака"] 

# Выбор случайного слова из словаря 
word = random.choice(words) 
guessed = ["_"] * len(word)  # Список для отслеживания угаданных букв 

# Параметры игры 
hangman_status = 0 
FPS = 60 
clock = pygame.time.Clock() 
run = True 

# Функция для вывода текста на экран 
def draw_text(text, font, color, x, y): 
    text_surface = font.render(text, True, color) 
    text_rect = text_surface.get_rect() 
    text_rect.center = (x, y) 
    win.blit(text_surface, text_rect) 

# Функция для рисования виселицы 
def draw_hangman(errors): 
    parts = [ 
        (200, 450, 200, 100),  # Вертикальная палка 
        (200, 100, 400, 100),  # Горизонтальная палка 
        (400, 100, 400, 150),  # Петля 
        (350, 150, 450, 150),  # Верёвка 
        (400, 200, 400, 300),  # Туловище 
        (400, 230, 350, 270),  # Левая рука 
        (400, 230, 450, 270),  # Правая рука 
        (400, 300, 350, 350),  # Левая нога 
        (400, 300, 450, 350)   # Правая нога 
    ] 

    for i in range(errors): 
        if i < len(parts): 
            pygame.draw.line(win, BLACK, parts[i][:2], parts[i][2:], 5) 

# Основной игровой цикл 
while run: 
    clock.tick(FPS) 
    win.fill(WHITE) 
     
    # Рисуем виселицу 
    draw_hangman(hangman_status) 
     
    # Отображение угаданных букв 
    display_word = " ".join(guessed) 
    draw_text(display_word, pygame.font.Font(None, 48), BLACK, WIDTH // 2, 400) 
     
    # Обработка событий 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
        elif event.type == pygame.KEYDOWN: 
            if event.key >= pygame.K_a and event.key <= pygame.K_z: 
                letter = chr(event.key) 
                if letter in word: 
                    for i in range(len(word)): 
                        if word[i] == letter: 
                            guessed[i] = letter 
                else: 
                    hangman_status += 1 

    # Проверка на поражение 
    if hangman_status == 6: 
        win.fill(WHITE) 
        draw_text("Вы проиграли!", pygame.font.Font(None, 48), BLACK, WIDTH // 2, HEIGHT // 2) 
        draw_text(f"Правильное слово: {word}", pygame.font.Font(None, 36), BLACK, WIDTH // 2, HEIGHT // 2 + 50) 
        pygame.display.update() 
        pygame.time.delay(3000) 
        run = False 

    # Проверка на победу 
    if "_" not in guessed: 
        win.fill(WHITE) 
        draw_text("Вы победили!", pygame.font.Font(None, 48), BLACK, WIDTH // 2, HEIGHT // 2) 
        pygame.display.update() 
        pygame.time.delay(3000) 
        run = False 

    pygame.display.update() 

pygame.quit()
