person_name1 = input()
test_score1 = int(input())
person_name2 = input()
test_score2 = int(input())
person_name3 = input()
test_score3 = int(input())
person_name4 = input()
test_score4 = int(input())

''' Your code goes here '''
test_scores = {person_name1: test_score1, person_name2: test_score2, person_name3: test_score3, person_name4: test_score4}

print(f'{person_name1}: {test_scores[person_name1]}')
print(f'{person_name2}: {test_scores[person_name2]}')
print(f'{person_name3}: {test_scores[person_name3]}')
print(f'{person_name4}: {test_scores[person_name4]}')