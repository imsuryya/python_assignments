from itertools import combinations


def calculate_probability(letters, k):
    """
    Calculate the probability that at least one of k selected indices contains 'a'.
    
    Args:
        letters: List of lowercase English letters
        k: Number of indices to select
        
    Returns:
        Probability as a float
    """
    n = len(letters)
    
    a_indices = [i for i, letter in enumerate(letters) if letter == 'a']
    
    if not a_indices:
        return 0.0
    
    if len(a_indices) == n:
        return 1.0
    
    total_combinations = len(list(combinations(range(n), k)))
    
    non_a_indices = [i for i in range(n) if i not in a_indices]
    
    if len(non_a_indices) < k:
        return 1.0
    
    combinations_without_a = len(list(combinations(non_a_indices, k)))
    
    combinations_with_a = total_combinations - combinations_without_a
    
    probability = combinations_with_a / total_combinations
    
    return probability
