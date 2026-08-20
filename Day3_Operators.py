#------------------💻 Exercises - Day 3--------------------
#1 : Declare your age as integer variable
age = 21 
print(age)
print(type(age))
#2 : declare your height as a float variable
height = 1.70 
print(height)
print(type(height))
#3 : declare a complex number variable
complex_number = 3 + 4j 
print(complex_number)
print(type(complex_number))
#4 : write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base :"))
height = float(input("Enter height : "))
area = 0.5 * base * height 
print("The area of the triangle is :", area)
#5 : write a script that prompts the user to enter side a, side b, and side c of the triangle and calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = int(input("Enter side a :"))
side_b = int(input("Enter side b :"))
side_c = int(input("Enter side c :"))
perimeter = side_a + side_b + side_c 
print("The perimeter of the triangle is :", perimeter)
#6 : write a script that prompts the user to enter length and width of a rectangle and calculate an area of this rectangle (area = length x width) and perimeter of the rectangle (perimeter = 2 x (length + width))
length = float(input("Enter length : "))
width = float(input("Enter width : "))
area = length * width 
perimeter = 2 * (length + width)
print("The area is : " , area)
print("The perimeter is : " , perimeter)
#7 : write a script that prompts the user to enter radius of a circle and calculate the area (area = π x r x r) and circumference (c = 2 x π x r) of the circle
import math 
radius = float(input("Enter radius : "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius 
print("The area of the circle is :", area)
print("The circumference of the circle is :", circumference)
#8 : Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2
x_intercept = -b/m
y_intercept = b

print("The slope is :", m)
print("the X-intercept is :", x_intercept)
print("the Y-intercept is :", y_intercept)

#9 : Slope is (y2-y1)/(x2-x1). Find the slope and euclidean distance between point (2, 2) and point (6,10)
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1)/(x2 -x1)
distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
print("Slope is :", slope)
print("Euclidean distance is :", distance)
#On peut aussi arrondir la distance à 2 décimales
distance = round(distance, 2)
print("Euclidean distance (rounded) is :", distance)

#10 : Compare the slope in tasks 8 and 9 
slope_8 = 2 
slope_9 = 2 
print(slope_8 == slope_9)

#ou Bien : 
if slope_8 == slope_9:
    print("The slopes are equal")
else :
    print("The slopes are not equal") 

#11 : Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = float(input("Enter x value : "))
y = x**2 + 6*x + 9 
print("y =", y)
#Pour tester plusieurs valeurs :
for x in [-5, -4, -3, -2, -1, 0, 1]:
    y = x**2 + 6*x + 9
    print("x=", x, "y=", y)

#12 : Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len("python")
len_dragon = len("dragon")
print(len_python)
print(len_dragon)
print(len_python != len_dragon)

#13 : Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

#14 : I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
#or 
print("jargon" in "I hope this course is not full of jargon.")

#15 : There is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "python")

#16 : Find the length of the text 'python' and convert the value to float and convert it to string
python ="python"
length = len(python)
print(length)
float_value = float(length)
print(float_value)

string_value = str(float_value)
print(string_value)
#Types : 
print(type(length))
print(type(float_value))
print(type(string_value))

#17 : Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("enter a number : "))
if number % 2 == 0:
    print(number, "is an even number")
else : 
    print(number, "is an odd number")
    








        