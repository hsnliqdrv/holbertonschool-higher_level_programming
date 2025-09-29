#!/usr/bin/python3
"""12-pascal_triangle
"""


def pascal_triangle(n):
    """Gives pascal triangle of given height

    Arguments:
        n (int): height

    Returns:
        (list of lists): pascal triangle
    """
    if (n <= 0):
        return []
    arr = [[1]]
    for i in range(n - 1):
        arr.append(arr[-1] + [1])
        for j in range(len(arr[-1]) - 2, 0, -1):
            arr[-1][j] += arr[-1][j - 1]
    return arr

if __name__ == "__main__":
    print(pascal_triangle(5))
