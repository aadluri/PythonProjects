#!/usr/bin/env python3
import os

# Shipping Calculator


width = os.get_terminal_size().columns 
print('=' * width)
print("Shipping Calculator")
print('=' * width)
print()

choice = "y"
while choice.lower() == "y":

    #Get item cost, reprompt for input if not positive
    while True:
        item_cost = float(input("Cost of Items Ordered: $ "))
        if  item_cost<0:
            print("You must enter a positive number, Please try agin")
            continue #reprompts for input
        else:
            break # positive numbers are valid and can be used to calculation
    
    # get shipping cost
    if item_cost > 75.00:
            shipping=0
            print("Shipping Cost: FREE")
    if item_cost<75.00 and item_cost>=50.00:
            shipping = 9.95
            print("Shipping Cost: $", shipping)
    if item_cost<50.00 and item_cost>=30.00:
            shipping = 7.95
            print("Shipping Cost: $", shipping)
    if item_cost<30.00 and item_cost>0:
            shipping = 5.95
            print("Shipping Cost: $", shipping)

    #calculate and output total cost
    total_cost=item_cost+shipping
    print(f"Total Cost: $ {total_cost:.2f}")

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print('-' * width)

print("Bye!")

