import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_letters = []
chosen_symbols = []
chosen_numbers = []
for i in range(0, nr_letters):
    i = random.randint(0,len(letters)-1)
    chosen_letters.append(letters[i])

for i in range(0, nr_symbols):
    i = random.randint(0,len(symbols)-1)
    chosen_symbols.append(symbols[i])

for i in range(0, nr_numbers):
    i = random.randint(0,len(numbers)-1)
    chosen_numbers.append(numbers[i])

ordered_pass = chosen_letters + chosen_numbers + chosen_symbols
print(f"Ordered Password: {ordered_pass}")
random.shuffle(ordered_pass)
print(f"Randomized Password: {ordered_pass}")