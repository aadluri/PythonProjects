#!/usr/bin/env python3

from pprint import pprint

choices=['list','view','add','del','exit'] #all potential choices, available to all functions
contacts=[['Eric Idle','eric@ericidle.com','+44 20 7946 0958'],['Scott Young','scott@fakeemail.com','709-123-4567']]
'''
Contact list format should be
Full Name,  Email, Phone
'''

def menu_print():
    print('COMMAND MENU')
    print('list - Display All Contacts ')    
    print('view - View A Contact')
    print('add - Add A Contact')
    print('Del - Delete A Contact')    
    print('exit - Exit Program')


def make_choice():
    flag = True
    while flag == True:
        choice=str(input("Command: \t"))
        if choice.lower() in choices:
             flag==False
             break
        elif choice.lower() not in choices:
             print("please choose a valid option")
    #return the lower case choice to make case-insensitive
    return(choice.lower())

def list_func():
    '''List Names only with as index-numbered list'''
    print('working on list_func')
    i=0
    # add names to temp list names
    for i in range(0,len(contacts)):
        print(f'{i+1}. {contacts[i][0]}')
        i+=1
    
    return()

def view_func():
    '''view a specific conatct given it position on the list'''
    while True:
        num=int(input("Number: \t"))
        num-=1 # list starts at 1, index starts at zero
        if num not in range(0,len(contacts)):
            print(f"Not in Range, try a number between 1 and ", len(contacts))
        else:
            print("Email: ", contacts[num][1])
            print("Phone: ", contacts[num][2])
            break
    return()        


def add_func():
    '''add a contact, must add name, email and phone'''
    new_contact=[]
    print("Add New Contact:")
    name=input("Enter Name: \t")
    new_contact.append(name)
    email=input("Enter Email: \t")
    new_contact.append(email)
    phone=input("enter Phone Number: \t")
    new_contact.append(phone)

    contacts.append(new_contact)
    print(name, "was added.")
    return(contacts)

def del_func():

    while True:
        num=int(input("Number: \t"))
        num-=1 # list starts at 1, index starts at zero
        if num not in range(0,len(contacts)):
            print(f"Not in Range, try a number between 1 and ", len(contacts))
        else:
            name=contacts[num][0]
            contacts.pop(num)
            print(name, 'was deleted')
            break
    return(contacts)        

    

def main():
    print("Contact Manager")

    menu_print()
    
    # create working copy of list while program is running
    # any changes are deleted when program closes
    # Can easily read/write the working list to a file instead of using the initial list

    while True:
        choice = make_choice() 
        if choice == 'view':
            view_func()
        elif choice == 'list':
            list_func()
        elif choice == 'add':
            add_func()
        elif choice == 'del':
            del_func()
        elif choice == 'exit':
            break
    
    print('Bye!')
        


if __name__ == "__main__":  # if main module
        main()