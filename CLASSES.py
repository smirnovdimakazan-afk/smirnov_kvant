class Animal:
    def __init__(self, color,name):
        self.color = color
        self.name = name

    def make_sound(self):
        print("I'm an animal")

class Dog(Animal):
    def __init__(self, color, name, master):
        Animal.__init__(self,color,name)
        self.master = master
    def make_sound(self):
        print("gavvv")

class Cat(Animal):
    def __init__(self, color,name,lifes):
        Animal.__init__(self, color, name)
        self.lifes = lifes
    def make_sound(self):
        print("miaaaaay")
    
animal = Animal("seri", "ponium")
cat = Cat("seriy", "Kessi", 9)
dog = Dog("brown", "pyos", "web67")
animal.make_sound()
dog.make_sound()
cat.make_sound()