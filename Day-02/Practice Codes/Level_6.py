# 🔵 LEVEL 6: CONDITIONALS + STRING LOGIC

# 1️⃣9️⃣ Take a string and check:

# If it contains "python" → print Python Found

# Else → print Python Not Found

# 2️⃣0️⃣ Take a string:

# If it starts with "H" → print Starts with H

# Else → print Does not start with H


str1 = input("Enter the string :")
a = str1.find("python")

if(a != -1):
    print("Python found.")
else:
    print("Python not found.")

str2 = input("Enter string :")
a = str2[0]

if(a == "H"):
    print("Starts with H")
else:
    print("Does not start with H")