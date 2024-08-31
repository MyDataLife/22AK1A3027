def find_pair_with_sum_nearest_to_zero(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find a pair

    arr.sort()  # Sort the array
    left = 0
    right = len(arr) - 1
    min_sum = float('inf')
    best_pair = (None, None)

    while left < right:
        current_sum = arr[left] + arr[right]
        
        # Update the minimum sum and best pair if the current sum is closer to zero
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            best_pair = (arr[left], arr[right])

        # Move pointers based on the sum
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break  # Perfectly zero sum found

    return best_pair

# Read array from user input
input_string = input("Enter the elements of the array separated by spaces: ")
# Remove any commas or non-numeric characters
cleaned_input = ''.join(char if char.isdigit() or char.isspace() else '' for char in input_string)
# Convert cleaned input to a list of integers
arr = list(map(int, cleaned_input.split()))

# Find and print the pair with sum nearest to zero
pair = find_pair_with_sum_nearest_to_zero(arr)

if pair:
    print(f"The pair with sum nearest to zero is: {pair}")
else:
    print("No valid pair found.")
