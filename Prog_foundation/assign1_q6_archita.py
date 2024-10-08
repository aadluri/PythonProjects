#!/usr/bin/env python3
print("Registration Form")
print()

first_name = input("First Name:")

last_name = input("Last Name:")

birth_year = input("Birth Year:")

print("Welcome", first_name , last_name, "!")
print("Your Temporary Password Is", first_name + "*" + birth_year)
