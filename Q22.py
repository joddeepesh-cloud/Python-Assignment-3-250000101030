# Question 22: Write a program to demonstrate the difference between raw strings and normal strings.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Normal string interprets escape sequences
normal_str = "C:\new_folder\test\assignment.py"

# Raw string treats backslashes as literal characters
raw_str = r"C:\new_folder\test\assignment.py"

print("Normal string (escapes interpreted):")
print(normal_str)
print("\nRaw string (literal r'...'):")
print(raw_str)
