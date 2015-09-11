# 素筛法_filter
# def  _odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield n
# def _not_divisiable(n):
# 	return lambda x: x%n>0

# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisiable(n),it)

# for n in primes():
# 	if n < 1000:
# 		print(n)
# 	else:
# 		break
#验证迭代器会随着next指向下一个对象
# it = iter([1,2,3,4,5,6])
# while True:
# 	try:
# 	    x = next(it)
# 	    print(x)
# 	except StopIteration:
# 		break;

# print(list(it))

#判断回文数 方法一_filter
# def is_palindrome(n):
# 	ret1 = n;
# 	ret2 = 0;
# 	while(n!=0):
# 		ret2 = ret2*10+n%10
# 		n=n//10
# 	return ret1==ret2
# output = filter(is_palindrome,range(1,1000))
# print(list(output))
#判断回文数 方法二_filter
# def is_palindrome(n):
# 	return n==int(str(n)[::-1])
# output = filter(is_palindrome,range(1,1000))
# print(list(output))

#排序_按照名字排序_sort
# def by_name(t):
# 	return t[0]
# L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',80)]

# L2 = sorted(L,key = by_name)
# print(L2)
# #排序_按照分数排序_sort
# def by_score(t):
# 	return t[1]
# L2 = sorted(L,key = by_score)
# print(L2)

#返回函数_指向同一个引用_i_函数作为返回值
#Tip:返回的函数不要引用循环中的变量或后续发生改变的变量
#Tip:返回的函数并未执行，所以函数内不要引用那些会发生变化的变量
# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def func():
# 			return i*i
# 		fs.append(func)
# 	return fs
# f1,f2,f3 = count()
# print(f1())
	
#函数对象的属性_(__name__):可以访问函数的名字
# def now():
# 	print("hahha")
# print(now.__name__)

#装饰器_无文本 now = log(now)
# def log(func):
# 	def wrapfunc(*args,**kw):
# 		print("call %s:" %func.__name__)
# 		func(*args,**kw)
# 	return wrapfunc
# @log
# def now():
# 	print("hahahah")
# now()
#装饰器_文本 now = log('fuckoff')(now)
# def log(text):
# 	def decorator(func):
# 		def wrapfunc(*args,**kw):
# 			print('call %s %s:' %(text,func.__name__))
# 			return func(*args,**kw)
# 		return wrapfunc
# 	return decorator

# @log('fuckoff')
# def now():
# 	print("hahahueueue")
# now()

# print(now.__name__)

# class Student(object):
# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score

# 	def print_score(self):
# 		print('%s: %s' %(self.__name,self.__score))

# 	def get_name(self):
# 		return self.__name

# 	def get_score(self):
# 		return self.__score

# 	def set_name(self,name):
# 		set_name = name

# 	def set_score(self,score):
# 		set_score = score


# Bob = Student("Bob",60)
# Alice = Student("Alice",80)
# Bob.print_score()
# Alice.print_score()
# print(Alice._Student__name)
# from types import MethodType
# def set_city(self,city):
# 	self.city = city
# class Student:
# 	__slots__=('name','score','set_city')
# 	pass
# stu = Student()
# #对当前的实例增加set_city的方法
# stu.set_city = MethodType(set_city,Student)
# stu.set_city('Beijing')
# print(stu.city)

# class Screen:
# 	@property
# 	def width(self):
# 	    return self._width
# 	@width.setter
# 	def width(self,value):
# 		self._width = value

# 	@property
# 	def height(self):
# 	    return self._height
# 	@height.setter
# 	def height(self, value):
# 	    self._height = value

# 	def prin(self):
# 		print(self._width,self._height)

# scre = Screen()
# scre.width = 10
# scre.height = 50
# scre.prin() 

# class student(object):
# 	def __init__(self,name):
# 		self.__name = name
# 	def __str__(self):
# 		return self.__name;

# s = student('Happy')
# print(s)

# class Fib(object):
# 	def __init__(self):
# 		self.a,self.b = 0,1
# 	def __iter__(self):#声明的作用是用来说明当前是否是一个迭代对象
# 		return self
# 	def __next__(self):#每一次外部循环迭代时都要调用next函数，每一次next时
# 					   #都要判断当前是否是迭代对象
# 		self.a,self.b = self.b,self.a+self.b
# 		if self.a >10000:
# 			raise StopIteration();
# 		return self.a
# for n in Fib():
# 	print(n)

# class Chain(object):
# 	def __init__(self,path=''):
# 		self._path = path
# 	def __getattr__(self,path):
# 		return Chain('%s/%s' %(self._path,path))
# 	def __str__(self):
# 		return self._path

# 	__repr__=__str__
# print(Chain().status.user.timeline.list)

#定制类_重写__str__
# class Student(object):
# 	def __init__(self,name):
# 		self.__name = name
# 	def __str__(self):
# 		return self.__name
# s = Student('Happy')
# print(s)

#定制类_重写__next__和__iter__
# class Fibo():
# 	def __init__(self):
# 		self.__a = 0;
# 		self.__b = 1;
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		self.__a ,self.__b = self.__b,self.__a+self.__b
# 		if self.__a>10000:
# 			raise StopIteration();
# 		return self.__a
# for n in Fibo():
# 	print(n)

#定制类_重写__getitem__
# class Fibo(object):
# 	def __init__(self):
# 		pass
# 	def __getitem__(self,n):
# 		if isinstance(n,int):
# 			a ,b = 0,1
# 			if n>100:
# 				raise StopIteration();
# 			for x in range(0,100):
# 				if x==n :
# 					return a
# 				else:
# 					a,b = b,a+b
# 		elif isinstance(n,slice):
# 			start = n.start
# 			end   = n.stop
# 			if start is None:
# 				start = 0
# 			L = []
# 			for i in range(end):
# 				if i>=start:
# 					L.append(i)
# 			return L
#  print(Fibo()[:8])
#定制类_重写__getattr__普通变量
# class Student(object):
# 	def __init__(self):
# 		pass
# 	def __getattr__(self,attr):
# 		if attr =='name':
# 			return 99
# s1 = Student()
# print(s1.name)
#定制类_重写__getattr__函数(返回的是一个函数)
#没有该属性则报错提示该属性不存在(object就用了该机制)
# class Student(object):
# 	def __init__(self):
# 		pass
# 	def __getattr__(self,attr):
# 		if attr =='age':
# 			return lambda :25
# 		else:
# 			raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# s1 = Student()
# print(s1.age())
# print(s1.name)
#定制类_重写__getattr__链式应用和Call的应用
# class Chain():
# 	def __init__(self,path=''):
# 		self.__path = path
# 	def __getattr__(self,attr):
# 		return Chain('%s/%s' % (self.__path,attr))
# 	def __str__(self):
# 		return self.__path
# 	def __call__(self,pthname):
# 		return Chain('%s/%s' %(self.__path,pthname));
# 	__repr__ = __str__	
#print(Chain().status.user.timeline.list)
#print(Chain().user('michael').repos)
# print(Chain().users('michael').repos)

#枚举类__
# from enum import Enum
# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# for name,member in Month.__members__.items():
# 	print(name,'=>',member,',',member.value)

#枚举类__继承Enum
#from enum import Enum,unique
#装饰器检测是否有重复的枚举值
#不能生成实例，直接用类直接调用(类似于静态变量)
# @unique
# class Week(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6
# #W = Week()
# print(Week.Sun.value)

# def inerFn1(self,name = ''):
# 	print('name %s' %name)
# def inerFn2(self,score = ''):
# 	print('score %s' %score)
#动态创建类:利用type创建类
#类名,继承的类的集合,和对应的成员函数
#可以理解Hello是由type创建出来的类的实例,但属于类(所以Hello的类型是type类型)
#类的声明(普通的写法)在python解释后利用type来生成类
# Hello = type('Hello',(object,),dict(hello=inerFn1,score=inerFn2))
# h = Hello()
# print(h.hello())
# print(h.score())

# metaclass是类的模板，所以必须从`type`类型派生；
#当我new一个MyList对象时,其实是调用ListMetaclass的__new__方法
#bases为MyList的继承类不包括metaclass=ListMetaclass
#attrs为继承MyList的所有属性
#等上述执行完之后再执行MyList的__init__方法
#上述新创建的Mylist类中(原有的list[list类未曾改变])增加了一个方法add
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         print(cls)
#         print(bases)
#         print(attrs)
#         return type.__new__(cls, name, bases, attrs)

# class MyList(list, metaclass=ListMetaclass):
# 	pass
#     # def __init__(self):
#     # 	print('fuck')
# L = MyList()
# L.add(1)
# print(L)

# class Field(object):

#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type

#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)

# class StringField(Field):

#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')

# class IntegerField(Field):

#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')

# class ModelMetaclass(type):

#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         #user继承了Model然后当User实例时则通过检测其父类是否元类
#         #且元类里的name为User
#         #print('attr: %s' %attrs)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         #for 循环表示属性集合里已经没有对应的属性
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)

# class Model(dict, metaclass=ModelMetaclass):

#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value

#     def save(self):
#         fields = []
#         params = []
#         args = []
#         #且通过ModelMetaclass的过程使得User类的attrs多了__mappings__
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))

#class User(Model):
    # 定义类的属性到列的映射：
    # id = IntegerField('id')
    # name = StringField('username')
    # email = StringField('email')
    # password = StringField('password')
    # pp = 10

# 创建一个实例：
#u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
#保存到数据库：
#并利用了父类到子类的多态
#u.save()
#对orm框架的理解
#定义metaclass-->创建类--->创建实例
#可以动态的去创建那些我们需要的类
#首先定义了数据库的一些字段
#然后定义了元类ModelMetalClass作用是为了动态的定义类
#元类中做的处理是排除Model然后对子类User类做处理:
#将子类中的涉及Filed的的属性全部删除并放到创建完的字典中
#利用多态如save可以读到对应的值
#这样做的目的是为了适应不同的表


# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#     	#pass
#         #print(e)
#         logging.exception(e)

# main()
# print('END')

# def g(n):

# 	if n==0:
# 		raise ValueError('除0错误')
# 	return 10/0
# def f(c):
# 	n = g(int(c))
# 	try:
# 		print(n)
# 	except ValueError as e:
# 		print(e)
# 	else:
# 		print('no error')
# 		pass
# 	finally:
# 		pass
# 	print('End')
# f('0')

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

#调试的第一种方式--直接输出
#如果程序不出错则print可以输出
#否则print不会输出(如遇到0)
# def foo(s):
# 	n = int(s)
# 	print('>>n %d' %n)
# 	return 10/n
# def main():
# 	foo('10')

# main()
#调试的第二种方式--断言
#如果n不为0则执行10/n否则输出'n is zero'
#用python -O 文件名 可以忽略断言
# def foo(s):
# 	n = int(s)
# 	assert n!=0,'n is zero'
# 	return 10/n
# def main():
# 	foo('0')
#
# main()
#调试的第三种方式--打印日志
#打印日志分4种等级:DEBUG , INFO, WARNING,ERROR
#当前响应的是低等级时,level = 低等级 然后代码中打印的等级比当前响应的等级高或等于是可以打印日志的
# import  logging
# logging.basicConfig(level=logging.WARNING)
# def foo(s):
# 	n = int(s)
# 	if n==0:
# 		logging.error('n==0 error')
# 	return 10/n
# def main():
# 	foo('0')
#main()
#调试的第四种方式--pdb[单步调试和设置断点]

# def foo(s):
# 	n = int(s)
# 	return 10/n
# def main():
# 	foo('0')
# main()

#单元测试
#重写一个Dict模块 用unittest.TestCase的继承类来判断当前写的模块是否存在错误
# import unittest
# class Dict(dict):
# 	def __init__(self,**kw):
# 		super().__init__(self,**kw);
#
# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise ArithmeticError("Error Key")
# 	def __setattr__(self, key, value):
# 		self[key] = value
# #所有要测试都必须加上test__
# class Test(unittest.TestCase):
# 	#检测所要检测类的初始化问题
# 	def test__init(self):
# 		d = Dict(a = 1,b = 'test')
# 		self.assertEquals(d.a,1)
# 		self.assertEquals(d.b,'test')
# 		self.assertTrue(isinstance(d,Dict))
# 	#检测当前的key值是否被正确的赋值
# 	def test__key(self):
# 		d = Dict()
# 		d['key'] = 'value'
# 		self.assertEquals(d.key,'value')
# 	#测试属性 判断当前动态增加的属性是否存在并且判断其对应的value值正不正确
# 	def test__attr(self):
# 		d = Dict()
# 		d.key = 'value'
# 		self.assertTrue('key'in d)
# 		self.assertEquals(d['key'],'value')
# 	#判断是否会产生键错误时当键发生错误时会抛一个错误
# 	def test_keyerror(self):
# 		d = Dict()
# 		with self.assertRaises(KeyError):
# 			value = d['empty']
# 	#测试当属性为空会不会报错,当属性不存在时会抛一个属性错误
# 	def test__attr(self):
# 		d = Dict()
# 		with self.assertRaises(AttributeError):
# 			value = d.empty
# 	if __name__ == '__main__':
# 		unittest.main()

# with语句
# with 某个类的对象:
#      语句
#是执行表达式后在执行语句(有时候表达式内有中断)
#该类必须要实现两个部分:__enter__,__exit__
#整个with语句先调用__enter__，调用语句,在调用__exit__
# class A:
# 	def __init__(self):
# 		pass
# 	def __enter__(self):
# 		print('enter')
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		print('exit')
#
# with A():
# 	print('With')

#文件的IO(类似于C语言)
#打开文件__只读(如果没有文件则报错)
#返回的是文件描述符
#f = open('E:\python\IO.txt','r',encoding='gbk')
#read函数读能如果默认是读文件内全部的内容
#print(f.read())
#f.close()
#文件打开时要注意关闭但有时在文件打开时会出错所以需要判断异常__方法1
# try:
# 	f = open('E:\python\IO.txt','r',encoding='gbk')
# 	print(f.read())
# finally:
# 	f.close()
#文件打开时要注意关闭但有时在文件打开时会出错所以需要判断异常__方法2_with
# with open('E:\python\IO.txt','r',encoding='gbk') as f:
# 	print(f.read())
#读文件时还可以用ReadLine:表示一行一行读
#ReadLines:表示将所有行都放在List里
# with open('E:\python\IO.txt','r',encoding='gbk') as f:
# 	print(f.readlines())
#表示以二进制流打开
#with open('E:\python\IO.txt','rb',encoding='gbk') as f
#写文件 write 向文件写数据会覆盖源文件的内容
# with open('E:\python\IO.txt','w',encoding='gbk') as f:
# 	f.write("dhakhdakshdkj")
#StringIO 内存读写数据(StringIO为保存所要存储和提供对应的值)_字符串流
#StringIO只能用来读或用来写不能两者同时
# from io import StringIO
# strIO = StringIO()
# strIO.write("hdhdhdhhdhdahjdshasdhkja\n")
#print(strIO.getvalue())
#当strIO用write时，用readlines只能读到换行
# for s in strIO.readlines():
#     print(str(s.strip()))
# while True:
#      s = strIO.readline()
#      if s == '':
#          break
#      print(s.strip())
#BytesIO 内存读写数据(StringIO为保存所要存储和提供对应的值)_二进制流
#BytesIO只能用来读或用来写不能两者同时
#from io import BytesIO
# f = BytesIO()
# f.write('中文\n英文\n法文\n'.encode('utf-8'))
# print(f.getvalue())
# f = BytesIO()
# f.write(b'\xe4\xb8\xad\xe6\x96\x87\n\xe8\x8b\xb1\xe6\x96\x87\n\xe6\xb3\x95\xe6\x96\x87\n')
# print(f.read())
#实现ls -l的效果得到当前目录文件的详细信息
#os stat返回的是文件信息        #st_gid:组ID
#st_mode:文件的权限            #st_size:文件的大小
#st_ino:文件的索引号           #st_atime:文件上次访问时间
#st_dev:文件的设备             #st_mtime:文件修改时间
#st_nlink:文件的链接号         #st_ctime:文件创建时间
#st_uid:用户ID
# import os
# import time
# L = [f for f in os.listdir('.') if os.path.isfile(f)]
# for f in L:
#     print(os.stat(f))
#实现对指定字符串找出所有包含该字符串的文件名的文件
#filepath表示当前的路径
#prepath表示之前的路径
# import os
#
#
# def getret(filepath, prepath):
#     #拿到当前路径的所有的文件夹
#    LDIR = [f for f in os.listdir(filepath) if os.path.isdir(f)]
#    #print(filepath)
#    LFile = [f for f in os.listdir(filepath) if os.path.isdir(f)==False and val.lower() in f]
#    #print(LFile)
#    for name in LFile:
#         print('%s/%s' % (prepath, name))
#    if len(LDIR)>0:
#         for name in LDIR:
#             getret(filepath+"/"+name, prepath+'/'+name)
# val = input()
# print(os.getcwd())
# getret(os.getcwd(), '')

#序列化反序列化
#序列化将对应的对象进行编码
#反序列化就是解码
# import pickle
# d = dict(name = 'Bob',age = 20,score = 80)
# #序列化
# f = open('/Users/lijiayueee/Documents/learnPython/pickle.txt','wb')
# #序列化d
# pickle.dump(d,f)
# f.close();
# #反序列化
# f = open('/Users/lijiayueee/Documents/learnPython/pickle.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)
#将python转化为json
# import json
# f = open('/Users/lijiayueee/Documents/learnPython/json','w+')
# d = dict(name = 'Bob' , age = 20 ,score = 80)
# json.dump(d,f)
# f.close()
#
# f = open('/Users/lijiayueee/Documents/learnPython/json','r')
# d = json.load(f)
# f.close()
# print(d)
#我们可以讲任一一个对象通过将自身的__dict__传给JSON即可得到对应的序列(__dict__:存储则这个实力中所有的属性和对应的值)
# import json
# class Student:
#     def __init__(self, name, age, score):
#         self.__name__ = name
#         self.__age__ = age
#         self.__score__ = score
#
#     def __str__(self):
#         return '(%s,%s,%s)' %(self.__name__,self.__age__,self.__score__)
#
# s = Student('Happy',12,88)
# s.num = 50
# f = open('/Users/lijiayueee/Documents/learnPython/json','w')
# json.dump(s,f,default= lambda obj: obj.__dict__)
# f.close()
#
# f = open('/Users/lijiayueee/Documents/learnPython/json','r')
# d = json.load(f)
# f.close()
# print(d)
#可通过d字典去初始化

#创建子进程
# import os
# def test():
#     print('the process is starting')
#     a = 1
#     pid = os.fork()
#     #子进程返回的id为0
#     if pid==0:
#         a = 0
#         print('this is child process %s %s %d',(os.getpid(),os.getppid(),a))
#     else:
#         print('this is parent process %s %s %d',(os.getpid(),pid,a))
# test()
#可以从上述例子得知子进程也是从fork开始的且申拷贝了原来进程中的资源(两个进程中得资源互不干扰)

#创建多进程(多进程中有一个主进程就是当前的入口程序，在当前主进程创建的进程为该主进程的子进程)
#首先我们先用process来创建一个子进程(process(target=function,args))
# import os
# from multiprocessing import Process
# def processrun(name):
#      #print('Run child process  %s...' % (os.getpid()))
#      #print('now process pid %s' % os.getpid())
#
# def processtest():
#     chpro = Process(target=processrun,args=('processrun',))
#     #启动进程
#     chpro.start()
#     #使创建的子进程与父进程同步
#     chpro.join()
#     print('processtest end')
#
# processtest()

#通过进程池的方式创建子进程


#正则表达式
# re.match(r'[0-9a-zA-Z]{1,18}[\.]{0,1}[0-9a-zA-Z]{1,18}\@[0-9a-zA-Z]{2,18}\.[0-9a-zA-Z]{3}','boll.someone@gmail.com')
# re.match(r'^\<[a-z\s+A-Z\s+]{0,14}\>\s+[0-9a-zA-Z]{0,18}[\.]{0,1}[0-9a-zA-Z]{1,18}\@[0-9a-zA-Z]{2,18}\.[0-9a-zA-Z]{3
# }','<Tom Paris> tom@voyager.org')
#
# m = re.match(r'\<([a-z\s+A-Z\s+]{0,20})\>\s+([0-9a-zA-Z\.\@]*)','<Tom Paris> tom@voyager.org')


#将给定的字符串转化为时间戳
# from datetime import datetime, timedelta, timezone
# import re
# #utc+8:00
# def to_timestamp(dt_str, tz_str):
#     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#     # re.match(r'([a-zA-Z]{3})([\+\-]{1})(\d{2})(\:)(\d{2})','UTC+07:00').groups()
#     l = list(re.match(r'([a-zA-Z]{3})([\+\-]{1})(\d{1,2})(\:)(\d{1,2})',tz_str).groups())
#     if len(l)==0:
#         return
#     h = int(l[2])
#     if l[1]=='-':
#         h = h*-1;
#     print(dt,h)
#     print(dt.timestamp())
#     tz_utc_h = timezone(timedelta(hours=h))
#     dt = dt.replace(tzinfo=tz_utc_h)
#     print(dt.timestamp())
#
# to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')

#用来判断当前的字符串是否是字节流还是字符串
# def p(s):
#     #t = str.encode('ascii')
#     if isinstance(s,str):
#         print('Str')
#     elif isinstance(s,bytes):
#         print('Bytes')
#     print(len(s))
# p(b'123')

#safe_base64_decode:该函数用于处理那些去掉=号的编码(当前的字节流长度不满足是8的倍数)
#还有一种方法是将字节流的长度变成4的整数倍因为6*x/4 = 3*x/4 所以x最小为4
# import base64
# def safe_base64_decode(s):
#     if isinstance(s,bytes):
#         stmp = s.decode('ascii')
#     else:
#         stmp = s
#     length = len(stmp)
#     if (length*6)%8==0:
#         stmp.encode('ascii')
#     else:
#         while True:
#             stmp+='='
#             length+=1
#             if (length*6)%8==0:
#                 stmp.encode('ascii')
#                 break
#
#     print(base64.b64decode(stmp))
#
# safe_base64_decode(b'YWJjZA==')
# safe_base64_decode(b'YWJjZA')
# safe_base64_decode('YWJjZA==')
# safe_base64_decode('YWJjZA')
# b1 = 0
# b2 = 156
# b3 = 64
# b4 = 99
# bs = bytes([b1,b2,b3,b4])
# print(bs)

#理解big-endian 和 little-endian
#假如说当前的4个字节: \x38\x8c\x0a\x00
#当我们用BigEndin时 则在内存中的字节序为 00 0a 8c 38 从低位到高位(高字节存储在高位 低字节存储在低位)
#当我们用little-Endin时 则在内存中的字节序为 38 8c 0a 00 从低位到高位(int存储的字节序相反)
#解析判断当前所传的值是否为bmp文件
# import struct
# def check_bmp(s):
#     if len(s)!=30:
#         return False
#     t = struct.unpack('<ccIIIIIIHH',s)
#     s1 = t[0].decode('ascii')
#     s2 = t[1].decode('ascii')
#     if s1 == 'B' and s2 =='M':
#         print('%d,%d' %(t[6],t[7]))
#     return True
#
# t = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# if check_bmp(t):
#     print('bmp')
#判断一个文件是否是bmp文件
#涉及到文件的读
#import struct
#检测某一路径下的文件类型是否满足bmp
#打开文件后读取内容
# def check_bmp(path):
#     with open(path, 'rb') as f:
#         s = f.read(30)
#         if len(s) < 30:
#             return False
#         s = struct.unpack('<ccIIIIIIHH', s)
#         #print(s[0].decode('utf-8'),s[1].decode('ascii'))
#         if s[0]== b'B' and s[1] == b'M':
#             print('%d,%d' % (s[6],s[7]))
#             return True
#
#         return False
#
# if check_bmp('C:\\Users\\happyli\\Desktop\\11.jpg'):
#     print('BMP')

#将当前传入的字符串转化为MD5hash
# import hashlib
# def cal_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()
#
# print(cal_md5('123456'))
# print(cal_md5('123456'))
#登陆的用户的密码是否正确
# import hashlib
# db = {
#       'michael':'e10adc3949ba59abbe56e057f20f883e',
#       'bob':'878ef96e86145580c38c87f0410ad153',
#       'alice':'99b1c2188db85afee403b1536010c2c9'
#       }
#
# def login(usr,passward):
#     md5 = hashlib.md5()
#     md5.update(passward.encode('utf-8'))
#     return str(md5.hexdigest())==db[usr]
#
# if login('bob','123456'):
#     print('Login Success')
#注册和登陆
# import hashlib
# db = {}
#
# def regist(usr,pwd):
#     if db.get(usr) != None:
#         return -1
#     md5 = hashlib.md5()
#     md5.update((usr+pwd+'the-Salt').encode('utf-8'))
#     db[usr] = str(md5.hexdigest())
#     return 1
# def login(usr,pwd):
#     if db.get(usr) == None:
#         return False
#     md5 = hashlib.md5()
#     md5.update((usr+pwd+'the-Salt').encode('utf-8'))
#     return str(md5.hexdigest()) == db[usr]
#
# if login('happy','123456'):
#     print('login success')
#
#
# if regist('happy','123456'):
#     print('regist success')
#
# if login('happy','12345'):
#     print('login success')


# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         if attrs.get('href'):
#             print('yes')
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# from xml.parsers.expat import  ParserCreate
# import re
#
# db = {}
# #tag = False
# #global tag
# class weathersaxhandle(object):
#     global tag
#     def start_element(self, name, attrs):
#         if attrs.get('city'):
#             db['city'] = attrs.get('city')
#         if attrs.get('country'):
#             db['country'] = attrs.get('country')
#         if attrs.get('day'):
#             tmp = attrs.get('day')
#             #print(len(db))
#             if len(db)==2:
#                 tmp = 'today'
#             elif len(db)==3:
#                 tmp = 'tomorrow'
#             else:
#                 return
#             db[tmp] = {}
#             if attrs.get('text'):
#                 db[tmp]['text'] =  attrs.get('text')
#                 #print('yes0')
#             if attrs.get('low'):
#                 db[tmp]['low'] = int(attrs.get('low'))
#                 #print(db[tmp]['low'])
#             if attrs.get('high'):
#                 db[tmp]['high'] = int(attrs.get('high'))
#                 #print('yes2')
#             #print(len(db))
#
#         #print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#     #global tag
#     def end_element(self, name):
#         pass
#
#     def char_data(self, text):
#         pass
#
# data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
# <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#         <title>Yahoo! Weather - Beijing, CN</title>
#         <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#         <yweather:location city="Beijing" region="" country="China"/>
#         <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#         <yweather:wind chill="28" direction="180" speed="14.48" />
#         <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#         <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#         <item>
#             <geo:lat>39.91</geo:lat>
#             <geo:long>116.39</geo:long>
#             <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#             <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#             <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#             <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#             <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#             <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#             <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#         </item>
#     </channel>
# </rss>
# '''
# handler = weathersaxhandle()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(data)
#
#
# assert db['city'] == 'Beijing', db['city']
# assert db['country'] == 'China', db['country']
# assert db['today']['text'] == 'Partly Cloudy', db['today']['text']
# assert db['today']['low'] == 20, db['today']['low']
# assert db['today']['high'] == 33, db['today']['high']
# assert db['tomorrow']['text'] == 'Sunny', db['tomorrow']['text']
# assert db['tomorrow']['low'] == 21, db['tomorrow']['low']
# assert db['tomorrow']['high'] == 34, db['tomorrow']['high']
# print('Weather:', str(db))
# import re
# t = re.match(r'([A-Za-z]{3})(,*)', 'Wed, 27 May 2015 11:00 am CST').groups()
# print(t)

# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#     bTitle = False
#     bLoca = False
#     bTime = False
#
#     def handle_starttag(self, tag, attrs):
#         if ('class','event-title') in attrs:
#             self.bTitle = True
#         elif ('class','event-location') in attrs:
#             self.bLoca = True
#         elif tag=='time':
#             self.bTime = True
#
#     def handle_endtag(self, tag):
#         if tag=='h3':
#             self.bTitle = False
#         elif tag == 'time':
#             self.bTime = False
#         elif tag == 'span':
#             self.bLoca = False
#         #print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         if self.bTitle or self.bLoca or self.bTime:
#             if self.bTitle:
#                 print('-'*50)
#             print(str(data).strip())
#
#     def handle_comment(self, data):
#         pass
#         #print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         pass
#         #print('&%s;' % name)
#
#     def handle_charref(self, name):
#         pass
#         #print('&#%s;' % name)
#
# parser = MyHTMLParser()
#
# with open('C:\\Users\\happyli\\Desktop\\python.html','r') as f:
#     parser.feed(f.read())


# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

#硬编码改为从url读取
# from urllib import request, parse
# def fetch_xml(url):
#     with request.urlopen(url) as f:
#         data = f.read()
#         print('Data: ',data.decode('utf-8'))
#
# fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')

#ip协议负责将数据从一台计算机上通过网络传到另一台计算机上,不能保证顺序到达，和能到达
#tcp协议保证数据能够顺序到达并且如果发的数据丢失，则重新发送
#一个IP包包含:目标IP,源IP,数据,端口
#端口的概念 因为一个计算机可能同时跑着多个网络程序 也就是说可能会收到很多IP包 所以需要通过端口来判断
#当前IP包对应哪个端口(计算机会给每个网络程序一个或多个端口,且端口是独一无二的 )












