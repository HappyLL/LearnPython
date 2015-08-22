import math
def quadratic(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "Numerous solutions","Numerous solutions"
            else:
                return  "No Solution","No Solution"
        else:
             return -c/b,-c/b
    else:
        t = b*b - 4*a*c;
        if t<0:
            return "No Solution","No Solution"
        else:
            return (-b-math.sqrt(t))/(2*a),(-b+math.sqrt(t))/(2*a)

x1,x2 = quadratic(1,3,-4)
print(x1,x2)

def dictParam(name,age,**dic):
    print('name:',name,'age:',age,'other:',dic)
dictParam('ljy','25',city='fuck')

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def fact_fi(n,pro):
    if n==1:
        return pro
    return fact_fi(n-1,pro*n)
def fact(n):
    return fact_fi(n,1)

def move(n,a,b,c):
    if n==1:
        print(a,'---->',c)
        return;
    move(n-1,a,c,b)
    print(a,'---->',c)
    move(n-1,b,a,c)

L = [1]
n = 1
def triangles():
    global L
    global n
    while True:
        yield L
        n = n +1
        L2 = []
        i = 1
        for i in range(n+1):
            if i==1 or i==n:
                L2.append(L[0])
            elif i>1 and i<n:
                L2.append(L[i-2]+L[i-1])
        L = L2

def normalize(L):
    s1 = ''
    for i,value in enumerate(L):
        if i==0:
            if value.islower():
                s1=s1+(value.upper())
            else:
                s1=s1+(value)
        else:
            if value.isupper():
                 s1=s1+(value.lower())
            else:
                s1=s1+(value)

    return s1
print(map(normalize,['adam', 'LISA', 'barT']))

def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print(prod([3, 5, 7, 9]))
def str2float(s):
    d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'-':0,'INF':'INF'}
    def fnmap(c):
        if c=='.':
            c = 'INF'
        return d[c]
    def fred(x,y):
        if x=='INF'or y=='INF':
            if x=='INF':
                return y
            else:
                return x
        if x<0:
            return x*10-y
        else:
            return x*10+y
    def ffn():
        ret = 1
        flag = 0
        for i,value in enumerate(s):
            if value=='.':
                flag =1
            elif flag==1:
                ret = ret*10
            elif value =='-':
                ret = ret*-1
        return ret
    return reduce(fred,map(fnmap,s))*1.0/ffn();

def newstr2float(s):
    L =s.split('.')
    d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'-':0,'INF':'INF'}
    



print(str2float('123.456'))
print(123456/1000)

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break









