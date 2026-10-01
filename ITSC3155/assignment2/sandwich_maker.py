class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, needed in ingredients.items():
            if self.machine_resources.get(item, 0) < needed:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        # take away ingredients used
        for item, needed in order_ingredients.items():
            self.machine_resources[item] -= needed
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
