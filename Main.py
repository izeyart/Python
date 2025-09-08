import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from Student import Student
from Course import Course
from Enrollment import Enrollment
from Attendance import Attendance
from Fee import FeeAccount

# "Databases"
students = {}
courses = {}
accounts = {}
attendances = {}
enrollments = []

# Tkinter main window
root = tk.Tk()
root.title("School Management System")
root.geometry("600x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame_student = ttk.Frame(notebook)
notebook.add(frame_student, text="Students")

tk.Label(frame_student, text="Student ID").grid(row=0, column=0)
tk.Label(frame_student, text="Name").grid(row=1, column=0)
tk.Label(frame_student, text="Email").grid(row=2, column=0)
tk.Label(frame_student, text="Phone").grid(row=3, column=0)

sID_entry = tk.Entry(frame_student); sID_entry.grid(row=0, column=1)
Name_entry = tk.Entry(frame_student); Name_entry.grid(row=1, column=1)
email_entry = tk.Entry(frame_student); email_entry.grid(row=2, column=1)
phone_entry = tk.Entry(frame_student); phone_entry.grid(row=3, column=1)

def register_student():
    sID = sID_entry.get()
    Name = Name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    if sID in students:
        messagebox.showerror("Error", "Student ID already exists")
        return
    s = Student(Name, email, phone)
    s.assign_StudentID(sID)
    students[sID] = s
    accounts[sID] = FeeAccount(s)
    messagebox.showinfo("Success", f"Registered {Name}")
    sID_entry.delete(0, tk.END); Name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END); phone_entry.delete(0, tk.END)

tk.Button(frame_student, text="Register", command=register_student).grid(row=4, column=1)

frame_course = ttk.Frame(notebook)
notebook.add(frame_course, text="Courses")

tk.Label(frame_course, text="Course Code").grid(row=0, column=0)
tk.Label(frame_course, text="Title").grid(row=1, column=0)
tk.Label(frame_course, text="Credit Hours").grid(row=2, column=0)
tk.Label(frame_course, text="Fee per Credit").grid(row=3, column=0)

code_entry = tk.Entry(frame_course); code_entry.grid(row=0, column=1)
title_entry = tk.Entry(frame_course); title_entry.grid(row=1, column=1)
credit_entry = tk.Entry(frame_course); credit_entry.grid(row=2, column=1)
fee_entry = tk.Entry(frame_course); fee_entry.grid(row=3, column=1)

def create_course():
    code = code_entry.get()
    title = title_entry.get()
    credit = int(credit_entry.get())
    fee = float(fee_entry.get())
    if code in courses:
        messagebox.showerror("Error", "Course already exists")
        return
    c = Course(code, title, credit, fee)
    courses[code] = c
    attendances[code] = Attendance(c)
    messagebox.showinfo("Success", f"Created course {title}")
    code_entry.delete(0, tk.END); title_entry.delete(0, tk.END)
    credit_entry.delete(0, tk.END); fee_entry.delete(0, tk.END)

tk.Button(frame_course, text="Create", command=create_course).grid(row=4, column=1)

frame_enroll = ttk.Frame(notebook)
notebook.add(frame_enroll, text="Enrollment")

tk.Label(frame_enroll, text="Student ID").grid(row=0, column=0)
tk.Label(frame_enroll, text="Course Code").grid(row=1, column=0)

sID_enroll_entry = tk.Entry(frame_enroll); sID_enroll_entry.grid(row=0, column=1)
code_enroll_entry = tk.Entry(frame_enroll); code_enroll_entry.grid(row=1, column=1)

def enroll_student():
    sID = sID_enroll_entry.get()
    code = code_enroll_entry.get()
    if sID in students and code in courses:
        e = Enrollment(students[sID], courses[code])
        enrollments.append(e)
        students[sID].enroll(courses[code])
        courses[code].add_student(students[sID])
        messagebox.showinfo("Success", f"{students[sID].Name} enrolled in {courses[code].title}")
    else:
        messagebox.showerror("Error", "Invalid student or course")

tk.Button(frame_enroll, text="Enroll", command=enroll_student).grid(row=2, column=1)

frame_attendance = ttk.Frame(notebook)
notebook.add(frame_attendance, text="Attendance")

tk.Label(frame_attendance, text="Course Code").grid(row=0, column=0)
att_code_entry = tk.Entry(frame_attendance); att_code_entry.grid(row=0, column=1)

def mark_attendance():
    code = att_code_entry.get()
    if code not in courses:
        messagebox.showerror("Error", "Course not found")
        return
    session_marks = {}
    for student in courses[code].students:
        status = tk.simpledialog.askstring("Attendance", f"{student.Name} (P/A):")
        if status is None: status = "A"
        session_marks[student.studentID] = status.upper()
    attendances[code].mark_session(session_marks)
    messagebox.showinfo("Success", "Attendance recorded")

tk.Button(frame_attendance, text="Mark Attendance", command=mark_attendance).grid(row=1, column=1)

frame_profile = ttk.Frame(notebook)
notebook.add(frame_profile, text="Profile & Fees")

tk.Label(frame_profile, text="Student ID").grid(row=0, column=0)
profile_sID_entry = tk.Entry(frame_profile); profile_sID_entry.grid(row=0, column=1)

def show_profile():
    sID = profile_sID_entry.get()
    if sID not in students:
        messagebox.showerror("Error", "Student not found")
        return
    s = students[sID]
    info = f"Name: {s.Name}\nEmail: {s.email}\nCourses:\n"
    for c in s.courses:
        percent = attendances[c.course_code].student_percentage(s.studentID)
        info += f" - {c.title} | Attendance: {percent:.1f}%\n"
    info += f"Balance: {accounts[sID].balance()}"
    messagebox.showinfo("Profile", info)

tk.Button(frame_profile, text="Show Profile", command=show_profile).grid(row=1, column=1)

def charge_tuition():
    sID = profile_sID_entry.get()
    if sID not in accounts:
        messagebox.showerror("Error", "Student not found")
        return
    total = sum(c.credit * c.fee for c in students[sID].courses)
    accounts[sID].charge(total)
    messagebox.showinfo("Charged", f"Tuition charged: {total}")

def make_payment():
    sID = profile_sID_entry.get()
    if sID not in accounts:
        messagebox.showerror("Error", "Student not found")
        return
    amount = float(tk.simpledialog.askstring("Payment", "Enter payment amount:"))
    accounts[sID].pay(amount)
    messagebox.showinfo("Payment", f"Payment of {amount} recorded")

tk.Button(frame_profile, text="Charge Tuition", command=charge_tuition).grid(row=2, column=0)
tk.Button(frame_profile, text="Make Payment", command=make_payment).grid(row=2, column=1)

root.mainloop()