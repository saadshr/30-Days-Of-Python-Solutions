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
