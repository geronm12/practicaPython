

square = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]

row = ""

for number in square:
    for element in number:
        row += f"{element}"

    row += '\n'

print(row)


piramyd = [[0, 0, 1, 0, 0],
           [0, 1, 1, 1, 0],
           [1, 1, 1, 1, 1]]

row_b = ""

for number in piramyd:
    for element in number:
        if element == 0:
            row_b += ' '
        else:
            row_b += f"{element}"
    print(row_b)
    row_b = ""
