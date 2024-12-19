'''

12.9 LAB: Arrays: Middle item

Given a sorted list of integers, output the middle integer. A negative number indicates the end of the input (the negative number is not a part of the sorted list). Assume the number of integers is always odd.

Ex: If the input is:

2 3 4 8 11 -1
the output is:

4
The maximum number of inputs for any test case should not exceed 9 positive values. If exceeded, output "Too many inputs".

Hint: Use an array of size 9. First read the data into an array. Then, based on the number of items, find the middle item.


'''
'''
integer array(5) userInts
integer i
integer count
integer input1
i = 0
count = 0
input1 = 0
while i < 5
   userInts[i]  = Get next input
   i = i + 1

input1 =  Get next input

for i = 0; i<userInts.size; i =i +1
   if userInts[i] < input1
      count = count + 1
      Put userInts[i] to output
      Put " " to output

if count == 0
   Put input1 to output
   Put " " to output
Put "\n" to output      
   
'''
''''
integer array(10) userInts
integer i

for i = 0; i < userInts.size; i = i + 1
   userInts[i] = Get next input

for i = userInts.size - 1; i >= 0; i = i - 1
   Put userInts[i] to output 
   Put " " to output
Put "\n" to output

'''