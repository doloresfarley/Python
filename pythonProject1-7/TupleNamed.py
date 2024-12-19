from collections import namedtuple
Person = namedtuple('Person',['first_name', 'last_name', 'license_plate', 'age'])

first_name = input()
last_name = input()
license_plate = input()
age = int(input())

person = Person(first_name, last_name, license_plate, age)

print(f'First name: {person.first_name}, Last name: {person.last_name}, License plate: {person.license_plate}, Age: {person.age}')