from collections import namedtuple

City = namedtuple('City', ['name', 'state', 'population'])

''' Your code goes here '''
name = input()
state = input()
population = int(input())

city = City(name, state, population)
print(f'City name: {city.name}, State: {city.state}, Population: {city.population}')
print(len(city))