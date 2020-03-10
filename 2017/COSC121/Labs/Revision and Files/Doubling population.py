def num_doublings(initial_population, final_population):
    """This will find out how long it takes for the population to double
    """
    doubling = 0
    current_pop = initial_population
    
    while current_pop < final_population:
        current_pop *= 2
        doubling += 1
        
    return doubling