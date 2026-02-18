def mutate_string(string: str, position: int, character: str) -> str:
    """
    Mutate a string by changing the character at a given position.
    
    Args:
        string: The original string to mutate
        position: The index position to change
        character: The new character to insert
    
    Returns:
        The mutated string
    """
    # Convert string to list, modify, and join back
    string_list = list(string)
    string_list[position] = character
    return ''.join(string_list)
