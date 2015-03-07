'''
teacher
student
classroom
person (teacher(mr.blue), student(Carthic, Kin-Tien, Aunorag, Sean, Douglas))
'''
class person():
    pass

class teacher(person):
    def __init__(self,name,subject):
        self.name =name
        self.subject = subject
        print('Just created a teacher ' + self.name + ' and they teach ' +self.subject)
class student(person):
    def __init__(self,name,grade):
        self.name = name
        self.grade  = grade
        print('Just created a student named ' +self.name +' who is in the ' +self.grade)
    def enroll(self,session):
        print(self.name + " has enrolled in " + session )
class classroom():
    def __init__(self,capacity,use,working_space):
        self.capacity = capacity
        self.use = use
        self.working_space = working_space
        print('Just created a classroom with a capacity of ' + self.capacity +' which is used for ' +self.use+ ' the childrens work area is a ' + self.working_space)
class subject ():
    def __init__(self,name,numberStudents,):
        self.name = name
        self.numberStudents = numberStudents
        print('Just created a class called '+ self.name +' there are '+self.numberStudents +' students enrolled')
kintien = student('kintien','7th grade')
sean = student('sean', '10th grade')
douglas = student('douglas', '7th grade')
aungneraguh = student('augneraguh', '7th grade')
karthic = student('karthic', '7th grade')
malik = teacher('malik','computer programing')
critosphere= classroom('24 people', 'teaching various things', 'table')
py103 = subject('py103', '5')
kintien.enroll(py103.name)
sean.enroll(py103.name)
douglas.enroll(py103.name)
karthic.enroll(py103.name)
aungneraguh.enroll(py103.name)