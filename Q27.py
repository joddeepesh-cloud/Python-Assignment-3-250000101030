# Question 27: Write a program to access the first, last and middle elements of a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
items = [15, 25, 35, 45, 55, 65, 75]

first_elem = items[0]
last_elem = items[-1]
mid_idx = len(items) // 2
mid_elem = items[mid_idx]

print("List:", items)
print("First Element :", first_elem)
print("Middle Element:", mid_elem, f"(at index {mid_idx})")
print("Last Element  :", last_elem)
