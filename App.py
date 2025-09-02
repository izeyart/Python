from Student import Student
from Course import Course
from Enrollment import Enrollment
from Attendance import Attendance
from Fee import FeeAccount

students = {}
courses = {}
accounts = {}
enrollments = []
attendances = {}

def register_student():
    sID = input("Enter Student ID: ")
    Name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    s = Student(Name, email, phone)
    s.assign_StudentID(sID)
    students[sID] = s
    accounts[sID] = FeeAccount(s)
    print("Student registered!")

def create_course():
    code = input("Enter Course Code: ")
    title = input("Enter Course Title: ")
    credit = int(input("Enter Credit Hours: "))
    fee = float(input("Enter Fee per Credit: "))
    c = Course(code, title, credit, fee)
    courses[code] = c
    attendances[code] = Attendance(c)
    print("Course created!")

def enroll_student():
    sID = input("Enter Student ID: ")
    code = input("Enter Course Code: ")
    if sID in students and code in courses:
        e = Enrollment(students[sID], courses[code])
        enrollments.append(e)
        students[sID].enroll(courses[code])
        courses[code].add_student(students[sID])
        print("Enrollment successful!")
    else:
        print("Invalid student or course")

def mark_attendance():
    code = input("Enter Course Code: ")
    if code not in attendances:
        print("Course not found.")
        return
    session_marks = {}
    for student in courses[code].students:
        status = input(f"Mark {student.Name} (P/A): ").upper()
        if status not in ["P", "A"]:
            status = "A"
    print("Attendance recorded!")

def fee_management():
    sID = input("Enter Student ID: ")
    if sID not in accounts:
        print("Student not found.")
        return
    print("1. Charge Tuition")
    print("2. Make Payment")
    choice = input("Enter choice: ")
    if choice == "1":
        total = 0
        for c in students[sID].courses:
            total += c.credit * c.fee
        accounts[sID].charge(total, "Tuition")
        print("Charged tuition:", total)
    elif choice == "2":
        amount = float(input("Enter payment amount: "))
        accounts[sID].pay(amount, "Payment")
        print("Payment recorded!")
    print("Balance:", accounts[sID].balance())

def show_student_profile():
    sID = input("Enter Student ID: ")
    if sID not in students:
        print("Student not found.")
        return
    s = students[sID]
    print("\n--- Student Profile ---")
    print(s)
    print("Courses:")
    for c in s.courses:
        percent = attendances[c.course_code].student_percentage(s.studentID)
        print(f"{c.title} | Attendance: {percent:.1f}%")
        print("Balance:", accounts[sID].balance())

def menu():
    while True:
        print("\n--- IZEYART SMS ---")
        print("1. Register Student")
        print("2. Create Course")
        print("3. Enroll Student")
        print("4. Mark Attendance")
        print("5. Fee Management")
        print("6. Show Student Profile")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            register_student()
        elif choice == "2":
            create_course()
        elif choice == "3":
            enroll_student()
        elif choice == "4":
            mark_attendance()
        elif choice == "5":
            fee_management()
        elif choice == "6":
            show_student_profile()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
