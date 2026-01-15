"""
Example 2: Student Grade Manager
Demonstrates lists, dictionaries, and functions.
"""

def add_student(students, name, grades):
    """Add a student to the dictionary."""
    students[name] = grades
    print(f"Added {name} to the system.")

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def display_student(name, grades):
    """Display student information."""
    avg = calculate_average(grades)
    print(f"\nStudent: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {avg:.2f}")
    
    if avg >= 90:
        print("Grade: A")
    elif avg >= 80:
        print("Grade: B")
    elif avg >= 70:
        print("Grade: C")
    elif avg >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def main():
    """Main function to run the grade manager."""
    students = {}
    
    # Add some students
    add_student(students, "Alice", [95, 87, 92, 88])
    add_student(students, "Bob", [78, 85, 82, 90])
    add_student(students, "Charlie", [92, 94, 89, 95])
    
    # Display all students
    print("\n" + "="*40)
    print("Student Grade Report")
    print("="*40)
    
    for name, grades in students.items():
        display_student(name, grades)
    
    # Find top student
    print("\n" + "="*40)
    top_student = max(students.items(), key=lambda x: calculate_average(x[1]))
    print(f"Top Student: {top_student[0]}")
    print(f"Average: {calculate_average(top_student[1]):.2f}")

if __name__ == "__main__":
    main()
