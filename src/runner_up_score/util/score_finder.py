def find_runner_up(scores: list) -> int:
    """
    Find the runner-up (second maximum) score.
    
    Args:
        scores: List of integer scores
    
    Returns:
        The runner-up (second highest) score
    """
    unique_scores = sorted(set(scores), reverse=True)
    return unique_scores[1]
