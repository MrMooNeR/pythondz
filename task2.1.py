import random

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]

def vernut(list):
    return random.choices(list, k=2)

print(vernut(list_el))