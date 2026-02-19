import numpy as np


def calculate_determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    
    Args:
        matrix: Square NumPy array
        
    Returns:
        Determinant rounded to 2 decimal places
    """
    det = np.linalg.det(matrix)
    return round(det, 2)
