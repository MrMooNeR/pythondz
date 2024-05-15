userInput = input("Введите строку")
result = {}

for char in userInput.lower():
    if char != ' ':
        result[char] = userInput.lower().count(char)

print(result)
