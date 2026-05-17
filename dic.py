# student_marks={'ram':93,'shyam':98,'hari':88}
# result=student_marks.get('hira','students not found')
# print(result)

# student_marks={'ram':93,'shyam':98,'hari':88} #to add new record in dictionary
# student_marks['sita']=75 
# #Or student_marks.update({'sita':88,'laxman':73})
# print(student_marks)

# # Initial dictionary
# student_marks = {"Ram": 75, "Sita": 90}

# # Updating Ram's marks from 75 to 85
# student_marks["Ram"] = 85

# print(student_marks)
# # Output: {'Ram': 85, 'Sita': 90}


# student_marks = {"Ram": 85, "Sita": 90, "Arjun": 70}

# # Remove the entry for "Arjun"
# del student_marks["Arjun"]

# print(student_marks)
# # Output: {'Ram': 85, 'Sita': 90}

# student_marks = {"Ram": 85, "Sita": 90}
# student_marks.clear()

# print(student_marks)
# # Output: {}


# student_marks={'ram':93,'shyam':98,'hari':88}

# for i in student_marks:
#     print(i)
# for i in student_marks.keys():
#     print(i)
# for i in student_marks.values():
#     print(i)
# for i in student_marks.items():
#     print(i)
# for i,j in student_marks.items():
#     print(i,'       ',j)


# student={
#     'ram':{'math':85,'science':90},
#     'shyam':{'math':92,'science':88},
#     'sita':{'math':78,'science':82}
# }
# print(student['ram']['science'])
# # print(student['ram']['0'])

# #write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.   
# items = [3, 5, 7, 9, 11, 13]        
# # Remove the item at index 4 (which is 11)
# item = items.pop(4)  # This will remove the item at index 4 and return it                       
# # Add the removed item to the 2nd position (index 1)            
# items.insert(1, item)  # This will insert the item at index 1
# # Add the removed item to the end of the list           
# items.append(item)  # This will add the item to the end of the list
# print(items)  # Output: [3, 11, 5, 7, 9, 13, 11] 

                                   
# first_set= {23,42,65,57,78,83,29}   
# second_set= {57,83,29,67,73,43,48}  

# # Find the intersection of the two sets     
# intersection = first_set.intersection(second_set)

# # Remove the common elements from the first set
# first_set.difference_update(intersection)

# # Add the common elements to the second set
# second_set.update(intersection)

# # Print both sets
# print("First Set after removing common elements:", first_set)
# print("Second Set after adding common elements:", second_set)

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

#Find the intersection of the two sets
intersection = first_set.intersection(second_set)

#Check if there are common elements
if intersection:
    # Remove the common elements from the first set
    first_set.difference_update(intersection)

    # Add the common elements to the second set
    second_set.update(intersection)

    print("Common elements found:", intersection)
else:
    print("No common elements found")

# Print both sets
print("First Set after removing common elements:", first_set)
print("Second Set after adding common elements:", second_set)
print(f"second set (unchanged): {second_set}")


first_set = {27,43,34}
second_set={34,93,22,27,43,53,48}
if first_set.issubset(second_set):
    print("First set is a subset of the second set.")
    first_set.clear()  # Clear all elements from the first set  
elif first_set.issuperset(second_set):
    print("First set is a superset of the second set.")
    second_set.clear()  # Clear all elements from the second set
else:
    print("No subset or superset relationship found.")




