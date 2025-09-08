Total_grade=0
Total_credit=0
Listing={}



number_of_courses=int(input("Enter the total number of courses: "))
    
for i in range(number_of_courses):
    course =input("Enter course "+str(i+1)+": ")
    score=int(input("Enter the score: "))
    credit_hours=int(input("Enter credit hours: "))
    Listing[course]=score

Total_grade+=score
Total_credit+=credit_hours


print(Total_grade)
print(Total_credit)
