def merge_the_tools(string: str, k: int) -> None:
    """
    Split string into substrings of length k and remove duplicate characters
    from each substring while maintaining order.
    
    Args:
        string: The input string to process
        k: The length of each substring
    """
    # Calculate number of substrings
    n = len(string)
    num_substrings = n // k
    
    # Process each substring
    for i in range(num_substrings):
        # Extract substring of length k
        start = i * k
        end = start + k
        substring = string[start:end]
        
        # Remove duplicates while maintaining order
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        # Print the result
        print(''.join(result))


def remove_duplicates(s: str) -> str:
    """
    Remove duplicate characters from a string while maintaining order.
    
    Args:
        s: The input string
    
    Returns:
        String with duplicates removed
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
