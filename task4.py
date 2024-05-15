def decor(ff):
    def wrap(n):
        print(f"Имя функции - {ff.__name__} с аргументом ({n})")
        return(ff(n))
    return(wrap)

@decor
def fibon(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

nn = int(input("Введите количество элементов: "))
for num in fibon(nn):
    print(num)

     # print(fibon(int(input("Введите кол-во элементов"))))
     #Выводит вот это - <generator object fibon at 0x0000028BD4B4FCA0>