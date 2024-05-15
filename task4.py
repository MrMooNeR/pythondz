
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"

shipLower = ship.lower()

shot = input("Куда стреляем? (например, А1): ").lower()

if shipLower.find(shot) != -1:
    print("Попадание!")
else:
    print("Промах!")



userName = input("Введите имя: ")
userSurname = input("Введите фамилию: ")
age = input("Введите возраст: ")

print("Ваше имя: {name}, Фамилия: {sur}, Возраст: {0} лет.".format(age, name=userName, sur=userSurname))
