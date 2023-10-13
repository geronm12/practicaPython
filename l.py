array = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


for number in array:
    if number != 2 and number != 3:
        if number % 2 == 0 or \
           number % 3 == 0:
            continue
        else:
            print(f"{number} is Prime")
    else: 
        print(f"{number} is Prime")