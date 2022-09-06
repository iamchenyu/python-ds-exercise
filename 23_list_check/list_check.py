def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # Option 1
    for el in lst:
        if type(el) != list: # or use if not
            return False
    return True

    # Option 2
    # for el in lst:
    #     if isinstance(el, list) == False:
    #         return False
    # return True