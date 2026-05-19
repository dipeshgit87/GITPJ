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
new_student = input("Enter the name of the new student: ")  
if new_student not in class_list:
    class_list.append(new_student)
    print(f"{new_student} has been added to the class list.")
else:
    print(f"{new_student} is already present in the class list.")
print("Updated class list:", class_list)

#4
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
blue_count = votes.count("Blue")
if blue_count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")

#5
grades = {"Ram": 85, "Shyam": 92, "Sita": 78}
student_name = input("Enter the student's name: ")
if student_name in grades:
    print(f"{student_name}'s grade: {grades[student_name]}")
else:
    print("Grade not available.")

#6
'''The candidate knows Python or Java, and has at least 2 years of experience. 
Check if at least one skill in applicant[‘skills’] is in required_skills, and 
experience >= 2. Print priya qualifies  or  priya does not qualify'''
applicant = {"name": "Priya" ,"Skills": ["Java", "SQL"], "experience_years": 1}
required_skills = {"Python", "React"}
common_skills=required_skills.intersection(set(applicant["Skills"]))
print(common_skills)
if common_skills:
    pass
else:
    print("No common skills found")

#7
banned_items = {"scissor", "knife", "lighter"}
items = input("Enter the items in your baggage: ")

if items not in banned_items:
    baggage_weight = int(input("Enter the weight of your baggage in kg: "))
    
    if baggage_weight >7:
        print("Bag not allowed")
    else:
        print("Bag allowed")
else:   
    print("Bag not allowed")


#8
sample_dict ={
    'emp1': {'name': 'John', 'salary':7500 },
    'emp2': {'name': 'Emma', 'salary':8000 },
    'epm3': {'name': 'Shyam', 'salary':500 }
}
for emp in sample_dict.values():
    if emp['name'] == 'Shyam':
        emp['salary'] = 8500
        print("Shyam's salary updated to 8500")
        break  
    print(sample_dict)     

#9
ram_items = {"apple", "banana", "orange"}
laxman_items = {"grape", "melon", "orange"}
common_items = ram_items.intersection(laxman_items)
if common_items:
    print("Ram and Laxman have some common items:", common_items)
else:
    print("Ram and Laxman picked completely different items.")

#10
l = [10, 20, 30]
t = (10, 20, 30)
s = {10, 30}
d = {'b': 20}

val = 20

if val in l and val in t:
    if 'b' in d and val not in s:
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")

#11
data = {'a': 10, 'b': 20, 'a': 30}

print(data) #The second value (30) overwrites the first value (10) for the key 'a'.

#12
[1,2,3] #Dictionary keys must be immutable (cannot change).

#13
d = {'val': 10}

if d.get('score'):
    print('Found')
else:
    print('Not Found') #Output: Not Found, because 'score' is not a key in the dictionary, so d.get('score') returns None, which is treated as False in the if statement.

#14
items = [10, 10, 20]

print(len(set(items))) #Output: 2, because the set will contain only unique elements, so it will have {10, 20}.

#15
my_set.add(40) 

#16
menu = {'Pizza': 15, 'Burger': 10, 'Salad': 8}
order = 'Pizza'

if order in menu:
    print(menu[order])
else:
    print("item not found")

#17
student_data = {"name": "Sam", "score": 85}

if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)

#18
# Dictionary stores username and password
database = {
    "admin": "1234",
    "user": "abcd"
}

# Define user input
user_input = "admin"
user_pass = "1234"

# Check if username exists and password is correct
if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")

#19
# emails list
emails = ['ram123@gmail.com', 'hari77@gmail.com']

# blacklisted emails
blacklisted_emails = {'hari77@gmail.com'}

# email to check
current_email = 'hari77@test.com'

# check conditions
if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")

#20
# inventory items
inventory = {'A1': 50, 'B2': 0, 'C3': 10}

# restricted zones
restricted_zones = {'B2', 'Z9'}

# target item
target = 'B2'

# outer check -> key exists
if target in inventory:

    # inner checks
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")

# key not found
else:
    print("invalid zone")

#21
# valid courses set
valid_courses = {"python", "robotics", "java"}

# high school grades list
hs_grades = [9, 10, 11, 12]

# collect input
name = input("Enter student name: ")
course = input("Enter course: ").lower()
grade = int(input("Enter grade: "))

# store in dictionary
student_records = {
    "name": name,
    "course": course,
    "grade": grade
}

# check course
if course not in valid_courses:
    print(f"{name} selected an invalid course.")

# check grade
elif grade < 9:
    print("grade too low")

elif grade > 12:
    print("grade too high")

# robotics rule
elif course == "robotics" and grade == 9:
    print(f"{name} is not eligible for {course} grade too low")

# approved
else:
    print(f"{name} is approved for {course}")
  


