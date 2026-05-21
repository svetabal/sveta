# Игра "Угадай число"
# Программа загадывает число от 1 до 100
# Игрок должен угадать это число

import random

def generate_number():
    # Генерируем случайное число от 1 до 100
    return random.randint(1, 100)

def check_guess(secret, guess):
    # Проверяем догадку игрока
    # Возвращаем подсказку: больше, меньше или угадал
    if guess < secret:
        return "больше"
    elif guess > secret:
        return "меньше"
    else:
        return "угадал"

def is_valid_number(number):
    # Проверяем что число в допустимом диапазоне 1-100
    return 1 <= number <= 100

def play_game():
    # Основная функция игры
    secret = generate_number()
    attempts = 0
    print("Я загадал число от 1 до 100. Угадай!")
    
    while True:
        guess = int(input("Твоя догадка: "))
        attempts += 1
        result = check_guess(secret, guess)
        
        if result == "угадал":
            print(f"Правильно! Ты угадал за {attempts} попыток!")
            break
        else:
            print(f"Нет, загаданное число {result}!")

if __name__ == "__main__":
    play_game()
