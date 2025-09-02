class Student:
    def __init__(self,Name,email, phone):
        self.Name = Name
        self.email = email
        self.phone = phone
        self.studentID = None
        self.courses = []

    def assign_StudentID(self, sID):
        self.studentID = sID        

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{self.studentID}  {self.Name} ({self.email})"