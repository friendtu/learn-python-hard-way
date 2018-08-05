class Animal(object):
    def sound(self):
        print "sound"

class Dog(Animal):
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        print "WangWang"
    
class Cat(Animal):
    def __init__(self,name):
        self.name=name

    def sound(self):
        print "%s MiaoMiao" % self.name

class Person(object):
    def __init__(self,name):
        self.name=name
        self.pet=None

class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        self.salary=salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover=Dog("Rover")

satan=Cat("Satan")
satan.sound()

mary=Person("Mary")
mary.pet=satan

frank=Employee("Frank",12000)
frank.pet=rover
print frank.name

flipper=Fish()

crouse=Salmon()

harry=Halibut()