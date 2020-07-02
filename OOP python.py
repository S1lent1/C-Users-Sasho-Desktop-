from abc import ABC, abstractclassmethod
#нужно создать класс утка(с характерными методами) так, чтобы небыло ошибок если создастся утка, не использующая
# те или иные методы
#1ая идея в том, что метод полета и крякания вынесены в отдельные абстрактные классы, от которых наследуется класс утка
# (от которой наследуются виды и типы уток)
# вопрос: как объявить метод, но не реализовать
#

# class Flyable(metaclass= ABCMeta):
#
#     def flybywings(self):
#
#
#     def flybymech(self):
#
#
#     def anflyable(self):
#
# class Quackable():
#     def quack(self):
#         print("*КРяя*КряяЯ*")
#     def anquackable(self):
#         print("*и треск сверчков*")



# другая в том, чтобы было две переменные, где хранятся значения от которых зависит будет ли ребенок использовать те или иные методы

class Duck(ABC):#Flyable, Quackable):

    def __init__(self, flying=0, quacking=0):
        self.flying = flying
        self.quacking = quacking

    def Flyable(self):
        if self.flying == 1:
            print('it can fly')

    def Quackable(self):
        if self.quacking == 1:
            print('it can quack')
            
class MallardDuck(Duck):
    def __init__(self):
        Duck.__init__(self)

class REdHeadDuck(Duck):
    def __init__(self):
        Duck.__init__(self)

# у уток ниже не должна реализовываться часть методов 
class RubberDuck(Duck): 
    def __init__(self):
        Duck.__init__(self)
        self.flying = 0

class DecoyDuck(Duck):
     def __init__(self, flying, quacking):
         Duck.__init__(self)
         self.flying = flying
         self.quacking = quacking

oleg = DecoyDuck()
mald = MallardDuck()
mald.quacking = 1
mald.flying = 1

