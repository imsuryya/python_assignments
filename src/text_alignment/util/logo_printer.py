def print_rangoli(thickness: int) -> None:
    """
    Print the HackerRank logo of variable thickness.
    
    Args:
        thickness: The thickness value (must be odd)
    """
    c = 'H'
    
    # Top cone
    for i in range(thickness):
        print((c * (2 * i + 1)).center(thickness * 2))
    
    # Top pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
    # Middle belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))
    
    # Bottom pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
    # Bottom cone
    for i in range(thickness):
        print(((c * (2 * (thickness - i) - 1)).rjust(thickness * 2) + (thickness * 4) * ' '))
