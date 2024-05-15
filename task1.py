import time

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umnozh(a, b):
    return a * b
def delit(a, b):
    if b == 0:
        raise ValueError("Давно на 0 делить можно стало?")
    return a / b
def stepen(a, b):
    return a ** b
def getNum(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Введите число")

def main():
    while True:
        print("\nЧто делаем?")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Степень (^)")
        print("6. Выход")
        operation = input("Введите номер операции (1-6): ")

        if operation not in ['1', '2', '3', '4', '5', '6']:
            print("По-русски же попросил, цифру 1-6 напиши")
            continue

        if operation == '6':
            print("Пока-пока")
            break

        number1 = getNum("Введите первое число ")
        number2 = getNum("Теперь второе ")

        try:
            if operation == '1':
                print("Result:", plus(number1, number2))
            elif operation == '2':
                print("Result:", minus(number1, number2))
            elif operation == '3':
                print("Result:", umnozh(number1, number2))
            elif operation == '4':
                print("Result:", delit(number1, number2))
            elif operation == '5':
                print("Result:", stepen(number1, number2))
        except ValueError as e:
            print(e)

        time.sleep(5)



if __name__ == "__main__":
    main()
