#coding=utf-8

''' 函数 '''

# 默认参数

def power(x,n=2):  # 给定一个默认参数
    s = 1
    while(n>0):
        s = s * x
        n = n-1
    return s

print power(5)  # 调用power(5) 相当于调用power(5,2)
print power(5,3)
print power(n=3,x=5) #也可以不按顺序提供部分默认参数，当不按顺序提供部分默认参数时，需要把参数名写上

# 注意点：必选参数在前，默认参数在后，当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 注意点：默认参数必须指向不变对象！
def add_end(L = []):
    L.append('END')
    return L
print add_end([1,3,4]) # [1, 3, 4, 'END']   正确
print add_end()  #['END']  刚开始是对的
print add_end()  #['END', 'END']  调用几次就有问题了
print add_end()  #['END', 'END', 'END']
''' Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
理解：默认参数会被认为是函数的一个变量，如果默认参加是可变的，那么当他被改变之后，下次调用就会使用改变之后的值
解决方法：默认参数要使用不可变对象
'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()  #['END']
print add_end()  #['END']
''' str、None 都是不可变对象'''


# 可变参数

def calc(*numbers):  #在参数前面加星号(*)，变成可变参数
    sum =0
    for n in numbers:
        sum = sum + n*n
    return sum

print calc(1,2,3)
print calc()
num = [1,2,3]
print calc(*num)  #在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去


#关键字参数

def person(name,age,**kw):  # 使用两个星号**，可以传入任意多个字典结构
    print 'name:',name,'age:',age,'other:',kw

print person('hwa',25)
print person('gw',25,city='LA',degree='master')
kw = {'city':'LA','degree':'master'}
print person('gw',25,**kw)


#参数组合
'''必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。'''

def func(a,b,c=0,*args,**kwargs):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kwargs=',kwargs

print func(1,2)
print func(1,2,c=3)
print func(1,2,3,'a','b')
print func(1,2,3,'a','b',x=99)

args = (1,2,3,4)
kw = {'x':99}
print func(*args,**kw)  #对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


#递归函数
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

def fabonacci(x):
    if(x==1):
        return 1
    elif(x==2):
        return 1
    else:
        return fabonacci(x-1)+fabonacci(x-2)

print fabonacci(1)
print fabonacci(2)
print fabonacci(3)
print fabonacci(4)
print fabonacci(5)


#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]  #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print L[1:3]
print L[:3]  #如果第一个索引是0，还可以省略
print L[0:]  #全部的数
print L[:]   #全部的数
print L[-2:] #从倒数第二个数开始，倒数第一个数是-1

R = range(100)
print R[:10:2] #前10个数，每两个取一个
print R[::5]   #所有数，每5个取一个

print (0,1,2,3,4,5)[:3]  #tuple也可以用切片操作，只是操作的结果仍是tuple。tuple也是一种list，唯一区别是tuple不可变
print 'ABCDEFGH'[:3]     #字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。
                         # 因此，字符串也可以用切片操作，只是操作结果仍是字符串


#迭代
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x,y


d = {'a': 1, 'b': 2, 'c': 3}

for key in d:  #dict中默认迭代的是key
    print key

for value in d.itervalues():   # 通过itervalues() 迭代value
    print value

for k,v in d.iteritems():  #通过iteritems()  迭代key-value
    print 'k=',k,'v=',v

for ch in 'ABCG':  #字符串也是迭代对象
    print ch

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable

print isinstance('abc',Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123, Iterable)  # 整数不可用于迭代


for i, value in enumerate(['A', 'B', 'C']):  #enumerate函数可以把一个list变成索引-元素对
    print i,value


# 列表生式
print range(1,11)

print [x*x for x in range(1,11)]  #把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

print [x*x for x in range(1,11) if x%2==0]   #for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方

print [m + n for m in 'ABC' for n in 'XYZ']  #还可以使用两层循环，可以生成全排列：

import os
print [d for d in os.listdir('.')]   # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k+'='+v for k,v in d.iteritems()]  #列表生成式也可以使用两个变量来生成list：


# 生成器
#一边循环一边计算的机制，称为生成器（Generator）

L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))  #把一个列表生成式的[]改成()，就创建了一个generator
print g
print g.next()  # 要一个一个打印出来，可以通过generator的next()方法
print g.next()  # 可以使用for循环来遍历取值
for x in g:
    print x

def fib(x):           #一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    n,a,b = 0,0,1     #函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    while n<x:        #而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
        yield b
        a,b = b,a+b
        n = n+1


print fib(6)
for x in fib(6):
    print x



'''高阶函数'''
# 变量可以指向函数
#函数名也是变量

print abs(-20)
print abs
f = abs     # 把函数指向变量，变量也成了一个函数的引用
print f
print f(-20)

#把函数作为参数
def add(x,y,f):
 return f(x)+f(y)

print add(-5,5,abs)


#map()
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
# map()函数接收两个参数，一个是函数，一个是序列

def f(x):
    return x*x

print map(f,[1,2,3,4,5])

#reduce()
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算

def add(x,y):
    return x+y

print reduce(add,[1,2,3,4,5])

def fn(x,y):
    return 10*x+y

print reduce(fn,[1,2,3,4,5])   #12345


#filter
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#filter()也接收一个函数和一个序列

def is_odd(n):
    return n%2==0

print filter(is_odd,[1,2,3,4,5,6,7,8])  #[2, 4, 6, 8]

#sorted()
#可以接收一个比较函数来实现自定义的排序。

print sorted([1,23,1,61,14,234,9])  #[1, 1, 9, 14, 23, 61, 234]

def reverser_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([1,23,1,61,14,234,9],reverser_cmp)  #[234, 61, 23, 14, 9, 1, 1]


# 返回一个函数

def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s=n+s
        return s
    return sum

f = lazy_sum(1,2,3,4,5,6)  # 相当与返回了函数sum，把sum赋给了f，f=sum
print f()   # 开始调用函数f

f2 = lazy_sum(1,2,3,4,5,6)
print f==f2  #False
             # 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

#闭包
#在上一个函数lazy_sum中，返回的函数sum其定义引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

#注意的问题，返回的函数并没有立刻执行，而是直到调用了f()才执行

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print f1()  #9
print f2()  #9
print f3()  #9

#可能认为结果是1,4,9 但却是9,9,9。原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#分析：
'''从网上看来的资料说，闭包 = 函数 + 引用环境，也就是说，当形成一个闭包之后，放进闭包的并不是具体的值。
   以这一节的例子来看，闭包中应该只包含变量i的地址，告诉程序当他被调用时这个i应该从哪里找，此时并不涉及i的值。
   只有当真正调用时，才根据此时i的值算出最终结果，而此时在返回3个函数之后，i的值已经成为3了，
   所以当我们开始调用函数时，返回的值就都是9了'''

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变

def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))     #到这里，函数g用到的值，已经是函数f的参数了。而已绑定到函数参数的值不变
    return fs
f1,f2,f3 = count()
print f1()   #1
print f2()   #4
print f3()   #9

#匿名函数

'''
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x10453d7d0>
>>> f(5)
25
同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y
'''

#装饰器
#decorator就是一个返回函数的高阶函数。
def log(func):
    def wrapper(*args,**kwargs):
        print 'call %s():' % func.__name__
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print '2017-03-22'

now()

'''
调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
>>> now()
call now():
2013-12-25
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。wrapper()函数的参数定义是(*args, **kw)，因此，
wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
这个3层嵌套的decorator用法如下：

@log('execute')
def now():
    print '2013-12-25'
执行结果如下：

>>> now()
execute now():
2013-12-25

我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，
参数是now函数，返回值最终是wrapper函数。

一个完整的decorator的写法如下：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
'''

# 偏函数
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#例如：
print int('1234')  #1234
print int('1234',base=8)  #668  八进制
print int('101010',base=2)  #42   二进制

def int2(x):   # 定义一个int2函数，默认让他的base=2
    return int(x,base=2)

print int2('101010')

import functools
int8 = functools.partial(int,base=8)   #  functools.partial()可以方便的创建偏函数
print int8('10')


#模块
'''请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是这个目录的名称。'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '  #这前面是注释

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv     #运行python hello.py获得的sys.argv就是['hello.py']；
                        #运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':    #在命令行运行模块时生效，而在其他地方导入模块是，if判断将失效
    test()



#别名
import cStringIO as StringIO   #import ... as ...指定了别名


#作用域
'''正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；'''


#类和实例

class Student(object):

    def __init__(self,name,score):   #__init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.score = score

    def print_score(self):     #定义一个方法，除了第一个参数是self外，其他和普通函数一样。
        print '%s:%s' %(self.name,self.score)

bart = Student('Bart',8)
list = Student('Lisa',9)
bart.age = 20
print bart.age  # 20
#print list.age # 会报错，没有给lisa绑定age数据
                # Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

#访问限制

class Student2(object):

    def __init__(self,name,score):
        self.__name = name     #实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__score = score

    def get_name(self):      # 通过get、set方法来访问私有变量
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
>>> bart._Student__name
'Bart'
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
'''


#继承和多态
class Animal(object):  #在class的定义中，把父类放到括号中
    def run(self):
        print 'Animal is running...'

class Dog(Animal):    #在class的定义中，把父类放到括号中
    def run(self):    #重写了父类的run方法
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal()) #多态
run_twice(Dog())    #父类可以出现的地方，都可以放子类进去，并且调用的是子类的具体方法
run_twice(Cat())


#获取对象信息
#使用type()
'''
>>> type(123)
<type 'int'>
>>> type('str')
<type 'str'>
>>> type(None)
<type 'NoneType'>

>>> type(abs)
<type 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>

>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True
最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：

>>> type(int)==type(str)==types.TypeType
True

'''

#使用isinstance()
#要判断class的类型，可以使用isinstance()函数。

#使用dir()
#要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
#['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__'......










































































