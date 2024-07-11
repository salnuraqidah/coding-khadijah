import json

data = {
  "employees" : [
    {
      "firstName" : "Jhon",
      "lastName" : "Doe"
    },
    {
      "firstName" : "Anna",
      "lastName" : "Smith"
    },
    {
      "firstName" : "Peter",
      "lastName" : "Jonas"
    },
  ]
}

print(type(data))

with open("11juli/data_file.json","w") as file:
  json.dump(data, file)
  

print(json.dumps(data, indent=2))


json_string = """
{
  "firstName" : "Salamah",
  "lastName" : "Aqidah",
  "address" : "Bekasi"
}
"""

print(type(json_string))
py_dict = json.loads(json_string)
print(py_dict)
print(type(py_dict))

with open("11juli/data_file.json","r") as file:
  py_dict_2 = json.load(file)
  
print(py_dict_2)
  
with open("11juli/data_json.json","r") as file:
  datas = json.load(file)
  
print(type(datas))
print(json.dumps(datas, indent=4))

print(datas[0]['name']['official'])
print(datas[0]['status'])
print(datas[0]['independent'])


