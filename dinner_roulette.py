import random
names_string = input("Give me everyone's names")
names = names_string.split(", ")

pay = random.randint(0, len(names)-1)

print(f"{names[pay]} will have to pay.")