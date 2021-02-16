file_name = input("Enter file name / Class name: ")
number_of_parameters = input("Enter number of parameters: ")
my_dict = {}

for i in range(int(number_of_parameters)):
    name = input(f"#{i + 1} Parameter Name: ")
    value_type = input(f"#{i + 1} Parameter Type (int, double, bool, string): ")

    if value_type == "int":
        my_dict[name] = ""
    elif value_type == "double":
        my_dict[name] = ""
    elif value_type == "bool":
        my_dict[name] = ""
    elif value_type == "string":
        my_dict[name] = ""
    else:
        print("Something went wrong, you choose a wrong type!!")
        exit(0)

for i in my_dict:
    print(i)


f = open(f"{file_name}.swift", "x")
f.write("import Foundation \n\n")
f.write(f"class {file_name}: Codable ")
f.write("{ \n")
for paramter in my_dict:
    f.write(f"let {paramter}: Int?\n")