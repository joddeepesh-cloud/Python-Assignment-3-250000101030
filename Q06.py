# Question 06: Write a program to count uppercase and lowercase characters in a string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "Deepesh Joshi - B.Tech CSE (2026)"
upper_count = 0
lower_count = 0

for ch in text:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print(f"Text: '{text}'")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
