#!/usr/bin/env python3

# Letter Grade Converter
print("Letter Grade Converter")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    num_grade = int(input("Enter Numerical Grade:"))

    #define lower grade boundaries - can be changed 
    agrade = 88
    bgrade = 80
    cgrade = 67
    dgrade = 60

    if num_grade>100:
        letter_grade = "Invalid, choose number between 0 and 100"
    if num_grade>=agrade and num_grade<=100:
        letter_grade = "A"    
    if num_grade<agrade and num_grade>=bgrade:
        letter_grade = "B"
    if num_grade<bgrade and num_grade>=cgrade:
        letter_grade = "C"
    if num_grade<cgrade and num_grade>=dgrade:
        letter_grade = "D"
    if num_grade<dgrade:
        letter_grade = "F"
   

    print("Letter Grade:" + letter_grade)

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")

