import json

# Python program to convert JSON to Dict
# Assuming you have some JSON data in a string
# data = '{"name": "John", "age": 30, "city": "New York"}'
#
# # Use json.loads to parse the JSON data
# empdict = json.loads(data)
#
# # Now empdict contains a Python dictionary
# print(empdict)
# print(f"typt of data :{type(data)} \ntype of empdict :{type(empdict)} ")
#################################################
# Python program to read json file
with open('test.json','r') as f:
# returns JSON object as
# a dictionary
    data = json.load(f)
    print(data)

# Serializing json
json_object = json.dumps(data)
print(json_object)
print(f"type of data : {type(data)}, type of json object : {type(json_object)}")

dictionary = {
    "name": "Nisha",
    "rollno": 420,
    "cgpa": 10.10,
    "phonenumber": "1234567890"
}
json.dump(dictionary,f)
f.close()