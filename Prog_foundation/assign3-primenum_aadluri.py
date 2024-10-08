#!/usr/bin/env python3

def get_valid_guess():
    
    while True:
        guess = int(input("Please enter and integer between 1 and 5000: \t"))
        if guess<1:
            print("Invalid Number")
        if guess >5000:
            print("Invalid Number")
        elif guess>1 and guess<5000:
            print()
            break
    return(guess)


def isit_prime(guess):
    flag=True
    if guess==1:
        flag=False
    else:
        for i in range(2,guess):
            if (guess % i==0):  
                flag=False
    return(flag)
    

def prime_factor(guess):
    primeFactors = [] #list of factors includes 1 and itself for prime numbers
    for i in range(1, guess+1):
        if guess % i == 0:
            primeFactors.append(i)
            
    
    print('It has', len(primeFactors), 'factors:', *primeFactors)
    print()

    #print('It has {} factors:{}'.format(len(primeFactors) primeFactors))

    return primeFactors

def main():
    print(' Prime Number Checker \n')
    choice = "y"
    while choice.lower() == "y":
   
        guess  = get_valid_guess()
        isprime=isit_prime(guess)

        if isprime == True:
            print(guess,"IS a prime number")
            print()

        elif isprime == False:
           print(guess,"IS NOT a prime number")
           prime_factor(guess)
        else:
            print('Error, Please Try Again') #just in case
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
    
if __name__ == "__main__":
    main()