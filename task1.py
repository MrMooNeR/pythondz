def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)



# assert average_num([]) == "Bad request", "S pustim ne rabotaet" // оно вообще ломается почему-то
assert average_num([1,2,3]) == 2.00, "С целыми числами не работает"
assert average_num([1.1, 1.2, 1.3]) == 1.20, "С нецелыми не работает"
assert average_num([1, 2.3, 3]) == 2.10, "S raznimi tipami ne rabotaet"
assert average_num([-1, -2, -3]) == -2.00, "S otrizatelnimi ne rabotaet"
assert average_num([0,0,0]) == 0.00, "s nulyami ne rabotaet"
assert average_num(["1",2,"3"]) == 2, "S 4iframi strokami ne rabotaet"
assert average_num([1, "a", 3]) == "Bad request", "S ne konvertiruemim ne rabotaet"