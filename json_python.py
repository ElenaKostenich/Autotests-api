import json

json_data = """{
  "name": "Ivan",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python", "QA Automation", "API Testing"
  ],
  "address": {
    "city": "Moscow",
    "zip": 123123
  }
}"""

parsed_data = json.loads(json_data)
print(parsed_data)

data = {
    "name": "Mary",
    "age": 25,
    "is_student": True,
    "courses": []
}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open ("json_user.json", "w") as file:
    json.dump(data, file, indent=4)
