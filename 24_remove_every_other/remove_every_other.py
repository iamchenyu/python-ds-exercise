def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    # Solution 1
    return lst[::2]

    # Solution 2
    return [item for count, item in enumerate(lst) if count % 2 == 0]


    # new_list = []
    # for el in lst:
    #     if lst.index(el) % 2 == 0:
    #         new_list.append(el)
    # return new_list

    # use list comprehensions
    return [el for el in lst if lst.index(el) % 2 == 0]
