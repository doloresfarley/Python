'''

LAB ACTIVITY
7.22.1: LAB: Output range with increment of 5


0 / 10

Write a program whose input is two integers.
Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.


'''

first = int(input())
second = int(input())

if second < first:
    print('Second integer can\'t be less than the first.')
else:
    while first <= second:
        print(first, end=' ')
        first = first + 5
    print()