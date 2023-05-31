float_age = input("WHat is your current age?")
age = int(float_age)
time_left = 90 - age
days = time_left * 365
weeks = time_left * 52
months = time_left * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")