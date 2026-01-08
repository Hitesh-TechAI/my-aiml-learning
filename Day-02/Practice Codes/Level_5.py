#  LEVEL 5: CONDITIONAL STATEMENTS (STRINGS)

# 1️⃣7️⃣ Take a name and check:

# If name is "admin" → print Welcome Admin

# Else → print Welcome User


# 1️⃣8️⃣ Take a string and check:

# If length > 10 → print Long string

# Else → print Short stri

name = input("Enter your name : (lowercase) \n: ")

if(name == "admin"):
    print("Welcome Admin.")
else:
    print("Welcome User.")

string = input("Enter string :")
a = len(string)

if( a > 10 ):
    print("Long string.")
else:
    print("Short string.")