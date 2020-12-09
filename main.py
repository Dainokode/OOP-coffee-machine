from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

time_break = True
while time_break:
    choice = input(f"What drink would you like? {menu.get_items()}")
    if choice == "off":
        print("Machine powering off...")
        time_break = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) and money.make_payment(menu.find_drink(choice).cost):
            coffee_maker.make_coffee(menu.find_drink(choice))
