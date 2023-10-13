array = [1, 2, 3, 4, 5]

array.insert(0, array[len(array) - 1])

array = array[:-1]

print(array)
