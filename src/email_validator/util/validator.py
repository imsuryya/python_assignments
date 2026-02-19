import re


def fun(s):
    """
    Validate if a string is a valid email address.
    
    Rules:
    - Format: username@websitename.extension
    - Username: letters, digits, dashes, underscores
    - Website name: letters and digits
    - Extension: only letters, max length 3
    
    Args:
        s: String to validate
        
    Returns:
        True if valid email, False otherwise
    """
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s) is not None


def filter_emails(emails):
    """
    Filter and sort valid email addresses.
    
    Args:
        emails: List of email strings
        
    Returns:
        Sorted list of valid emails
    """
    valid_emails = list(filter(fun, emails))
    return sorted(valid_emails)
