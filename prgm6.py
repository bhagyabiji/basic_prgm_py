# Find the frequency of each character in a string

text = input("Enter a string: ")

visited = ""

for i in text:
    if i not in visited:
        count = 0

        for j in text:
            if i == j:
                count += 1

        print(i, ":", count)

        visited += i