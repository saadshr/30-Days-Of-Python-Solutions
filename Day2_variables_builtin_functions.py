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

