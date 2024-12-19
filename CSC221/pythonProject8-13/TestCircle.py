from Circle import Circle

c1 = Circle(1)

print(c1.get_radius())
c1.set_radius(2)
print(c1.get_radius())
print(c1.get_area())

# approach #1 makes the driver more convoluted
r = int(input())
if r > 0:
    c1.set_radius(r)

# approach #2 makes the driver more abstract and clean
c1. set_radius(int(input()))

print(c1.get_perimeter())