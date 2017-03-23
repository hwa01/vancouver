#coding=utf-8


#动态属性
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法

class Student(object):
    pass

s = Student()
s.name = 'hwa'   # 动态给实例绑定一个属性
print s.name

#还可以尝试给实例绑定一个方法

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Student)  #  利用MethodType给实例绑定了一个方法
s.set_age(23)
print s.age

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
#s2.set_age(23) #会报错，因为s2实例没有绑定这个方法

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,None,Student) #给一个类绑定了方法，所有的实例都有了这个方法

s3 = Student()
s3.set_score(100)
print s3.score

#使用__slots__

#如果我们想要限制class的属性，比如，只允许对Student实例添加name和age属性，不能随意添加其他属性
#定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student5(object):
    __slot__=('name','age') # 用tuple定义允许绑定的属性名称

g = Student5()
g.name = 'gwh'
g.age = 25
print g.name
print g.age

g.height = 170
'''  根据教程，这里应该报错，但是为什么没有报错呢？ '''

#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
'''
>>> class GraduateStudent(Student):
...     pass
...
>>> g = GraduateStudent()
>>> g.score = 9999
除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
'''


#  使用@property

# 自己写getter、setter方法比较麻烦，可以使用@property来简化

class Student(object):

    @property       #把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@birth.setter
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property       #可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    def age(self):
        return 2014 - self._birth

print Student


#多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')


class Dog(Mammal, Runnable):  #dog 多继承关系
    pass


#Mixin


#定制类   __xxx__

#重写__str__方法

class Friend(object):
    def __init__(self,name):
        self.name = name
print Friend('gwh')  #<__main__.Friend object at 0x00000000026EC358>

class Friend(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Friend object (name:%s)' % self.name
print Friend('gwh')   #Friend object (name:gwh)


#__iter__

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值

#__getitem__

#__getattr__

'''重写这个方法，可以对类实现扩展'''


#type()
'''
type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<type 'type'>
>>> print(type(h))
<class '__main__.Hello'>
'''



#metaclass
'''
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''


#异常处理
import logging

try:
    print 'try...'
    r = 10/0
    print 'result:',r
except ZeroDivisionError, e:
    print 'exception:',e
    logging.exception(e)
finally:
    print 'finally...'
print 'end'

#raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型

# 调试程序

#print
#logging
#assert
#pdb




