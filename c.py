fishes = []

while True:
    fish = input("Insert fish weigth\n")
    try:
        decimal_fish = float(fish)
        fishes.append(decimal_fish)
    except ValueError:
        print("The value inserted must be decimal value")

    if len(fishes) > 5:
        question = input("do you want to continue? y/n\n")
        if (question.lower() == "n"):
            break

fishes.sort(reverse=True)


print(fishes[0])
print(fishes[1])
print(fishes[2])
