print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?")
str_add_pepperoni = input("Do you want pepperoni? Y or N?")
str_extra_cheese = input("Do you want extra cheese? Y or N?")
bill = 0
add_pep = False
extra_cheese = False

if str_extra_cheese == "Y":
    bill+=1
if size == "S":
    bill += 15
    if str_add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if str_add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if str_add_pepperoni == "Y":
        bill += 3
else:
    print("Invalid option")

print(f"Your final bill is: ${bill}")