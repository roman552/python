class Students():
   
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
   
    def out(self):
        print('Name:',self.name,'\nAge:', self.age,'\nGender:',self.gender,'\n------------')
   
a=Students('Steve',21,'man')
b=Students('Alex',20,'woman')

a.out()
b.out()