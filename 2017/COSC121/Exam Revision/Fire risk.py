def fire_risk(rainfall, material):
    """docstring"""
    if material == "Grass" and rainfall < 20:
        return "High"
    elif material == "Grass" and rainfall >= 20:
        return "Medium"
    elif material == "Wood" and rainfall < 20:
        return "Medium"
    else:
        return "Low"