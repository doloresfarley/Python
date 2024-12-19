i = 0
count = 0
while i <= 100:
    print(i)
    i = i + 2
    count +=1
print(count)

#18
x = 0
i = 5
while i > 1:
    x = x + i
    i = i - 1
print(x)

#19
x = 0
i = 1
while i <= 6:
    x += i
    i += 2
print(x)

#20
names = ['Bob', 'Jill', 'Xu']
ages = [24, 18, 33]
for index in [2, 0, 1]:
    print(f'{names[index]}:{ages[index]}')

#Q21
cities = ['Sydney', 'Paris', 'New York', 'Cairo']
for c in reversed(cities):
    print(c, end=' ')
#q23
print()
rentals = {
    'skis' : 20.00,
    'boots' : 10.00,
    'skates' : 4.00
}
for x in rentals:
    print(x, end=' ')

#q24
grades = {
    'Jennifer' : 'A',
    'Ximin' : 'C',
    'Julio' : 'B',
    'Jason' : 'C'
}
for name in grades:
    print(name,":",grades[name])

#q26
for index in range(1,10,3):
    print(index)

#q27
for index in range(20,31,2):
    print(index)
#Q28
sports_list = [ 'Hockey', 'Football', 'Cricket' ]
for i in range(len(sports_list)):
    print(f'{i+1}. {sports_list[i]}')
#q29
my_list = [ 3, 2, 7, 8, 6, 9 ]
count = 0
for i in range(1, len(my_list)):
    print(i)
    if my_list[i] > my_list[i-1]:
        count = count + 1
print(count)

#32
count = 0
for i in range(10):
    for j in range(3):
        count+=1
        print(f'{i}. {j}')
print(count)
#Q33
count = 0
for i in range(1, 3): #2
    for j in range(8, 12, 2): #2
        count += 1
        print(f'{i}. {j}')
print(count)

#Q34
for i in range(5):
    for j in range(10):
        print('*', end='')
    print()

#q35
c1 = 'c'
while c1 > 'a':
    for i in range(3):
        print(f'{c1}{i}', end=' ')
    c1 = chr(ord(c1) - 1)

#q38
print()
num = 10;
while num <= 15:
    print(num, end=' ')
    if num == 12:
        break
    num += 1

#q39
print()
for j in range(2):
    for k in range(4):
        if (k == 2):
            break
        print(f'{j}{k}', end=' ')

#q40
print()
for i in range(11):
    if i == 6:
        continue
    else:
       print(i, end=' ')

#41
print()
z = 0
a = 5
while a > 0:
    a = a - 1
    if a == 2:
        continue
    z = z + a

print(z)

#q42
print()
id_list = [13, 984, 231, 140]
for id in id_list:
    if id != 231:
        print(id, end=' ')
else:
    print('Done')

#
print()
names = [ 'Gerry', 'Preet', 'Jimin', 'Susan' ]
index = 0
while index < len(names):
    if names[index] == 'Susan':
        break
    else:
        index += 1
else:
    print('Done')
print(index)

#Q44
print()
num_list = [ 3, 8, 5, 15, 12, 32, 45 ]
for index, value in enumerate(num_list):
    if index > 0:
        if value < num_list[index-1]:
            print('*', end='')
    print(value, end=' ')

#q
print()
num_list = [ 8, 2, 1, 3, 4, 7, 6 ]
for index, value in enumerate(num_list):
    if index == value:
        print('*', end='')
    print(value, end=' ')
#q
print()
calc = 0
z =25
while z <= 100:
   calc = calc + z
   z = z * 2
print(calc)

#q65
x = 9
y = 1


while y <= x:
   if y % 3 == 0:
     print(y)
   y = y + 1

#
calc = 0
limit = 15
data =  [2, 3, 6, 9]
index = 0
userVal = data[index]


while (calc + userVal) <= limit:
   calc = calc + userVal
   index +=1
   userVal = data[index]
print(calc)

#q18
#What is the ending value of count?

#What is the ending value of x?


x = 0
i = 5
while i > 1:
    x = x + i
    i = i - 1
print(x)

#Q19 What is the ending value of x?


x = 0
i = 1
while i <= 6:
    x += i
    i += 2
print(x)