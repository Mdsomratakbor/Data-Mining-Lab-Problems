class Student:
    pass
class Marks:
    pass

student1 = Student()
marks = Marks()

is_instance_studetn = isinstance(student1, Student)
is_instance_marks = isinstance(marks, Marks)

print("Is student1 instance of Student: ", is_instance_studetn)
print("Is marks instance of Marks: ", is_instance_marks)

is_subclass_student = issubclass(Student, Marks)
is_subclass_marks = issubclass(Marks, Student)

print("Is Student subclass of Marks: ", is_subclass_student)
print("Is Marks subclass of Student: ", is_subclass_marks)

is_student_subclass_object = isinstance(student1, object)
is_marks_subclass_object = isinstance(marks, object)

print("Is student1 subclass object of Marks: ", is_student_subclass_object)
print("Is marks subclass object of Student: ", is_marks_subclass_object) 