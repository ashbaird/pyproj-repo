unfinished = True
info = []
winningBid = {}

while unfinished:
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))
    dicto = {"Name" : name, "Bid": bid}
    info.append(dicto)
    another = input("Are there any other users that would like to bid? 'y' or 'n' ")
    if another == "y":
        continue
    else:
        unfinished = False

def highestBid():
    y = 0
    for dicto in info:
        x = dicto["Bid"]
        if x > y:
            y = dicto["Bid"]
            name = dicto["Name"]
    winningBid = {"Name": name, "Bid": y}
    return winningBid      

result = highestBid()
print(f"The winner is {result['Name']} with a bid of {result['Bid']}")

