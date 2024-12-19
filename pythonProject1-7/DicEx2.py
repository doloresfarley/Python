test_scores = {'Fay': 43, 'Noa': 17}

''' Your code goes here '''
student = input()
print(test_scores[student])
del(test_scores[student])
print('Remaining pairs:')
print(test_scores)