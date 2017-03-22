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







































