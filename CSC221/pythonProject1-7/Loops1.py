
result = 0
n = 1
while n < 6:
    print(n, end=' ')
    result -= 2
    n += 1
else:
    print(f'\ {result}')
print('done')


result = 0
n = 1
while n < 8:
    print(n, end=' ')
    result -= 3
    if result < -6:
        print('!')
        break
    n += 1
else:
    print(f'\ {result}')
print('done')