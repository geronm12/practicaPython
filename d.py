elements = [1, 115, 231, 124, 18, 33, 45, 15, 21, 90, 44]


for element in elements:
    result = element
    while result >= 1:
        result -= 2

    if result < 0:
        print(f"{element} es Impar")
    else:
        print(f"{element} es Par")
    

