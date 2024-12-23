'''
11.16 LAB: Vending machine

LAB ACTIVITY
11.16.1: LAB: Vending machine


0 / 10

Given three integers as user inputs that represent the number of bottles of drinks to purchase, to restock, and to purchase afterward, create a VendingMachine object that performs the following operations:

Purchase the first input number of bottles of drinks
Restock the second input number of bottles of drinks
Purchase the last input number of bottles of drinks
Report inventory
A VendingMachine's initial inventory is 20 bottles of drinks.

Ex: If the input is:

5
2
7
the output is:

Inventory: 10 bottles

'''


class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f'Inventory: {self.bottles} bottles')


if __name__ == "__main__":
    # TODO: Create VendingMachine object
    machine1 = VendingMachine()
    # TODO: Purchase first input number of bottles of drinks
    machine1.purchase(int(input()))
    # TODO: Restock second input number of bottles of drinks
    machine1.restock(int(input()))
    # TODO: Purchase last input number of bottles of drinks
    machine1.purchase(int(input()))
    # TODO: Report inventory
    machine1.report()