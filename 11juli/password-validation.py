import re
print("Account Registration")
print("====================")

firstname = str(input("Your first name :\n"))
lastname = str(input("Your last name:\n"))
email = str(input("Your active email:\n"))
password = str(input("Your password:\n"))


# while password doesn't contain any of rules
while not re.fullmatch(r"[A-Za-z0-9]{8,}", password):
    print("Your password must be:")
    print("At least 8 charcater")
    print("At least has one uppercase letter")
    print("At least has one lowercase letter")
    password = str(input("Your password must be:\n"))
else:
    print("Welcome to the social media")
    print("Your name is", f"{firstname} {lastname}")
