cart=['apple','orange']
cart.append('orange')
cart.extend('orange')
print(cart)
cart.insert(0,'cocacola')
print(cart)

cart=['apple','orange']
a=cart.pop()
print(a)

cart=['apple','orange']
cart.pop()
print(cart)

cart=['apple','orange'] #list bata kunai item directly remove garne tarika
cart.remove('apple')
print(cart)

cart=['apple','orange'] #list ma modify garne tarika
cart[0]='cocacola'
print(cart)

cart=['apple','orange'] #clear method list ma vako sab item lai clear garxa
cart.clear()
print(cart)

cart=[1,2,3,4,5,6] #max use garda maximum value return garxa same for min
print(max(cart))

cart=1,2,3,4,5

s = str(cart)  

s = s.replace('1', '', 1)  # only remove 1 occurrence
print(s)  # '2345'

cart = 1, 2, 3, 4, 5  # this is a tuple
cart1 = list(cart)     # convert tuple to list to allow modification
cart1.pop(0)           # remove the first element
cart1 = tuple(cart1)   # convert back to tuple
print(cart1)           # print the new tuple

empty_set = set()
print(empty_set)         # set()
print(type(empty_set))   # <class 'set'>

items={1,2,3,4,4,5}
items.remove(4)
items.discard(4)
print((items))

items={1,2,3,4,4,5}
items.clear()
print(items)

items={1,2,3,'ram','shyam',4,5}
print(items)
items.pop() #use garxa first indexing ma vako item lai delete garxa randomy shuffle garda
print(items)

# items={1,2,3,'ram','shyam',4,5}
# items2={9,8,10,'ram','shyam',4,5}
# items3=items.difference(items2)
# items4=items.symmetric_difference(items2)
# items4=items.union(items2)
# items4=items.intersection(items2)
# items3=items.isdisjoint(items2)
# items4=items.issuperset(items2)
# items5=items.issubset(items2)
# print(items3)
# print(items4)
# print(items5)

# 1. Define a dictionary of users
users = {
    "user123": "Alice Smith",
    "user456": "Bob Jones",
    "user789": "Charlie Brown"
}

# 2. Get input from the user
search_id = input("Enter the User ID: ")

# 3. Use the .get() method
# If search_id exists, it returns the value. 
# If not, it returns "User not found".
result = users.get(search_id, "User not found")

# 4. Print the result
print(result)



