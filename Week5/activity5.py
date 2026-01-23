#define super class
class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def behavevior(self, action):
        print(f"{self.name} can {action}")


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        super().__init__(feature)

    def behavevior(self, action):
        print(f"{self.name} can {action}")
    

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def behavevior(self, action):
        print(f"{self.name} can {action}")
    

class Dog(Mammal):
    def __init__(self, name, feature):
        super().__init__(name)
        super().__init__(feature)

    #Override walk method
    def behave(self):
        super().behavevior("walk")

class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)

    #Override walk method
    def behave(self):
        super().behavevior("walk")

def main():
    dog = Dog("Rover","Fur")
    dog.behave()

    cat = Cat("Garfield","Fur")
    cat.behave()

if __name__ == "__main__":
    main()

