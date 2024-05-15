num = int(input("Введите число: "))

negSum = 0
posSum = 0

for number in range(-num, num + 1):
    print(number)
    if number < 0:
        negSum += number
    elif number > 0:
        posSum += number

print("Сумма -чисел:", negSum)
print("Сумма +чисел:", posSum)