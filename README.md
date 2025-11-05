# gradebook-.py
Analyzing and Reporting Student Grades
# 🎓 Gradebook Analyzer (Python CLI)

A command-line Gradebook Analyzer that allows users to enter student records manually or via CSV file, calculates statistics, assigns grades, and shows pass/fail results — all in a clean table format.
---
<img width="1348" height="928" alt="Screenshot 2025-11-05 160932" src="https://github.com/user-attachments/assets/2026ad9b-b2b2-42cf-bf7c-32d530d44789" />
OUTPUT:-
Enter 1 for manual entry or 2 for CSV import: 1
How many students? 5
Enter student name: ram
Enter marks: 77
Enter student name: aarav
Enter marks: 35
Enter student name: rohan
Enter marks: 60
Enter student name: harsh
Enter marks: 40
Enter student name: mohan
Enter marks: 37

Name    Marks   Grade
----------------------------
ram     77      C
aarav   35      F
rohan   60      D
harsh   40      F
mohan   37      F

Statistics:
Average: 49.80
Median: 40
Highest: 77
Lowest: 35

Grade Distribution: {'C': 1, 'F': 3, 'D': 1}
Passed Students (3): ['ram', 'rohan', 'harsh']
Failed Students (2): ['aarav', 'mohan']

Do you want to run again? (y/n): 
