while True:
    num = input("Введите число или 'exit' для выхода: ")
    if num.lower() == "exit":
        break
    try:
        number = int(num)
        print("Длина числа:", len(str(number)))
    except ValueError:
        print("Это не число")
