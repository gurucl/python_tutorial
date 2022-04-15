import json

file_content = open('/Users/gurumurthy.cl/Documents/python_tutorial/resources/json_data.json', 'r')

file_data = file_content.read()

json_data = json.loads(file_data)

data = json_data['data']

# print("Type:", type(data))

# print("Data:", data)