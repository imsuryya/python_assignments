import numpy as np


def compute_statistics(arr):
    """
    Compute mean, variance, and standard deviation on a 2-D array.
    
    Args:
        arr: 2-D NumPy array
        
    Returns:
        Tuple of (mean along axis 1, var along axis 0, std of entire array)
    """
    mean_axis1 = np.mean(arr, axis=1)
    var_axis0 = np.var(arr, axis=0)
    std_all = np.std(arr)
    
    return mean_axis1, var_axis0, std_all
