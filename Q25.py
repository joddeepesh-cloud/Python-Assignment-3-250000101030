# Question 25: Write a program to check whether two strings are equal, ignoring their case.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
str1 = "Uttarakhand"
str2 = "UTTARAKHAND"

are_equal = (str1.lower() == str2.lower())

print(f"String 1: '{str1}'")
print(f"String 2: '{str2}'")
print("Are they equal ignoring case?", are_equal)
