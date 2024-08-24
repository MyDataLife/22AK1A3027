with open('sample.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f"This is line {i}\n")

n = 50

with open('sample.txt', 'r') as file:
    content = file.read(n)

reversed_content = content[::-1]

print(reversed_content)