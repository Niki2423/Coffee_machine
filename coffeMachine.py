# Coffee Machine Program

# Resources and their initial quantities
resources = {
    "water": 300,  # in ml
    "milk": 200,   # in ml
    "coffee": 100, # in g
    "money": 0.0   # in dollars
}

# Menu with drink ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Function to print the current resource report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

# Function to check if there are enough resources to make the selected drink
def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to process coins inserted by the user
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

# Function to check if the transaction is successful
def check_transaction(drink, money_inserted):
    cost = MENU[drink]["cost"]
    if money_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = money_inserted - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        resources["money"] += cost
        return True

# Function to make the coffee and deduct resources
def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")

# Main program loop
def coffee_machine():
    while True:
        # Prompt the user
        print("What would you like? (espresso/latte/cappuccino): ")
        choice = input().lower()

        # Turn off the machine
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break

        # Print report
        elif choice == "report":
            print_report()

        # Check if the choice is a valid drink
        elif choice in MENU:
            drink = choice
            if check_resources(drink):
                money_inserted = process_coins()
                if check_transaction(drink, money_inserted):
                    make_coffee(drink)

        else:
            print("Invalid choice. Please try again.")

# Run the coffee machine program
coffee_machine()