def print_formatted(number: int) -> None:
    """
    Print formatted output for numbers 1 to number in decimal, octal, hex, and binary.
    
    Args:
        number: The maximum value to print
    """
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")


def format_number(num: int, base: str) -> str:
    """
    Format a number in the specified base.
    
    Args:
        num: The number to format
        base: The base ('dec', 'oct', 'hex', 'bin')
    
    Returns:
        Formatted string representation
    """
    if base == 'dec':
        return str(num)
    elif base == 'oct':
        return oct(num)[2:]
    elif base == 'hex':
        return hex(num)[2:].upper()
    elif base == 'bin':
        return bin(num)[2:]
    else:
        raise ValueError(f"Unsupported base: {base}")
