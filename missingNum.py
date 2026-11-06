# Find the missing number in an array

numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2

actual = 0

for i in numbers:
    actual = actual + i

missing = total - actual

print("Missing number:", missing)