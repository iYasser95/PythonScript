import script_generator
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

script_generator.generate_script(file_name, my_dict, my_types)