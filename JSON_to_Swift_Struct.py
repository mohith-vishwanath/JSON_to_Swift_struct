import requests
import json
from pprint import pprint

# PYTHON SCRIPT TO CONVERT JSON FORMAT TO SWIFT STRUCT


url = "https://api.openweathermap.org/data/2.5/weather?lat=28.448560415519535&lon=77.51167803006174&appid=65566541869f384610f77957287978c2"
response = requests.get(url).json() # Comment this line if you are reading from a file

# response = json.load(open("response.json", "r")) # Comment this line if you are fetching from an API

main_class_name = "Weather"

main_string = ["struct " + main_class_name + " : Codable {"]
extra_classes = []

swift_types = {
    type(9.41): "Float",
    type("String"): "String",
    type(8): "Int",
    type([1]): "List",
    type({}): "Dict",
    type(True) : "bool"
}

base_value_types = ["Int","Float","String"]


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
        else:
            for item in value:
                if type(item) == dict:
                    class_string.append("let " + key + " : [" + key + "Class]")
                    new_class_string = ["struct " + key + "Class : Codable {"]
                    extra_classes.append(create_struct(item,new_class_string))
                else:
                    class_string.append("let " + key + " : [" + swift_types[type(item)] + "]")
                    break

        if index == (len(keys)-1):
            class_string.append("}")

    return class_string

print("\n")
print("\n".join(create_struct(response)))
print("\n")
for ec in extra_classes:
    print("\n".join(ec))
    print("\n")
