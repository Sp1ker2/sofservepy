import string

password = str(input("Password : "))
has_digit = False
has_letter = False
has_special = False
dlina = len(password)
for i in password:
    if i.isdigit():
        has_digit = True
    elif i.isalpha():
        has_letter = True
    elif i in string.punctuation:
        has_special = True
    elif 16 < dlina < 6:
        print("Password must be between 16 and 6 characters")

if has_digit and has_letter and has_special:
        print("Password is strong.")
else:
        print("Password must contain at least one letter, one digit, and one special character.")
