student_info = {
    'Anu': {'Math': 85, 'Science': 90, 'English': 78},
    'Keerthu': {'Math': 92, 'Science': 88, 'English': 95},
    'Nikhil': {'Math': 78, 'Science': 85, 'English': 88}
}
students = ['Anu', 'Keerthu', 'Nikhil']
subjects = ['Math', 'Science', 'English']
i= 0
while i < len(students):
    student = students[i]
    print(f"Grades for {student}:")
    j= 0
    while j < len(subjects):
        subject = subjects[j]
        grade = student_info[student][subject]
        print(f"{subject}: {grade}")
        
        if grade < 80:
            print(f" - Needs improvement in {subject}")
        j += 1
    i += 1

print("Grade analysis completed.")
