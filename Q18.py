# Question 18: Write a program to find the longest word in a given sentence using string operations.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
sentence = "Python provides exceptional readability and modular development"
words = sentence.split()

longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w

print(f"Sentence    : '{sentence}'")
print(f"Longest word: '{longest_word}' (Length: {len(longest_word)})")
