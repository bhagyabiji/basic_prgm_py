a = 33
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")


#checking even or odd numbers
num = 7
if num%2 == 0:
    print(num,"is an even nmber")
else:
    print("is an odd nmbr")

#Short Hand If
a =5
b = 2
if a>b : print("Message")

print("A") if a > b else print("B")

big = a if a>b else b
print("big", big)

a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")

#Finding the maximum of two number
a = 20
b = 15
max_value = a if a>b else b if a<b else print("err")
print(max_value, "is the max")