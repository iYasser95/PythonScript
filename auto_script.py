import helper
import script_generator
# Variables
value = []
name = []
parameters = []
line = ""

# Introduction for the user.
print("*" * 50)
print("Please enter your json formatted response to generate the file: ")
print("*" * 50)
file_name = input("Enter file name / Class name: ")
print("Paste your JSON response here: ")

# Get the JSON Response and break at the end '}'
while True:
    user_input = input()
    line += user_input
    if user_input == "}":
        break
# Format the string into an array
line = line.replace("\n", "")
line = line.replace("\t", "")
line = line.replace(" ", "")
line = line.replace("}", "")
line = line.replace("{", "")
parameters_array = line.split(",")
my_types = []
my_dict = {}

for s in parameters_array:
    parameters += s.split(":")

# Get the value and name of the parameters
for i in range(len(parameters)):
    if i % 2 == 0:
        name.append(parameters[i])
    else:
        value.append(parameters[i])

for parameter_name in name:
    formatted_name = parameter_name.replace('"', '')
    my_dict[formatted_name] = ""

for parameter_value in value:
    if '"' in parameter_value:
        my_types.append("String")
    elif helper.is_int(parameter_value):
        my_types.append("Int")
    elif helper.is_float(parameter_value):
        my_types.append("Double")
    elif helper.is_bool(parameter_value):
        my_types.append("Bool")

script_generator.generate_script(file_name, my_dict, my_types)