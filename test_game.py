# Тесты для игры "Угадай число"
# Проверяем что все функции работают правильно

from game import check_guess, generate_number, is_valid_number

def test_check_guess_больше():
    # Тест: если загадано 50, а угадываем 30 - должно быть "больше"
    assert check_guess(50, 30) == "больше"
    print("PASSED: подсказка больше работает правильно")

def test_check_guess_меньше():
    # Тест: если загадано 50, а угадываем 70 - должно быть "меньше"
    assert check_guess(50, 70) == "меньше"
    print("PASSED: подсказка меньше работает правильно")

def test_check_guess_угадал():
    # Тест: если загадано 50 и угадываем 50 - должно быть "угадал"
    assert check_guess(50, 50) == "угадал"
    print("PASSED: определение победы работает правильно")

def test_generate_number():
    # Тест: сгенерированное число должно быть от 1 до 100
    number = generate_number()
    assert 1 <= number <= 100
    print("PASSED: число генерируется в диапазоне 1-100")

def test_is_valid_number():
    # Тест: проверка допустимых и недопустимых чисел
    assert is_valid_number(50) == True
    assert is_valid_number(0) == False
    assert is_valid_number(101) == False
    print("PASSED: проверка диапазона работает правильно")

# Запускаем все тесты
if __name__ == "__main__":
    test_check_guess_больше()
    test_check_guess_меньше()
    test_check_guess_угадал()
    test_generate_number()
    test_is_valid_number()
    print("Все тесты пройдены успешно!")
