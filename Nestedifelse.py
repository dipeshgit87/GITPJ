# -------- 1. Theme Park Ride Eligibility --------
print("\n--- Theme Park Ride Eligibility ---")
valid = True

age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))

if age < 0 or height < 0:
    print("Invalid input")
    valid = False

if valid:
    if age >= 12 and height >= 140:
        print("You can ride the roller coaster.")
    else:
        print("You cannot ride the roller coaster.")

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 2. Traffic Light System --------
print("\n--- Traffic Light System ---")
valid = True

light = input("Enter light color: ").lower()

if light not in ["red", "yellow", "green"]:
    print("Invalid color")
    valid = False

if valid:
    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Get Ready")
    else:
        print("Go")

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 3. Match Statement (Seasons) --------
print("\n--- Season Finder ---")
valid = True

num = int(input("Enter a number (1-4): "))

if num not in [1, 2, 3, 4]:
    print("Invalid number")
    valid = False

if valid:
    match num:
        case 1:
            print("Spring")
        case 2:
            print("Summer")
        case 3:
            print("Autumn")
        case 4:
            print("Winter")

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 4. Login System --------
print("\n--- Login System ---")
valid = True

username = input("Enter username: ")
password = input("Enter password: ")

if username != "admin":
    print("Wrong username")
    valid = False
elif password != "pass123":
    print("Wrong password")
    valid = False

if valid:
    print("Login successful")

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 5. Bank Loan Approval --------
print("\n--- Bank Loan Approval ---")
valid = True

age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if age < 21 or age > 60:
    print("Age condition failed")
    valid = False
elif income < 30000:
    print("Income condition failed")
    valid = False
elif credit_score < 700:
    print("Credit score condition failed")
    valid = False

if valid:
    print("Loan approved")

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 6. Movie Ticket Booking --------
print("\n--- Movie Ticket Booking ---")
valid = True

age = int(input("Enter age: "))
membership = input("Do you have membership? (yes/no): ").lower()

if age < 0 or membership not in ["yes", "no"]:
    print("Invalid input")
    valid = False

if valid:
    if age < 12:
        price = 0
    elif age <= 60:
        price = 150 if membership == "yes" else 200
    else:
        price = 100

    print("Ticket price: Rs.", price)

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 7. Employee Bonus --------
print("\n--- Employee Bonus ---")
valid = True

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if salary < 0 or years < 0:
    print("Invalid input")
    valid = False

if valid:
    if years > 5:
        bonus = salary * 0.05
    else:
        bonus = 0

    print("Bonus amount:", bonus)

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 8. Area of Circle --------
print("\n--- Area of Circle ---")
valid = True

radius = float(input("Enter radius: "))

if radius < 0:
    print("Invalid radius")
    valid = False

if valid:
    area = 3.1416 * radius * radius
    print("Area of circle:", area)

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")


# -------- 9. Wages Calculation --------
print("\n--- Wages Calculation ---")
valid = True

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of working days: "))

if age < 18 or age > 40:
    print("Invalid age")
    valid = False

if gender not in ['M', 'F']:
    print("Invalid gender")
    valid = False

if days < 0:
    print("Invalid days")
    valid = False

if valid:
    if age < 30:
        wage = 700 if gender == 'M' else 750
    else:
        wage = 800 if gender == 'M' else 850

    print("Wage per day:", wage)
    print("Total wage:", wage * days)

if valid:
    print("Process successful!")
else:
    print("Process failed. Please try again.")
