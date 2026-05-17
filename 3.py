#price = '$12.33'
#print(price.replace('$','$'*2)) 

#prog_lan='python'
#print(prog_lan.replace('p','P').replace('n','N'))

#prog_lan='python'
#print(prog_lan.maketrans('pn','PN'))

#prog_lan='python' #PythoN
#as_v=prog_lan.maketrans('pn','PN')
#print(prog_lan.replace('p','P').replace('n','N'))

#na='STUDENT ID CARD'
#print(na.center(25,'*'))

#Taking input from user
name = input("Enter your full name: ")
age = input("Enter your age: ")
cls = input("Enter your class: ")
college = input("Enter your college: ")
blood_group = input("Enter your blood group: ")

#Printing ID card
na='STUDENT ID CARD'
print("\n" + na.center(25,'*'))

print(f"FullName :{name}")
print(f"Age :{age}")
print(f"Class :{cls}")
print(f"College :{college}")
print(f"Blood Group :{blood_group}")
