def calculate_average(marks: list) -> float:
    """
    Calculate the average of marks.
    
    Args:
        marks: List of marks (can be int or float)
    
    Returns:
        Average of the marks
    """
    if not marks:
        return 0.0
    return sum(marks) / len(marks)
