def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    reversed_vowels = [char for char in s if char in "aAeEiIoOuU"][::-1]
    idx = 0
    changed_str = []
    for char in s:
        if char in "aAeEiIoOuU":
            char = reversed_vowels[idx]
            idx = idx + 1
        changed_str.append(char)
    return "".join(changed_str)