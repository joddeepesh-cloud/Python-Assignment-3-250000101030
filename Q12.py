# Question 12: Write a program to find the first and last occurrence of a character using string methods.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "engineering education in uttarakhand"
target = "e"

first_idx = text.find(target)
last_idx = text.rfind(target)

print(f"Text: '{text}'")
print(f"Target character: '{target}'")
print(f"First occurrence index: {first_idx}")
print(f"Last occurrence index : {last_idx}")
