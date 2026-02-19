import numpy as np


def apply_operations(arr):
    """
    Apply floor, ceil, and rint operations to a NumPy array.
    
    Args:
        arr: NumPy array of floats
        
    Returns:
        Tuple of (floor_result, ceil_result, rint_result)
    """
    np.set_printoptions(legacy='1.13')
    
    floor_result = np.floor(arr)
    ceil_result = np.ceil(arr)
    rint_result = np.rint(arr)
    
    return floor_result, ceil_result, rint_result
