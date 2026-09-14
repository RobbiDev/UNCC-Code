### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
            Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # check if we have enough ingredients
        for item, needed in ingredients.items():
            if self.machine_resources.get(item, 0) < needed:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
            Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # ask user for coins
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: ") or 0)
        half_dollars = int(input("how many half dollars?: ") or 0)
        quarters = int(input("how many quarters?: ") or 0)
        nickels = int(input("how many nickels?: ") or 0)

        return (dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
            Hint: use the output of process_coins() function for cost input"""
        # check if user paid enough
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
            Hint: no output"""
        # take away ingredients used
        for item, needed in order_ingredients.items():
            self.machine_resources[item] -= needed
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
is_running = True

while is_running:
    choice = input("What would you like? (small/medium/large/ off/ report): ").lower()

    if choice == "off":
        is_running = False
    elif choice == "report":
        for item, amount in machine.machine_resources.items():
            unit = "slice(s)" if item != "cheese" else "pound (s)"
            print(f"{item.capitalize()}: {amount} {unit}")
    elif choice in recipes:
        recipe = recipes[choice]
        if machine.check_resources(recipe["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, recipe["cost"]):
                machine.make_sandwich(choice, recipe["ingredients"])