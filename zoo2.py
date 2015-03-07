class mammal():
    def FeedMIlkToYoung(self):
        pass
    def drink (self, substance):
        print(self.name + " is drinking" + substance)
class Ape(mammal):
    def eat_bannana(self):
        print(self.name + " is eating a bannana")

class monkey(Ape):
    def __init__(self,name,age,weight,tail):
    self.name =name
    self.age = age
    self.weight = weight
    self.tail = tail
    print('Just created a monkey called ' +name+ ".")
    print(name + "'s tail is" + str(tail) + "ft long.")
    def hang_by_tail(self):
        print(self.name + " is hanging by its tail")

class Gorrilla(Ape):
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        print('Just created a gorrila called ' +name+ ".")

class tiger (mammal):
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight =