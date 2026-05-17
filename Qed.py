# 1

num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print(f"{num} is between 1 and 100.")
else:
    print(f"{num} is NOT between 1 and 100.")



# 2


num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
 
 

# 3


num=int(input("enter number between 1-12"))
if num==1:
    print("January")
elif num==2:
    print("February")  
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("august")
elif num==8:
    print("september")
elif num==8:
    print("october")
elif num==8:
    print("november")
elif num==8:
    print("december")
else:
    print("invalid")
 
 

# 4

marks = float(input("Enter marks: "))
if marks < 25:
   grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks <= 80:
    grade = "B"
else:
    grade = "A"
print(f"Grade: {grade}")
 
 

# 5
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is divisible by 7.")
else:
    print(f"{num} is NOT divisible by 7.")
 
 

# 6


a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
op = input("Enter operator (+, -, *, /): ")
 
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print(f"Your Answer is: {result}")
 
 

# 7


salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")
 
 

# 8

n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)
 
 

# 9


char = input("Enter a character: ").lower()
if len(char) == 1 and char.isalpha():
    if char in "aeiou":
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")
else:
    print("Please enter a single alphabetic character.")
 
 

# 10


marks = float(input("Enter marks (0–100): "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
else:
    print("Grade: Fail")
 
 

# 11

print("=" * 50)
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")
 
 

# 12


char = input("Enter a character: ")
if len(char) == 1:
    if char.isupper():
        print(f"'{char}' is Uppercase.")
    elif char.islower():
        print(f"'{char}' is Lowercase.")
    elif char.isdigit():
        print(f"'{char}' is a Digit.")
    else:
        print(f"'{char}' is a special character.")
else:
    print("Please enter a single character.")
 
 

# 13


color = input("Enter color (Red / Yellow / Green): ").strip().capitalize()
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Get Ready")
elif color == "Green":
    print("Go")
else:
    print("Invalid color entered.")
 
 

# 14


age = int(input("Enter your age: "))
experience = int(input("Enter years of experience: "))
if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")
 
 

# 15

temp = float(input("Enter temperature (°C): "))
if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")
 
 

# 16

item = input("Enter menu item (Pizza / Burger / Pasta): ").strip().capitalize()
if item == "Pizza":
    print("Price: $10")
elif item == "Burger":
    print("Price: $7")
elif item == "Pasta":
    print("Price: $8")
else:
    print("Item not found in menu.")
 
 

# 17

height = float(input("Enter height in feet: "))
if height >= 6:
    print("Selected")
else:
    print("Not Selected")
 
 

# 18


age = int(input("Enter your age: "))
if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")
 
 

# 19

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")
 
 

# 20


month = int(input("Enter month number (1–12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number. Please enter a value between 1 and 12.")
 