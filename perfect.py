def classify_number(n):
    sum_of_factors = sum([i for i in range(1, n) if n % i == 0])
    
    if sum_of_factors > n:
        return "Abundant Number"
    elif sum_of_factors < n:
        return "Deficient Number"
    else:
        return "Perfect Number"


number = 6
result = classify_number(number)
print(f"{number} is a {result}")