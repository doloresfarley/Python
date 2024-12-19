'''
9.7 LAB: Count characters

LAB ACTIVITY
9.7.1: LAB: Count characters


0 / 10

Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase. The output should include the input character and use the plural form, n's, if the number of times the characters appears is not exactly 1.

Ex: If the input is:

n Monday
the output is:

1 n
Ex: If the input is:

z Today is Monday
the output is:

0 z's
Ex: If the input is:

n It's a sunny day
the output is:

2 n's
Case matters. n is different than N.

Ex: If the input is:

n Nobody
the output is:

0 n's

'''

input1 = input().split()
letter = (input1[0])
input1.remove(input1[0])
input2 = " ".join(input1)
count1 = input2.count(letter)
if count1 == 1:
  print(f'{count1} {letter}')
else:
  print(f'{count1} {letter}\'s')