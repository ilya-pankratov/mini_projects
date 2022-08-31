from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


def generate_password(length, character_set, count):        # генерируем пароли и предлагаем начать заново
    print('\nСгенерированные пароли:')
    for _ in range(count):
        password = ''
        for _ in range(length):
            password += choice(character_set)
        print(password)

    again = is_valid_answer(input('\nЗапустить программу еще раз? (+/-): \n'))
    if again:
        collect_characters()
    else:
        print('\nДо встречи!')


def is_valid_answer(answer):        # проверка на вопросы да/нет
    if answer == '+':
        answer = True
        return answer
    elif answer == '-':
        answer = False
        return answer
    else:
        is_valid_answer(input("Команда не распознана."
                              "\nВведите '+' для ответа 'да' или '-' для ответа 'нет': "))


def is_valid_value(value):          # проверка на введеные значения
    if value.isdigit() and int(value) > 0:
        return int(value)
    else:
        is_valid_value(input('Неккоректное значение. Попробуйте еще раз: '))


def collect_characters():       # определяем параметры для генерации паролей
    chars = ''
    flag = False    # проверка, что хоть что-то выбрано
    something_is = False    # проверка, стоит ли предлагать последнее условие

    count_passwords = is_valid_value(input('Введите количество паролей для генерации: '))
    len_password = is_valid_value(input('Введите длину одного пароля: '))

    digits_on = is_valid_answer(input('Включать ли цифры? (+/-): '))
    if digits_on:
        chars += DIGITS
        flag = True
        something_is = True

    capital_letters_on = is_valid_answer(input('Включать ли прописные буквы? (+/-): '))
    if capital_letters_on:
        chars += UPPERCASE_LETTERS
        flag = True
        something_is = True

    lower_case_on = is_valid_answer(input('Включать ли строчные буквы? (+/-): '))
    if lower_case_on:
        chars += LOWERCASE_LETTERS
        flag = True
        something_is = True

    symbols_on = is_valid_answer(input('Включать ли символы "!#$%&*+-=?@^_"? (+/-): '))
    if symbols_on:
        chars += PUNCTUATION
        flag = True

    if not flag:
        print('Вы не выбрали никаких символов для пароля. Попробуйте еще раз.\n')
        return collect_characters()

    if something_is:
        ambiguous_symbols_off = is_valid_answer(input('Исключать ли неоднозначные символы "il1Lo0O"? (+/-): '))
        if ambiguous_symbols_off:
            for i in chars:
                if i in 'il1Lo0O':
                    chars = chars.replace(i, '')

    generate_password(len_password, chars, count_passwords)


input('Данная программа генерирует пароли по заданным параметрам.\nЧтобы начать нажмите Enter.\n')
collect_characters()
