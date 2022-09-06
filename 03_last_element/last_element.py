def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # return lst[len(lst)-1] if lst else None

    #Solution
    if lst:
        return lst[-1]