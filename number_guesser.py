from random import randint


def is_valid_right(value):      # проверка введеной правой границы (возвращает только правильно введенное)
    if value.isdigit() and int(value) > 1:
        return int(value)
    else:
        print("Не пойдет. Напоминаю: n - целое число и больше 1")
        return is_valid_right(input())


def is_valid(value, right_n):        # проверка введенного значения попытки (возвращает только правильно введенное)
    if value.isdigit() and 0 < int(value) < right_n + 1:
        return int(value)
    else:
        print(f"А может быть все-таки введешь целое число от 1 до {right_n}?")
        return is_valid(input(), right_n)


def game():         # сама игра
    print("Введи число n. Оно должно быть целым и больше 1.")
    n = is_valid_right(input())
    number = randint(1, n)
    print(f"\nХорошо. Я загадал целое число от 1 до {n}.\nПопробуй его угадать.")
    attempt = is_valid(input(), n)
    counter = 1

    while number != attempt:
        counter += 1
        if attempt < number:
            print("Мое число побольше, попробуй еще разок.")
            attempt = is_valid(input(), n)
        else:
            print("Мое число поменьше, попробуй еще разок.")
            attempt = is_valid(input(), n)

    print(f"\nВ точку, поздравляю!\nКоличество попыток: {counter}\n")
    continue_or_end()


def continue_or_end():         # предложение продолжить или закончить игру
    print("Хочешь сыграть ещё? (да/нет)")
    answer = input()
    if answer.lower() in ['да', 'д', 'yes', 'y', '+']:
        game()
    elif answer.lower() in ['нет', 'не', 'н', 'not', 'no', 'n', '-']:
        print("Спасибо, за игру.\nПриходи, когда появится желание играть снова...")
    else:
        print("Не разобрал.")
        continue_or_end()


print("Привет. Добро пожаловать в числовую угадайку!\n")
print("Правила игры:\n"
      "Я загадываю число от 1 до n, где n ты выбираешь сам.\n"
      "Например, если ты введешь 100. Я загадаю число от 1 до 100 включительно.\n"
      "И тебе нужно будет угадать мое число. Начинаем...\n")

game()          # вызов игры
