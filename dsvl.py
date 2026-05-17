#1
students = {
    "Anthony": "anthony@example.com",
    "Ronaldo": "ronaldo@example.com",
    "Dembele": "dembele@example.com"
}

name = input("Enter a student name: ")
if name in students:
    print(students[name])
else:
    print("Contact not found.")

#2
shopping_list = {"Milk", "Bread", "Eggs",}
bought = {"Bread", "Eggs"}
#Use set operations to find out which items are still needed to be bought.
needed = shopping_list - bought
print("Items still needed to be bought:", needed)

#3
class_list = ["ram", "sita", "laxman"]
new_student = input("Enter the name of the new student:")
class_list.append(new_student)
print("Updated class list:", class_list)
