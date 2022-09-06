def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # formatted_str = "".join(phrase.lower().split())
    # str_list = list(formatted_str)
    # str_list.reverse()
    # reversed_str = "".join(str_list)
    # return True if formatted_str == reversed_str else False

    # Solution
    normalized_phrase = phrase.lower().replace(" ", "")
    return normalized_phrase == normalized_phrase[::-1]
