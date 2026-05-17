#Create a dictionary mapping student names to email addresses. Write a program that prompts the user for a name. If the name exists, display the email, otherwise display contact not found. 
students = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}

name = input("Enter a student name: ")
if name in students:
    print(students[name])
else:
    print("Contact not found.")

#Define shopping_list and bought as sets. 
shopping_list = {"Milk", "Bread", "Eggs",}
bought = {"Bread", "Eggs"}
#Use set operations to find out which items are still needed to be bought.
needed = shopping_list - bought
print("Items still needed to be bought:", needed)

#Starting with write a program to add a new_student. 
class_list = ["Alice", "Bob", "Charlie"]
new_student = input("Enter the name of the new student: ")
class_list.append(new_student)
print("Updated class list:", class_list)
