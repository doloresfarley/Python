

colors = ['red', 'green', 'blue']

colors[1] = 'yellow'  # Change list element
print(colors)
fav_color = colors # NOT COPY REFF
fav_color_copy = colors[:] # COPY REFF
colors[0] = 'black'
print("REF: ",fav_color)
print("COPY: ",fav_color_copy)
print()

fav_color = colors[2]  # Bind to 'blue'
print(fav_color)
fav_color = 'turquoise'  # List not altered
print(colors)
print(fav_color)


vals = [1, 4, 16]

vals.append(9)
vals.insert(2, 18)
value = vals.pop()
vals.remove(4)
# vals.remove(55)  # Errors out
my_list = [55, 6, 20, 22, 7]
my_list.sort()
my_list.pop()
print(my_list)


# Using the sorted() function
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]

# Using the sort() method
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 5, 8]

# Sorting in descending order
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [8, 5, 3, 2, 1]

# Sorting strings
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']

# Sorting by a specific key
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)  # Output: [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}, {"name": "Charlie", "age": 35}]



my_list = [[25], [15, 25, 35], [10, 15]]

sorted_list = sorted(my_list, key=max)

print(f'Sorted list: {sorted_list}')

sorted_list = sorted(my_list)

print(f'Sorted list: {sorted_list}')

# x= ['Serena Williams', 'Venus Williams', 'john McEnroe', 'rafael Nadal']
x = ["a","b","c","d","A","B","C","D"]
x.sort( )
print(x)
#Sort the elements of x so the greatest element is in position 0.
x.sort( reverse =True)
print(x)

#Arrange the elements of x from lowest to highest, comparing the upper-case variant of each element in the list.
x.sort( key=str.upper)

print(x)