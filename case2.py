import abc


class Animal:
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, food, age, habitat):
        self.__name = name
        self.__food = food
        self.__age = age
        self.__habitat = habitat

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    @food.deleter
    def food(self):
        del self.__food

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, habitat):
        self.__habitat = habitat

    @habitat.deleter
    def habitat(self):
        del self.__habitat

    @abc.abstractmethod
    def eat(self, food):
        return


class Dog(Animal):

    def __init__(self, name, food, age, habitat, breed, toy):
        super().__init__(name, food, age, habitat)
        self.__breed = breed
        self.__toy = toy

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @breed.deleter
    def breed(self):
        del self.__breed

    @property
    def toy(self):
        return self.__toy

    @toy.setter
    def toy(self, toy):
        self.__breed = toy

    @toy.deleter
    def toy(self):
        del self.__toy

    def eat(self, food):
        if food == self.food:
            print("*BARK* *BARK* *barks from excitement* *proceeds to eat the food ravishingly!* *BARK* *barks for "
                  "more*")
        else:
            print("*BARK* *proceeds to eat the food* *leaves*")

    def play(self):
        print("*you through " + self.toy + " WOOF!WOOF! *fetches toy and comesback* *Wags tail *")

    def pet(self):
        print("*Wags tail* *gives nose bump and lick*")


class Cat(Animal):

    def __init__(self, name, food, age, habitat, breed):
        super().__init__(name, food, age, habitat)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @breed.deleter
    def breed(self):
        del self.__breed

    def eat(self, food):
        if food == self.food:
            print("*Miau* *proceeds to eat the food slowly!* *Miau* *Miaus for "
                  "more*")
        else:
            print("*Stares at you* *leaves*")

    def play(self):
        print("*Stares at you and leaves *")

    def pet(self):
        print("Purr...Purr...*Leaves*")

    def hide(self):
        print("*proceeds to walk slowly to the box on the corner and hiding in it*")


puppy = Dog("Max", "beef", "1", "home", "German Shepherd", "flying disc")
feline = Cat("Felicia", "tuna", "3", "home", "Bengal")

puppy.pet()
puppy.play()
puppy.toy = "tennis ball"
puppy.play()
puppy.eat("dog food")
feline.pet()
feline.play()
feline.hide()
feline.eat("cat food")