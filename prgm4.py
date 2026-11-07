#Find the second smallest and second largest elements

n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

if len(unique) < 2:
    print("Need at least 2 distinct elements")
else:
    unique.sort()

    print("\nSecond smallest:", unique[1])
    print("\nSecond largest:", unique[-2])