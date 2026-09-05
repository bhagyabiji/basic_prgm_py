#Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#looping through a string
for x in "banana":
    print(x)

#Exit the loop when x is "banana"
for x in fruits:
    if x == "cherry":
        break
    print(x)

print("\n------------------")

#Do not print banana
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("\n------------------")

for x in range(4):
    print(x)

print("\n------------------")

for x in range(2,6):
    print(x)

print("\n------------------")

#Increment the sequence with 3 (default is 1)
for x in range(2, 30 , 3):
    print(x)

print("\n------------------")
for x in range(6):
    print(x)
else:
    print("nthg")

print("\n------------------")

#Break the loop when x is 3, and see what happens with the else block
for x in range(10):
    if x == 3:
        break
    print(x)
else:
    print("finished")

print("\n------------------")

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)