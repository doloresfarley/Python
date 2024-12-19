'''

My library
>
CSC 221: Introduction to Problem Solving and Programming home
>
8.30: LAB: A jiffy
zyBooks catalog
Help/FAQ
8.29 LAB: Fibonacci sequence
Your score for Ch 8 is higher in the zyBook than in canvas. Resubmit latest score?


Resubmit latest score
Students:
Section 8.30 is a part of 1 assignment:
Ch 8
Includes:

zyLab
Due: 10/30/2024, 6:30 PM EDT
8.30 LAB: A jiffy

LAB ACTIVITY
8.30.1: LAB: A jiffy


0 / 10

In computer animation, a "jiffy" is commonly defined as 1/100th of a second. Define a function named jiffies_to_seconds that takes the number of "jiffies" as a parameter, and returns the number of seconds. Then, write a main program that reads the number of jiffies (float) as an input, calls function jiffies_to_seconds() with the input as argument, and outputs the number of seconds.

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

Ex: If the input is:

15.25
the output is:

0.152
The program must define and call the following function:
def jiffies_to_seconds(user_jiffies)
'''

def jiffies_to_seconds(user_jiffies):
    return user_jiffies/100.0


if __name__ == '__main__':
# Type your code here. Your code must call the function.
    num1 = float(input())
    num1 = jiffies_to_seconds(num1)
    print(f'{num1:.3f}')
