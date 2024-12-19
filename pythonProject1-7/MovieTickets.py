'''
CHALLENGE ACTIVITY
7.8.3: Nested loops: Print seats.

Integers num_rows and num_columns are read from input representing the number of rows and columns of a theater's seating plan. Complete the nested for loop to output each seat label, as shown in the example. Each seat label is followed by a space, and each row is followed by a newline.

Click each step for instructions:

Step 1
Define the outer for loop to iterate through each row of the theater. Use the loop variable current_row and iterate num_rows times, starting with integer 1.

Step 2
In the outer loop's body, initialize current_column_letter with 'A'.

Step 3
In the outer loop's body, define the inner for loop to iterate through each column of the theater. Use the loop variable current_column and iterate num_columns times, starting with integer 1.

Ex: If the input is:
2
3
then the output is:
1A 1B 1C
2A 2B 2C 
'''

num_rows = int(input())
num_columns = int(input())

for current_row in range(1,num_rows+1):
    current_column_letter = 'A'
    while current_column_letter < chr(ord('A') + num_columns):

        print(f'{current_row}{current_column_letter}', end=' ')
        current_column_letter = chr(ord(current_column_letter) + 1)  # Used to increment letters
    print()