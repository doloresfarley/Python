'''
10.11 LAB: Middle item

LAB ACTIVITY
10.11.1: LAB: Middle item


10 / 10

Given a sorted list of integers, output "Middle item: " followed by the middle integer. Assume the number of integers is always odd.

Ex: If the input is:

2 3 4 8 11
the output is:

Middle item: 4
The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".

Hint: First read the data into a list. Then, based on the list's size, find the middle item.

'''
input_list = input().split(" ")

if len(input_list) > 9:
    print("Too many inputs")
else:
    print(f'Middle item: {input_list[len(input_list)//2]}')