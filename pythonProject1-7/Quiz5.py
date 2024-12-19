
#Q2
empty_string = ''
print(len(empty_string))

#q3
text_line = 'one fish two fish'
print(text_line[6])

#Q7
my_list = [2, 8, 3, 1, 18, 5]
print("Q7")
print(my_list[3] + my_list[1] * 2)

names_list = ['one', 'two', 'three']
digits_list= ['1', '2', '3']
names_list = names_list + digits_list

print(names_list)
'''
Question 11 1 pts
Which statement correctly explains a difference between lists and tuples?
Group of answer choices

List items use [ ] operators to access items by index, while tuples use ( ) operators to access items by index.

The built-in function len() works with lists but not with tuples.

List items can be changed, while tuple items can’t be changed. <-------------

List items can be of any type, while tuple types can only be numbers.
'''

my_set = set([1, 2, 3, 7, 8, 9, 10] )
my_set.pop()
print(my_set)

#17
my_set = {1, 2, 3, 4, 5, 6}
other_set = {2, 4, 6}
result_set = my_set.union(other_set)
print(result_set)

#18
my_set = {1, 2, 3, 4, 5, 6}
other_set = {2, 4, 6}
result_set = other_set.difference(my_set)
print(len(result_set))
print(result_set)

# A dictionary is a Python container used to describe associative relationships
'''Dictionaries are containers used to describe a(n) associative relationship.
Group of answer choices

associative

isolated

one-to-one

recursive'''

# Question 20
emails_dict = {
    'C2104': "myemail@aol.com",
    'Cristiano Ronaldo': "myemail2@aol.com",
}

print(emails_dict['C2104'])

#Question 21
# A __KEY___ can be located in a dictionary and is associated with a value.

# Question 22
'''
Which statement changes the value associated with key "Lemon" to 0.75 in the dictionary fruits_dict?
Group of answer choices

fruits_dict[0.75] = "Lemon"
 
dict("Lemon") = fruits_dict[0.75]
 
fruits_dict["Lemon"] = 0.75 <-----
 
fruits_dict[Lemon] = 0.75

'''
fruits_dict = {
    'Lemon': 123,
    'Cristiano Ronaldo': 345,
}
fruits_dict["Lemon"] = 0.75
print(fruits_dict)

#q23
# Which statement removes entry "1G1JB6EH1E4159506" from the dictionary cars_dict?
cars_dict = {
    '1G1JB6EH1E4159506': 123,
    '1G1JB6EH1E4159597': 345,
}
print(cars_dict)
del cars_dict["1G1JB6EH1E4159506"]
print(cars_dict)

#Q24
'''
string, immutable sequence type

A string is an immutable sequence of characters.
The other options are incorrect:

set, mutable unordered collection

A set is a mutable, unordered collection of unique elements.

int is a numeric type, but it's an integer, not a floating-point type.
tuple is an immutable sequence type, not mutable.
dict is a mutable mapping type, not an immutable sequence type.
'''
#Q25
# Which data type is the correct choice to store the number of wins associated with each basketball team in the NBA?
# dict

#Q26
# Which data type is the correct choice to store a student's test scores in chronological order?
# list

'''
Which data type is the correct choice to store the names of all the hockey players who have scored 3 or more goals in a single game in no specific order?
set

A set is ideal for storing the names of all hockey players who have scored 3 or 
more goals in a single game because it is an unordered collection that automatically 
ensures unique elements (i.e., no duplicate player names).

'''

sales = { "apples": 0, "lemonade": 0 }
sales["apples"] = sales["apples"] + 1
del sales["lemonade"]
#ERROR print(len(0))
#print(len(sales["apples"]))

'''
Q29
Which of the following expressions causes an implicit conversion between types? Assume variable x is an integer, t is a float, and name is a string.
Group of answer choices
#Both x and 2 * x are integers, so no conversion occurs.
x + 2 * x
 
#This explicitly converts the float t to a string; thus, it’s not implicit.
print(str(t))
 
7.5 + (x / 2)

#This explicitly converts name (a string) to a string again, so there’s no conversion happening.
"Hello, " + str(name)

ANSWER: 7.5 + (x / 2)
'''
value =  1 + int(3.5) / 2
value2 = int(3.5)
print(value2)

#Q32
# What is the result of the expression: int('1750.0')?
# An error: the string does not represent an integer value
# print(int('1750.0'))

#Q40
print(f'{"Tokyo":s} had {9.273:f} million people in {2015:d}')

#Q11
tuple1 = (1,2,3,4)
print(len(tuple1))

#q12
west_cities = ('Vancouver', 'Portland', 'Eugene')
print(west_cities)


my_set2= { 1,2,3,4,5}
print(my_set2.pop())


valuestr='156.6'
valuef = float(valuestr)
# ERROR
# print(int( valuestr))
print(int( valuef))

value43 = 43
print(f'{value43:X}')

companies = { 'Apple', 'Microsoft', 'Google', 'Amazon' }
# ERROR
# companies.pop(2)
companies.remove('Google')
print(companies)