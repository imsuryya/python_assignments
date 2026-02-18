from datetime import datetime


def time_delta(t1: str, t2: str) -> int:
    """
    Calculate the absolute difference in seconds between two timestamps.
    
    Args:
        t1: First timestamp in format "Day dd Mon yyyy hh:mm:ss +xxxx"
        t2: Second timestamp in format "Day dd Mon yyyy hh:mm:ss +xxxx"
    
    Returns:
        Absolute difference in seconds
    """
    fmt = '%a %d %b %Y %H:%M:%S %z'
    
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    diff = abs((dt1 - dt2).total_seconds())
    
    return int(diff)
