# 🟡 LEVEL 4: SORTING & MUTABILITY

# 1️⃣6️⃣ Sort a list in ascending order
# 1️⃣7️⃣ Sort the same list in descending order
# 1️⃣8️⃣ Show that list is mutable by changing one element using index
# 1️⃣9️⃣ Try changing a tuple element and observe the error (DON’T fix it)

list1 = [ 6 , 5 , 8 , 6 , 5 , 7 , 9 , 8 , 2 , 0 , 1 , 3]
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)
list1[5] = "Hitesh"
print(list1)