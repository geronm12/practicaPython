number = 2301
counter = 0
result = []

while number > 1000:
    counter += 1000
    number -= 1000

if counter > 0:
    result.append(counter)

counter = 0

while number > 100:
    counter += 100
    number -= 100

if counter > 0:
    result.append(counter)

counter = 0

while number >= 10:
    counter += 10
    number -= 10

if counter > 0:
    result.append(counter)

counter = 0

while number > 0:
    counter += 1
    number -= 1

if counter > 0:
    result.append(counter)


print(result)
