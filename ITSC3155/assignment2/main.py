
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_running = True

    while is_running:
        choice = input("What would you like? (small/medium/large/ off/ report): ").lower()

        if choice == "off":
            is_running = False
        elif choice == "report":
            for item, amount in sandwich_maker_instance.machine_resources.items():
                unit = "slice(s)" if item != "cheese" else "pound (s)"
                print(f"{item.capitalize()}: {amount} {unit}")
        elif choice in recipes:
            recipe = recipes[choice]
            if sandwich_maker_instance.check_resources(recipe["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, recipe["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, recipe["ingredients"])

if __name__=="__main__":
    main()
