# Find the longest word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
print("Length:", len(longest))