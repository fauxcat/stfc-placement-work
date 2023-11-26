class Beverage:
    def __init__(self, description):
        self.description = description
        self.milk = False
        self.sugar = False
        self.cream = False
        self.sprinkles = False

    def getDescription(self):
        return self.description

    def getExtraCost(self):
        extra_cost = 0
        if self.milk:
            extra_cost += 0.53
        if self.sugar:
            extra_cost += 0.17
        if self.cream:
            extra_cost += 0.73
        if self.sprinkles:
            extra_cost += 0.29
        return extra_cost


class RegularCoffee(Beverage):
    def __init__(self):
        super().__init__("Regular")

    def getCost(self):
        return 2.11 + self.getExtraCost()

    def getDescription(self):
        return "Regular"


class DecafCoffee(Beverage):
    def __init__(self):
        super().__init__("Decaf")

    def getCost(self):
        return 1.51 + self.getExtraCost()

    def getDescription(self):
        return "Decaf"


class Muffins:
    def __init__(self):
        self.description = "muffins"
        self.extra_cost = 2.03


class Flapjacks:
    def __init__(self):
        self.description = "flapjacks"
        self.extra_cost = 2.59


class Panettone:
    def __init__(self):
        self.description = "panettone"
        self.extra_cost = 2.88


def calculate_order_cost(order):
    items = order.split(", ")
    total_cost = 0.0

    for item in items:
        components = item.split(" + ")
        quantity, product_type = components[0].split(" x ")
        quantity = int(quantity)

        if product_type == "regular":
            product = RegularCoffee()
        elif product_type == "decaf":
            product = DecafCoffee()
        elif product_type == "muffins":
            product = Muffins()
        elif product_type == "flapjacks":
            product = Flapjacks()
        elif product_type == "panettone":
            product = Panettone()

        extras = components[1:]
        if isinstance(product, Beverage):
            for extra in extras:
                if extra == "milk":
                    product.milk = True
                elif extra == "sugar":
                    product.sugar = True
                elif extra == "cream":
                    product.cream = True
                elif extra == "sprinkles":
                    product.sprinkles = True

            total_cost += product.getCost() * quantity
        else:
            total_cost += product.extra_cost * quantity

    return f"Final bill is ${total_cost:.2f}"


order_input = "1 x regular + milk + sugar, 1 x decaf + sprinkles, 2 x muffins"
print(calculate_order_cost(order_input))
