# Question 37: Write a program to find the second-largest element in a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
numbers = [24, 76, 12, 98, 55, 98, 83]
print("List:", numbers)

# Remove duplicates to find unique elements
unique_nums = list(set(numbers))
unique_nums.sort()

if len(unique_nums) >= 2:
    second_largest = unique_nums[-2]
    print("Second-largest element is:", second_largest)
else:
    print("Not enough unique elements to find second largest.")
