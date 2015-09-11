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












