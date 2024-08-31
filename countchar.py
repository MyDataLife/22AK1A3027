def count_characters(input_string):
    # Create a dictionary to store the count of each character
    char_count = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Update the count for each character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

# Input string
input_string = "Raja"

# Count characters in the input string
char_count = count_characters(input_string)

# Print the character counts
print("Character counts:")
for char, count in char_count.items():
    print(f"{char}: {count}")
