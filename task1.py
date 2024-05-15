n = int(input("Введите количество элементов в списке: "))

numbersList = []

for i in range(n):
    element = input(f"Введите элемент {i + 1}: ")
    try:
        numbersList.append(int(element))
    except ValueError:
        numbersList.append(element)

power = int(input("Введите степень: "))

resultList = []

for item in numbersList:
    if isinstance(item, float) or isinstance(item, int):
        resultList.append(item ** power)
    elif isinstance(item, str):
        resultList.append(item * power)

print(resultList)
