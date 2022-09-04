
def is_valid_key(value):
    if value.isdigit() and int(value) > 0:
        return int(value)
    else:
        return is_valid_key(input('Неккоректное значение. Попробуйте еще раз: '))


def is_valid_language(value):
    if value.lower() == 'английский':
        return 'английский'
    elif value.lower() == 'русский':
        return 'русский'
    else:
        is_valid_language(input('Неккоректное значение. Попробуйте еще раз: '))


def is_valid_code(value):
    if value.lower() == 'шифрование':
        return 'шифрование'
    elif value.lower() == 'дешифрование':
        return 'дешифрование'
    else:
        is_valid_code(input('Неккоректное значение. Попробуйте еще раз: '))


def encrypt(code, language, key, message):
    if code == 'дешифрование':
        key = -key
    if language == 'русский':
        upper_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lower_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        max = 32
    if language == 'английский':
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        max = 25

    for i in range(len(message)):
        if message[i].isalpha():
            if message[i] == message[i].upper():
                index_old = upper_letters.find(message[i])
                index_new = index_old + key
                if index_new > max:
                    index_new -= max + 1
                message[i] = upper_letters[index_new]
            else:
                index_old = lower_letters.find(message[i])
                index_new = index_old + key
                if index_new > max:
                    index_new -= max + 1
                message[i] = lower_letters[index_new]

    print('\nЗашифрованное сообщение:')
    print(''.join(message))


code = is_valid_code(input('Выберите направление (шифрование/дешифрование): '))
language = is_valid_language(input('Выберите язык сообщения (английский/русский): '))
key = is_valid_key(input('Введите шаг сдвига: '))
message = [i for i in input('Введите сообщение: ')]

encrypt(code, language, key, message)

