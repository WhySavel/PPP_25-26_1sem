def check_letters(stroka):
    lowletters_cntr = {}
    upletters_cntr = {}
    for i in stroka:
        if 'a' <= i <= 'z':
            lowletters_cntr[i] = lowletters_cntr.get(i, 0) + 1
        elif 'A' <= i <= 'Z':
            upletters_cntr[i] = upletters_cntr.get(i, 0) + 1

    remove_letters = set()
    for letter in lowletters_cntr:
        up_letter = letter.upper()
        low_cntr = lowletters_cntr.get(letter, 0)
        up_cntr = upletters_cntr.get(up_letter, 0)
        if low_cntr > up_cntr:
            remove_letters.add(letter)
            remove_letters.add(up_letter)

    res = []
    for symbol in stroka:
        if symbol not in remove_letters:
            res.append(symbol)
    return ''.join(res)

stroka = input('Введите строку из литанских букв любого регистра: ')
result = check_letters(stroka)
print(f'Начальная строка: {stroka}')
print(f'Конечная строка: {result}')
