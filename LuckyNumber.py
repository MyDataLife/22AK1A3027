def calculate_lucky_number(dob):
    digits = [int(char) for char in dob if char.isdigit()]
    lucky_number = sum(digits)
    
    while lucky_number > 9:
        lucky_number = sum(int(digit) for digit in str(lucky_number))
    
    return lucky_number

dob = input("Enter your date of birth (dd-mm-yy): ")
lucky_number = calculate_lucky_number(dob)
print(f"Your lucky number is: {lucky_number}")
