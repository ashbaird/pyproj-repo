student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "A - Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "B - Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "C - Acceptable"
    else:
        student_grades[key] = "D - Fail"   

print(student_grades)