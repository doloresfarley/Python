'''
Program Specifications. Write a program to calculate the cost of hosting three pizza parties on Friday, Saturday and Sunday. Read from input the number of people attending, the average number of slices per person and the cost of one pizza. Dollar values are output with two decimals. For example, print(f"Cost: ${cost:.2f}").

Note: this program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

Step 1 (2 pts). Read from input the number of people (int), average slices per person (float) and cost of one pizza (float). Calculate the number of whole pizzas needed (8 slices per pizza). There will likely be leftovers for breakfast. Hint: Use the ceil() function from the math library to round up to the nearest whole number and convert to an int. Calculate and output the cost for all pizzas. Submit for grading to confirm test 1 passes.
Ex: If the input is:

10  2.6  10.50
The output is:

Friday Night Party
4 Pizzas: $42.00
'''
import math

# Type your code here.
#
weekendTotal = 0
# cars = ["Ford", "Volvo", "BMW"]
days = ["Friday Night Party", "Saturday Night Party", "Sunday Night Party" ]
for x in range(3):
  inputs = input().split()

# Parse the inputs
  people = int(inputs[0])
  avg_per_person = float(inputs[1])
  cost_per_pizza = float(inputs[2])

  num_slices = avg_per_person * people

  num_pizzas = math.ceil( num_slices/8)
  # Calculate and output the sales tax (7%).

  cost = cost_per_pizza * num_pizzas
  tax = 0.07* cost
  delivery = 0.20 *(tax+cost)
  total = delivery + tax + cost
  weekendTotal += total
  print(days[x])
  print(num_pizzas,f'Pizzas: ${cost:.2f}')
  print(f'Tax: ${tax:.2f}')
  print(f'Delivery: ${delivery:.2f}')
  print(f'Total: ${total:.2f}')
  print('')
#Weekend Total: $199.53
print(f'Weekend Total: ${weekendTotal:.2f}')


