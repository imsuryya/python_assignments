def find_runner_up(scores: list) -> int:
    """
    Find the runner-up (second maximum) score.
    
    Args:
        scores: List of integer scores
    
    Returns:
        The runner-up (second highest) score
    """
    # Remove duplicates by converting to set, then sort in descending order
    unique_scores = sorted(set(scores), reverse=True)
    
    # Return the second highest score
    return unique_scores[1]
