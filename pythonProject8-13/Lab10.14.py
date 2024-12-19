'''
10.14 LAB: Subtracting list elements from max - functions

LAB ACTIVITY
10.14.1: LAB: Subtracting list elements from max - functions


10 / 10

When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers. For this program, adjust the values by subtracting each value from the maximum. Input values should be added to the list until -1 is entered.

Ex: If the input is:

30
50
10
70
65
-1
the output is:

40
20
60
0
5
Your program must define and call the function:
def get_max_int(nums)

Note: get_max_int() returns the maximum value in the list.
'''


def get_max_int(nums):
    max_data = max(nums)
    return max_data


if __name__ == '__main__':
    key = int(input())
    number = []
    while (key != -1):
        number.append(key)
        key = int(input())

    max_data = get_max_int(number)

    for n in number:
        print(max_data - n)
