def failik(text, filename):
    with open(filename, "a+") as f:
        f.write(text + "\n")
        f.seek(0)
        lines = f.readlines()
    for index, line in enumerate(lines):
        if (index + 1) % 2 == 0:
            print(line, end='')

tt = input("Vvedite text dlya faila")
name = input("Teper nazvanie faila")

failik(tt, name)