'''
5.19 LAB: Input and formatted output: House real estate summary

LAB ACTIVITY
5.19.1: LAB: Input and formatted output: House real estate summary


0 / 10

Sites like Zillow get input about house prices from a database and provide nice summaries for readers. Write a program with two inputs, current price and last month's price (both integers). Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')
'''

current_price = int(input())
last_months_price = int(input())
difference = current_price - last_months_price
mortgage_est = (current_price * 0.051) / 12.

#This house is $200000. The change is $-10000 since last month.
#The estimated monthly mortgage is $850.00.
print(f'This house is ${current_price:d}. The change is ${difference:d} since last month.')
print(f'The estimated monthly mortgage is ${mortgage_est:.2f}.')