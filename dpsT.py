
# 1.________________________________________________________


# a.i<j → 3<5 → True → go inside
# j<k → 5<7 → True → i=j → i=5
# Output: 5 5 7


# b) i=-2, j=-5, k=9

# i<j → -2<-5 → False → go to else
# j>k → -5>9 → False → i=k → i=9
# Output: 9 -5 9


# c) i=8, j=15, k=12

# i<j → 8<15 → True → go inside
# j<k → 15<12 → False → j=k → j=12
# Output: 8 12 12


# d) i=13, j=15, k=13

# i<j → 13<15 → True → go inside
# j<k → 15<13 → False → j=k → j=13
# Output: 13 13 13


# e) i=3, j=5, k=17

# i<j → 3<5 → True → go inside
# j<k → 5<17 → True → i=j → i=5
# Output: 5 5 17


# f) i=25, j=15, k=17

# i<j → 25<15 → False → go to else
# j>k → 15>17 → False → i=k → i=17
# Output: 17 15 17




# 2.________________________________________________________
# 
# a) i=3, j=5, k=7

# j<k → 5<7 → True → go inside
# i>j → 3>5 → False → k=i → k=3
# Output: 3 5 3


# b) i=-2, j=-5, k=9

# j<k → -5<9 → True → go inside
# i>j → -2>-5 → True → j=i → j=-2
# Output: -2 -2 9


# c) i=8, j=15, k=12

# j<k → 15<12 → False → go to else
# j>k → 15>12 → True → i=j → i=15
# Output: 15 15 12


# d) i=13, j=15, k=13

# j<k → 15<13 → False → go to else
# j>k → 15>13 → True → i=j → i=15
# Output: 15 15 13


# e) i=3, j=5, k=17

# j<k → 5<17 → True → go inside
# i>j → 3>5 → False → k=i → k=3
# Output: 3 5 3


# f) i=25, j=15, k=17

# j<k → 15<17 → True → go inside
# i>j → 25>15 → True → j=i → j=25
# Output: 25 25 17








# 3.________________________________________________________
# 
# a) i=3, j=5, k=7

# k<i → 7<3 → False → go to else
# k>i → 7>3 → True → i=j → i=5
# Output: 5 5 7


# b) i=-2, j=-5, k=9

# k<i → 9<-2 → False → go to else
# k>i → 9>-2 → True → i=j → i=-5
# Output: -5 -5 9


# c) i=8, j=15, k=12

# k<i → 12<8 → False → go to else
# k>i → 12>8 → True → i=j → i=15
# Output: 15 15 12


# d) i=13, j=15, k=13

# k<i → 13<13 → False → go to else
# k>i → 13>13 → False → k=i → k=13
# Output: 13 15 13


# e) i=3, j=5, k=17

# k<i → 17<3 → False → go to else
# k>i → 17>3 → True → i=j → i=5
# Output: 5 5 17


# f) i=25, j=15, k=17

# k<i → 17<25 → True → go inside
# i>j → 25>15 → True → j=i → j=25
# Output: 25 25 17








4.________________________________________________________
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Access Denied: Invalid username or password")


5.________________________________________________________

total = float(input("Enter total purchase amount: $"))

if total >= 5000:
    membership = input("Is membership card present? (yes/no): ").lower()
    if membership == "yes":
        discount = total * 0.30
        print(f"Total Saved: ${discount:.2f}")
        print(f"Final Bill: ${total - discount:.2f}")
    else:
        print(f"Total: ${total:.2f}, Discount: $0")
else:
    print(f"Total: ${total:.2f}, Discount: $0")





6.________________________________________________________

print("Welcome to the Magic jungle")
go=input("go north or south")
if go=="south":
    print("game over")
else:
    print("go to next step")
    gone=input("cross the river or follow the path")
    if gone=="cross the river":
        print("the end")
    else:
        print("follow the path")
        choose=input("fairy, ogre, elf")
        if choose=="fairy" or choose=="ogre":
            print("game over")
        else:
            print("hahaha😎 you won the game")

7.________________________________________________________

match light:
        case "red":
            print("Stop!")
        case "yellow":
            print("Get ready...")
        case "green":
            print("Go!")
        case _:
            print(f"Error: '{light}' is not a valid traffic light color.")


8.________________________________________________________

match num:
        case 1:
            print("Spring")
        case 2:
            print("Summer")
        case 3:
            print("Autumn")
        case 4:
            print("Winter")
        case _:
            print("Unknown")

9.________________________________________________________


age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if age < 21:
    print("Loan Denied: Age must be at least 21.")
elif age > 60:
    print("Loan Denied: Age must be 60 or below.")
elif income < 30000:
    print("Loan Denied: Monthly income must be at least 30,000.")
elif credit_score < 700:
    print("Loan Denied: Credit score must be at least 700.")
else:
    print("Loan Approved: All conditions met.")





10.________________________________________________________

weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:")) 
bmi=weight/(height*height)
print(f"your bmi is {bmi:.2f}")
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("overweight")
else:

    print("obese")


11.________________________________________________________


age = int(input("Enter your age: "))

if age < 12:
    print("Ticket Price: Free")
elif age <= 60:
    membership = input("Do you have a membership card? (yes/no): ").strip().lower()
    if membership == "yes":
        print("Ticket Price: Rs. 150")
    else:
        print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 100 (Senior Citizen Discount)")

12.________________________________________________________

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print(f"Bonus Amount: Rs. {bonus:.2f}")
else:
    print("Not eligible for bonus")

13.________________________________________________________


radius = float(input("Enter radius of circle: "))
area = math.pi * radius ** 2
print(f"Area of Circle: {area:.2f}")



14.________________________________________________________
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").strip().upper()
days = int(input("Enter number of days worked: "))

if 18 <= age < 30:
    wage = 700 if gender == "M" else 750
elif 30 <= age <= 40:
    wage = 800 if gender == "M" else 850
else:
    print("Age out of range")
    wage = 0

if wage:
    print(f"Total Wages: Rs. {wage * days}")



15.________________________________________________________
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)



16.________________________________________________________
units = int(input("Enter units consumed: "))

if units < 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)
else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print(f"Total Bill: Rs. {bill}")



17.________________________________________________________

p1 = input("Player 1 - Enter move (rock/paper/scissors): ").strip().lower()
p2 = input("Player 2 - Enter move (rock/paper/scissors): ").strip().lower()

if p1 == p2:
    print("It's a Tie!")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")


18.________________________________________________________
n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Number is not positive")

19.________________________________________________________
total = float(input("Enter total amount: Rs. "))
is_member = input("Are you a member? (true/false): ").strip().lower() == "true"

if total > 1000 and is_member:
    final = total - (total * 0.20)
    print(f"20% discount applied. Final Amount: Rs. {final:.2f}")
elif total > 1000:
    final = total - (total * 0.10)
    print(f"10% discount applied. Final Amount: Rs. {final:.2f}")
else:
    print(f"No discount. Final Amount: Rs. {total:.2f}")


20.________________________________________________________
earth_weight = float(input("Enter your Earth weight (kg): "))
planet = int(input("Enter planet number (1-7): "))

if planet == 1:
    print(f"Mercury: {earth_weight * 0.38:.2f} kg")
elif planet == 2:
    print(f"Venus: {earth_weight * 0.91:.2f} kg")
elif planet == 3:
    print(f"Mars: {earth_weight * 0.38:.2f} kg")
elif planet == 4:
    print(f"Jupiter: {earth_weight * 2.53:.2f} kg")
elif planet == 5:
    print(f"Saturn: {earth_weight * 1.07:.2f} kg")
elif planet == 6:
    print(f"Uranus: {earth_weight * 0.89:.2f} kg")
elif planet == 7:
    print(f"Neptune: {earth_weight * 1.14:.2f} kg")
else:
    print("Invalid planet number")


21.________________________________________________________

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Total: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")



22.________________________________________________________

is_valid = True
balance = 5000
correct_pin = 123

if is_valid:
    pin = int(input("Enter PIN: "))

    if pin != correct_pin:
        print("Wrong PIN!")
    else:
        print("\n1. Withdraw\n2. Check Balance\n3. Exit")
        choice = int(input("Select option: "))

        if choice == 1:
            amount = float(input("Enter amount to withdraw: Rs. "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print(f"Withdrawn Rs. {amount}. Remaining Balance: Rs. {balance}")
        elif choice == 2:
            print(f"Current Balance: Rs. {balance}")
        elif choice == 3:
            print("Thank you for visiting!")
        else:
            print("Invalid option!")


23.________________________________________________________

floor = int(input("Enter target floor (0-10): "))
weight = float(input("Enter total weight (kg): "))
door = input("Enter door status (open/closed): ").strip().lower()

if floor < 0 or floor > 10:
    print("INVALID FLOOR")
elif weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")
elif door == "open":
    print("WARNING: CLOSE THE DOOR")
else:
    print("ACTIVATE ELEVATOR MOTION.")



24.________________________________________________________


first = input("First Name: ").strip()
last  = input("Last Name: ").strip()
email = input("Email Address: ").strip()
re_email = input("Re-enter Email: ").strip()
password = input("New Password: ").strip()

if not first or not first.isalpha():
    print("Invalid first name.")
elif not last or not last.isalpha():
    print("Invalid last name.")
elif "@" not in email or "." not in email:
    print("Invalid email address.")
elif email != re_email:
    print("Emails do not match.")
elif len(password) < 6:
    print("Password must be at least 6 characters.")
else:
    print("Account created successfully!")





