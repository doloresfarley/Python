x = int(input())
y = int(input())
z = int(input())
'''

if x<y and x<z:
    print(x)
elif y<x and y<z:
    print(y)
elif z<y and z<x:
    print(z)
else:
    print(x)
'''
# Find the smallest number using min() function
smallest = min(x, y, z)

# Output the smallest number
print(smallest)