class Student:
    students = []  # Class variable to store student data

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        Student.students.append(self)

    @classmethod
    def add_student(cls, student_id, name, age):
        new_student = cls(student_id, name, age)
        print(f"Student {name} added successfully.")

    @classmethod
    def edit_student(cls, student_id, new_name, new_age):
        for student in cls.students:
            if student.student_id == student_id:
                student.name = new_name
                student.age = new_age
                print(f"Student {student_id} edited successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    @classmethod
    def delete_student(cls, student_id):
        for student in cls.students:
            if student.student_id == student_id:
                cls.students.remove(student)
                print(f"Student {student_id} deleted successfully.")
                return
        print(f"Student with ID {student_id} not found.")

# Example usage:
Student.add_student(1, "Alice", 20)
Student.add_student(2, "Bob", 22)

# Print current students
print("Current Students:")
for student in Student.students:
    print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}")

# Edit a student
Student.edit_student(1, "Alicia", 21)

# Delete a student
Student.delete_student(2)

# Print updated students
print("Updated Students:")
for student in Student.students:
    print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}")