for token in tokens:
    values_list.append(int(token))

print(f'Raw samples: {values_list}')

num_good = 0

for num, value in enumerate(values_list):
    if value < 50:
       num_good+=1
       print(f'Sample {num} is good')
    else:
       print(f'Sample {num} needs attention')

print(f'Total good samples: {num_good}')

print(f'All data: {blood_samples}')

all_good = True

for num, blood in enumerate(blood_samples):
    if num % 2 == 0:
        print(f'Index {num}: {blood}')
        if blood >= 45:
            all_good = False

if all_good:
    print('All integers at even indices are less than 45.')
else:
    print('At least one integer at an even index is greater than or equal to 45.')

# Read input and split input into tokens
tokens = input().split()

trend_data = []
for token in tokens:
    trend_data.append(int(token))

print(f'Sequence: {trend_data}')

for index, data in enumerate(trend_data):
   if 0 < index < len(trend_data) -1:
       if trend_data[index] < trend_data[index-1] and trend_data[index] < trend_data[index+1]:
           print(f'Dip: {trend_data[index-1]} {trend_data[index]} {trend_data[index+1]}')

'''
Integer num_tours is read from input, representing the number of rows of data remaining in the input. Two-dimensional list tour_lists consists of data read from the remaining input, with each row representing the locations visited in a tour group. For each row of tour_lists:

Output 'Tour ', the row index plus 1, and ':' on one line.
Output all the elements in the row on the next line, ending each element with a space.
Click here for example
Note:

enumerate() returns the index and the value of the list element in the current iteration.
print(x, end=' ') outputs x and ends with a space instead of a default newline.

'''

num_tours = int(input())
tour_lists = []
for row_index in range(num_tours):
    tour_lists.append(input().split())

for index, tours in enumerate(tour_lists):
    print(f'Tour {index+1}:')
    for index, col in enumerate(tours):
        print(col, end=' ')
    print()


'''
10.5.1: List nesting.

597432.4355728.qx3zqy7

Jump to level 1
Integer grid_size is read from input, 
representing the number of rows and columns of a two-dimensional list. 
Two-dimensional list grid_2d is created with zeros, 0, as the initial values. 
For each element at row index j and column index k of grid_2d, 
assign the element with the sum of j and k.
'''
grid_2d = []
for j in range(grid_size):
    row = []
    for k in range(grid_size):
        row.append(0)
    grid_2d.append(row)

for j,row in enumerate(grid_2d):
  for k,col in enumerate(row):
        grid_2d[j][k] = j+k

for row in grid_2d:
    for cell in row:
        print(cell, end=' ')
    print()



'''
Jump to level 1
List food_list contains words read from the first line of input. List food_to_avoid contains words read from the second line of input. For each element in food_list that is also in food_to_avoid:

Output the element, followed by ' avoided'.
Remove the element from food_list.
'''
food_list = input().split()
food_to_avoid = input().split()

print('Food on menu:', end=' ')
for food in food_list:
    print(food, end=' ')
print()

print('Food to avoid:', end=' ')
for food in food_to_avoid:
    print(food, end=' ')
print()
copy_food = food_list[:]

for food in copy_food:
    if food in food_to_avoid:
        print(f'{food} avoided')
        food_list.remove(food)

print('Safe to eat:', end=' ')
for food in food_list:
    print(food, end=' ')
print()