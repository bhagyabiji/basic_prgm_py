# Check whether two strings are anagrams
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if len(str1) != len(str2):
    print("Not Anagrams")

else:
    for i in str1:
        if str1.count(i) != str2.count(i):
            print("Not Anagrams")
            break
    else:
        print("Anagrams")