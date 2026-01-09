# 🟠 LEVEL 5: LIST vs TUPLE THINKING

# 2️⃣0️⃣ Convert a tuple into a list
# 2️⃣1️⃣ Convert a list into a tuple
# 2️⃣2️⃣ Count how many times an element appears in a tuple
# 2️⃣3️⃣ Find index of an element in a tuple

list1 = [ 1,2,3,4,5,5,7,6,8,9,4,5,6,1,2,5,4,8,7,5,6,8,4,2,0,5,9,8,]
tup = tuple(list1)
print(type(tup))
print(tup)
list2 = list(tup)

print(type(list2))

print(tup.count(5))

print(tup.index(5))

