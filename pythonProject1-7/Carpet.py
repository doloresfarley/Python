# Input: carpet price per square foot, room width, and room length

# Input: carpet price per square foot, room width, and room length on one line
total_cost =0
for x in range(2):
  inputs = input().split()

# Parse the inputs
  carpet_price_per_sqft = float(inputs[0])
  room_width = int(inputs[1])
  room_length = int(inputs[2])

# Calculate the area of the room
  room_area = room_width * room_length

# Add 20% for waste
  waste_area = room_area * 1.2

# Calculate the carpet cost
  carpet_cost = carpet_price_per_sqft * waste_area

  labor = 0.75 * room_area
#Step 3 (2 pts). Calculate sales tax (7%) on carpet and labor cost. Total cost includes carpet,
# labor and sales tax. Output sales tax and total cost. Submit for grading to confirm 3 tests pass.
  tax = 0.07*carpet_cost + 0.07 *labor
  cost = labor + carpet_cost + tax
  total_cost += cost
  # Output the results
  print('Order #',end='')
  print(x+1)
  print(f'Room: {room_area} sq ft')
  print(f'Carpet: ${carpet_cost:.2f}')
  print(f'Labor: ${labor:.2f}')
  # Tax: $10.08
  #Cost: $154.08
  print(f'Tax: ${tax:.2f}')
  print(f'Cost: ${cost:.2f}')
  print('')
print(f'Total Sales: ${total_cost:.2f}')
