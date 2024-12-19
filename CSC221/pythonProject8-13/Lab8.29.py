'''

LAB ACTIVITY
8.29.1: LAB: Fibonacci sequence


0 / 10

The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use a for loop and DO NOT use recursion.
'''
def fibonacci(n):
    # Type your code here.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n <0:
        return -1
    else:
        x1 = 0
        x2 = 1
        curr = 0
        for i in range(2,n+1):
            curr = x1 + x2
            x1 = x2
            x2 = curr
        return curr

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')