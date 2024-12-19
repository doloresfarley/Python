# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)


cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
#Note: You cannot sort a list that contains BOTH string values AND numeric values.
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

a = ("Jenifer", "Sally", "Jane")
x = sorted(a, key=len)
print(x)


def myfunc(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)

