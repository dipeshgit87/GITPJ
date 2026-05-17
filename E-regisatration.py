first_name = input("Enter your first name:") 
last_name = input("Enter your last name:")
email = input("Enter your email address:")
re_email = input("Re-enter your email address:")
password = input("Enter your password:")

if not (first_name and last_name and email and re_email and password):
    print("all fields are mandatory")
elif not(first_name.isalpha() and last_name.isalpha()):
    print("must enter or type letters only")
elif not('@' in email and '.' in email and '@' in re_email and '.' in re_email):
    print("invalid email address")
elif email!=re_email:
    print("emails donot match")
elif len(password)<6:
    print("password length must be greater than 6")
else:
    print("Registered successfully")