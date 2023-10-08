class  Student:
    def __init__(self, studentId, studentName):
        self.studentName = studentName
        self.studentId = studentId
        
    def display_attributes(self):
        attributes = vars(self)
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")
        
# Create an instance of the Student class
student1 = Student("Samrat", 85)

# Display all attributes and their values
print("Attributes and Values:")
print(f"Student ID: {student1.studentId}")
print(f"Student Name: {student1.studentName}")

# Add a new attribute 'studentClass'
student1.studentClass = "Class 10"


# Display all attributes and their values with the new attribute
print("\nAttributes and Values (with studentClass):")
print(f"Student ID: {student1.studentId}")
print(f"Student Name: {student1.studentName}")
print(f"Student Class: {student1.studentClass}")


# Remove the 'studentName' attribute
del student1.studentName

# Display all attributes and their values after removing 'studentName'
print("\nAttributes and Values (after removing studentName):")
print(f"Student ID: {student1.studentId}")
# This will raise an AttributeError because 'studentName' has been removed
# print(f"Student Name: {student1.studentName}")
print(f"Student Class: {student1.studentClass}")


print("Displaying all attributes and their values using a method:")
student1.display_attributes()



