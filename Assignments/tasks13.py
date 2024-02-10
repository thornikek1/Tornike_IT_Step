my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

def display_student_ids_and_get_input(my_dict):
    # Display the list of student IDs
    student_ids = [str(student["id"]) for student in my_dict["students"]]
    print("Student IDs: " + ", ".join(student_ids))
    
    # Get input from the user
    selected_id = input("Enter the student ID: ")
    
    # Validate the input
    if selected_id not in student_ids:
        print("Invalid student ID. Please enter a valid ID.")
        return
    
    # Find the selected student
    selected_student = next(student for student in my_dict["students"] if str(student["id"]) == selected_id)
    
    # Display the student information
    print("\nStudent Information:")
    print(f"ID: {selected_student['id']}, Name: {selected_student['name'].capitalize()}, Age: {selected_student['age']}")
    
    # Display the grades for each subject
    for subject in my_dict["subjects"]:
        grade = subject["grades"][selected_id]
        print(f"Subject: {subject['name']}, Grade: {grade}")

display_student_ids_and_get_input(my_dict)