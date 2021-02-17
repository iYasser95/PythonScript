import methods
import script_generator
print("*" * 50)
print("This scrip is used to generate Codable Swift classes")
print("Range of parameters is 100, you've to specify the name and type of each parameter")
print("[Int, Double, Bool, String]")
print("You can enter '#' to skip the parameter and generate the file")
print("*" * 50)
user_choice = input("Do you wish to use manual or auto generate? (M/A): ")
user_choice = user_choice.lower()
if user_choice == "a":
    exec(open('auto_script.py').read())
else:
    exec(open("manual_script.py").read())


