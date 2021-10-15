"""Helper functions for matrix operations"""

import numpy as np


def create_matrix(values, row, col):
    """
    Parse a numpy matrix from a list of number.
    :param list values: list of matrix values, first row then col.
    :param int row: number of row.
    :param int col: number of columns.
    :return: a numpy matrix
    """
    if not values:
        print(f'Return empty {row}x{col} matrix')
        return np.matrix(np.zeros(shape=(row, col)))
    if (row * col) != len(values):
        raise ValueError(f'Cannot construct {row}x{col} matrix from this set of values')
    print(f'Return {row}x{col} matrix')
    return np.matrix([values[i:i+col] for i in range(0, len(values), col)])
