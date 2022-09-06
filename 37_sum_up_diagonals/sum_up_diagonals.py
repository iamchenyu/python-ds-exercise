def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    start_with_top_left = [matrix[y][y] for y in range(len(matrix))]
    start_with_top_right = [matrix[y][len(matrix)-1-y] for y in range(len(matrix))]
    # or matrix[y][-1-y]

    return sum(start_with_top_left) + sum(start_with_top_right)

    # Solution
    # return sum([matrix[y][y] + matrix[y][-1-y] for y in range(len(matrix))])