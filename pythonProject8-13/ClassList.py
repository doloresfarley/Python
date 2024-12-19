def chanfeList(mlist):
    mlist.append("Helli")

my_list = [1,2,3,4,5]
my_list2 = [1,2,3,4,5]
chanfeList(my_list)
print(my_list)

new_list = my_list = my_list2
print(new_list)
x = list("123abcdefghi")