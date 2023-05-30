height = input("Enter your height: ")
weight = input("Enter your weight: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print("Your BMI is: " + str(bmi_as_int))
