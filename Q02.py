# Question 02: Write a program to count the number of vowels in a given string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
text = "Computer Science and Engineering"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"String: '{text}'")
print(f"Total number of vowels: {count}")
