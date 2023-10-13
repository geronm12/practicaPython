array = [10, 12, 24, 35, 105, 1, 333, 18, 53, 101]
selected_value = 0

while True:
    user_input = input("Please, inser the number that you want to find \n")
    if user_input.isnumeric():
        selected_value = int(user_input)
        break
    else:
        print("You should insert only numbers")


for item in array:
    if item == selected_value:
        print(f"Your number is in the array")



