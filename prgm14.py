# Remove duplicate characters from a string

text = input("Enter a string: ")

result = ""

for i in text:
    if i not in result:
        result = result + i

print("After removing duplicates:", result)