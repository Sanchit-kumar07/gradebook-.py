# gradebook.py
# Author: Sanchit Kumar
# Date: 2025-11-05
# Title: Gradebook Analyzer Project

# Task 1: Project Setup and Initialization
import csv

print(" Welcome to the Gradebook Analyzer ")
print("--------------------------------------")
print("Choose your data input method:")
print("1. Manual Entry")
print("2. Import from CSV File\n")


#  Task 2: Data Entry or CSV Import
def get_data():
    choice = input("Enter 1 for manual entry or 2 for CSV import: ")
    marks = {}

    if choice == "1":
        n = int(input("How many students? "))
        for i in range(n):
            name = input("Enter student name: ")
            score = int(input("Enter marks: "))
            marks[name] = score

    elif choice == "2":
        filename = input("Enter CSV file name (with .csv): ")
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 2:  # prevent error
                        name, score = row
                        marks[name] = int(score)
        except FileNotFoundError:
            print(" File not found. Try again.")
            return get_data()

    else:
        print(" Invalid choice, try again.")
        return get_data()

    return marks


#  Task 3: Statistical Analysis Functions
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n % 2 == 1:
        return scores[n // 2]
    else:
        return (scores[n//2 - 1] + scores[n//2]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


#  Task 4: Grade Assignment and Distribution
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def count_grades(grades):
    grade_count = {}
    for g in grades.values():
        grade_count[g] = grade_count.get(g, 0) + 1
    return grade_count


#  Task 5: Pass/Fail Filter with List Comprehension
def pass_fail(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed


#  Task 6: Results Table and User Loop
while True:
    marks = get_data()

    if len(marks) == 0:
        print(" No data entered. Try again.\n")
        continue

    grades = assign_grades(marks)

    print("\nName\tMarks\tGrade")
    print("----------------------------")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")

    print("\nStatistics:")
    print(f"Average: {calculate_average(marks):.2f}")
    print(f"Median: {calculate_median(marks)}")
    print(f"Highest: {find_max_score(marks)}")
    print(f"Lowest: {find_min_score(marks)}")

    print("\nGrade Distribution:", count_grades(grades))

    passed, failed = pass_fail(marks)
    print(f"Passed Students ({len(passed)}): {passed}")
    print(f"Failed Students ({len(failed)}): {failed}")

    again = input("\nDo you want to run again? (y/n): ").lower()
    if again != "y":
        print("bye")
        break