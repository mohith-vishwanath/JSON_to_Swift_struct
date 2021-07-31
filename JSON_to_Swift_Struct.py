import requests
import json
from pprint import pprint

# PYTHON SCRIPT TO CONVERT JSON FORMAT TO SWIFT STRUCT


url = "https://gorest.co.in/public/v1/users"
response = requests.get(url).json() # Comment this line if you are reading from a file

# pprint(response)

# response = json.load(open("/Users/mohith/Downloads/response.json", "r")) # Comment this line if you are fetching from an API

main_class_name = "Weather"

main_string = ["struct " + main_class_name + " : Codable {"]
extra_classes = []

swift_types = {
    type(9.41): "Float",
    type("String"): "String",
    type(8): "Int",
    type([1]): "List",
    type({}): "Dict",
    type(True) : "bool",
    type(None) : "None"
}

base_value_types = ["Int","Float","String"]
previous_struct_names = []


def create_struct(json_file,class_string=main_string):
    keys = list(json_file.keys())
    values = list(json_file.values())
    for index, (key, value) in enumerate(zip(keys, values)):
        value_type = swift_types[type(value)]
        if value_type in base_value_types:
            class_string.append("let " + key + " : " + value_type)
        elif value_type == "Dict":
            new_class_string = ["struct " + key + "Class : Codable {"]
            extra_classes.append(create_struct(value,new_class_string))
            class_string.append("let " + key + " : " + key + "Class")
        elif value_type == "List":
            for item in value:
                if type(item) == dict:
                    if key+"Class" not in previous_struct_names:
                        class_string.append("let " + key + " : [" + key + "Class]")
                        new_class_string = ["struct " + key + "Class : Codable {"]
                        extra_classes.append(create_struct(item,new_class_string))
                        previous_struct_names.append(key+"Class")
                else:
                    class_string.append("let " + key + " : [" + swift_types[type(item)] + "]")
                    break

        if index == (len(keys)-1):
            class_string.append("}")

    return class_string

# pprint(response)

print("\n")
print("\n".join(create_struct(response)))
print("\n")
for ec in extra_classes:
    print("\n".join(ec))
    print("\n")
