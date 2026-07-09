import json
import os

def student_record():
    if not os.path.exists('StudentGrade-Management-System\student_records.json'):
        with open('StudentGrade-Management-System\student_records.json', 'w') as file:
            json.dump({}, file)

    with open('StudentGrade-Management-System\student_records.json', 'r') as file:
        data = json.load(file)
    return data

def add_student_record(student_id, name, age, student_class, physics_marks, chemistry_marks, mathematics_marks):
    import json
    data = student_record()
    data[student_id] = {
        'name': name,
        'age': age,
        'class': student_class,
        'physics_marks': physics_marks,
        'chemistry_marks': chemistry_marks,
        'mathematics_marks': mathematics_marks
    }
    with open('StudentGrade-Management-System\students_record.json', 'w') as file:
        json.dump(data, file, indent=4)

def update_student_record(student_id, name=None, age=None, student_class=None, physics_marks=None, chemistry_marks=None, mathematics_marks=None):
    import json
    data = student_record()
    if student_id in data:
        if name is not None:
            data[student_id]['name'] = name
        if age is not None:
            data[student_id]['age'] = age
        if student_class is not None:
            data[student_id]['class'] = student_class
        if physics_marks is not None:
            data[student_id]['physics_marks'] = physics_marks
        if chemistry_marks is not None:
            data[student_id]['chemistry_marks'] = chemistry_marks
        if mathematics_marks is not None:
            data[student_id]['mathematics_marks'] = mathematics_marks
    with open('students_record.json', 'w') as file:
        json.dump(data, file, indent=4)

def delete_student_record(student_id):
    import json
    data = student_record()
    if student_id in data:
        del data[student_id]
    with open('students_record.json', 'w') as file:
        json.dump(data, file, indent=4)


def search_student_record(student_id):
    data = student_record()
    if student_id in data:
        return data[student_id]
    else:
        return None


if __name__ =="__main__":
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student Record")
        print("2. Update Student Record")
        print("3. Delete Student Record")
        print("4. Search Student Record")

        choice = input("Enter your choice: ")
    
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            class_name = input("Enter Class: ")
            physics_marks = int(input("Enter Physics Marks: "))
            chemistry_marks = int(input("Enter Chemistry Marks: "))
            mathematics_marks = int(input("Enter Mathematics Marks: "))
            add_student_record(student_id, name, age, class_name, physics_marks, chemistry_marks, mathematics_marks)
            print("Student record added successfully.")
    
        if choice == '2':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter Name (leave blank to skip): ")
            age_input = input("Enter Age (leave blank to skip): ")
            class_name = input("Enter Class (leave blank to skip): ")
            physics_marks_input = input("Enter Physics Marks (leave blank to skip): ")
            chemistry_marks_input = input("Enter Chemistry Marks (leave blank to skip): ")
            mathematics_marks_input = input("Enter Mathematics Marks (leave blank to skip): ")
    
            age = int(age_input) if age_input else None
            physics_marks = int(physics_marks_input) if physics_marks_input else None
            chemistry_marks = int(chemistry_marks_input) if chemistry_marks_input else None
            mathematics_marks = int(mathematics_marks_input) if mathematics_marks_input else None
    
            update_student_record(student_id, name=name or None, age=age, student_class=class_name or None,
                                  physics_marks=physics_marks, chemistry_marks=chemistry_marks,
                                  mathematics_marks=mathematics_marks)
            print("Student record updated successfully.")
    
    
        if choice == '3':
            student_id = input("Enter Student ID to delete: ")
            delete_student_record(student_id)
            print("Student record deleted successfully.")
    
    
    
        if choice == '4':
        
            student_id = input("Enter Student ID to search: ")
            record = search_student_record(student_id)
            if record:
                print(f"Student ID: {student_id}")
                print(f"Name: {record['name']}")
                print(f"Age: {record['age']}")
                print(f"Class: {record['class']}")
                print(f"Physics Marks: {record['physics_marks']}")
                print(f"Chemistry Marks: {record['chemistry_marks']}")
                print(f"Mathematics Marks: {record['mathematics_marks']}")
            else:
                print("Student record not found.")



