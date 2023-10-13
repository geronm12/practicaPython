str_array = ['hello', 'how are you',
             'do you want some icecream?',
             'i love it', 'programming is fun']
last_word = str_array[0]

for element in str_array:
    if len(element) >= len(last_word):
        last_word = element
print(f"The longest word is: {last_word}")
