def count_word_occurrences(words: list) -> tuple:
    """
    Count word occurrences maintaining order of first appearance.
    
    Args:
        words: List of words
    
    Returns:
        Tuple of (distinct_count, list of occurrence counts)
    """
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    distinct_count = len(word_count)
    occurrences = list(word_count.values())
    
    return distinct_count, occurrences
