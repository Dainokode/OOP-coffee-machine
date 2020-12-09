from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drinks available
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 18, 2.5)
cappuccino = MenuItem("cappuccino", 300, 200, 18, 3.5)

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

time_break = True
while time_break:
    choice = input(f"What would you like? {menu.get_items()} ").lower()
    if choice == "off":
        print("Machine powering off...")
        time_break = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    elif choice == "espresso" and coffee_maker.is_resource_sufficient(espresso) and money.make_payment(espresso.cost):
        coffee_maker.make_coffee(espresso)
    elif choice == "latte" and coffee_maker.is_resource_sufficient(latte) and money.make_payment(latte.cost):
        coffee_maker.make_coffee(latte)
    elif choice == "cappuccino" and coffee_maker.is_resource_sufficient(cappuccino) and money.make_payment(cappuccino.cost):
        coffee_maker.make_coffee(cappuccino)
