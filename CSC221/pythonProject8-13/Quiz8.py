#2
print("Q2")
def print_sum(num1, num2):
    print(num1 + num2)


y = print_sum(4, 5)
print(y)
print()


# 4
#What is the result when the program is executed?
'''
def add(x, y):
    return x + y


print('Begin test')
s = add('Hello', 5)
print(s)
print('End test')

#
# Begin test
 File "~/PycharmProjects/pythonCSC221/pythonProject8-13/Quiz8.py", line 10, in <module>
    s = add("Hello", 5)
        ^^^^^^^^^^^^^^^
  File "~/PycharmProjects/pythonCSC221/pythonProject8-13/Quiz8.py", line 6, in add
    return x + y
           ~~^~~
TypeError: can only concatenate str (not "int") to str
'''

# 12
def calc_square(x):
    return x * x
t = calc_square(calc_square(2))
#t = calc_square(4) * calc_square(2)

print(t)

#13
def calc_cube(x):
    return x * x * x
def display(x):
    print(x)

display(calc_cube(2.0))

#calc_cube(x) = 8.0

#14
'''
In some cases, a programmer may want a program to stop executing if an unfinished function is called. Ex: A program that requires user input should not execute if the user-defined function that gets input is not completed. In such cases, a NotImplementedError can be generated with the statement raise NotImplementedError. The NotImplementedError indicates that the function is not implemented and causes the program to stop execution. NotImplementedError and the "raise" keyword are explored elsewhere in material focusing on exceptions. The following demonstrates an error being generated by a function stub:

Figure 8.5.3: Stopping the program using NotImplementedError in a function stub.
import math

def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError
        
def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter

coordinates = get_points(3)
print(f'Perimeter of triangle: {get_perimeter_length(coordinates)}')
'''
#Raise NotImplementedError
#17
def print_water_temp_for_coffee(temp):
    if temp < 195:
        print('Too cold.')

    elif (temp >= 195) and (temp <= 205):
        print('Perfect temperature.')

    elif (temp > 205):
        print('Too hot.')


print_water_temp_for_coffee(205)
print_water_temp_for_coffee(190)

#18
def print_fever_check(temperature):
    NORMAL_TEMP = 98.6
    CUTOFF_TEMP = 95
    degrees_of_fever = 0
    if (temperature > NORMAL_TEMP):
        degrees_of_fever = temperature - NORMAL_TEMP
        print(f'You have {degrees_of_fever:f} degrees of fever.')
    elif (temperature < CUTOFF_TEMP):
        degrees_of_fever = CUTOFF_TEMP - temperature
        print(f'Your temperature is {degrees_of_fever:f} below 95.')


body_temperature = 96.0
print('Checking for fever...')
print_fever_check(body_temperature)

#19
def print_shipping_charge(item_weight):
   if (item_weight > 0.0) and (item_weight <= 10.0):
      print(item_weight * 0.75)
   elif (item_weight > 10.0) and (item_weight <= 15.0):
     print(item_weight * 0.85)
   elif (item_weight > 15.0) and (item_weight <= 20.0):
      print(item_weight * 0.95)


print_shipping_charge(18)
print_shipping_charge(6)
print_shipping_charge(25)

def find_min_value(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <=c:
        return b
    else:
        return c


w1 = 7
w2 = 3
w3 = 12
y = find_min_value(w1, w2, w3)/2 + 1
print(y)

#22
def print_x_eyes():
    print('x  x')


def print_o_eyes():
    print('o  o')


def face(eyes):
    eyes()
    print(' >  ')
    print('----')

face(print_x_eyes)

#23
def print_hello():
    print('hello')

alternate = print_hello
alternate()

#24
def print_message1():
    print('Message #1')


def print_message2():
    print('Message #2')

print_message0 = print_message1 #fix warning
print_message1 = print_message2
print_message2 = print_message1
print_message1()
print_message2()
#OUTPUT:
#Message #2
#Message #2

#25
def find_sqr(a):
   t = a * a
   return t
square = find_sqr(10)
print(square)


#27
def compute_sum_of_squares(num1, num2): # Line 1
  sum = (num1 * num1) + (num2 * num2)   # Line 2
  return                                # Line 3

#28
'''
print("#28")
cone_vol = cone_volume(2, 4)
print(cone_vol)


def compute_square(r):
    return r * r


def cone_volume(r, h):
    return (0.33) * 3.14 * compute_square(r) * h
# NameError: name 'cone_volume' is not defined
'''

'''
#28
def is_even(num):
    if num % 2 == 0:
        even = True
    else:
        even = False


is_even(7)
print(even)
NameError: name 'even' is not defined
'''
#30
LB_PER_KG = 2.2

def kgs_to_lbs(kilograms):
   pounds = kilograms * LB_PER_KG
   return pounds

pounds = kgs_to_lbs(10)
print(pounds)

'''
#31
A namespace is a normal Python dictionary whose keys are the names and whose values are the objects. 
A programmer can examine the names in the current local and global namespace by using the  locals() and globals() built-in functions.
'''
print("Q30")
x = 10
y = 20

# Access the global namespace
global_namespace = globals()

# Print the namespace dictionary
print(global_namespace)


'''
#32
"Namespace scope."

Python manages namespaces using three main scopes:

Local scope: Refers to variables defined within the current function.
Global scope: Refers to variables defined at the top level of a module or script.
Built-in scope: Refers to names that are pre-defined in Python, such as len() or print().
There is no specific "Namespace scope." "Namespace" refers to the concept of how Python organizes and manages variable names, but it is not a specific scope.
'''

'''

'''
#Q33
print("Q33")
x = 10  # Global scope

def my_function():
    x = 5  # Local scope
    print(x)  # This will print 5, the local variable

my_function()
print(x)  # This will print 10, the global variable
print("")
#34
print("#34")

multiplier = 1
def do_multiplication(x):
     return x * multiplier


def set_multiplier(x):
    global multiplier
    multiplier = x


user_value = 5
set_multiplier(2)
print(do_multiplication(user_value))

# 35
# The process of searching for a name in the available namespaces is called scope resolution.

#39
print("q39")
def modify(names, score):
    names.append('Robert')
    score = score + 20


players = ['James', 'Tanya', 'Roxanne']
score = 150
modify(players, score)
print(players, score)

#40
print("Q40")
def reset(data):
    data[1] = 34
    print(data)
data = [15, 0, 47, 12, 0]
reset(data)
print(data)

#41 Which function call would cause a logic error?
def print_product(product_name, product_id, cost):
   print(f'{product_name} (id: #{product_id}) - ${cost:.2f}')


#print_product('Speakers', cost=32.99, product_id=21224)
#print_product(product_id=21224, product_name='Speakers', cost=32.99)
#print_product('Speakers', 21224, 32.99)
print_product('Speakers', 32.99, 21224) # logic error

#42
print("42")
def print_app(app_id, plan='basic', term=30):
   print(f'App:{app_id} ({plan} plan, {term} days)')
print_app(10032, term=14)

'''
A common error is to provide a mutable object, like a list, as a default parameter. 
Such a definition can be problematic because the default argument object is created only once, at the time the function is defined
 (when the script is loaded), and not every time the function is called.
  Modification of the default parameter object will persist across function calls, 
  which is likely not what a programmer intended. 
  The below program demonstrates the problem with mutable default objects and illustrates a solution that creates a new empty list each time the function is called.
'''


#43
def display(product, options=[]):
    if 'monitor' in product:
        options.append('HDMI')

    print(product, options)

display('Acer monitor')
display('Samsung monitor')

#44
def purchase(user_name, id_number=-1, item_name='None', quantity=0):
    print()
    # ... process a user's purchase as required ...
#ERROR:  purchase(item_name='Orange', 10)

#45
# One or both of *args or **kwargs can be used. They must come last (and in that order if both are used) in the parameter list, otherwise an error occurs.
#Adding a final function parameter of **kwargs, short for keyword arguments, creates a dictionary containing "extra" arguments not defined in the function definition.
#The keys of the dictionary are the parameter names specified in the function call.

#46
def concat(*args):
    s = ''
    for item in args:
        s += ' ' + item
    return s

print(concat('red', 'fish', 'blue', 'fish'))
#print(concat(red), concat(fish), concat(blue), concat(fish))

#47
def gen_command(application, **kwargs):
    command = application
    for key in kwargs:
        value = kwargs[key]
        command += f' --{key}={value}'
    return command


print(gen_command('ls', color='always', sort='size', format='long'))

def get_stats(int_list):
    result_sum = 0
    result_min = int_list[0]
    result_max = int_list[0]
    for value in int_list:
        result_sum += value
        if value < result_min:
            result_min = value
        if value > result_max:
            result_max = value


    return result_sum, result_min, result_max


values = [ 6, 4, 12, 8 ]
c,a,b = get_stats(values)
print(f'{a}, {b}, {c}')

#49
import math
def get_random_pair():
    a =2
    b = 2
    return a, b

[x,y] = get_random_pair()
'''
#50
Which symbols are used to start and end a docstring?
'''

#51  A docstring is a string literal placed in the first line of a function body.
'''
def num_seats(airliner_type):
    """Determines number of seats on a plane"""
    #Function body statements ...

def ticket_price(origin, destination, coach=True, first_class=False):
    """Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.

    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport

    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket (default False)

    """
    #Function body statements ...

'''
#56
def calc(num1, num2):
    return 1 + num1 + num2


print(calc(4, 5), calc(1, 2))

'''
#60
Which function gives the change in temperature for an object, given the heat transfer, mass and specific heat capacity? Note that Q=mcΔT

, where Q is heat transfer, m is mass, c is specific heat capacity, and ΔT

is the change in temperature.
ΔT = Q/mc
'''

#61
def final_velocity(initial_velocity, distance, time):
    return 2 * distance / time - initial_velocity


def meters_to_feet(distance_in_meters):
    return 3.28084 * distance_in_meters


# display final velocity in feet per second
t = 35 # seconds
d = 7.2 # meters
v_i = 4.6 # meters / second
print(f'Final velocity: {final_velocity(meters_to_feet(v_i), meters_to_feet(d), t):f} feet/s')

# SeedRandomNumbers(11)
