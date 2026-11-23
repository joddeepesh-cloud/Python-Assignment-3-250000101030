# Question 38: Write a program to remove duplicate elements from a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
original_list = [10, 20, 20, 30, 40, 40, 50, 10, 60]

# Preserving order while removing duplicates
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original List with duplicates:", original_list)
print("List after removing duplicates:", unique_list)
