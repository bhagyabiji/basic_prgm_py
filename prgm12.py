# Find common elements in two arrays

n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second array: "))
arr2 = []

for i in range(n2):
    arr2.append(int(input("Enter element: ")))

common = []

for i in arr1:
    if i in arr2 and i not in common:
        common.append(i)

print("Common elements:", common)