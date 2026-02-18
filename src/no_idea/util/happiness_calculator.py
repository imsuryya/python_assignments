def calculate_happiness(array: list, set_a: set, set_b: set) -> int:
    """
    Calculate happiness based on array elements in sets A and B.
    
    Args:
        array: List of integers
        set_a: Set of integers we like (adds 1 to happiness)
        set_b: Set of integers we dislike (subtracts 1 from happiness)
    
    Returns:
        Total happiness
    """
    happiness = 0
    
    for element in array:
        if element in set_a:
            happiness += 1
        elif element in set_b:
            happiness -= 1
    
    return happiness
