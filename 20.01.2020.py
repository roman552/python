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

#Практическая работа наследование
import random

class Units():
	def __init__(self,team,id):
		self.team=team
		self.id=id

class Hero(Units):
	def __init__(self,id,team,name,lvl=1):
		Units.__init__(self,team,id)
		self.name=name
		self.lvl=lvl
	
	def get_lvl(self):
		return self.lvl
	
	def IncLvl(self):
		self.lvl+=1
		print('Уровень героя',self.name,'стал больше на 1 и равен',self.lvl)


class Soldier(Units):
	def follow_the_hero(self,Hero):
		print('Солдат номер',self.id,'следует за героем',Hero.name,'под номером',Hero.id)
hero_1=Hero(1,1,'Oleg')
hero_2=Hero(2,2,'Igor')
army_hero_1=[]
army_hero_2=[]

for i in range(3,10):
	n=random.randint(0,1)
	if n:
		army_hero_1.append(Soldier(i,1))
		print('Солдат с номером', i, 'добавлен в армию',hero_1.name)
	else:
		army_hero_2.append(Soldier(i,2))
		print('Солдат с номером', i, 'добавлен в армию', hero_2.name)

print('Армия героя', hero_1.name, ':', len(army_hero_1))
print('Армия героя', hero_2.name, ':', len(army_hero_2))

if len(army_hero_1) > len(army_hero_2):

    print('В армии', hero_1.name, 'больше солдат, увеличиваем его уровень')

    hero_1.IncLvl()

else:

    print('В армии', hero_2.name, 'больше солдат, увеличиваем его уровень')

    hero_2.IncLvl()

army_hero_1[1].follow_the_hero(hero_2)
