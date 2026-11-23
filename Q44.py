# Question 44: Write a program to copy one list into another and demonstrate the difference between copy() and direct assignment.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
original = [10, 20, 30]

# Direct assignment (creates a reference/alias)
alias_list = original

# Shallow copy using copy()
copied_list = original.copy()

# Modify original
original.append(40)

print(f"Original after append(40): {original}")
print(f"Alias list (affected)   : {alias_list}")
print(f"Copied list (unaffected): {copied_list}")
