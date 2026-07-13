first_name='Saad'
last_name='Sahraoui'
country='Morocco'
city='Tangier'
age= 21 
is_married=False
skills=['Python','Javascript','HTML','CSS']

#...
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)

# Multiple variables can also be declared in one line:
first_name, last_name, country, age, is_married = 'Saad', 'Sahraoui', 'Morocco', 21, False
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# using the input() function to get user input
first_name=input('Enter your first name: ')
age=input('Enter your age: ')
print(first_name)
print(age)
# Casting 
# str to list
first_name = 'Saad'
print(first_name)               
first_name_to_list = list(first_name)
print(first_name_to_list)  
#💻 Exercises - Day 2
#Exercises: Level 1
#1. Done 
#2.Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming
#3.Declare a first name variable and assign a value to it
first_name = 'Saad'
#4.Declare a last name variable and assign a value to it
last_name = 'Sahraoui'
#5.Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name
#6.Declare a country variable and assign a value to it
country = 'Morocco'
#7.Declare a city variable and assign a value to it
city = 'Tangier'
#8.Declare an age variable and assign a value to it
age = 21
#9.Declare a year variable and assign a value to it
year = 2024
#10.Declare a variable is_married and assign a value to it
is_married = False 
#11.Declare a variable is_true and assign a value to it
is_true = True 
#12.Declare a variable is_light_on and assign a value to it
is_light_on = True
#  13.Declare multiple variable on one line
first_name, last_name, country, age, is_married = 'Saad', 'Sahraoui', 'Morocco', 21, False
#Exercises: Level 2 
#1
# Check the data type of all your variables
# ============================================
first_name='Saad'
last_name='Sahraoui'
country='Morocco'
city='Tangier'
age= 22
is_married=False
skills=["Python","Machine learning","Git"]
person_info = {
    "first_name": first_name,
    "last_name": last_name,
    "country": country,
    "city": city,
    "age": age,
    "is_married": is_married,
    "skills": skills
}
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))
#2:Using the len() built-in function, find the length of your first name
#Trouver la longueur du prenom :
print(len(first_name))
length_first_name = len(first_name)
print('Length of first name:', length_first_name)
#3: Comprarer la longueur du prenom et du nom de famille : 
if len(first_name) > len(last_name):
    print('First name is longer than last name.')
elif len(first_name) < len(last_name):
    print('Last name is longer than first name.')
else:
    print('First name and last name have the same length.')
#4: Declare 5 as num_one and 4 as num_two
num_one = 5 
num_two = 4 
#5: Add num_one and num_two and assign the value to a variable total
total = num_one + num_two 
print('Total:', total)
#6:Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two 
print("La difference est : ",  diff)
#7: Multiply num_two and num_one and assign the value to a variable product 
product = num_one * num_two 
print("La difference entre le premier nombre et deuxieme nombre est : " , product)
#-------------------------
#8: Divide num_one by num_two and assign the value to a variable division 
division = num_one / num_two
print("La division entre les deux nombres est :" , division)
#------------------------
#9: Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print("Le reste de la division entiere entre les 2 nombres est:" , remainder)
#-------------------------------
#10: Calculate num_one to the power of num_two and assign the value to a variable exp
pow = num_one ** num_two
print("Numero 1 a la puissance numero 2 est:" , pow)
#---------------------------------
#11: Find floor division of num_one by num_two and assign the value to a variable floor_division
# ----------Division entiere-----------------
floor_division = num_one // num_two 
print("La division entiere entre les 2 nombres est:" , floor_division)
#---------------------------------
#12:The radius of a circle is 30 meters.
import math 
#12.1- Calculate the area of a circle and assign the value to a variable name of area_of_circle 
radius = 30
area_of_circle = math.pi * radius ** 2
print("L'aire du cercle de rayon 30 est : " , area_of_circle)
#12.2- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius 
print("Le perimtre du cercle de rayon 30 est :" , circum_of_circle)
#13.3- Take radius as user input and calculate the area.
rad = float(input("Entrer le rayon du cercle : "))
surface = math.pi * rad ** 2 
print(f"La surface du cercle de rayon {rad} est : " , surface)
#--------------------------------------------- 
#13: Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#----------Demander les informations a l'utilisateur--------------
first_name = input("Entrer votre prenom :")
last_name = input(" Entrer votre nom : ")
country = input(" Entrez votre pays : ")
age = int (input("Entrez votre age :"))
#------------Affichage-------------------
print("Prenom:" , first_name)
print("Nom : " , last_name)
print("Pays : " , country)
print("Age : " , age)
#-------------------------------------------------
#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")



#-----------------------CODE COMPLET-----------------------
import math

first_name = "Saad"
last_name = "Sahraoui"
country = "Morocco"
city = "Tangier"
age = 22
is_married = False
skills = ["Python", "Machine Learning", "Git"]
person_info = {
    "first_name": first_name,
    "last_name": last_name,
    "country": country
}

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))

print(len(first_name))

if len(first_name) > len(last_name):
    print("Le prénom est plus long.")
elif len(first_name) < len(last_name):
    print("Le nom est plus long.")
else:
    print("Même longueur.")

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radius = 30

area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print(area_of_circle)
print(circum_of_circle)

radius = float(input("Entrer le rayon : "))
area = math.pi * radius ** 2
print("L'aire est :", area)

first_name = input("Entrez votre prénom : ")
last_name = input("Entrez votre nom : ")
country = input("Entrez votre pays : ")
age = int(input("Entrez votre âge : "))

print(first_name)
print(last_name)
print(country)
print(age)

help("keywords")

