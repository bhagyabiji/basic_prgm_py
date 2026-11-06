# Remove duplicate elements from a list

numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print(result)