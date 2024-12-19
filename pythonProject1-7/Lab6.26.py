'''
6.26 LAB: Golf scores

LAB ACTIVITY
6.26.1: LAB: Golf scores


0 / 10

Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (possible values: 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par
Given two integers that represent the number of strokes used and par, write a program that prints the appropriate score name. Print "Error" at the end of the output if par is not 3, 4, or 5, or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".

Ex: If the input is:


'''


strokes = int(input())
par = int(input())
legal =  [ 3, 4, 5]
num = par -strokes
if par not in legal:
    print(f'Par {par} in {strokes} strokes is Error')
else:
    if ( num >= 2):
        print(f'Par {par} in {strokes} strokes is Eagle')
    elif (num >= 1):
        print(f'Par {par} in {strokes} strokes is Birdie')
    elif( num == 0):
        print(f'Par {par} in {strokes} strokes is Par')
    elif( num == -1):
        print(f'Par {par} in {strokes} strokes is Bogey')
    else:
        print(f'Par {par} in {strokes} strokes is Error')