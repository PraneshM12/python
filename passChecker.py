password = input("Enter password: ")

has_upper = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
else:
    print("Weak Password")1234