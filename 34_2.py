import json

student_json = """{"name":"Hasan","surname":"Husanov","ybirth":2000}"""

student = json.loads(student_json)

print(student['name'], student['surname'])

with open('student.json', 'w') as f:
    json.dump(student, f)