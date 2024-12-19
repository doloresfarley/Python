'''
12.10 LAB: Arrays: Output values below an amount

Write a program that first reads a list of 5 integers from input. Then, read another value from the input, and output all integers less than or equal to that last value.

Ex: If the input is:

50 60 140 200 75 100
the output is:

50 60 75
For coding simplicity, follow every output value by a space, including the last one. Then, output a newline.

Such functionality is common on sites like Amazon, where a user can filter results.

597432.4355728.qx3zqy7
LAB ACTIVITY
12.10.1: LAB: Arrays: Output values below an amount
0 / 10




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
'''
integer i
integer j
integer array(5) userValues
integer upperThreshold

for i = 0; i < userValues.size; i = i + 1
   userValues[i] = Get next input

upperThreshold = Get next input

for j = 0; j < userValues.size; j = j + 1
   if userValues[j] <= upperThreshold
      Put userValues[j] to output
      Put " " to output

Put "\n" to output
'''