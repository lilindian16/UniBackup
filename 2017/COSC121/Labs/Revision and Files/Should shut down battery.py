def should_shutdown(battery_level, time_on):
    """This function will decide if you need to shut down the battery or not
    """
    if battery_level < 4.7 and time_on < 60:
        return True
    elif battery_level < 4.8 and time_on >= 60:
        return True
    else:
        return False
    