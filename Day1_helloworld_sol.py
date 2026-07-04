# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
 
 # Exercice : Level 2  : 
print('3+4')
print('3-4')
print('3*4')
print('3/4')
print('3%4')
print('3//4')
print('3**4')

print("Saad sahraoui")
print("22 yo")
print("Morocco")
print("I am enjoying 30 days of python challenge")
 
#Exercise : Level 3
#Integer
age=21
#float
height=1.75
#complex
complex_num=3+4j
#string 
name="Saad sahraoui"
#Boolean
is_student=True
#List
fruits=["apple","banana","cherry"]
#Tuple
coordinates=(10,20)
#Dictionary
student={"name":"Saad",
         "age":21,
         "major":"Computer Science"}
#Print all variables 
print("Integer:",age)
print("Float:",height)
print("Complex:",complex_num)
print("String:",name)
print("Boolean:",is_student)
print("List:",fruits)
print("Tuple:",coordinates)
print("Dictionary:",student)
#2Find the Euclidiean distance between the points (2, 3) and (10, 8)
import math
#Points 
x1, y1 = 2, 3
x2, y2 = 10, 8
#Calculate the Euclidean distance
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Euclidean distance = ", distance)
print(f"Euclidean distance = {distance:.2f}")

