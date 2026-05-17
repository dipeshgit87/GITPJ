valid = True  # assume everything is valid at start

first_name = input("Enter your first name: ")
if first_name == "":
    print("First name cannot be blank")
    valid = False
elif not first_name.isalpha():
    print("Please enter letters only")
    valid = False

last_name = input("Enter your last name: ")
if last_name == "":
    print("Last name cannot be blank")
    valid = False
elif not last_name.isalpha():
    print("Please enter letters only")
    valid = False

email = input("Enter your email: ")
if "@" not in email or "." not in email:
    print("Invalid email address")
    valid = False

re_email = input("Re-enter your email: ")
if re_email != email:
    print("Email does not match")
    valid = False

password = input("Create a password: ")
if len(password) < 6:
    print("Password must be at least 6 characters long")
    valid = False

# Final result
if valid:
    print("Registration successful!")
else:
    print("Registration failed. Please try again.")


light = input("Enter traffic light color: ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color")

number = int(input("Enter a number:"))
match number:
    case 1: print("Spring")
    case 2: print("Winter")
    case _: print("Invalid Number")

age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
if age >= 12 and height >= 140:
    print("You can ride the roller coaster")
else:
    print("You are not eligible!!!!!")

salary = int(input("Enter your salary:"))
exp = float(input("Enter your years of experience:"))





