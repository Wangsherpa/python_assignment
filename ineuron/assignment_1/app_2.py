"""
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
firstname_r = ''
lastname_r = ''

for i in range(1, len(firstname) + 1):
    firstname_r += firstname[-i]

for i in range(1, len(lastname) + 1):
    lastname_r += lastname[-i]

print(firstname_r + ' ' + lastname_r)