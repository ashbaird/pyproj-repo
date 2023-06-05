import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user = input("Rock, paper, or scissors?")


if user == "rock":
    uindex = 0
elif user == "paper":
    uindex = 1
else:
    uindex = 2        

comp = random.randint(0, 2)

if uindex == comp:
    result = "Tie."
elif uindex == 0:
    if comp == 1:
        result = "You lose."
    else: 
         result = "You win!"
elif uindex == 1:
    if comp == 0:
        result = "You win!"
    else:
        result = "You lose"
else:
    if comp == 0:
        result = "You lose."
    else:
        result = "You win!"                         


print(f"You: {choices[uindex]}")
print(f"Computer chose: {choices[comp]}")
print(result)


