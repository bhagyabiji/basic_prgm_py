# Find the first non-repeating character

text = input("Enter a string: ")

found = False

for i in range(len(text)):
    count = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1

    if count == 1:
        print("First non-repeating character:", text[i])
        found = True
        break

if found == False:
    print("No non-repeating character")