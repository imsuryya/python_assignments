from collections import namedtuple


def calculate_student_average(n: int, columns: list, students_data: list) -> float:
    """
    Calculate the average marks of students using namedtuple.
    
    Args:
        n: Number of students
        columns: List of column names
        students_data: List of student data rows
    
    Returns:
        Average marks rounded to 2 decimal places
    """
    Student = namedtuple('Student', columns)
    total = 0
    
    for data in students_data:
        student = Student(*data)
        total += int(student.MARKS)
    
    return total / n
