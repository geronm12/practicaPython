values = []
counter = 0

while counter < 5:
    while True:
        value = input("Please, insert a numeric value \n")
        try:
            value_decimal = int(value)
            values.append(value_decimal)
            break
        except ValueError:
            print("The value provided is not numeric.")

    counter += 1

default_element = values[0]
ordered_array = []

for value in values:
    if (len(ordered_array) <= 0):
        ordered_array.append(value)
    else:
        if value >= ordered_array[len(ordered_array) - 1]:
            ordered_array.append(value)
        elif value <= ordered_array[0]:
            ordered_array.insert(0, value)
        else:
            if value >= ordered_array[0] and \
               value <= ordered_array[1]:
                ordered_array.insert(1, value)
            elif value <= ordered_array[len(ordered_array) - 1] and \
                 value >= ordered_array[len(ordered_array) - 2]:
                ordered_array.insert(len(ordered_array) - 1, value)


print(ordered_array)
