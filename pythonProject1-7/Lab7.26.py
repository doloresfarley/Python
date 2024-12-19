'''
7.26 LAB: Months until payoff

LAB ACTIVITY
7.26.1: LAB: Months until payoff


0 / 10

Write a program that reads a loan amount, payment amount, and interest rate as inputs and outputs the number of payments required until the loan is paid. Interest is added to current balance before a payment is applied. Ex: If current balance is $100.00 and the interest rate is 0.02, the new balance is $102.00 before a payment is applied. All values are floats.

Ex: If the input is:

1000.0
50.0
0.03
the output is:

31 payments
Ex: If the input is:

50.0
100.0
0.02
the output is:

1 payment

'''

loan = float(input())
payment = float(input())
rate = float(input())

balance = loan
num = 0
while balance >0:
    # : If current balance is $100.00 and the interest rate is 0.02, the new balance is $102.00 before a payment is applied.
    balance = balance + balance*rate
    balance -= payment
    num = num +1

payment_str = "payments" if num>1 else "payment"
print(num,payment_str)