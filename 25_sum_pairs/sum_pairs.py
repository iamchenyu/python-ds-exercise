def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # Solution
    already_checked = set()
    for num in nums:
        other_pair = goal - num
        if other_pair in already_checked:
            return (other_pair, num)
        already_checked.add(num)
    return ()



    # checked = []
    # result = []
    # for num in nums: 
    #     other_pair = goal - num
    #     if other_pair in nums and other_pair not in checked:
    #         checked.append(num)
    #         result.append((num, other_pair))
    # if result:
    #     idx = min([nums.index(val2) for (val1, val2) in result])
    #     for (val1, val2) in result:
    #          if nums.index(val2) == idx:
    #             return ((val1, val2))
    # else:
    #     return ()
        
         
    

        
sum_pairs([5, 1, 4, 8, 3, 2], 7)
