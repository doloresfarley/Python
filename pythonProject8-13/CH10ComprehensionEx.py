# ODD LIST negative list
#[i for i in x if (i < 0) and  (i%2 ==1)]


# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

# Return a list of only even numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print(f'Even numbers only: {even_numbers}')
'''
List raw_list contains floats read from input. Use list comprehension to convert each float in raw_list to a string showing the float to three decimal places. Then, assign adjusted_list with the new list returned by list comprehension.

Click here for example
Ex: If the input is 6.75 0.25 0.5 2.5, then the output is:
Floats: [6.75, 0.25, 0.5, 2.5]

As strings: ['6.750', '0.250', '0.500', '2.500']

Note: f'{x:.3f}' converts float x to a string showing x to three decimal places.
'''

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number + 4 for number in my_list if (number >= 1) and (number % 2 == 1) ]
print(new_list)

raw_list = []

# Read input
for token in input().split():
    raw_list.append(float(token))

adjusted_list = [ f'{i:.3f}' for i in raw_list] # Your code goes here

print(f'Floats: {raw_list}')
print(f'As strings: {adjusted_list}')


'''
List input_list contains integers read from input. Assign accepted_list with the new list containing all the odd numbers in input_list, in that order.

Click here for example
Note: (x % 2 == 0) returns False if x is odd.
'''

# Read input
input_list = [int(x) for x in input().split()]

accepted_list = [x for x in  input_list if (x % 2 == 1) ] # Your code goes here

print(f'All numbers: {input_list}')
print(f'Odd numbers: {accepted_list}')


'''
Integer num_rows is read from input, representing the number of rows in a two-dimensional list. List input_list is a two-dimensional list containing the remaining integers read from input. Assign processed_list with the new list containing the largest value in each row of input_list.

Click here for example
Note: max(a_list) returns the largest element in a_list given that a_list contains numbers only.
'''
# Read input
num_rows = int(input())
input_list = []
for i in range(num_rows):
    input_list.append([int(x) for x in input().split()])

processed_list = [max(x) for x in input_list ]# Your code goes here

print(f'All numbers: {input_list}')
print(f'Largest value in each row: {processed_list}')

'''
Integer num_rows is read from input, representing the number of rows in a two-dimensional list. List input_list is a two-dimensional list containing the remaining integers read from input. Assign computed_result with the largest of all the elements in input_list.

Click here for example
Note: max(a_list) returns the largest element in a_list given that a_list contains numbers only.
'''
# Read input
num_rows = int(input())
input_list = []
for i in range(num_rows):
    input_list.append([int(x) for x in input().split()])

computed_result = max([max(x) for x in input_list ])# Your code goes here

print(f'All numbers: {input_list}')
print(f'Largest element: {computed_result}')