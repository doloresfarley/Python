numbers_selected = {19, 47}

new_number = int(input())

''' Your code goes here '''
numbers_selected.add(new_number)
num_numbers = len(numbers_selected)

print(sorted(numbers_selected))
print(f'Number of values selected: {num_numbers}')