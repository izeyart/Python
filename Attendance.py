class Attendance:
    def __init__(self, course):
        self.course = course
        self.records = {}

    def mark_session(self, session_marks):
        self.records.append(session_marks)

    def student_percentage(self, studentID):
        total_sessions = len(self.records)
        if total_sessions == 0:
            return 0
        present = sum(1 for session in self.records if session.get(studentID)== "P")
        return (present /total_sessions)*100