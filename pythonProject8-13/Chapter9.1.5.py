item_name = "Test1234"
item_quantity = 10
print(f'{item_name:[<11}{item_quantity:]>11}')



my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[::2])
#String orig_string is read from input. Assign variable partial_string with the orig_string slice that only includes the first two characters and the last four characters of orig_string.
orig_string = input()

partial_string = orig_string[0:2] + orig_string[-4:]

print(partial_string)

#String full_string is read from input. Assign partial_quote with every third element in the last half of full_string.
full_string = input()
index = int(len(full_string)/2)
partial_quote = full_string[index::3]
print(partial_quote)

'''

zyBooks catalog
Help/FAQ
9.1 String slicing
Students:
Section 9.2 is a part of 1 assignment:
Ch 9
Includes:

PA

CA
Due: 11/06/2024, 6:30 PM EST
9.2 Advanced string formatting

Field width

A program must display formatted output beyond the ability of basic print usage such as print(x). Consider a program that displays a table of soccer player statistics:

Figure 9.2.1: A formatted table of soccer statistics.
Player Name      Goals    Games Played     Goals Per Game   
------------------------------------------------------------
Sadio Mane         22          36               0.61        
Mohamed Salah      22          38               0.58        
Sergio Aguero      21          33               0.64        
Jamie Vardy        18          34               0.53        
Gabriel Jesus       7          29               0.24
 
Feedback?
Note in the above example how the text is formatted into columns with the contents of each column (except the leftmost column) centered under the column header. A programmer could achieve this careful formatting by placing spaces into their output strings, but each row would require different numbers of spaces depending on the player name (longer names require fewer spaces between the first and second columns).

A format specification may include a field width that defines the minimum number of characters that must be inserted into the string. If the replacement value is smaller in size than the given field width, then the string is padded with space characters. Field widths set on each column in the example above cause the output to be formatted. A field width is defined in a format specification by including an integer after the colon, as in {name:16} to specify a width of 16 characters. 

Numbers will be right-aligned within the width by default, whereas most other types like strings will be left-aligned.
'''

'''
Aligning text

A format specification can include an alignment character that determines how a value should be aligned within the width of the field. Alignment is set in a format specification by adding a special character before the field width integer. The basic set of possible alignment options include left-aligned (<), right-aligned (>) and centered (^). Numbers will be right-aligned within the width by default, whereas most other types like strings will be left-aligned.
'''
'''
Three strings are read from input and stored into list musicians. Then, three more strings are read from input and stored into list instruments. Lastly, string separator_char is read from input. Use five print(f' ') statements to output the following five lines:

"Musicians", with a field width of 24, centered. Then "Instruments", with a field width of 24, centered.
48 instances of separator_char.
musicians[0], with a field width of 24, centered. Then, instruments[0] with a field width of 24, centered.
musicians[1], with a field width of 24, centered. Then, instruments[1] with a field width of 24, centered.
musicians[2], with a field width of 24, centered. Then, instruments[2] with a field width of 24, centered.
'''

musicians = input().split()
instruments = input().split()
separator_char = input()

blank =""
print(f'{"Musicians":^24}{"Instruments":^24}')
print(f'{blank:{separator_char}>48}')
print(f'{musicians[0]:^24}{instruments[0]:^24}')
print(f'{musicians[1]:^24}{instruments[1]:^24}')
print(f'{musicians[2]:^24}{instruments[2]:^24}')
'''
Three strings are read from input and stored into list musicians. Then, three more strings are read from input and stored into list instruments. Lastly, string separator_char is read from input. Use five print(f' ') statements to output the following five lines:

"Musicians", with a field width of 24, centered. Then "Instruments", with a field width of 24, centered.
48 instances of separator_char.
musicians[0], with a field width of 24, centered. Then, instruments[0] with a field width of 24, centered.
musicians[1], with a field width of 24, centered. Then, instruments[1] with a field width of 24, centered.
musicians[2], with a field width of 24, centered. Then, instruments[2] with a field width of 24, centered.

'''
'''
Methods to create new strings:
capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
lower() -- Returns a copy of the string with all characters lowercased.
upper() -- Returns a copy of the string with all characters uppercased.
strip() -- Returns a copy of the string with leading and trailing whitespace removed.
title() -- Returns a copy of the string as a title, with first letters of words capitalized.
'''

'''
String user_entry is read from input with leading and trailing whitespaces. Remove any leading and trailing whitespaces in the string. If user_entry contains the string 'Paint color:', capitalize all the characters in user_entry. Otherwise, capitalize the first letter for each word in user_entry. Finally, print out the resulting string.
'''
user_entry = input()

user_entry = user_entry.strip()

if 'Paint color:' in user_entry:
    user_entry = user_entry.upper()
else:
    x = user_entry.split()
    temp =""
    for y in x:
        temp += y.capitalize() +" "
    temp = temp.strip()
    user_entry = temp

print(user_entry)

''''
Note: The positional and inferred positional replacement types cannot be combined.
 Ex: '{} + {1} is {2}'.format(2, 2, 4) is not allowed. 
 However, named and either positional replacement type can be combined. 
 Ex: '{} + {} is {sum}'.format(2, 2, sum = 4)
'''
