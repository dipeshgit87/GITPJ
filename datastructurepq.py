# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list. 
# Define the list   
items = [3, 5, 7, 9, 11, 13]
print("Original list:", items)
# Remove the item at index 4
item = items.pop(4)
# Add the item to the 2nd position
items.insert(1, item)
# Add the item to the end of the list
items.append(item)
print("Modified list:", items)

#Given two sets first_set={23,42,65,57,78,83,29} and second_set={57,83,29,67,73,43,48}, Write a code to identify their intersection. Remove these common elements specifically from the first_set.
# Define the sets
first_set = {23, 42, 65, 57, 78, 83, 29}   
second_set = {57, 83, 29, 67, 73, 43, 48}
# Find the intersection
intersection = first_set.intersection(second_set)
# Remove the common elements from first_set
first_set.difference_update(intersection)
#Print the results
print("Intersection:", intersection)
print("First set after removing common elements:", first_set)

#Write a program to determine if first_set is a subset or superset of second_set. If a relationship is found, delete all elements from the set that is identified as the subset. first_set ={27,43,34} second_set{34,93,22,27,43,53,58}
# Define the sets
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 58}
# Check if first_set is a subset of second_set
if first_set.issubset(second_set):
    print("first_set is a subset of second_set.")
    first_set.clear()  # Remove all elements from first_set
# Check if first_set is a superset of second_set
elif first_set.issuperset(second_set):
    print("first_set is a superset of second_set.")
    second_set.clear()  # Remove all elements from second_set
else:
    print("No subset or superset relationship found.")
# Print the results
print("first_set:", first_set)
print("second_set:", second_set)

#Given a dictionary month containing names and numerical values, write a script to extract all values and store them in a list. Ensure the final list contains no duplicate values. month = {"Jan": 47, "feb": 52, "Mar": 47, "Apr": 44, "May": 52, "Jun": 53, "Jul": 54, "Aug": 44, "Sep": 54,}
# Define the dictionary
month = {"Jan": 47, "feb": 52, "Mar": 47, "Apr": 44, "May": 52, "Jun": 53, "Jul": 54, "Aug": 44, "Sep": 54}
# Extract values and store in a list without duplicates
unique_values = list(set(month.values()))
# Print the final list of unique values
print("Unique values:", unique_values)

#Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number. sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Define the sample list
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Remove duplicates and create a tuple
unique_tuple = tuple(set(sample_list))
# Find the minimum and maximum numbers
min_value = min(unique_tuple)
max_value = max(unique_tuple)
# Print the results
print("Unique tuple:", unique_tuple)
print("Minimum value:", min_value)
print("Maximum value:", max_value)  


# Write a Python program that defines two sets: club_A = {"ram","hari","shyam"} club_B = {"ram","gita","hari"} The program should check whether the two clubs have any members in common. If they do, print the following members exist in both groups and if they have no common members, print no overlapping members found between groups
# Define the sets
club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}
# Check for common members
common_members = club_A.intersection(club_B)
if common_members:
    print("The following members exist in both groups:", common_members)
else:
    print("No overlapping members found between groups.")


#Define required_tasks and completed_tasks. required_tasks = {"Email", "Report", "Meeting"} completed_tasks = {"Email", "Report"} write a code to check if all required tasks are completed by  checking if required_tasks is a subset of completed_tasks. Print all tasks done or some tasks pending accordingly
# Define the sets
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}
# Check if all required tasks are completed
if required_tasks.issubset(completed_tasks):
    print("All tasks done.")
else:
    print("Some tasks pending.")



