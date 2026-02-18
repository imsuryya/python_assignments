def can_pile_up(cubes: list) -> bool:
    """
    Check if cubes can be stacked vertically by picking from left or right.
    
    Args:
        cubes: List of cube side lengths
    
    Returns:
        True if cubes can be stacked, False otherwise
    """
    left = 0
    right = len(cubes) - 1
    last_cube = float('inf')
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1
        
        if current > last_cube:
            return False
        
        last_cube = current
    
    return True
