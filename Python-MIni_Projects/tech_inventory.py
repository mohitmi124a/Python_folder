# This segment stores device general information

name = input("Enter your Device's Name: ")
model = input("Enter your Device's Model: ")
year = input("Enter your Device's Year: ")
owner = input("Enter your Device's Owner: ")

device = {
    "Name": name,
    "Model": model,
    "Year": year,
    "Owner": owner,
}

# This segment stores installed tools in the device

tool_1 = input("Enter the name of Tool 1: ")
tool_2 = input("Enter the name of Tool 2: ")
tool_3 = input("Enter the name of Tool 3: ")
tool_4 = input("Enter the name of Tool 4: ")

installed_tools = {tool_1, tool_2, tool_3, tool_4}

required_tools = {"Python", "GitHub", "Linux", "VS Code"}

print("\n\n===== DEVICE INFO =====")

print("Device Name :", device["Name"])
print("Device Model:", device["Model"])
print("Device Year :", device["Year"])
print("Device Owner:", device["Owner"])

print("\nInstalled Tools:")
print(installed_tools)

print("\nCommon Tools:")
print(installed_tools.intersection(required_tools))

print("\nMissing Tools:")
print(required_tools.difference(installed_tools))

print("\nAll Tools:")
print(installed_tools.union(required_tools))





















































































