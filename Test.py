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






















