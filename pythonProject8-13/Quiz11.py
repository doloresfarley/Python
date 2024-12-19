'''
Which of the following variables and functions can be used together to create a useful object type?
Group of answer choices

my_favorite_pet, student_name, my_string.title()

weather_today, my_favorite_pet, my_string.title()

cooking_ingredients, weather_today, calculate_average()

student_marks, student_name, calculate_average() <<<- Answer

'''
'''
Question 2 
Given that my_val is a list of float values, 
which of the following is an example of a built-in function?


my_val.capitalize() <<<--error

my_val.title() <<<--error

len(my_val) <<<---Answer

average(my_val) <<<-- average(my_val): This is not a built-in function in Python.
To compute the average of a list, you might use a library function like statistics.mean() or calculate it manually using

'''
'''
Question 3
A user is interested in creating an object to create a stock inventory at a grocery store. Which of the following would be appropriate attributes of an object that they may use?
Group of answer choices

managers_name, no_of_days_on_shelf, employee_id, calculate_employee_age()

stock_item_names, expiry_dates, aisle_number, calculate_if_expired() <<<--- ANSWER

stock_item_names, managers_name, total_employees, street_address

totat_employees, employee_id, aisle_number, calculate_if_expired()
'''

''''
Which built-in object is mutable?
Group of answer choices

str

int

bool

list <<<-- list
'''

'''
Question # 5
Which of the following is an attribute of the class shown below?


class Student:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.weight = 0
Group of answer choices

init

student

weight <<<-weight

def __init__(self)
'''

#Q6
class Student:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.weight = 0
student1 = Student()
student1.age = 10
student2 = Student()
student2.height = 155
print(student1.age, student1.weight, student1.height)
print(student2.age, student2.weight, student2.height)

print()
#Q7
class Score:
    def __init__(self):
        self.marks = 0
        self.no_subjects = 1
        self.average = 1
student1 = Score()
student1.marks = 422
student1.no_subjects = 5
student1.average = student1.marks / student1.no_subjects
print(f'The average score of the student is {student1.average:.1f}')
print()

#8
'''
Complete the code below to produce 'Student Name: ABC' and 'Student Age: 10' as the output.
XXX
student1 = Student()
student1.age = 10
print(f'Student Name: {student1.name}\n Student Age: {student1.age}')

'''

print("#8")
class Student:
    def __init__(self):
        self.name = 'ABC'
        self.age = 10

student1 = Student()
student1.age = 10
print(f'Student Name: {student1.name}\n Student Age: {student1.age}')

print("")
print("#9")
'''
Which of the following is an instance created by the code given below?


class Employee:
    def __init__(self):
        self.id = 0
        self.name = 'ABC'
        self.title = 'Business Analyst'
employee1 = Employee()
employee1.id = 122654
print(employee1.id, employee1.name, employee1.title)
'''
class Employee:
    def __init__(self):
        self.id = 0
        self.name = 'ABC'
        self.title = 'Business Analyst'
employee1 = Employee()
employee1.id = 122654
print(employee1.id, employee1.name, employee1.title)

print(employee1.__class__)

print()
print("#10")
'''
class Student:
    def __init__(self):
        self.first_name = 'ABC'
        self.last_name = 'DEF'
    XXX
student1 = Student()
student1.first_name = 'Alex'
student1.last_name = 'Smith'
student1.print_name()
'''

class Student:
    def __init__(self):
        self.first_name = 'ABC'
        self.last_name = 'DEF'

    def print_name(self):
        print(f'{self.first_name} {self.last_name} is a student in middle school.')

student1 = Student()
student1.first_name = 'Alex'
student1.last_name = 'Smith'
student1.print_name()

print()
print("#11")
'''
Given the following class definition, which of the following is the correct call for the method?
'''
class Games:
    def __init__(self):
        self.fav_game= 'Tennis'
    def print_game(self, diff_game):
        print(f'{self.fav_game} is a better game than {diff_game}')

my_game = Games()
my_game.print_game('Rugby')
#my_game.print_game(self)
#my_game.print_game(self, 'Rugby')
#my_game.print_game()

print()
print("#12")
'''
Which of the following is a correct definition for an instance method, print_age(), that has two parameters, date_of_birth and date_today, passed to it?
'''
print("def print_age(self, date_of_birth, date_today):")


print()
print("#13")
'''
Total marks:    500 
No of subjects: 6
Average Score:  83.3

'''
class Score:
    def __init__(self):
        self.marks = 100
    def print_avg(self, no_of_subjects):
        print(f'Total marks:\t{self.marks}')
        print(f'No of Subjects:\t{no_of_subjects}')
        average = self.marks / no_of_subjects
        print(f'Average Score:\t{average:.1f}')
student1 = Score()
student1.marks = 500
student1.print_avg(6)

print()
print("#14")
'''
A function defined within a class is known as a(n) _________.
'''
print("instance method")

print()
print("#15")
'''
A(n) _________ acts as a factory

that creates instance objects.
'''
print("class object")

print()
print("#16")
'''
A(n) _________ represents a single instance of a class.
Group of answer choices

class object

instance attribute

instance object

class attribute
'''
print("instance object")

print()
print("#17")
'''
Consider the code below. Which of the following is an example of an instance attribute?


class Student:
    def __init__(self):
        self.first_name= 'ABC'
        self.last_name = 'DEF'
    def print_name(self):
        print(self.first_name)
        print(self.last_name)
student1 = Student()
student1.print_name()

'''
print("last_name ")

print()
print("#19")
''''
What is the value of the instance attribute when the following code is run?


class Temperature:
    temp_today = 85
    def __init__(self):
        self.temp= 0
    def print_temp(self, temp_yesterday):
        print(self.temp)
        print(temp_yesterday)
temp1 = Temperature()
temp1.print_temp(90)

'''
print("0")
print()
print("#19")
'''
Functions that are also class attributes are known as _______.
Group of answer choices

instance objects

instance attributes

instance methods

class objects
'''
print("instance methods")
print("")
print("#20")
#Question 20 1 pts
#In the code below, identify the correct instantiation of a new class object.


class Subtract:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2 = num2
    def calculate_diff(self):
        diff = self.num1 - self.num2
        print(diff)

diff1 = Subtract(25, 10)
print("")
print("#21")
class Factorial:
    def __init__(self, num1 = 5):
        self.num1= num1
    def calculate_fact(self):
        fact = 1
        for i in range(1, self.num1 + 1):
            fact *= i
        print(fact)
fact1 = Factorial(2)
fact1.calculate_fact()
print("")
print("#22")
class Student:
    def __init__(self,first_name, last_name, sub='Math'):
        self.sub= sub
        self.first_name = first_name
        self.last_name = last_name
student = Student('Daniel', 'Smith')
print(student.first_name, student.last_name)
print("")
print("#23")
'''
Complete the code to generate 'Rita Williams attends English class' as the output.
class Student:
    def __init__(self,first_name, last_name, sub='Math'):
        self.sub = sub
        self.first_name = first_name
        self.last_name = last_name        
XXX

'''
class Student:
    def __init__(self,first_name, last_name, sub='Math'):
        self.sub = sub
        self.first_name = first_name
        self.last_name = last_name

student1 = Student('Rita', 'Williams', 'English')
print(f'{student1.first_name} {student1.last_name} attends {student1.sub} class')
print("")
print("#24")
'''
A ________ consists of methods to interact with an instance.

class instantiation

class interface

class attribute

class object

'''
print("class interface")
print("A class interface consists of the methods that a programmer calls to create, modify, or access a class instance.")
print("")
print("#25")
'''
Abstraction occurs when a user interacts with an object at a high level, allowing lower-level internal details to remain hidden (aka information hiding or encapsulation). 

Ex: An oven supports an abstraction of a food compartment and a knob to control heat. An oven's user does not need to interact with the internal parts of an oven.

Objects support abstraction by hiding entire groups of functions and variables and exposing only certain functions to a user.

An abstract data type (ADT) is a data type whose creation and update are constrained to specific well-defined operations. A class can be used to implement an ADT.

'''
print("information hiding")
print("")
print("#26")
'''
Which of the following methods is an internal method that the user doesn't need to access?
Group of answer choices

volume()

circumference()

surface_area()

_pi_value()

'''
print("_pi_value()")
print("")
print("#27")
class Company():
    def __init__(self,employees):
        self._employees = employees
    def __len__(self):
        return len(self._employees)
members = Company(['manager','team lead','mentor'])
print(len(members))

print("")
print("#28")
'''
Which of the following code blocks produces 
'The sum of 5 and 3 is 8' as the output?
'''
class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __str__(self):
        return(f'The sum of {self.num1} and {self.num2} is {self.num1 + self.num2}')
print(Sum(5, 3))

print("")
print("#29")
'''
Which of the following is an example of operator overloading?
Numeric operators such as +, -, *, and / can be overloaded using class customization techniques
'''
class SumofPairs:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __str__(self):
        return(f'{self.num1} {self.num2}')

sum1 = SumofPairs(3,4)
print(sum1)

class SumofPairs:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __add__(self, other):
        num1 = self.num1 + other.num1
        num2 = self.num2 + other.num2
        return SumofPairs(num1, num2)

sum1 = SumofPairs(3,4)
sum2 = SumofPairs(1,1)
sum3 = (sum1 + sum2)
print(sum3.num1, sum3.num2)

print("")
print("#30")
print("")
print("#31")
'''
For num_diff = Diff(5, 25)

, complete the code to print the following output when num_diff is printed. First Number: 5 Second Number: 25 Difference: -20
'''
class Diff:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __str__(self):
        return (f'First Number: {self.num1} Second Number: {self.num2} Difference: {self.num1 - self.num2}')

diff1 = Diff(5, 25)
print(diff1 )
print("")
print("#32")
'''
Which operator does the __ge__(self, other) method overload?
Group of answer choices

>

==

!=

>=
'''
print(">=")
print("")
print("")
print("#33")
'''
Which of the following methods overloads the '*' operator?
Group of answer choices

__int__(self, other)

__mul__(self, other)

__prod__(self, other)

__mod__(self, other)
'''
print("__mul__(self, other)	Multiply (*)")
print("")
print("")
print("#34")

class Exponents:
    def __init__(self, a = 1, b = 1):
        self.a = a
        self.b = b
    def __pow__(self, other):
        a = self.a ** other.a
        b = self.b ** other.b
        return (a, b)

e1 = Exponents(4, 2)
e2 = Exponents(2, 2)
print(e1 ** e2)


print("")
print("")
print("#35")
'''
To handle subtraction of arbitrary object types, the built-in isinstance() function can be used. The isinstance() function returns a True or False Boolean depending on whether a given variable matches a given type. The __sub__ function is modified below to first check the type of the right operand, and subtract an hour if the right operand is an integer, or find the time difference if the right operand is another Time24 instance.
Which of the following functions returns a Boolean value depending on whether a given variable matches a given type?

isvalue()

isnan()

isinstance()

isdtype()
'''
print("isinstance()")
print("")
print("#36")
class PairDivision:
    def __init__(self, a = 1, b = 1):
        self.a = a
        self.b = b
    def __floordiv__(self, other):
        a = self.a // self.b
        b = other.a // other.b
        return(a, b)

p1 = PairDivision(10.3, 2.5)
p2 = PairDivision(20.5)
print(p1 // p2)

print("")
print("")
print("#37")
'''
Which of the following code outputs 'The absolute value is 12'?
'''
class PositiveValue:
    def __init__(self, a = 1):
        self.a = a
    def __abs__(self):
        a = abs(self.a)
        return a
p = PositiveValue(-12)
print(f'The absolute value is {abs(p)}')

print("")
print("")
print("#38")
'''
Which of the following requests memory from the operating system?
Group of answer choices

Python compiler

Reference counter

Python runtime

Memory allocation device

'''
print("")
print("#39")
print("")
print("")
print("#40")
print("")
print("")
print("#41")
print("")
print("")
