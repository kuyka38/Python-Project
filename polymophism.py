class Animal:
    def sound(self):
        print("Animal is speaking")

class cat(Animal):
    def sound(self):
        print("Cat says: meow!!")

class Dog(Animal):
    def sound(self):
        print("Dog says: woof!!")


a = Animal()
a.sound()

b = cat()
b.sound()

c = Dog()
c.sound()

