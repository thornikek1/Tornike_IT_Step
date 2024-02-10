import csv
import os

# სტუდენტის დამატება ფაილში
def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    subject_name = input("Enter subject name: ")
    marks = int(input("Enter marks: "))

    filename = "students.csv"
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, grade, subject_name, marks])

# ინფორმაციის წაკითხვა
def read_students(student_id=None):
    filename = "students.csv"
    students = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if student_id is None or (student_id and int(row[0]) == student_id):
                students.append(row)
    return students

# ქულის განახლება
def update_score():
    student_id = int(input("Enter student ID: "))
    subject_name = input("Enter subject name: ")
    updated_score = int(input("Enter updated score: "))

    filename = "students.csv"
    temp_filename = "temp.csv"
    with open(filename, mode='r') as infile, open(temp_filename, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if int(row[0]) == student_id and row[4] == subject_name:
                row[5] = updated_score
            writer.writerow(row)
    os.remove(filename)
    os.rename(temp_filename, filename)

# ტესტირება
if __name__ == "__main__":
    while True:
        print("\n1. Add a student")
        print("2. Read student information")
        print("3. Update student's score")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            student_id = int(input("Enter student ID to read information (Enter 0 to read all): "))
            print(read_students(student_id))
        elif choice == '3':
            update_score()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")