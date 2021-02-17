import methods
from datetime import date
def generate_script(file_name, my_dict, my_types):
    today = str(date.today())
    print(file_name)
    print(my_dict)
    print(my_types)
    f = open(f"{file_name}.swift", "x")
    f.write(f"// \n// {file_name}.swift \n// Created on {today} \n//\n\n")
    f.write("import Foundation \n\n")
    f.write(f"class {file_name}: Codable ")
    f.write("{ \n")
    for parameter in my_dict:
        index = list(my_dict.keys()).index(parameter)
        f.write(f"\tlet {parameter}: {my_types[index]}?\n")
    f.write("\n")
    f.write("\tinit(")
    my_index = 0
    for parameter in my_dict:
        my_index += 1
        index = list(my_dict.keys()).index(parameter)
        f.write(f"{parameter}: {my_types[index]}?")
        if my_index != len(my_dict):
            f.write(", ")
    f.write(") {\n")
    for parameter in my_dict:
        f.write(f"\t\tself.{parameter} = {parameter} \n")
    f.write("\t} \n}\n\n")
    f.write(f"// MARK: {file_name} convenience initializers and mutators\n\n")
    f.write(f"extension {file_name}")
    f.write(" {\n")
    f.write("\tconvenience init(data: Data) throws {\n")
    f.write(f"\t\tlet object = try newJSONDecoder().decode({file_name}.self, from: data)\n")
    f.write("\t\tself.init(")
    my_index = 0
    for parameter in my_dict:
        my_index += 1
        f.write(f"{parameter}: object.{parameter}")
        if my_index != len(my_dict):
            f.write(", ")
    f.write(")\n")
    f.write("\t}\n")
    f.write(methods.convenience_init)
    f.write("\n")
    f.write(f"\tfunc with(\n")
    my_index = 0
    for parameter in my_dict:
        my_index += 1
        index = list(my_dict.keys()).index(parameter)
        f.write(f"\t\t{parameter}: {my_types[index]}?? = nil")
        if my_index != len(my_dict):
            f.write(",")
        f.write("\n")
    f.write(f"\t) -> {file_name} ")
    f.write("{\n")
    f.write(f"\t\t return {file_name}(")
    my_index = 0
    for parameter in my_dict:
        my_index += 1
        if my_index != 1:
            f.write("\t\t\t\t\t\t\t\t  ")
        f.write(f"{parameter}: {parameter} ?? = self.{parameter}")
        if my_index != len(my_dict):
            f.write(",")
        else:
            f.write(")")
        f.write("\n")
    f.write("\n \t }\n")
    f.write(methods.json_data)
    f.write("\n}")
    should_add_encoders = input("Do you require encoders functions? (Y/N): ")
    should_add_encoders = should_add_encoders.lower()
    if should_add_encoders == "y" or should_add_encoders == "yes":
        f.write("\n")
        f.write(methods.json_encoders)
