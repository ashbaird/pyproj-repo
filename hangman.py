import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list)-1)]
length = len(chosen_word)
guess = input("Guess a letter").lower()
word = list(chosen_word)
print(f"{chosen_word}")

for i in range(0, len(chosen_word)):
    if guess == word[i]:
        print(f"{i}: Correct")
    else:
        print(f"{i}: Wrong")    



