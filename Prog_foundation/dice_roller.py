from dice import Dice, Die #importing from library

def main(): #define main function even though there are no other functions
    print("The Dice Roller program") #header
   
    count = int(input("Enter the number of dice to roll: ")) #get number of dice

    dice = Dice()#initialize dice counter
    for i in range(count): #loop through each dice
        die = Die() #make each into a dice accroring to dice list
        dice.addDie(die) #sum up number of die

    while True:        #keep looping while there are dice
        
        dice.rollAll() #roll all dice initilized in previous for loop
        print("YOUR ROLL: ", end="") # print your roll, dont end the line
        for die in dice.list: #loop through dice elements in order to print roll values
            print(die.value, end=" ") # add all roll values to previous print statement
        print("\n") #print empty line

        choice = input("Roll again? (y/n): ") # ask if they want another roll, store which one in choice
        if choice != "y": # if they dont enter 'y' ...
            print("Bye!") #print Bye!
            break #exit loop since choice was not 'y'

# if started as the main module, call the main function

if __name__ == "__main__":
    main()
