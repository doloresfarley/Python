names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

result_set0 = names1;
print(result_set0)
result_set0 = result_set0.difference(names4)
print(result_set0)
# Union names1 and names2
result_set = names1
print(result_set)
result_set = result_set.symmetric_difference(names4)

print(result_set)

# Intersection btwn result_set and names3
result_set = result_set.intersection(names3)
print(result_set)
# Difference btwn result_set and names4
result_set = result_set.difference(names4)
print(result_set)

data = (1,2,3,4,5,6,7,8,9,10)
for r in data:
    print(r)
