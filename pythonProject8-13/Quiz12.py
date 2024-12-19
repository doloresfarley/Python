'''
Question 1 1 pts
Given an array numList of size 5, and x = 3, which is an invalid access for the array?
Group of answer choices

Put numsList[x] to output

Put numsList[x-3] to output

Put numsList[(2*x) - x] to output

Put numsList[x+2] to output

'''
x=3
numsList =[0,1,2,3,4]
print(numsList[x] )
print(numsList[x-3] )
print(numsList[(2*x) - x] )
# print(numsList[x+2] ) <<<--- ERrror
'''
Given integer array examScores, which is a valid assignment? Assume x is an integer variable.
Group of answer choices

x = examScores + 5

examScores = x

x = examScores[4] + 5 <<-answer

x[4] = examScores
'''
'''
Given array examScores, which assigns variable newScore with the examScores array element at the index ONE BEFORE the value held in variable i?
Group of answer choices

newScore = examScores[i] - 1

newScore = examScores[i + 1] 

newScore = examScores[i - 1] <<-- Answer

newScore = examScores[i]
'''

'''

Question 4
Which assigns the last element of the examScores array of size n with the value 95?
Group of answer choices

examScores = 95

examScores[n] = 95

examScores[n-1] = 95 <--1 Answer

examScores[0] = 95

'''
'''
Question 5 1 pts
How is the size of the array myArray accessed?
Group of answer choices
Note below that in Coral,
 an array stores a size attribute, indicating the number of array elements.

myArray.length

myArray[size]

myArray.getSize

myArray.size <<--Answer

'''
'''
Which code sets the integer value to the sum of the first and last elements of the array myArray?
Group of answer choices

value = myArray[1] + myArray[size]

value = myArray[0] + myArray[size - 1]  <<--Asnwer

value = myArray[1] + myArray[size - 1]

value = myArray[0] + myArray[size]
'''

'''
The array userVals holds 5 integers. What is output?
In Coral, an array is initialized with all its elements set to 0 by default. This means that when you declare an array, all its elements automatically hold the value 0 unless explicitly assigned otherwise.
'''

'''
Q9
'''
x=4
y=8
x=y
y=x
x = y
print()
print(x)
print(y)

'''
Q10

'''
a=10
b=25
tmp = a
a =b
b = tmp
print()
print(a)
print(b)
'''
Given an array with values 5, 10, 15, 20, 25, what are the fewest number of swaps needed to reverse the list?
Group of answer choices

2 <<Answer

3

5

4
'''
'''
Which is an invalid access for the array?


integer x
integer array(3) numsList
numsList[0] = 1
numsList[1] = 2
numsList[2] = 0
x = 3
Group of answer choices

numsList[numsList[2]]

numsList[(x - 4) + 1]

numsList[(x * 2) - 3] <<--Anser numsList[3] 

numsList[x - 1]
'''
x=3
numsList = [0,1,2]

numsList[numsList[2]]

numsList[(x - 4) + 1]

#numsList[(x * 2) - 3] # <<Error

numsList[x - 1]

'''
Q14

Which XXX / YYY declare an array having 4 elements and initializes all elements with -1?


integer array(XXX) myNumbers
integer i
for i = 0; i < YYY; i = i + 1 
   myNumbers[i] = -1
Group of answer choices

XXX: 3 / YYY: 3

XXX: 4 / YYY: 4

XXX: 4 / YYY: 3

XXX: 3 / YYY: 4
'''
'''
What is output?


integer array(4) myNumbers
integer i
for i = 0; i < 4; i = i + 1 
   myNumbers[i] = i
   
for i = 0; i < 4; i = i + 1
   myNumbers[i] = myNumbers[i] * myNumbers[i]


Put myNumbers[3] to output
Group of answer choices

0

9 <<answer

16

3
'''
'''
#16
'''
myNumbers = [0,1,2,3]
for i in range(len(myNumbers)):
   myNumbers[i] = i * 2

print("Q16")
print(myNumbers[myNumbers[1]])
'''
What is wrong with the program?


Function PrintArray(integer array(?) ints) returns nothing
   integer i


   for i = 0; i < ints; i = i + 1
      Put ints[i] to output
      Put " " to output
Group of answer choices

A function with an array parameter must return a value

The array size must be used in the for loop condition

An array variable must be declared in the function

The array size must be specified in the function definition
'''
print("Q17")
print("The array size must be used in the for loop condition")
'''
Which XXX completes the program to call CalcSum()?


Function CalcSum(integer array(?) vals) returns integer sum
   integer i


   sum = 0
   for i = 0; i < vals.size; i = i + 1
      sum = sum + vals[i]
   
Function Main() returns nothing
   integer i
   integer array(4) nums
   integer sum
   
   for i = 0; i < nums.size; i = i + 1
      nums[i] = Get next input


   sum = XXX
   Put "Sum: " to output
   Put sum to output
Group of answer choices

CalcSum(nums)

CalcSum(array(4) nums)

CalcSum(nums(4))

CalcSum(nums())

'''
'''
If CountEvenNums is called with numList equal to [4 5 6 7 8] , what is the returned value?


Function CountEvenNums(integer array(?) numList) returns integer numEven
   integer i
   numEven = 0
   for i = 0; i < numList.size; i = i + 1
      if numList[i] % 2 == 0 
         numEven = numEven + 1
   
Function Main() returns nothing
   integer i
   integer array(5) userNums
   integer numEven
   
   for i = 0; i < userNums.size; i = i + 1
      userNums[i] = Get next input


   numEven = CountEvenNums(userNums)
   Put "Num even: " to output
   Put numEven to output
Group of answer choices

18

5

30

3

'''