from datetime import date
today = str(date.today())
print("*" * 50)
print("This scrip is used to generate Codable Swift classes")
print("Range of parameters is 100, you've to specify the name and type of each parameter")
print("[Int, Double, Bool, String]")
print("You can enter '#' to skip the parameter and generate the file")
print("*" * 50)
file_name = input("Enter file name / Class name: ")
my_dict = {}
my_types = []

for i in range(100):
    name = input(f"#{i + 1} Parameter Name: ")
    if name == "#":
        break
    value_type = input(f"#{i + 1} Parameter Type [Int, Double, Bool, String]: ")
    print("You can enter '#' to skip the parameter and generate the file")
    if value_type == "#":
        break
    value_type = value_type.lower()
    if value_type == "int":
        my_dict[name] = ""
        my_types.append("Int")
    elif value_type == "double":
        my_dict[name] = ""
        my_types.append("Double")
    elif value_type == "bool":
        my_dict[name] = ""
        my_types.append("Bool")
    elif value_type == "string":
        my_dict[name] = ""
        my_types.append("String")
    else:
        print("Something went wrong, you choose a wrong type!!")
        exit(0)

if len(my_dict) == 0:
    print("No data available, File will not get generated.")
    exit(0)

f = open(f"{file_name}.swift", "x")
f.write(f"// \n// {file_name}.swift \n// Created on {today} \n//\n\n")
f.write("import Foundation \n\n")
f.write(f"class {file_name}: Codable ")
f.write("{ \n")
for paramter in my_dict:
    index = list(my_dict.keys()).index(paramter)
    f.write(f"\tlet {paramter}: {my_types[index]}?\n")
f.write("\n")
f.write("\tinit(")
my_index = 0
for paramter in my_dict:
    my_index += 1
    index = list(my_dict.keys()).index(paramter)
    f.write(f"{paramter}: {my_types[index]}? ")
    if my_index != len(my_dict):
        f.write(",")

f.write(") {\n")

for paramter in my_dict:
    index = list(my_dict.keys()).index(paramter)
    f.write(f"\t\tself.{paramter} = {paramter} \n")
f.write("\t} \n}")