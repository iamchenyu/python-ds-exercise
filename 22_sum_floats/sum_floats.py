def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    
    # Solution
    return sum([num for num in nums if isinstance(num, float)]) # can use sum([list]) function

    
    # sum = 0
    # for num in nums:
    #     # Option 1
    #     # if type(num) == float:
    #     #     sum = sum + num

    #     # Option 2
    #     if isinstance(num, float):
    #         sum = sum + num
    # return sum
