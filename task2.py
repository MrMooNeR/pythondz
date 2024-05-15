def fibon(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

nn = int(input("Введите количество элементов: "))
for num in fibon(nn):
    print(num)