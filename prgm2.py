numbers = [10, 25, 8, 45, 30]

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)