#Первое задание
#1
class Dog():
    age=0
    name=''
    weight=0

#2
class Person():
    name=''
    cellPhone=''
    email=''

#3
class Bird():
    color=''
    name=''
    breed=''
myBird=Bird()
myBird.color='green'
myBird.name='Sunny'
myBird.breed='Sun Conure'

#4
class Hero():
    name=''
    power=0
    x=0
    y=0
myhero=Hero()
myhero.x=1
myhero.y=2
myhero.cords=myhero.x,myhero.y
myhero.name='Igor'
myhero.power=10
#5    
class Person2():
    name=''
    money=0
nancy=Person2()
nancy.name='Nancy'
nancy.money=100

#6
class Person3():
    name=''
    money=0
bob=Person3()
bob.name='Bob'
print(bob.name,'has',bob.money,'dollars.')

#Второе задание
#1
class Cat():
    name=''
    color=''
    weight=0
    def meow(self):
        print('Meow')
shrek=Cat()
shrek.name='shrek'
shrek.color='red'
shrek.weight=47
shrek.meow()       

#2

#.....
        
#3
class Monster():
    name=''
    health=0
    def decreaseHealth(self,amount):
        while True:
            self.health-=amount
            if self.health<=0:
                print('Монстр умер!')
                break
            else:
                print('У монстра',self.health,'здоровья.')
                
monster=Monster()
monster.name='Oleg'
monster.health=100
monster.decreaseHealth(10)

#Практическая работа (класс "Воин")
import random
class warrior():
    health=100

    def fight(self,first,second):
        self.first=first
        self.second=second
       
        while first.health>0 and second.health>0:
            fighter=random.randint(1,2)
           
            if fighter==1:
                second.health-=20
                print('Олег наносит урон Игорю')
                print('Олег','=',first.health,'HP')
                print('Игорь','=',second.health,'HP')
                if second.health==0:
                    print('Олег выйграл!')
           
            elif fighter==2:
                first.health-=20
                print('Игорь наносит урон Олегу')
                print('Олег','=',first.health,'HP')
                print('Игорь','=',second.health,'HP')
                if first.health==0:
                    print('Игорь выйграл!')
                
oleg=warrior()
igor=warrior()

start=warrior()
start.fight(oleg,igor)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        