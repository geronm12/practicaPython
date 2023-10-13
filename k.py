
text = input("Please, provide a text\n")
dictionary = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}


for letter in text:
    if letter in dictionary:
        dictionary[letter] += 1


print(dictionary)
