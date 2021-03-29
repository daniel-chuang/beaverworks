# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

"""
**Pizza**
- \$13.00

**Toppings**
- pepperoni : \$1.00
- mushroom : \$0.50
- olive : \$0.50
- anchovy : \$2.00
- ham : \$1.50

**Drinks**
- small : \$2.00
- medium : \$3.00
- large : \$3.50
- tub : \$3.75

**Wings**
- 10 : \$5.00
- 20 : \$9.00
- 40 : \$17.50
- 100 : \$48.00
"""

def cost_calculator(*pizzas, wings=[], drinks=[], coupon=0.0):
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    print(pizzas, drinks, wings, coupon)
    # Set up the original cost and the prices for things
    cost = 0.0
    topping_costs = {"pepperoni":1.0, "mushroom":0.50, "olive":0.50, "anchovy":2.00, "ham":1.50}
    drink_costs = {"small":2.0, "medium":3.0, "large":3.5,"tub":3.75}
    wings_cost = {10:5.0, 20:9.0, 40:17.50,100:48.00}

    # Loops through the pizzas
    for pizza in pizzas:
        cost += 13.0 # Base cost of pizza
        for topping in pizza:
            cost += topping_costs[topping]

    # Loops through the drinks
    for drink in drinks:
        cost += drink_costs[drink]

    # Loops through the wings
    for wing in wings:
        cost += wings_cost[wing]

    taxed_cost = cost*1.0625

    discounted_cost = cost * coupon

    cost = round(taxed_cost - discounted_cost, 2)

    return cost