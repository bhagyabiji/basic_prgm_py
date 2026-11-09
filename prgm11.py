# Check whether one string is a rotation of another

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not a rotation")

elif len(str1) == 0:
    print("Rotation")

else:
    combined = str1 + str1

    if str2 in combined:
        print("Rotation")
    else:
        print("Not a rotation")