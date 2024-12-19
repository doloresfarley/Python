'''
10.12 LAB: Scrabble points

LAB ACTIVITY
10.12.1: LAB: Scrabble points


10 / 10

Scrabble is a word game in which words are constructed from letter tiles, each letter tile containing a point value. The value of a word is the sum of each tile's points added to any points provided by the word's placement on the game board.

Write a program using the given dictionary of letters and point values that takes a word as input and outputs the base total value of the word (before being put onto a board).

Ex: If the input is:

PYTHON
the output is:

PYTHON is worth 14 points.
'''

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

data = input().upper()

total = 0
new_list = [ch for ch in data if ch in tile_dict]
for ch in new_list:
    total += tile_dict[ch]
'''
#OLD
for ch in data:
    if ch in tile_dict:
       total += tile_dict[ch]
'''
total = sum([tile_dict[key] for key in data if key in tile_dict])

print(f'{data} is worth {total} points.')