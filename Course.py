class Course:
    def __init__(self, course_code, title, credit, fee):
        self.course_code = course_code
        self.title = title
        self.credit = credit
        self.fee = fee
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"{self.course_code} {self.title}"