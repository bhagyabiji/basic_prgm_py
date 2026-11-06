# Count vowels and consonants in a string

text = input("Enter a string: ")

vowels = 0
consonants = 0

for i in text.lower():
    if i >= 'a' and i <= 'z':
        if i in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)