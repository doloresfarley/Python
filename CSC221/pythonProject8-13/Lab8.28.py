'''8.28 LAB: Swapping variables

LAB ACTIVITY
8.28.1: LAB: Swapping variables


0 / 10

Define a function named swap_values that takes four integers as parameters and swaps the first with the second, and the third with the fourth values. Then write a main program that reads four integers from input, calls function swap_values() to swap the values, and prints the swapped values on a single line separated with spaces.

Ex: If the input is:

3
8
2
4
function swap_values() returns and the main program outputs:

8 3 4 2
The program must define and call the following function.
def swap_values(user_val1, user_val2, user_val3, user_val4)
'''
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3


if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    t,u,v,w = swap_values(num1, num2, num3, num4)
    print(t,u,v,w)