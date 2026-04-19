import json

user_json = """
{
    "name": "Elena",
    "age": 29,
    "skills": ["Python", "API Testing", "SQL"],
    "is_student": true
}
"""
user_data = json.loads(user_json)
# print(user_data)
# print("User name:", user_data.get("name"))
# print("User's skills:", user_data.get("skills"))
# print("Object type:", type(user_data))

data = {
    "project": "autotests-api",
    "tests": 15,
    "passed": True,
    "failed": 2
}

test_data = json.dumps(data, indent=4, sort_keys=True)
parsed_test_data = json.loads(test_data)

assert parsed_test_data["project"] == "autotests-api"
assert parsed_test_data["passed"] is True
# print(parsed_test_data, type(parsed_test_data))
# print(test_data)
# print("Type:", type(test_data))

with open("student.json", "r") as file:
    student = json.load(file)

assert student["name"] == "Anna"
assert student["course"] == "QA Automation"


# print(student, "Object type", type(student))
# print("Name: ",student.get("name"))
# print("Course: ", student.get("course"))
# print(student.get("age", "No age provided"))

new_user = {
    "name": "Mike",
    "age": 31,
    "city": "Miami",
    "has_experience": True
}

JSON_FILE = "new_user.json"

with open(JSON_FILE, "w") as file:
    json.dump(new_user, file, indent=4)

with open(JSON_FILE, "r") as file:
    data = json.load(file)
assert data["name"] == "Mike"