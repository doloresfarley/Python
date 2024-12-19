'''
6.22 LAB: Interstate highway numbers

LAB ACTIVITY
6.22.1: LAB: Interstate highway numbers


0 / 10

Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

Ex: If the input is:

'''

num = int(input())
even = True if (num%2==0) else False
primary = True if (1<= num<=99) else False
auxiliary = True if (100<= num<=999) else False
two_digits = num%100
direction = "going east/west." if(even==True) else "going north/south."

if two_digits == 0:
    print(f'{num:d} is not a valid interstate highway number.')
elif (primary == True):
    print(f'I-{num:d} is primary, {direction}' )
elif (auxiliary == True):
    print(f'I-{num:d} is auxiliary, serving I-{two_digits:d}, {direction}' )