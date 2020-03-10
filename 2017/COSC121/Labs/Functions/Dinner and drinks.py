def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    cost_of_drinks_discounted = drinks_cost - (drinks_cost * (3 / 10))     
    total_cost = (meal_cost + cost_of_drinks_discounted) * 1.15
    return total_cost
    