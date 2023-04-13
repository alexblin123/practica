letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
shift = int(input('Введите сдвиг: '))
message = input('Введите сообщение: ').lower()
result = ''
for i in message:
    place = letters.find(i)
    new_place = place + shift
    if i in letters:
        result += letters[new_place]
    else:
        result += i

print(f'Зашифрованное сообщение: {result}')
