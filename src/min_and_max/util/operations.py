import numpy as np


def min_max_operation(arr):
    """
    Perform min along axis 1 and then find max of that result.
    
    Args:
        arr: 2-D NumPy array
        
    Returns:
        Maximum of the minimums along axis 1
    """
    min_along_axis1 = np.min(arr, axis=1)
    max_of_min = np.max(min_along_axis1)
    
    return max_of_min
