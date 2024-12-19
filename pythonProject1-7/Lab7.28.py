'''
Write a program to draw a right-justified triangle given the height as input. The first row has one asterisk (*) and increases by one for each row. Each asterisk is followed by a blank space and each row ends with a newline.

Ex: If the input is:

3
the output is:

    *
  * *
* * *
'''

num = int(input())

for i in range(num):
    for j in range(num):
        if (j<(num-i -1 )):
           print("  ",end='')
        else:
           print("* ", end='')
    print()