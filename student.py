class Student:
    def __init__(self, studentName, marks):
        self.studentName = studentName
        self.marks = marks

# Create an instance of the Student class
student1 = Student("Samrat", 85)

# Print the original attribute values
print("Original Attribute Values:")
print(f"Student Name: {student1.studentName}")
print(f"Marks: {student1.marks}")

# Modify the attribute values
student1.studentName = "Akbor"
student1.marks = 92

# Print the modified attribute values
print("\nModified Attribute Values:")
print(f"Student Name: {student1.studentName}")
print(f"Marks: {student1.marks}")