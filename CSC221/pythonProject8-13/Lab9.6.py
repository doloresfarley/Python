'''

zyBooks catalog
Help/FAQ
9.5 LAB: Checker for integer string
Students:
Section 9.6 is a part of 1 assignment:
Ch 9
Includes:

zyLab
Due: 11/06/2024, 6:30 PM EST
9.6 LAB: Name format

LAB ACTIVITY
9.6.1: LAB: Name format


10 / 10

Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.

'''
name = input().split()
dot = '.'
first = ""
if len(name[0]) >0:
    first = name[0][0].upper() + dot
middle = ""
if len(name[1]) >0:
    middle = name[1][0].upper() + dot
last =""
if len(name) >2:
    last = name[2] + ", "
    print(f'{last}{first}{middle}')
elif len(name) == 2:
    last = name[1] + ", "
    print(f'{last}{first}')
#lastName, firstInitial.middleInitial.
