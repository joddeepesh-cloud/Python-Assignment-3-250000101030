# Question 04: Write a program to reverse a string without using built-in reverse functions.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
original_str = "Faculty of Technology"
reversed_str = ""

for ch in original_str:
    reversed_str = ch + reversed_str

print(f"Original String: '{original_str}'")
print(f"Reversed String: '{reversed_str}'")
