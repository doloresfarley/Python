'''
The map() function is used to apply a given function to every item of an iterable,
 such as a list or tuple, and returns a map object (which is an iterator).
'''

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)

a, b, c = map(int, input().split())
print(a,b,c)

j = [input().split()]

print(j)