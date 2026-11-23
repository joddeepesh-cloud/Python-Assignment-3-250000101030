# Question 07: Write a program to count the number of digits, alphabets and special characters in a string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "RollNo: 250000101030, Score = 95.5%!"
digits = 0
alphabets = 0
special = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print(f"String: '{text}'")
print(f"Alphabets         : {alphabets}")
print(f"Digits            : {digits}")
print(f"Special characters: {special}")
