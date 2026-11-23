# Question 28: Write a program to find the largest and smallest elements in a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
data = [45, 12, 89, 7, 63, 98, 24]

largest = data[0]
smallest = data[0]

for x in data:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print("List:", data)
print("Largest Element :", largest)
print("Smallest Element:", smallest)
