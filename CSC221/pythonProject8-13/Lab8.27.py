'''
LAB ACTIVITY
8.27.1: LAB: Convert to binary - functions


0 / 10

Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2
Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

Ex: If the input is:

6
the output is:

110
The program must define and call the following two functions. Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() that takes an input string as a parameter and returns a string representing the input string in reverse.
def int_to_reverse_binary(integer_value)
def string_reverse(input_string)
'''

# Define your functions here.
def int_to_reverse_binary(integer_value):
    binary_string = ""
    #print( __name__)
    while integer_value > 0:
        binary_string += str(integer_value % 2)  # Append remainder to the string (binary digit)
        integer_value = integer_value // 2  # Update integer_value to be integer division by 2
    return binary_string

def string_reverse(input_string):
    #print(__name__)
    return input_string[::-1]  # Reverse the string using slicing


if __name__ == '__main__':
    # Type your code here.
    # Your code must call int_to_reverse_binary() to get
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    x = int(input())
    reverse_binary = int_to_reverse_binary(x)  # Convert to reverse binary
    final_binary = string_reverse(reverse_binary)  # Reverse the string to get the correct binary
    print(final_binary)
