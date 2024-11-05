# average_calculator.py

# List of students with their names and grades
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 84]},
    {"name": "Charlie", "grades": [75, 80, 79]},
    {"name": "Diana", "grades": [95, 94, 92]}
]

# Function to calculate the average of a list of grades
def calculate_average(grades):
    return sum(grades) / len(grades)

# Main function to calculate and save the averages
def main():
    # Open a text file to write the results
    with open("student_averages.txt", "w") as file:
        for student in students:
            # Calculate the average grade for each student
            average_grade = calculate_average(student["grades"])
            # Write the result to the file
            file.write(f"{student['name']}: {average_grade:.2f}\n")

    print("Student averages written to student_averages.txt")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
