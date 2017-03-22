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








