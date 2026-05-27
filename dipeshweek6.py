# # 1._________________________________________________________
# # for num in range(1, 6):
# #     if num % 2 == 0:
# #         print(f"Number {num} is even.")
# #     else:
# #         print(f"Number {num} is odd.")


# # 2._________________________________________________________
# # data = [10, 20, 30, 40]
# # total = 0
# # for num in data:
# #     total += num
# #     print(f"Added {num}. Running total is {total}.")
# # print(f"Total sum: {total}")


# 3._________________________________________________________

# print("--- Email Greetings Generated ---")
# student_names = ["Ram", "Hari", "Sita"]
# for name in student_names:
#     print(f"Hi {name}, your course approval is ready!")
 
 
# 4._________________________________________________________

# print("\n--- Book Chapter Summary ---")
# chapter_pages = [45, 30, 50, 40]
# for number, pages in enumerate(chapter_pages, start=1):
#     print(f"Chapter {number} has {pages} pages.")
 
 
# 5._________________________________________________________

# lst = [4, 5, 3, 2]
# product = 1
# for num in lst:
#     product *= num
# print(f"\nProduct of {lst} = {product}")
 
 
# 6._________________________________________________________

# number = 11
# print(f"\nMultiplication Table of {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
 
 
# 7._________________________________________________________

# given_list = [3, 2, 1, 4, 5]
# reversed_list = given_list[::-1]
# print(f"\nOriginal list : {given_list}")
# print(f"Reversed list : {reversed_list}")
 
 
# 8._________________________________________________________


# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
# for num in list1:
#     if num in list2:
#         common.append(num)
# print(f"\nList1 : {list1}")
# print(f"List2 : {list2}")
# print(f"Common elements: {common}")
 
# 9._________________________________________________________

# lst = [1, 2, 3, 4]
# print(f"\nList: {lst}")
# print(f"First element : {lst[0]}")
# print(f"Last element  : {lst[-1]}")
 
 
# 10._________________________________________________________

# string = "Hello World"
# vowels = "aeiouAEIOU"
# result = ""
# for ch in string:
#     if ch not in vowels:
#         result += ch
# print(f"\nOriginal string : {string}")
# print(f"After removing vowels: {result}")
 
 
# 11._________________________________________________________

# sentence = "Loops are Fun"
# vowel_count = 0
# consonant_count = 0
# for ch in sentence:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print(f"\nSentence : '{sentence}'")
# print(f"Vowels    : {vowel_count}")
# print(f"Consonants: {consonant_count}")
 
# 12._________________________________________________________

# numbers = [1, 2, 3, 4, 5]
# odd_list = []
# even_list = []
# for num in numbers:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print(f"\nOriginal : {numbers}")
# print(f"Odd  numbers: {odd_list}")
# print(f"Even numbers: {even_list}")
 
# 13._________________________________________________________

# num = 29
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# print(f"\n{num} is {'a prime' if is_prime else 'not a prime'} number.")
 
 
# 14._________________________________________________________

# mixed_list = [1, 2, 3, 4, "a", "b"]
# int_list = []
# str_list = []
# for item in mixed_list:
#     if isinstance(item, int):
#         int_list.append(item)
#     elif isinstance(item, str):
#         str_list.append(item)
# print(f"\nOriginal list : {mixed_list}")
# print(f"Integer elements: {int_list}")
# print(f"String elements : {str_list}")
 
# 15._________________________________________________________

# text = input("\nQ15 - Enter a string: ")
# digit_count = 0
# letter_count = 0
# for ch in text:
#     if ch.isdigit():
#         digit_count += 1
#     elif ch.isalpha():
#         letter_count += 1
# print(f"Letters: {letter_count}")
# print(f"Digits : {digit_count}")
 
# 16._________________________________________________________

# VALID_USERNAME = "admin"
# VALID_PASSWORD = "pass123"
# username = input("\nQ16 - Enter username: ")
# password = input("Enter password: ")
# if username == VALID_USERNAME and password == VALID_PASSWORD:
#     print("Login successful!")
# else:
#     print("Invalid username or password.")
 
 
# 17._________________________________________________________


# n = int(input("\nQ17 - Enter a number: "))
# if n % 2 == 0:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")
 
 
# 18._________________________________________________________


# num = int(input("\nQ18 - Enter a number for factorial: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num} = {factorial}")
 
 
# 19._________________________________________________________


# print("\n--- Multiplication Tables (1 to 8) ---")
# for table in range(1, 9):
#     print(f"\nTable of {table}:")
#     for i in range(1, 11):
#         print(f"  {table} x {i} = {table * i}")
 
 
# 20._________________________________________________________


# lst = [1, 2, 3, 4]
# print(f"\nList: {lst}")
# print(f"First element : {lst[0]}")
# print(f"Second element: {lst[1]}")
 
 
# 21._________________________________________________________


# start, end = 1, 50
# odd_sum = 0
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         odd_sum += i
# print(f"\nSum of odd numbers from {start} to {end} = {odd_sum}")
 
 
# 22._________________________________________________________


# even_sum = 0
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         even_sum += i
# print(f"Sum of even numbers from {start} to {end} = {even_sum}")
 
 
# 23._________________________________________________________


# text = "Python is fun to learn"
# space_count = 0
# for ch in text:
#     if ch == " ":
#         space_count += 1
# print(f"\nString: '{text}'")
# print(f"Number of spaces: {space_count}")
 
 
# 24._________________________________________________________


# lst = [1, 2, 3, 4]
# cubed = [x ** 3 for x in lst]
# print(f"\nOriginal : {lst}")
# print(f"Cubed    : {cubed}")
 
 
# 25._________________________________________________________


# a = "programming"
# reversed_str = a[::-1]
# print(f"\nOriginal string : {a}")
# print(f"Reversed string : {reversed_str}")
 
 
# 26._________________________________________________________


# print("\nNumbers 0 to 7 using break:")
# for i in range(50):
#     print(i, end=" ")
#     if i == 7:
#         break
# print()
 
 
# 27._________________________________________________________


# word = "Python"
# print(f"\nLetters in '{word}':")
# for letter in word:
#     print(letter)
 
# 28._________________________________________________________


# a = ["ram", "shyam", 1, 2]
# print("\nGreetings (strings only):")
# for item in a:
#     if isinstance(item, str):
#         print(f"Hello!{item}")
 
 
# 29._________________________________________________________


# a = ["ram", "shyam", 1, 2]
# lst = []
# for item in a:
#     lst.append(f"Dr.{item}")
# print(f"\nResult: {lst}")
 
 
# 30._________________________________________________________


# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(f"\nNumbers : {numbers}")
# print(f"Squares : {squares}")
 
 
# 31._________________________________________________________


# lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
# positives = []
# for num in lst1:
#     if num > 0:
#         positives.append(num)
# print(f"\nOriginal : {lst1}")
# print(f"Positives: {positives}")
 
 
# 32._________________________________________________________


# lst = [0, 1, 2, 3, 4, 5, 6]
# print("\nNumbers (excluding 3 and 6):", end=" ")
# for num in lst:
#     if num == 3 or num == 6:
#         continue
#     print(num, end=" ")
# print()
 
 
# 33._________________________________________________________


# list1 = [1, "hello", 3.14, True, None]
# list2 = []
# for item in list1:
#     list2.append(type(item).__name__)
# print(f"\nList1     : {list1}")
# print(f"Data types: {list2}")
 
 
# 34._________________________________________________________


# items = [10, 20, 30]
# for item in items:
#     print(item, end=" ")
# else:
#     print("\nDone")
 
 
# 35._________________________________________________________


# print("\nSeries (105 to 7, step -7):")
# for i in range(105, 0, -7):
#     print(i, end=" ")
# print()
 
 
# 36._________________________________________________________


# bad_chars = [';', ':', '!', '*', ' ']
# string = "py;th* o:n ! ;py * t*h:o !n"
# cleaned = ""
# for ch in string:
#     if ch not in bad_chars:
#         cleaned += ch
# print(f"\nOriginal : {string}")
# print(f"Cleaned  : {cleaned}")
 
 
# 37._________________________________________________________


# series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_count = 0
# odd_count = 0
# for num in series:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"\nSeries: {series}")
# print(f"Even count: {even_count}")
# print(f"Odd  count: {odd_count}")
 
 
# 38._________________________________________________________


# for i in range(3, 100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(f"\nSum of multiples of 3 or 5 (3 to 99) = {total}")
 


# 39._________________________________________________________


even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"\nRange: 1 to 100")
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd  numbers: {odd_sum}")
      
# 40._________________________________________________________


# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count = 0
 
# for num in list1:
#     if num == target:
#         count += 1
 
# print(f"List   : {list1}")
# print(f"Target : {target}")
# print(f"Count  : {target} appears {count} times")

