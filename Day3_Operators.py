#------------------💻 Exercises - Day 3--------------------
#1 : Declare your age as integer variable
age = 22 
# 2 : Declare your height as a float variable
height = 170.00
# 3 : Declare a variable that store a complex number
complex_num = 1 + 2j
# 4 : Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base :"))
height = float(input("Enter height :"))
area = 0.5 * base * height 
print("The area of the triangle is : " , area )
# 5 : Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Entrez la face A : "))
side_b = float(input("Entrez la face B : "))
side_c = float(input("Entrez la face C : "))
perimeter = side_a + side_b + side_c 
print("Le perimetre de ce triangle est : " , perimeter)
# 6 : Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Entrer la hauteur du rectangle : "))
width = float(input("Entrer la largeur du rectangle :  "))
area = length * width 
print(" La surface du rectangle est : ", area)
# 7 : Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math 
radius = float(input("Entrer la rayon du cercle : "))
area_tr= math.pi * radius ** 2
circumf = 2 * math.pi * radius 
print("La surface du triangle est : ", area_tr)
print("Le perimetre du triange est :" , circumf)
# 8 : Calculate the slope, x-intercept and y-intercept of y = 2x -2
#-----------x-intercept --------------
y = 0
x = int(input( "entrer la valeur de x :"))
y  = 2*x - 2 
print("L'intersection de cette equation avec l'axe des abssices lorque y vaut 0 est : ", x)
#-----------y-intercept--------------
x = 0
print("l'intersection de cette equation avec l axe des ordonnee lorque x vaut 0 est :", y)
# 9 : Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2 
y1 = 2 
x2 = 6 
y2 = 10
m = (y2 - y1)/(x2 - x1)
d = math.sqrt((x2 - x1)**2 +(y2 -y1)**2)
print("the slope between (2,2) et (6,10) est : ", m)
print("La distance euclidienne entre (2,2) et (6,10) est ", d)
# 10 : Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("strings : ")




        