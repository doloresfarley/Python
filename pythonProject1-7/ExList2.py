set1 = {"Apple","Bananna","GGGG"}
my_list =["John",set1, "Jake","Shannon"]

print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[0][3])

# Although List element is mutable,
# The String as an element of a list is immutable
# my_list[0][0] = 'j'

my_list[0] = 'john'
#my_list[1] = 5
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[0][3])

print(my_list[1])