#1
password = 'Pass@123'
lowercase_password = password.lower()
print(lowercase_password) # Output: 'pass@123'

#2
patient_name = 'rahUl DahaL'
title_case_name = patient_name.title()
print(title_case_name) # Output: 'Rahul Dahal'

#3
movie_name = 'spider-man no way home'
title_case_movie = movie_name.title()
print(title_case_movie) # Output: 'Spider-Man No Way Home'

#4
sentence = 'hELLO wORLD'
swapped_case = sentence.swapcase()
print(swapped_case)  # Output: 'Hello World'

#5
heading = 'annual sports day'
all_caps_heading = heading.upper()
print(all_caps_heading) # Output: 'ANNUAL SPORTS DAY'

#6
log = 'System error detected, error code 404'
print(log.find('error'))  # Output: 7

#7
email = 'user@gmail.com'  # or input()
print(email.endswith('@gmail.com'))  # Output: True

#8
msg = 'Get free stuff, free gifts and free coupons now!'
print(msg.count('free'))  # Output: 3

#9
url = 'https://example.com'  # or input()
print(url.startswith('https'))  # Output: True

#10
resume = 'Experienced in Python programming'
print('Python' in resume)  # Output: True

#11
log = 'Transaction FAILED due to low balance'
print(log.index('FAILED'))  # Output: 12

#12
filename = 'budget_report.pdf'
print(filename.endswith('.pdf'))  # Output: True

#13
phone = '+9779841123111'
print(phone.startswith('+977'))  # Output: True

#14
url = 'https://www.moha.gov.np/'
print(url.endswith('.gov.np/'))  # Output: True

#15
feedback = ' Great service! '
print(feedback.strip())  # Output: Great service!

#16
msg = "I hate this, hate it completely"
print(msg.replace('hate', '****'))  # Output: I **** this, **** it completely

#17
filename = '///student_records.pdf '
print(filename.lstrip('/'))  # Output: student_records.pdf 

#18
price = 'Price: $120.33 '
clean_price = price.rstrip().replace('$', '').replace('Price: ', '')
print(clean_price)  # Output: 120.33

#19
phone = '+977 984-123-4567'
print(phone.replace('-', ''))  # Output: +977 9841234567

#20
data = 'Aarav,22,Kathmandu,Computer Science'
fields = data.split(',')
for field in fields:
    print(field)
# Output:
# Aarav
# 22
# Kathmandu
# Computer Science

#21
hashtags = 'Python, Coding, Nepal, Tech'
words = hashtags.split(', ')
result = '#'.join(words)
print(result)  # Output: Python#Coding#Nepal#Tech

#22
names = 'Ram, Shyam, Hari, Sita'
passengers = names.split(',')
print(len(passengers))  # Output: 4

#23
words = ['The', 'flight', 'departs', 'at', '6AM']
sentence = ' '.join(words)
print(sentence)  # Output: The flight departs at 6AM 

#24
age = '25'  # or input()
print(age.isdigit())  # Output: True
# age = '25abc' → False

#25
username = 'user123'
print(username.isalnum())  # Output: True

#26
name = 'Aarav'
print(name.isalpha())  # Output: True

#27
pin = 'ASDF'
print(pin.isupper())  # Output: True

#28
field = '   '
print(field.isspace())  # Output: True