def reverse_words_in_string(s):
    
    words = s.split()
    
    reversed_words = [word[::-1] for word in words]
    
    
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string


input_string = "Hello World"
reversed_string = reverse_words_in_string(input_string)
print(reversed_string)  