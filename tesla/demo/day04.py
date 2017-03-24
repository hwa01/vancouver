#coding=utf-8

#文件
#读取文件
import os
f= open('E://workcode//vancouver//.gitignore','r')   #标示符'r'表示读
print f.read()

# 打开文件，需要确保close
try:
    f= open('E://workcode//vancouver//.gitignore','r')
    print f.read()
finally:
    if f:
        f.close()

#使用with解决try...finally 问题
with open('E://workcode//vancouver//.gitignore','r') as f:
    print f.read()

#二进制文件
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
#f = open('/Users/michael/test.jpg', 'rb')

'''
字符编码

要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：

>>> f = open('/Users/michael/gbk.txt', 'rb')
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u
测试
如果每次都这么手动转换编码嫌麻烦（写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码），Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：

import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'
'''


#写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# f = open('/Users/michael/test.txt', 'w')
# f.write('Hello, world!')
# f.close()

with open('E://workcode//vancouver//test.txt', 'w') as f:  #同样的，用with来解决close问题
    f.write('Hello, world!')


#操作文件和目录
import os
print os.name
# 操作系统名字,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

print os.environ #全部的环境变量

print os.getenv('PATH')   #获取某个环境变量的值


#JSON
'''
JSON类型	    Python类型
{}	        dict
[]	        list
"string"	'str'或u'unicode'
1234.56	    int或float
true/false	True/False
null	    None
'''

import json
d = dict(name='Bob',age=20,score=88)
print json.dumps(d)    #{"age": 20, "score": 88, "name": "Bob"}

json_str = '{"age":20,"socre":20,"name":"bob"}'
print json.loads(json_str)  #{u'age': 20, u'socre': 20, u'name': u'bob'}
#需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，
# 所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。
j = json.loads(json_str)
print j.get('age')


#json与对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dic(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s = Student('Bob', 20, 88)
print json.dumps(s,default=student2dic)  #Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。

print json.dumps(s,default=lambda obj:obj.__dict__)
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str,object_hook=dict2student)
#要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例


#多进程
'''
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
# multiprocessing.py
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
运行结果如下：

Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''

#多线程

import time,threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n<5:
        n = n+1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t=threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name


#Lock

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        # do something...
        finally:
            # 改完了一定要释放锁:
            lock.release()





#ThreadLocal
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 执行结果
# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)
# 道理和java类似

#正则表达式

#内建模块
#collections

