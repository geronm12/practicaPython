array = [1, 131, 22, 48, -5, -44, 1, 48, 22, 22]
array_dicionary = {}

for element in array:
    if str(element) in array_dicionary:
        array_dicionary[str(element)] += 1
    else:
        array_dicionary[str(element)] = 1



print(array_dicionary)