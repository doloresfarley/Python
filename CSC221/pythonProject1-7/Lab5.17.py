import math

'''
5.17 LAB*: Program: Painting a wall

LAB ACTIVITY
5.17.1: LAB*: Program: Painting a wall


0 / 10

Program Specifications Write a program to calculate the cost to paint a wall. Amount of required paint is based on the wall area. Total cost includes paint and sales tax.

Note: This program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

Step 1 (2 pts). Read from input wall height, wall width, and cost of one paint can (floats). Calculate and output the wall's area to one decimal place using print(f"Wall area: {wall_area:.1f} sq ft");. Submit for grading to confirm 1 test passes.


'''

#Read from input wall height, wall width, and cost of one paint can (floats).
wall_height = float(input())
wall_width = float(input())
cost = float(input())

wall_area = wall_height*wall_width
print(f"Wall area: {wall_area:.1f} sq ft")

#Step 2 (2 pts). Calculate and output the amount of paint needed to three decimal places
# One gallon of paint covers 350 square feet. Submit for grading to confirm 2 tests pass.
paint_needed = wall_area/350.0
print(f"Paint needed: {paint_needed:.3f} gallons")

#Step 3 (2 pts). Calculate and output the number of 1 gallon cans needed to paint the wall. Extra paint may be left over.
# Hint: Use ceil() from the math module to round up to the nearest gallon (int). Submit for grading to confirm 4 tests pass.
num_gallons = math.ceil(paint_needed)
print(f"Cans needed: {num_gallons:d} can(s)")

#Step 4 (4 pts). Calculate and output the paint cost, sales tax of 7%, and total cost.
# Dollar values are output with two decimal places. Submit for grading to confirm all tests pass.
paint_cost = num_gallons*cost
sales_tax = 0.07 *paint_cost
total_cost = paint_cost + sales_tax
print(f'Paint cost: ${paint_cost:.2f}')
print(f'Sales tax: ${sales_tax:.2f}')
print(f'Total cost: ${total_cost:.2f}')
'''
8.0
8.0
49.20
Wall area: 64.0 sq ft
Paint needed: 0.183 gallons
Cans needed: 1 cans
Paint cost: $49.20
Sales tax: $3.44
Total cost: $52.64
'''