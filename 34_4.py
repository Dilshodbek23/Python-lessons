import json

with open('students.json') as f:
    students_py = json.load(f)

print(students_py)
print(type(students_py))
name1 = students_py['student'][0]['name']
lastname1 = students_py['student'][0]['lastname']
course_num1 = students_py['student'][0]['year']
faculty1 = students_py['student'][0]['faculty']
name2 = students_py['student'][1]['name']
lastname2 = students_py['student'][1]['lastname']
course_num2 = students_py['student'][1]['year']
faculty2 = students_py['student'][1]['faculty']
name3 = students_py['student'][2]['name']
lastname3 = students_py['student'][2]['lastname']
course_num3 = students_py['student'][2]['year']
faculty3 = students_py['student'][2]['faculty']
print(f"{name1} {lastname1}, course number: {course_num1}, faculty: {faculty1}")
print(f"{name2} {lastname2}, course number: {course_num2}, faculty: {faculty2}")
print(f"{name3} {lastname3}, course number: {course_num3}, faculty: {faculty3}")
