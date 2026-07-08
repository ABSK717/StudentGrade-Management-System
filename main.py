import json
import os

def student_record():
    if not os.path.exists('StudentGrade-Management-System\student_records.json'):
        with open('StudentGrade-Management-System\student_records.json', 'w') as file:
            json.dump({}, file)

    with open('StudentGrade-Management-System\student_records.json', 'r') as file:
        data = json.load(file)
    return data

student_data = student_record()
print(student_data)