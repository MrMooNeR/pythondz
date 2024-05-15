number = input("Введите трехзначное число: ")

if len(number) != 3 or not number.isdigit() or len(set(number)) != 3:
    print("Ошибка: введите трехзначное число с неповторяющимися цифрами")
else:
    a = int(number) % 10
    number = int(number) // 10
    b = int(number) % 10
    number = int(number) // 10
    c = int(number) % 10

    a = str(a)
    b = str(b)
    c = str(c)

    print(a + b + c)
    print(a + c + b)
    print(b + a + c)
    print(b + c + a)
    print(c + a + b)
    print(c + b + a)
