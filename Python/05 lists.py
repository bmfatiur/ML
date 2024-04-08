print("===================")

items = ["bread", "pasta", "fruits"]
print( items )

# append = add item at end
items.append("milk")
print( items )

# insert = add item at specific index; index starts from 0
items.insert(1,"cake")
print( items )

print("===================")

# read from 0 to 1
print(items[0:2])
# or
print(items[:2])

print("===================")

# index = -1 means the last item in list
print( items[-1] )

print("===================")

# length of th list
print( len(items) )

print("===================")

# concatenation
food=["apple", "rice", "chili"]
toiletries = ["paste", "shampoo", "soap", "face wash"]

print(food+toiletries)

print("===================")

# check item from list
answer="bread" in items
print(answer)

answer="honey" in items
print(answer)

print("===================")