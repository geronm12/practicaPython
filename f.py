array = [10, 12, 24, 35, 105]
selected_value = 0

while True:
    user_input = input("Please, inser the number that you want to multiply \n")
    if user_input.isnumeric():
        selected_value = int(user_input)
        break
    else:
        print("You should insert only numbers")


for item in array:
    print(f"The result is: {selected_value * item}")

