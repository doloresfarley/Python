# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student1 = collections.namedtuple('Student', ['name', 'age', 'DOB'])
Student2 = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student1('Nandini', '19', '25-4-1997')

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))
print(S.DOB)

empty_string = ''
print(len(empty_string))
text_line = 'one fish two fish'
print(text_line[6])

my_list = [2, 8, 3, 1, 18, 7]
print(my_list[3] + my_list[1] * 2)
my_list.pop(len(my_list)-1)
#print(my_list)

#my_list.remove(len(my_list)-1)
print(my_list)