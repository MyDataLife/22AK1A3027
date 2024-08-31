def is_fibonacci_number(n):
    if n < 0:
        return False, -1
    
    a, b = 0, 1
    position = 1  

    while a <= n:
        if a == n:
            return True, position
        a, b = b, a + b
        position += 1

    return False, -1

number = int(input("Enter an integer: "))

is_fib, pos = is_fibonacci_number(number)
if is_fib:
    print(f"{number} is a Fibonacci number at position {pos}.")
else:
    print(f"{number} is not a Fibonacci number.")