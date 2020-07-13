en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

text = input('Текст для шифровки/дешифровки: ')

print('\nЕсли хотите зашифровать введите любую цифру от 0 до 9')
print('Если хотите дешифровать введите любой знак(и)')
cod = input('\nЗашифровать или дешифровать: ')
cod = 1 if cod.isdigit() else 0

alph = input('Русский(Рус/Ru) или English(Англ/En): ')
while alph not in ('рус', 'англ', 'ru', 'en'):
    alph = input('Введите корректный ответ: ')
alph = en if alph in ('en', 'англ') else ru

step = input('Введите шаг сдвига - целое положительное число больше 0: ')
while not step.isdigit() or int(step) < 1:
    step = input('Введите целое положительное число больше 0: ')
step = int(step)

answer = ''
for i in text:
    if i.lower() in alph:
        case = 1 if i != i.lower() else 0
        i = i.lower()

        if cod == 1:
            if alph.find(i) + step <= len(alph) - 1:
                i = alph[alph.find(i) + step]
            else:
                i = alph[(alph.find(i) + step) - (len(alph) - 1) - 1]

        if cod == 0:
            if alph.find(i) - step >= 0:
                i = alph[alph.find(i) - step]
            else:
                i = alph[(alph.find(i) - step) - 0]

        if case:
            i = i.upper()

    answer += i

print('\n' + answer + '\n')
