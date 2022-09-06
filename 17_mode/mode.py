def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Option 1
    dict = {num: nums.count(num) for num in nums}
    for key in dict.keys():
        if dict[key] == sorted(dict.values(), reverse=True)[0]: # or use built-in function max(dict.values())
            return key

    # Option 2
    # max = 1
    # number = None
    # for num in nums:
    #     if nums.count(num) > max:
    #         max = nums.count(num)
    #         number = num
    # return number