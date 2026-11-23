# Question 40: Write a program to find common elements between two lists.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
list_a = [10, 20, 30, 40, 50]
list_b = [30, 40, 50, 60, 70]

common = []
for item in list_a:
    if item in list_b and item not in common:
        common.append(item)

print("List A:", list_a)
print("List B:", list_b)
print("Common Elements:", common)
