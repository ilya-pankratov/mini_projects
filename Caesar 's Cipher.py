
def is_valid_key(value):
    if value.isdigit() and int(value) > 0:
        return int(value)
    else:
        return is_valid_key(input('Некоректное значение. Попробуйте еще раз: '))


def is_valid_language(value):
    if value.lower() == 'английский':
        return 'abcdefghijklmnopqrstuvwxyz'
    elif value.lower() == 'русский':
        return 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    else:
        is_valid_language(input('Некоректное значение. Попробуйте еще раз: '))


def is_valid_code(value):
    if value.lower() == 'шифрование':
        return 'шифрование'
    elif value.lower() == 'дешифрование':
        return 'дешифрование'
    else:
        is_valid_code(input('Некоректное значение. Попробуйте еще раз: '))


def encrypt(code, letters, key, message):
    if code == 'дешифрование':
        key = -key
    if language == 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
        max = 32
    if language == 'abcdefghijklmnopqrstuvwxyz':
        max = 25

    for i in range(len(message)):
        if message[i].isalpha():
            if message[i] == message[i].upper():
                index_old = letters.upper().find(message[i])
                index_new = index_old + key
                if index_new > max:
                    index_new -= max + 1
                message[i] = letters.upper()[index_new]
            else:
                index_old = letters.find(message[i])
                index_new = index_old + key
                if index_new > max:
                    index_new -= max + 1
                message[i] = letters[index_new]

    return ''.join(message)


code = is_valid_code(input('Выберите направление (шифрование/дешифрование): '))
language = is_valid_language(input('Выберите язык сообщения (английский/русский): '))
key = is_valid_key(input('Введите шаг сдвига: '))
message = [i for i in input('Введите сообщение: ')]

print('\nЗашифрованное сообщение:')
print(encrypt(code, language, key, message))

