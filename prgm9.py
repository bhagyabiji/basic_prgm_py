# Rotate an array to the right by K positions

# Enter array size: 5
# Enter elements: 1 2 3 4 5
# Enter K: 2


n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

k = int(input("Enter K: "))

k = k % n

result = []

for i in range(n - k, n):
    result.append(numbers[i])

for i in range(0, n - k):
    result.append(numbers[i])

print("Rotated array:", result)