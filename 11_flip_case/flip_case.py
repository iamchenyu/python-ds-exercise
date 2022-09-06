def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # Solution 1
    to_swap = to_swap.lower()
    result = [char.swapcase() if char.lower() == to_swap else char for char in phrase]
    return "".join(result)

    # Solution 2
    to_swap = to_swap.lower()
    result = ""
    for char in phrase:
        if char.lower() == to_swap:
            char = char.swapcase()
        result = result + char
    return result



    fliped_list = []
    if to_swap.lower() == to_swap:
        for char in phrase:
            if char == to_swap:
                fliped_list.append(char.upper())
            elif char.lower() == to_swap:
                fliped_list.append(char.lower())
            else:
                fliped_list.append(char)
    if to_swap.upper() == to_swap:
        for char in phrase:
            if char == to_swap:
                fliped_list.append(char.lower())
            elif char.upper() == to_swap:
                fliped_list.append(char.upper())
            else:
                fliped_list.append(char)
    return "".join(fliped_list)


