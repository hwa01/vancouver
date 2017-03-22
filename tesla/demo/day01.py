#coding=utf-8
# 遇到中文注释，需要指明encode方式

a = 100
if a>=0:
    print a
else:
    print -a

#引号内引号用 \转义符
print 'I\' am \"OK\"'

#Python允许用'''...'''的格式表示多行内容,或者多行注释

print '''
学习Python
增长知识
保持进步
'''

'''这里
可以是
多行注释
'''

#布尔值 True False
#布尔值可以用and、or和not运算。
print 3>2
print True and False
print True or False
print 'not False:', not False

#空值是Python里一个特殊的值，用None表示。
print None

#Python是动态语言，变量本身类型不固定
a = 123 # a是整数
print a
a = 'ABC' # a变为字符串
print a

#整数除法
print 10/3 #3
print 10.0/3 #3.333333
print 10%3  #1

#编码
print u'中文'

#>>> u'中'
# u'\u4e2d'
'''
写u'中'和u'\u4e2d'是一样的，\u后面是十六进制的Unicode码。因此，u'A'和u'\u0041'也是一样的。
两种字符串如何相互转换？字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码。
把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
'''
print u'ABC'
print u'ABC'.encode('utf-8')

print u'中国'
print u'中国'.encode('utf-8')


#关于编码的介绍
#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819196283586a37629844456ca7e5a7faa9b94ee8000
'''
写u'中'和u'\u4e2d'是一样的，\u后面是十六进制的Unicode码。因此，u'A'和u'\u0041'也是一样的。
两种字符串如何相互转换？字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码。
把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
>>> u'ABC'.encode('utf-8')
'ABC'
>>> u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'
英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同），
而中文字符转换后1个Unicode字符将变为3个UTF-8字符，你看到的\xe4就是其中一个字节，因为它的值是228，
没有对应的字母可以显示，所以以十六进制显示字节的数值。
反过来，把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法：

>>> 'abc'.decode('utf-8')
u'abc'
>>> '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
u'\u4e2d\u6587'
>>> print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
中文


'''

#格式化
print 'hello %s' % 'world'
print  'Hi, %s, you have $%d.' % ('Michael', 1000000)
print  u'Hi, %s' % u'Michael'
#   %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换,%f表示浮点数
#  如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

'''List'''
'''list是一种有序的集合，可以随时添加和删除其中的元素。'''

classmates = ['h','w','a','o','k']
print classmates
print len(classmates)  #用len()函数可以获得list元素的个数
print classmates[0]
print classmates[1]
print classmates[len(classmates)-1]  #最后一个元素的索引是len(classmates) - 1
print classmates[-1]  #可以用-1做索引，直接获取最后一个元素
print classmates[-2]

classmates.append('g')  #list中追加元素到末尾
print classmates
print classmates.insert(2,'gwh')  #把元素插入到指定的位置
print classmates

classmates.pop()  #删除list末尾的元素，用pop()方法
print classmates

classmates.pop(-1)  #删除指定位置的元素，用pop(i)方法，其中i是索引位置
print classmates

classmates[1] = 'love' #把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print classmates


love = ['h',1234,True,23.03]  #list里面的元素的数据类型也可以不同
print love

aoe = ['python','java',['scala','javascript'],'c++']  #list元素也可以是另一个list
print aoe

aa = ['scala','javascript']
aoe = ['python','java',aa,'c++']
print aa[0]
print aoe[2][0]   # 拿到scala的两种写法

aaa = []  #一个空的list，它的长度为0
print len(aaa)



'''tuple'''
'''tuple和list非常类似，但是tuple一旦初始化就不能修改'''
classmates = ('h','l','g')
print classmates

#classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

# tuple 的陷阱
t = (1,2)
print t
t = ()
print t
t = (1)
print t
# 当tuple中只有一个元素，需要在后面加一个逗号，否则会当成小括号来计算
t = (1,)
print t

#可变的tuple
t = ('a','b',['A','B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t

'''
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，
tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，
就不能改成指向其他对象，但指向的这个list本身是可变的！
'''


# 条件判断
# 注意if 和 else 后面都有冒号：
age = 20
print 'your age is:',age
if age>=18:
    print 'adult'
elif age>=6:
    print 'teenager'
else:
    print 'kid'

'''
if x:
    print 'True'

只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
'''


# 循环
# for ...in 循环
names = ['a','b','c','d']
for name in names:
    print name

print range(5) # range()函数，可以生成一个整数序列，包左不包右

sum = 0
for x in range(101):
    sum +=x
print sum


#dict 字典，即map
dic = {'a':1,'b':2,'c':3}
print dic['b']

dic['d'] = 4 #根据key添加元素
print dic

# 如果key不存在，就会报错  print dic['e'] ，可以使用 in 来做判断
print 'e' in dic   # False

print dic.get('b')  # 也可以使用get方法
print dic.get('f',200)  #如果key不存在，可以返回None，或者自己指定的value

dic.pop('b')  #要删除一个key，用pop(key)方法
print dic


# set 只存储key，不存储value，并且元素不重复，重复元素在set中自动被过滤
s= set(['a','b','c'])
print s
s.add(4)  # add()方法添加元素
print s
s.remove('b')  # remove()方法删除元素
print s

s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2    # set 无序无重复元素，所以可以做交集、并集等操作
print s1 | s2


slist = ['w','a','g'] # 可以把一个lsit放入一个set中
s = set(slist)
print s

tu = ('w','a','g')  # 可以把一个tuple放入一个set中
s = set(tu)
print s


#list 是可变对象
a = ['c', 'b', 'a']
a.sort()
print a

# str 是不可变对象
a = 'abc'
b = a.replace('a','A')
print a
print b



#函数
print cmp(1,3)  #自带函数
print int('1234')  #类型转换函数
print int(1234.1)

def my_abs(x): # 利用def 自定义函数
    if x>=0:
        return x
    else:
        return -x

print my_abs(-03)

def nop():
    pass   # 利用pass语句定义空函数，先占个坑，如果什么都不写会报错

def my_abs(x):
    if not isinstance(x,(int,float)):   # 利用isinstance做类型检查
        raise TypeError('类型错误')
    if x>=0:
        return x
    else:
        return -x


import math
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = x+step*math.sin(angle)
    return nx,ny          #返回多个值

x,y = move(100,100,60,math.pi/6)
print x,y

r = move(100,100,60,math.pi/6)  #返回的多个值其实就是一个tuple，可以省略括号而已
print r





