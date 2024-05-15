import time

class Wallet:
    paymentSystem = "Платежная система"

    def __init__(self, name, currency, balance=0):
        self.name = name
        self.currency = currency
        self.balance = balance

    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
            print(f"Кошелек '{self.name}' пополнен на {sum} {self.currency}.")
        else:
            print("Точно пополняешь?.")

    def pay(self, sum):
        if sum <= self.balance:
            self.balance -= sum
            print(f"Со счета кошелька '{self.name}' списано {sum} {self.currency}.")
        else:
            print(f"Недостаточно средств для оплаты {sum} {self.currency}.")

    def dispBalance(self):
        print(f"Баланс кошелька '{self.name}': {self.balance} {self.currency}.")

    def delete_account(self):
        del self
        print(f"Кошелек '{self.name}' удален.")

wallName = input("Давай придумаем имя кошельку")
list = ["USD", "EUR", "JPY", "GBR", "AUD", "CAD", "RUB", "CNY"]
x = True
while x:
    wallCur = input("Введи предпочитаемую валюту, используя Буквенный код (Пр: USD, RUB)").upper()
    if wallCur == "UAH":
        print("Возможно, вы имели ввиду RUB, в качестве валюты установлен Российский рубль ")
    if (wallCur in list):
        x = False
wallBal = int(input("Введи начальный баланс"))

my_wallet = Wallet(name=wallName, currency=wallCur, balance=wallBal)
while True:
    print("\nЧто делаем?")
    print("1. Вывести баланс")
    print("2. Пополнить")
    print("3. Траты")
    print("4. Удалить аккаунт")
    operation = input("Введите номер операции (1-4): ")

    if operation not in ['1', '2', '3', '4']:
        print("По-русски же попросил, цифру 1-4 напиши ")
        continue

    if operation == '4':
        print("Удаление...")
        my_wallet.delete_account()
        break

    try:
        if operation == '1':
            print(my_wallet.dispBalance())
        elif operation == '2':
            sum = int(input("Введи сумму пополнения "))
            my_wallet.deposit(sum)
        elif operation == '3':
            sum = int(input("Введи сумму "))
            my_wallet.pay(sum)
    except ValueError as e:
        print(e)

    time.sleep(2)


