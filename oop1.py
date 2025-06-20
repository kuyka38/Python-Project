class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def sound(self):
        print(self.name, "is barking")
        print(self.breed)
        print(self.age)
        print(self.color)

dog1 = Dog("Victory","German shephard", 5,"white")
print(dog1.name)
print(dog1.breed)
print(dog1.age)
print(dog1.color)

print()

dog2 = Dog( "Braxton", "Chihuahua", 7,"blue")
print(dog2.name)
print(dog2.breed)
print(dog2.age)
print(dog2.color)

print()

dog3 = Dog( "Tony", "Mutina", 2,"pink")
print(dog3.name)
print(dog3.breed)
print(dog3.age)
print(dog3.color)

print()

dog4 = Dog( "Tamar", "Siberian Husky", 3,"yellow")
print(dog4.name)
print(dog4.breed)
print(dog4.age)
print(dog4.color)


