# Question 14: Write a program to remove leading and trailing spaces from a string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
raw_text = "   Welcome to Python   "
stripped = raw_text.strip()
l_stripped = raw_text.lstrip()
r_stripped = raw_text.rstrip()

print(f"Original    : '{raw_text}' (len: {len(raw_text)})")
print(f"strip()     : '{stripped}' (len: {len(stripped)})")
print(f"lstrip()    : '{l_stripped}' (len: {len(l_stripped)})")
print(f"rstrip()    : '{r_stripped}' (len: {len(r_stripped)})")
