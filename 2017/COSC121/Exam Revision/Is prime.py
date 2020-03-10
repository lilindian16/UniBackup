def isprime(n):
    """docstring"""
    numbers = []
    for num in range(1, n + 1):
        result = n % num
        if result == 0:
            numbers.append(result)

    if len(numbers) > 2:
        return False
    
    else:
        return True