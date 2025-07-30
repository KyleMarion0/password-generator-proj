#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to My Password Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Choose random letters, numbers, and symbols from above lists

ran_str = ""

for let in letters:
    if nr_letters > 0:
      ran_str += random.choice(letters)
      nr_letters -= 1

for num in numbers:
    if nr_numbers > 0:
      ran_str += random.choice(numbers)
      nr_numbers -= 1

for symb in symbols:
    if nr_symbols > 0:
      ran_str += random.choice(symbols)
      nr_symbols -= 1

# Shuffle the characters and return them as a string

ran_pass_list = random.sample(ran_str, len(ran_str))
ran_pass_str = ''.join(ran_pass_list)
print(f"Your password is: {ran_pass_str}")
