import calendar


def get_day_of_week(month: int, day: int, year: int) -> str:
    """
    Get the day of the week for a given date.
    
    Args:
        month: Month (1-12)
        day: Day of the month
        year: Year
    
    Returns:
        Day of the week in uppercase
    """
    day_index = calendar.weekday(year, month, day)
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    return days[day_index]
