from typing import List

def mnozhElements(inputList: List[int], multiplier: int = 2) -> List[int]:
    return [x * multiplier for x in inputList]

n = int(input("Введите количество элементов в списке: "))

numbersList = []

for i in range(n):
    element = input(f"Введите элемент {i + 1}: ")
    try:
        numbersList.append(int(element))
    except ValueError:
        numbersList.append(element)

multLambada = lambda lst, mult=2: [x * mult for x in lst]

a = input("Введите множитель (или '-' если не хотите):")
if a == "-":
    new_list = mnozhElements(numbersList)
    lambda_list = multLambada(numbersList)
if a != "-":
    new_list = mnozhElements(numbersList, int(a))
    lambda_list = multLambada(numbersList, int(a))

print(new_list)
print(multLambada)