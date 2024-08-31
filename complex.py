def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def conjugate_complex(c):
    return c.conjugate()

def parse_complex_input(prompt):
    while True:
        try:
            # Get input and strip any extra whitespace
            user_input = input(prompt).strip()
            # Convert input to complex number
            c = complex(user_input)
            return c
        except ValueError:
            print("Invalid input. Please enter a complex number in the format a+bj or a-bj.")

# Example usage
def main():
    print("Enter complex numbers in the format a+bj or a-bj where a and b are real numbers.")
    
    # Input complex numbers with validation
    c1 = parse_complex_input("Enter the first complex number: ")
    c2 = parse_complex_input("Enter the second complex number: ")

    # Perform operations
    addition_result = add_complex(c1, c2)
    subtraction_result = subtract_complex(c1, c2)
    multiplication_result = multiply_complex(c1, c2)
    conjugate_c1 = conjugate_complex(c1)
    conjugate_c2 = conjugate_complex(c2)

    # Print results
    print(f"Addition: {c1} + {c2} = {addition_result}")
    print(f"Subtraction: {c1} - {c2} = {subtraction_result}")
    print(f"Multiplication: {c1} * {c2} = {multiplication_result}")
    print(f"Conjugate of {c1} = {conjugate_c1}")
    print(f"Conjugate of {c2} = {conjugate_c2}")

if __name__ == "__main__":
    main()
