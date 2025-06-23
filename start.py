import math


#numbers in python
'''
a= 5
b= 4
c= 4.4
print("Addition =",a+c)
print("Subtraction =",a-c)
print("foat and integer Multiplication =",a*c)
print("divide 2 integers return float =", int(a/b))
print("Remainder of 2 integers =", a%b)
print("Square of a number =", a**3)
'''

# Celcius OR Farenheight
'''
celcius= 30
faren = 122
print("Celcius to farenheight =", (celcius * 9/5) + 32 )
print("Farebheight to celcius = ", (faren -32) * 0.5 )
'''

#Area of a Rectangle,square and circle
''' 
length= 32
width= 43
print("Area of a Triangle is =",length*width)
print("Area of a square is =", length*length)

radius= float(input("Enter the radius of a cicle :"))
area= math.pi * (radius * radius)
print("Area of cicle is = ", area)
'''

#hour into Second, minues etc
'''
hour = int(input("Enter the hours here: "))
minute= hour * 60
sec= hour * 3600
print("Total Minutes in ", hour,"are", minute)
print("Total Seconds in ", hour,"are", sec)
'''


#Hypotenius of a Right Triangle
'''
base= int(input("Enter the base of Triangle: "))
height= int(input("Enter the Height of a Triangle: "))
hypotenius= math.sqrt((base**2) + (height**2))
print(hypotenius)
'''

#Average of the numbers
'''
n1= int(input("Enter the 1st num : "))
n2= int(input("Enter the 2nd num : "))
n3= int(input("Enter the 3rd num : "))
avg= (n1+n2+n3)/3
print(avg)
'''

#Swap two variables without a temporary variable.
'''
a= 3
b= 5
print("A = ",a, "B =",b)
a, b= b, a

print("A = ",a, "B =",b)

a= 3
b=5
c=2
d=1

print(a,b,c,d)

a,b,c,d= c,a,d,b
print(a,b,c,d)
'''

#Check if a number is even or odd.

#Method 1
'''
num =int(input("Enter a number: "))

if (num%2)==0:
    print("The number is even")
else :
    print("The number is not even")
'''


#Check if a number is positive, negative, or zero
'''
num =int(input("Enter a Number: "))

if num > 0:
    print("Number is positive")
elif num< 0:
    print("Number is Negative")
else:
    print("Number is Zero")
    '''

# Eval input typecasting
'''
a= eval(input("Enter your First Name: "))
b= eval(input("Enter your Last Name: "))
print("Wellcome ",a+" "b)
'''



                      #/\..................... Array AND List........................./\


#Method  1
# Find the Minimum
'''
A= [4,2,6,1,7,3,8,3,0]

l=len(A)
if A[0] < A[1]:
    c = A[0]
elif A[0] > A[1]:
    c= A[1]
for i in range(1, l):
    if A[i] < c:
        c= A[i]
print(c)


#Find the Maximum

A= [4,2,6,1,7,3,8,3,10]

l=len(A)
if A[0] < A[1]:
    c = A[1]
elif A[0] > A[1]:
    c= A[0]
for i in range(1, l):
    if A[i] > c:
        c= A[i]
print(c)


#Method 2

#
a=[3,1,7,4,6,1,9,0,2,4,3,9]

for i in range(0, 12):
    if a[i] %2==0:
        continue
    print(a[i])
    

while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Invalid input")
        continue
    age = int(age)
    break'''


sen = "ther is an apple at the table"

vovel=0
for let in sen:
    if let == "a"  or let == "e"or let == "i"or let == "o"or let == "u":
        continue
    vovel+=1
cons =len(sen) - vovel
print(cons)