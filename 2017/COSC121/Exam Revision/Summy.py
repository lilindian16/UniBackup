def summy(nums):
    """docstring"""
    total = 0
    if len(nums) < 4:
        total = 0
    else:
        total += nums[1] + nums[-2]
    return total