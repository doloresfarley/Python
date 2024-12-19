'''
9.9 LAB: Palindrome

LAB ACTIVITY
9.9.1: LAB: Palindrome


0 / 10

A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

palindrome: bob
Ex: If the input is:

bobby
the output is:

not a palindrome: bobby
Hint: Start by removing spaces. Then check if the string equals itself in reverse.
'''

data = input()
org = data
data = data.replace(" ","")
pal = data[::-1]

if data == pal:
    print(f'palindrome: {org}')
else:
    print(f'not a palindrome: {org}')