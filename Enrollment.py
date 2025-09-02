class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def __str__(self):
        return f"{self.student.Name} enrolled in {self.course.title}"        