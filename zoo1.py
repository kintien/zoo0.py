__author__ = 'kintien'

class mammal():
    pass
class ape (mammal):
    pass

class monkey (ape):
    def __init__(self):
        print('Just created a monkey')
class gorrila (ape):
    def __init__(self):
        print('Just created a monkey')
class tiger(mammal):
    def __init__(self,name,age,weight,stripes):
        self.name = name
        self.age = age
        self.weight = weight
        self.stripes = stripes
        print('Just created a tiger called ' + name + ".")
        print(name + " weighs " + str(weight) + " lbs and has " + str(stripes) + 'stripes.')
    def longe(self):
        print(self.name + " is lounging under a tree")




kintien = tiger('kintien', 20, 300, 50)
print('kintien' (longe))