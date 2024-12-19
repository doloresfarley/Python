word = input()
password = ''

for char in word:
    if char == 'i':
        password = password+ "1"
    elif char == 'a':
        password = password+ "@"
    elif char == 'm':
        password = password+ "M"
    elif char == 'B':
        password = password+ "8"
    elif char == 's':
        password = password+ "$"
    else:
        password = password+ char
password = password + "!"
print(password)