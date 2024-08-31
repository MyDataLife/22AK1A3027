def find_even_length_substrings(s):
    length = len(s)
    even_length_substrings = []
    
    for start in range(length):
        for end in range(start + 2, length + 1, 2):  # Ensure even length substrings
            substring = s[start:end]
            even_length_substrings.append(substring)
    
    return even_length_substrings

# Read input string
input_string = input("Enter a string: ")

# Find and print even length substrings
even_length_substrings = find_even_length_substrings(input_string)

print("Substrings of even length:")
for substring in even_length_substrings:
    print(substring)
