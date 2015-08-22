#素筛法_filter
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






