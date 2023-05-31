#print("Welcome to the tip calculator.")
str_total = input("What was the total bill? $")
str_percent = input("What percentage tip would you like to give? 10, 15, or 20?")
str_people = input("How many people to split the bill?")

total = float(str_total)
percent = float(str_percent) / 100 + 1
people = int(str_people)
total_plus_tip = total * percent
total_divided = total_plus_tip / people
round_total = round(total_divided, 2)

print(f"Each person should pay: {round_total}")

