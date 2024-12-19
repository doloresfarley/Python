'''
5.18 LAB: Input and formatted output: Caffeine levels

LAB ACTIVITY
5.18.1: LAB: Input and formatted output: Caffeine levels


0 / 10

A half-life is the amount of time it takes for a substance or entity to fall to half its original value. Caffeine has a half-life of about 6 hours in humans. Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 24 hours. Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')


'''

caffeine_mg = float(input())

''' Type your code here. '''
after_6_hours = caffeine_mg/2
after_12_hours = after_6_hours/2
after_18_hours = after_12_hours/2
after_24_hours = after_18_hours/2
print(f'After 6 hours: {after_6_hours:.2f} mg')
print(f'After 12 hours: {after_12_hours:.2f} mg')
print(f'After 24 hours: {after_24_hours:.2f} mg')