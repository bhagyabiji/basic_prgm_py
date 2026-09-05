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


#Setting a default value
username = ""
dp_name = username if username else "Guest"
print("WELCOME", dp_name)

# AND operator
a = 200
b = 130
c = 190
if a>b and c>b:
    print("True - AND")

#Test if a is greater than b, OR if a is greater than c
a = 300
b = 200
c = 250
if a>b or a>c:
    print("True - OR")

#Test if a is NOT greater than b
a = 2
b = 10
if not a > b:
    print("True - NOT")

#User authentication check
user_name = "Hello"
pswd = "se123"
is_verified = True
if user_name and pswd and is_verified:
    print("Login Successfull")
else:
    print("login failed")

#Range checking with logical operators
score = 35
if score >= 0 and score <= 50:
    print("valid")
else:
    print("invalid")

#Checking multiple conditions with nesting
age = 20
is_licensed = True
if age>=18:
    if is_licensed:
        print("You can drive")
    else:
        print("not allowed to drive")
else:
    print("u r underaged")

#Login validation with nested checks
userName = "MM"
pswrd = "mm10"
is_emp = True
if userName and pswrd:
    if is_emp:
        print("yup LOGIN")
    else:
        print("NOT")
else:
    print("check credentials")


#pass statement
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


#match statement
day = 3
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
            print("wed")
    case 4:
            print("Thur")
    case 5:
            print("Fri")
    case 6:
            print("Sat")
    case 7:
            print("Sun")
    case _:
        print("Default")


#while loop
i = 1
while i < 6:
    print(i)
    i += 1

print("\n------------------")
#break 
i = 2
while i< 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\n------------------")
#continue
i = 0
while i<6:
    i+=1
    if i ==3:
        continue
    print(i)