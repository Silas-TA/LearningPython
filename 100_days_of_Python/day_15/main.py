# from turtle import Turtle, Screen
# from prettytable import PrettyTable as pt
# # timmy = Turtle()
# # timmy.shape('turtle')
# # timmy.color('blue')
# # timmy.forward(100)
# # print(timmy)
# #
# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()
#
# table = pt()
# table.add_column('Pokemon', '.')
# table.add_column('Power', '.')
# # table.add_row('Pikachu')
# print(table)

from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

isRunning = True
while isRunning:
    # print out options and ask for choice
    options = menu.get_items()
    choice = input(f"What  drink would you like to have- {options}: ")
    if choice == 'off':
        isRunning = False
    elif choice == 'report':
        # print out report
        money_machine.report()
        coffee_maker.report()
    else:
        # check resource for coffee asked and compare with resource left
        drink = menu.find_drink(choice)
        check_res = coffee_maker.is_resource_sufficient(drink)
        if check_res and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

