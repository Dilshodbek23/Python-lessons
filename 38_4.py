# Python Standard Libraries

# The user was asked to enter a phone number. The entered value was checked against the template.

import re

regex = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
phone = input("Please enter phone number: ")
if re.match(regex, phone):
    print(f"phone: {phone}")
else:
    print(f"phone number is incorrecr")
