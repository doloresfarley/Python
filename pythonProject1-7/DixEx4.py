word_to_num = {
	'forty': 40, 'one': 1, 'two': 2, 'three': 3,
	'four': 4, 'five': 5, 'six': 6, 'seven': 7,
	'eight': 8, 'nine': 9
}

''' Your code goes here '''
word1 = input()
word2 = input()
num1 = word_to_num[word1]
num2 = word_to_num[word2]
print(num1 + num2)