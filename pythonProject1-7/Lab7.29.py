'''
7.29 LAB: Draw upside down triangle

LAB ACTIVITY
7.29.1: LAB: Draw upside down triangle


0 / 10

Write a program that outputs a right triangle of asterisks given the height as input. Each line ends with a blank space.

Ex: If the input is:

3
the output is:

* * *
* *
*
'''

num = int(input())

for i in range(num):
    for j in range(num):
        if (j>(num-i -1 )):
           #print("  ",end='')
           x =1 #NOP
        else:
           print("* ", end='')
    print()