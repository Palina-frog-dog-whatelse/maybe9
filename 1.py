def trans_notation():
    num = int(input('Введите число '))
    base_num = int(input('Выберите систему счисления(двоичная-2,восьмиричная-8) '))
    new_num = str('')
    while num > 0:
        new_num = str(num % base_num) + new_num
        num //= base_num
    print(new_num)

trans_notation()
