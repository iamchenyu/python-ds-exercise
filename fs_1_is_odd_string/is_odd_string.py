def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # alphabet = []
    # for i in range(97, 123):
    #     alphabet.append(chr(i))
    # chart = {}
    # i = 1
    # while i < 26:
    #     for char in alphabet:
    #         chart[char] = i
    #         i = i + 1
    # sum = 0
    # for char in word.lower():
    #     sum = sum + chart[char]
    # if sum % 2 == 0:
    #     return False
    # else:
    #     return True

    # Formatted version:
    DIFFERENCE = 96 # because ord("a") is 97, so start from 1 means to subtract 96
    # or DIFFERENCE = ord("a") - 1
    return sum([ord(char) - DIFFERENCE for char in word.lower()]) % 2 == 1


    
    
        
    
