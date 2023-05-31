year = int(input("What year would you like to check?"))
leap = False
if year % 4 == 0: #every year that is evevly divided by 4
    if year % 100 == 0: #except every year that is evenly divisible by 100
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False
  
if leap:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")


