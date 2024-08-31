def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    while True:
        n += 1
        if is_palindrome(n):
            return n

def check_number(n):
    if is_prime(n):
        print(next_palindrome(n))
    else:
        print("not prime")

# Example usage
number = 31
check_number(number)