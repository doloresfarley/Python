numbers = '0123456789'

print(f'All numbers: {numbers[::]}')
print(f'Every even number: {numbers[::2]}')
print(f'Every odd number: {numbers[1::2]}')
print(f'Every third number between 1 and 8: {numbers[1:9:3]}')
print(f'Number in reversed: {numbers[::-1]}')
print(f'Find empty return index: {numbers.find('',3)}')


phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''.join(phrases)
print(sentence)
song = "I scream; you scream; we all scream, for ice cream."
print(song.split('\n'))

print(f'Number in odds in reversed: {numbers[::-2]}')
print(f'Number in evens in reversed: {numbers[-2::-2]}')