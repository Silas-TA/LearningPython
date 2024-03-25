from day_12_data import MENU
from day_12_data import resources
from replit import clear



def payment():
    print("Put in your coins below")
    coins = []
    quarter = 0.25  # $0.25 (25 cents)
    dime = 0.10  # $0.10 (10 cents)
    nickel = 0.05  # $0.05 (5 cents)
    penny = 0.01  # $0.01 (1 cent)

    quarter_count = int(input("Enter how many quarters you have: "))  # Exeample: 0.25
    dime_count = int(input("Enter how many dime you have: "))  # Example: 0.10
    nickel_count = int(input("Enter how many nickel you have: "))  # Example: 0.05
    penny_count = int(input("Enter how many penny you have: "))  # Example: 0.01

    quarter_value = quarter_count * quarter
    dime_value = dime_count * dime
    nickel_value = nickel_count * nickel
    penny_value = penny_count * penny

    total_value = (quarter_value + dime_value + nickel_value + penny_value)

    return total_value


def repair():
    if drink_choice == 'off':
        print("System has been shut for maintenance")
    return


def get_drink():
    if drink_choice == 'off':
        repair()
        return
    drink = MENU[drink_choice]
    for key in drink['ingredients']:
        if drink['ingredients'][key] > resources[key]:
            print(f"Unfortunately, there isn't enough {key}")
            return
        else:
            resources[key] = resources[key] - drink['ingredients'][key]

    print(resources)
    print(f"The price of a {drink_choice} is ${MENU[drink_choice]['cost']}")
    paid = payment()
    if paid < drink['cost']:
        print(f"Unfortunately, {paid} is not enough")
    elif paid == drink['cost']:
        print(f"Your {drink_choice} order is ready")
    else:
        change = paid - MENU[drink_choice]['cost']
        print(f"Your {drink_choice} order is ready")
        print(f"Collect your ${round(change,2)} change")

def report():
    print(f"Water: {resources['water']}ml\nCoffee: {resources['coffee']}mg\nMilk: {resources['milk']}ml")

isComplete = True

while isComplete:
    drink_choice = input("Enter a drink you want (espresso/latte/cappuccino): ")
    get_drink()
    report()
    isComplete = False
    clear()
