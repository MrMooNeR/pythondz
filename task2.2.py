import re
import calendar
import time

def calen(date):
    dateType = r"^\d{4}-(0[1-9]|1[0-2])$" # без помощи не обошлось

    if re.match(dateType, date):
        year, month = map(int, date.split('-'))
        cal = calendar.month(year, month)
        print(cal)
    else:
        print("Неверный формат")

phoneType = r"^\+?7|7|8? ?\(?[3489][0-9]{2}\)? ?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$" # помогите это прочесть

cal = input("Вводи дату в формате 'ГГГГ-ММ': ")
nomer = input("Вводи номер телефона")

calen(cal)
time.sleep(2)

if re.match(phoneType, nomer):
    print(f"Nomer {nomer} correct")
else:
    print(f"Nomer {nomer} uncorrect")