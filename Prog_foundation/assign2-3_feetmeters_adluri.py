#!/usr/bin/env python3

def feet_to_meters(feet):
     f2m=feet*0.3048
     return (f2m)

def meters_to_feet(meters):
     m2f = meters/0.3048
     return (m2f)

def header_print():
    print("Conversions Menu:")
    print("a. Feet to meters")
    print("b. meters to feet")
    return()


def main():
    choice = "y"
    while choice.lower() == "y":
        header_print()
        # get input from the user
        which_convert = (input("Select and Conversion (a/b): "))
        
        # Assignment said assume valid input but I didnt read that until after I figured this out
        while True:
            which_convert = (input("Select and Conversion (a/b): "))
            if  which_convert == "a":
                break
            if which_convert == "b":
                break
            else:
                print("Select a or b")
                continue 
    

        if which_convert == "a":
            feet = float(input("Enter feet: "))
            answer=feet_to_meters(feet)
            print(f"{answer:.2f}  meters")
        if which_convert == "b":
             meters = float(input("Enter meters: "))
             answer = meters_to_feet(meters)
             print(f"{answer:.2f}  feet")

        choice = input("Continue? (y/n): ")
        print()
    print("Thanks, Bye!")

if __name__ == "__main__":  # if main module
        main()