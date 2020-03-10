def unique_species(animal_species):
    """
    """
    end = []
    species = animal_species.values()
    
    for spec in sorted(species):
        if spec not in end:
            
            end.append(spec)
        
    return end
        