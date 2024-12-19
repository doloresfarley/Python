'''
x =3
y =4

if x=3:
    print(x)
else:
    print(y)
'''

'''
key ='q'
key='a'
print(not(key == 'q'))

x = input()
if x == 'a':
  print('first')
print('second')
x =10
print('start')
if x > 10:
    print('large')
else:
    print('small')
print('done')

print('start')
if x > 10:
         print('large')
else:
         print('small')
print('done')
'''
#
day = 23
if day % 10 == 1:
    ending = "st"
elif day % 10 == 2:
    ending = "nd"
elif day % 10 == 3:
    ending = "rd"
else:
    ending = "th"
print(str(day) + ending)

year = 300
if year < 101:
    print("1-100")
elif year < 201:
    print("101-200")
elif year < 301:
    print("201-300")
else:
    print("Other")
x = 9
if x < 10 :
    print("Branch1")
elif x > 9:
    print("Branch2")
else:
    print("Branch3")

x = 17
if x * 2 <= 34:
    x = 0
else:
    x = x + 1

x = x + 1
print(x)

x=1
print(not(10<x<20))
print(not (x > 10 or x < 20))

year = 2009
if (year >= 2010 and year <= 2014):
    print('Jen employed at Regal Cinemas')
elif (year >= 2018):
    print('Jen employed at  AMC Cinemas')
else:
    print('Unemployed')

score = 65
group = ''
if score <= 60:
    group = group + 'A'
if score <= 70:
    group = group + 'B'
if score <= 80:
    group = group + 'C'
else:
    group = group + 'D'
print(group)

grades = { 'A': 90, 'B': 80, 'C': 70, 'D': 60 }
my_grade = 70
if my_grade not in grades:
    z = 1
else:
    z = 2
if 'F' in grades:
    z = z + 10
else:
    z = z + 20

print(z)

my_name = "Bob"
your_name = "Jane"
if id(my_name) == id(your_name):
    print("Same name", id(my_name))

'''
Question 49 1 pts
A child is required to use a booster seat in a car until the child is 9 years old, unless the child reaches the height of 59 inches before age 9. Which expression can be used to decide if a child requires a car seat or not?
Group of answer choices

if age >= 9 or height >= 59:

if age >= 9 and height >= 59:

if age <= 9 and height <=59:

if age < 9 or height < 59:
'''
age = 81
height =40
if age >= 9 or height >= 59:
    print(" age >= 9 or height >= 59:")

if age >= 9 and height >= 59:
    print(" age >= 9 and height >= 59:")

if age <= 9 and height <=59:
    print(" age <= 9 and height <=59:")

if age < 9 or height < 59:
    print(" age < 9 or height < 59:")

x =51
if (50 >= x <= 100):
    print("True")
