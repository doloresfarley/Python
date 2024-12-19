'''
7.27 LAB: Matching strings

LAB ACTIVITY
7.27.1: LAB: Matching strings


0 / 10

Write a program that compares two strings given as input. Output the number of characters that match in each string position. The output should use the correct verb (match vs matches) according to the character count.

Ex: If the input is:

crash
crush
the output is:

4 characters match
Ex: If the input is:

cat
catnip
the output is:

3 characters match
Ex: If the input is:

mall
saw
the output is:

1 character matches
Ex: If the input is:

apple
orange
the output is:
'''

first = input()
second = input()
length = len(first) if len(first) < len(second) else len(second)
count =0
for i in range(length):
    if first[i] == second[i]:
        count +=1
count_str = str(count) + " characters match"
if count <= 1:
    count_str = "1 character matches" if count== 1 else "0 characters match"
print(count_str)

