# move all zeros to the end of an array

n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

result = []

zero_count = 0

for i in numbers:
    if i == 0:
        zero_count += 1
    else:
        result.append(i)

for i in range(zero_count):
    result.append(0)

print("\nResult:", result)