_numbers = []
_continue = True
_result = 0

for i in range(5):
    while True:
        user_input_value = input(f"Ingrese el elemento {i + 1} \n")
        if user_input_value.isnumeric():
            _numbers.append(int(user_input_value))
            break
        else:
            print("Por favor ingrese un valor numérico")

for number in _numbers:
    _result += number

print(f"El resultado de la sumatoria de todos los elementos es: {_result}")
