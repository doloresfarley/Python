'''
7.23 LAB: Print string in reverse

LAB ACTIVITY
7.23.1: LAB: Print string in reverse


0 / 10

Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
'''

str = input()

while str !="Done" or  str !="done" or str !="d":
    for output1 in reversed(str):
        print(output1, end='')
    print()
    str = input()
