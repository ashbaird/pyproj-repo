def prime_checker(number):
    isPrime = True;
    for i in range (2, number):
        if number % i == 0:
            #not a prime
            isPrime = False;
    return isPrime

prime = int(input("Enter a number: "))

result = prime_checker(prime)

if result == True:
    print(f"{prime} is a Prime number.")
else:
    print(f"{prime} is not a Prime number.")    
            
