scores_dict = {'Mai': 58, 'Zoe': 68}
print('Original:')
print(scores_dict)

''' Your code goes here '''
key = input()
scores_dict[key] = 2*scores_dict[key]

print('Updated:')
print(len(scores_dict))