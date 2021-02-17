# Variables
value = []
name = []
parameters = []
line = ""

# Introduction for the user.
print("*" * 50)
print("Please enter your json formatted response to generate the file: ")
print("*" * 50)
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


for s in parameters_array:
    parameters += s.split(":")

# Get the value and name of the parameters
for i in range(len(parameters)):
    if i % 2 == 0:
        name.append(parameters[i])
    else:
        value.append(parameters[i])