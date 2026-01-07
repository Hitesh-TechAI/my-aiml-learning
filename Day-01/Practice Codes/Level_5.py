# 1️⃣5️⃣ Take your name and age as input and print a sentence like:

# > Hello Hitesh, you are 18 years old.



# 1️⃣6️⃣ Take marks of 3 subjects and print their total
# 1️⃣7️⃣ Take price of an item and quantity, print total cost
# 1️⃣8️⃣ Take year of birth and print current age
# (Assume current year manually)

#15
name1 = input("Enter Your Name :")
name2=","
name = name1 + name2
age = int(input("Enter Your Age :"))
print("Hello" , name , "you are" , age , "years old.")

#16

eng = int(input("Enter marks of English :"))
maths = int(input("Enter marks of Maths:"))
sci = int(input("Enter marks of Science :"))
total = eng + maths + sci
print("Total marks =" , total)

# 17

price_of_product = int(input("Enter Price of Product :"))
quantity = int(input("Enter Quantity :"))
total_cost = price_of_product * quantity
print("Total cost is :" , total_cost)

# 18 
birth_year = int(input("Enter Birth Year :"))
age = 2026 - birth_year
print("Your age is :", age)