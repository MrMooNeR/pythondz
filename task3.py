dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys = set()
values = set()

for key, value in dct.items():
    keys.add(key)
    values.add(value)

result = keys | values
print(result)
