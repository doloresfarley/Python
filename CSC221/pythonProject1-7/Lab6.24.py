import math

#Dollars, Quarters, Dimes, Nickels, and Pennies

money = int(input())
dollars = math.floor(money//100)
quarter = math.floor( (money - dollars*100) // 25)
dimes = math.floor((money - (dollars*100 + quarter*25)) //10)
nickels = math.floor((money - (dollars*100 + quarter*25 + dimes*10 )) //5)
pennies = math.floor( money - (dollars*100 + quarter*25 + dimes*10 + nickels*5 ) )


if money <=0 :
    print("No change")
else:
    dollars_str = "Dollars" if(dollars>1) else "Dollar"
    quarter_str = "Quarters" if(quarter>1) else "Quarter"
    dimes_str = "Dimes" if(dimes>1) else "Dime"
    nickels_str = "Nickels" if(nickels>1) else "Nickel"
    pennies_str = "Pennies" if(pennies>1) else "Penny"
    if (dollars > 0):
        print(f'{dollars:d} {dollars_str}')
    if (quarter > 0):
        print(f'{quarter:d} {quarter_str}')
    if (dimes > 0):
        print(f'{dimes:d} {dimes_str}')
    if (nickels > 0):
        print(f'{nickels:d} {nickels_str}')
    if (pennies > 0):
        print(f'{pennies:d} {pennies_str}')