names_set1 = {'Del'}
names_set2 = set() # Empty set
names_set2.add(input())
names_set2.add(input())
names_set2.add(input())

''' Your code goes here '''
names_set1.update(names_set2)
names_remove = input()
names_set1.remove(names_remove)
names_add = input()
names_set1.add(names_add)

print(f'names_set1: {sorted(names_set1)}')
print(f'names_set2: {sorted(names_set2)}')