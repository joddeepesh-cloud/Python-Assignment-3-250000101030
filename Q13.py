# Question 13: Write a program to check whether a given string starts and ends with a particular character.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "!Hello World!"
start_char = "!"
end_char = "!"

starts = text.startswith(start_char)
ends = text.endswith(end_char)

print(f"String: '{text}'")
print(f"Starts with '{start_char}'? {starts}")
print(f"Ends with '{end_char}'?   {ends}")
