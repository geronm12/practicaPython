
counter = 0
previous_number = 1

while counter <= 233:
    print(counter)
    if counter == 1:
        print(counter)
        previous_number = 1
        counter += 1
    else:
        counterX = counter
        counter += previous_number
        previous_number = counterX
