'''


Write a program that reads a list of 10 integers, and outputs those integers in reverse. For coding simplicity, follow each output integer by a space, including the last one. Then, output a newline.

Ex: If the input is:

2 4 6 8 10 12 14 16 18 20
the output is:

20 18 16 14 12 10 8 6 4 2
To achieve the above result, first read the integers into an array. Then output the array in reverse.

597432.4355728.qx3zqy7
LAB ACTIVITY
12.8.1: LAB: Arrays: Output numbers in reverse

'''

'''
integer array(10) userInts
integer i
integer temp
integer half

half = 5
for i = 0; i < userInts.size; i = i + 1
   userInts[i] = Get next input
   
for i = 0; i < half; i = i + 1
   temp = userInts[i] 
   userInts[i] = userInts[userInts.size -1 -i] 
   userInts[userInts.size -1 -i] = temp

for i = 0; i < userInts.size; i = i + 1
   Put userInts[i] to output
   Put " " to output

Put "\n" to output

'''
'''
integer currValue
integer midIndex
integer i

currValue = Get next input

while (currValue >= 0) and (i < 9)
   userValues[i] = currValue
   currValue = Get next input
   i = i + 1

if currValue >= 0
   Put "Too many inputs" to output
else
   midIndex = i / 2
   Put userValues[midIndex] to output

'''