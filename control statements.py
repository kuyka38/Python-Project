# program 1

age = int(input("How old are you?"))

if age > 18 :
    print("You are a voter")

else:
    print("You are not a voter")


#program 2
temperature = float(input("Enter current room temperature e.g 25.0:"))
if temperature > 25.0 :
    print("it is too hot")

if temperature < 25.0:
    print("it is too cold")

elif temperature < 25.0 :
    print("it is too cold")

else:
    print("it is normal")

    input()

#program 3
first = int(input("Enter first number"))
second = int(input("Enter second number"))
third = int(input("Enter third number"))

if first>second and first>third:
    print(first, "is the largest number")

elif second>third and second>first:
    print(second, "is the largest number")

else:
    print(third, "is the largest number")
