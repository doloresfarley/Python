#Q1
# What is output?
new_string = 'One giant leap for mankind'
print(new_string[0:6])
print()
#Q2
# Consider the string new_string = 'Code development in Python'.
# Which statement will return 'velop' as a substring?
new_string = 'Code development in Python'
#print(new_string[7:12])
print(new_string[-19:12]) # <- Answer
print(new_string[8:12])
print( new_string[7:11] )
print( new_string[-18:12])
print('Answer:','velop')
print()
#Q3
# What is output?
new_string = 'Python'
my_index = 0
while my_index != len(new_string)/2:
    print(new_string[my_index:int(len(new_string)/2)])
    my_index += 1
print()

#Q4
# What is output?
new_string = 'Python'
print(new_string[0:-1:2])
print()

#Q5 Consider the string new_string = 'Berlin is the capital of Germany'.
# Which statement will return 'capital of Germany' as a substring?
# In a slice, the notation [start:stop] extracts characters starting from the start index up to, but not including, the stop index.
# If the start index is greater than or equal to the stop index, the slice will return an empty string.
new_string = 'Berlin is the capital of Germany'
#print(new_string[14:31])
print(new_string[-18:])
print()

#Q6 What XXX and YYY will left align the column values
'''
print(f'{"Product":XXX}{"Price(cash)":YYY}')
print('-' * 24)
print(f'{"Banana":XXX}{1.02:YYY}')
print(f'{"Apple":XXX}{5.08:YYY}')
'''

print(f'{"Product":<16}{"Price(cash)":<8}')
print('-' * 24)
print(f'{"Banana":<16}{1.02:<8}')
print(f'{"Apple":<16}{5.08:<8}')

print()

#Q7
# What will be output for print(f'{1.6180339:.5f}')?
print(f'{1.6180339:.5f}')
print()

#Q8
# If factor = 24, which format will generate '**24', right aligned in its field?
factor = 24
print(f'{factor:*>4}')
print()

#Question 9
# What defines the minimum number of characters that must be inserted into the string?
#A format specification may include a field width that defines the minimum number of characters that must be inserted into the string.

#Q10
# For print(f'{"Mike":XXX}{1:YYY}'), which XXX and YYY will generate 'Mike=1' as the value of format_print?

print(f'{"Mike":*>4}{1:=>2}') #<-answer
print(f'{"Mike":*>4}{1:=>3}')
print(f'{"Mike":*<5}{1:=<2}')
print(f'{"Mike":*>4}{1:<2}')
print()
'''
9. Chapter 9. Strings

9.3 String methods

find(x)
Find(x) -- Returns the index of the first occurrence of item x in the string, otherwise, find(x) returns -1.
find(x, start)
Find(x, start) - Same as find(x), but begins the search at index start.
find(x, start, end)
Find(x, start, end) -- Same as find(x, start), but stops the search at index end - 1.
rfind(x)
Rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string.

'''
#Q11 What is output?
#However, find on an empty string will return the starting position specified if it's within the string's bounds.
my_books = 'Books 105'
index = my_books.find('',3)

print(index)
print()

#12
# What is the output

my_string = 'The area postal code is 99501'
print(my_string[-5:].isdigit())
print(my_string[:3].isupper())
print(my_string[:3].islower())
print()

#13
# Consider my_string = 'roy came third in the running race'.
# Which option will return 'Roy came 3rd in the running race' as the value of new_string?
# capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
# lower() -- Returns a copy of the string with all characters lowercased.
# upper() -- Returns a copy of the string with all characters uppercased.
# strip() -- Returns a copy of the string with leading and trailing whitespace removed.
# title() -- Returns a copy of the string as a title, with first letters of words capitalized.

my_string = 'roy came third in the running race'
my_string = my_string.capitalize()
my_string = my_string.replace('thi','3')
print(my_string)
print('Roy came 3rd in the running race' )
print()

#Q14
# What is output?
my_string = 'Greetings!'
print(my_string == 'greetings!')
print('tin' in my_string)
print('Hello' > my_string) # Is Hello greater then my_string
print()

#Q15
# Which of the following methods will change the string 'Python Programming' into 'PYTHON PROGRAMMING'?
my_string = 'Python Programming'
print(my_string.upper())
print('PYTHON PROGRAMMING')
print()

#Q16 Consider the list my_list = ['www', 'python', 'org'].
# Choose the option that returns 'www.python.org' as the value to my_string.
my_list = ['www', 'python', 'org']
print(('.'.join(my_list)))
print('www.python.org')
print()

#Q17 What is output?
my_string = 'What is your name?'
print(my_string.split('?'))
# ['What is your name', '']

#18
# Complete the following code to get
# 'Email me at abc@gmail.com or call at 333 222 1111' as output.
email = 'Email: abc@gmail.com'
phone = 'Ph: 333-222-1111'
XXX =  email.split(' ')[1]
YYY = ' '.join((phone.split(': ' )[1]).split('-'))
print(f"Email me at {XXX} or call at {YYY}")
print('Email me at abc@gmail.com or call at 333 222 1111' )

XXX= email.split(' ')[0]
YYY = ' '.join((phone.split(': ' )[0].split('-')))
print(f"Email me at {XXX} or call at {YYY}")
XXX, YYY = email.split(' '), ' '.join((phone.split(': ' )))
print(f"Email me at {XXX} or call at {YYY}")
XXX, YYY = email.split(' '), ' '.join((phone.split(': ' )[1]))
print(f"Email me at {XXX} or call at {YYY}")
print()

#Q19 What is output?
my_poem = 'Roses are red; Violets are blue'
new_separator = '.'
new_poem = my_poem.split(';')
print(new_separator.join(new_poem))
print()
#20

title = 'Python for Beginners'
tokens = title.split(' ')
if 'Chapter 1' not in tokens:
        tokens.append('Chapter 1')
new_title = ' '.join(tokens)
print(new_title)
