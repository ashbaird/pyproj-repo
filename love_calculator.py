print("Welcome to the Love Calculator <3!")
uc_name1 = input("What is your name?")
name1 = uc_name1.lower()
uc_name2 = input("What is their name?")
name2 = uc_name2.lower()

t_occurance = name1.count("t") + name2.count("t")
r_occurance = name1.count("r") + name2.count("r")
u_occurance = name1.count("u") + name2.count("u")
e_occurance = name1.count("e") + name2.count("e")

l_occurance = name1.count("l") + name2.count("l")
o_occurance = name1.count("o") + name2.count("o")
v_occurance = name1.count("v") + name2.count("v")

first_digit = t_occurance + r_occurance + u_occurance + e_occurance
second_digit = l_occurance + o_occurance + v_occurance + e_occurance
love_score = str(first_digit) + str(second_digit)
print(f"{love_score}")
