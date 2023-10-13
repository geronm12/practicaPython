array_a = [2, 3, 4, 133, 105]
array_b = [101, 4, 1, 0, 133]
array_c = []

for number in array_a:
    for number_b in array_b:
        if (number == number_b):
            array_c.append(number)


print(array_c)
