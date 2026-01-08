# 🔵 LEVEL 7: NESTED IF (THINKING TEST)

# 2️⃣1️⃣ Take username and password:

# If username is "admin":

# If password is "1234" → print Login successful

# Else → print Wrong password


# Else → print Invalid user

user_name = input("Enter username :")

if(user_name == "admin"):
    password = input("Enter your Password :")
    if(password == "1234"):
        print("Login successfull")
    else:
        print("Wrong password.")
else:
    print("Login Restricted")
