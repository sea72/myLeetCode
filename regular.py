# int
# 1 
# 0xa5b3c3d2 = 0x a5_b3_d2
# 1000 = 100_00

# float
# 1.23 3.14 1.2e3 = 1200

# string 
# "a"   'a'   r'a'
# ''' a b c d '''

# bool
# True False and or not

# None

# string encode/decode
ord('中')
chr(66)
'中文' == '\u4e2d\u6587'

# bytes differs from string
x = b'abc'
b'abc' != 'abc'
'abc'.encode('ascii') == b'abc'
b'abc'.decode('ascii') == 'abc'
# one char = 1 byte / one chinese char = 3bytes(UTF-8)

# announce utf-8
# -*- coding: utf-8 -*-

# format string
'hello %s' % 'world'
'hellos {0}'.format('world')
world = 'world'
f'hello {world}'

# list
array = []
len(array)
array[0]
array[-2]
# insert before index
array.insert(0,'hello')
array.pop()
array.pop(3)
array = ['abc' , 3 , world]
array.append(4)
# slice works for list/tuple
# array[:3] == array[0:3] = [0,3)
# array[-2:] == array[-2:-1]
# array[:10:2] specify int increment

# tuple
chars = ('a', 'b', 'c')
chars = ('a',) # one element tuple
chars = ('a', ['a', 'c']) # tuple could also be variable

# if and else and elif
if 1 == 1:
    pass
elif 2 == 2:
    pass
else:
    pass

# for recycle
for i in chars:
    print(i)
for i in [1,2,3]:
    pass
# range(3) == range(0,3) ?= list(range(0,3)) == [0,3) = [0,1,2]

# while recycle
i = 1
while True:
    if i%2 == 0:
        break
    else:
        continue

# dict => map
dic = {'a':65, 'b':66, 'c':67} # key must be const, cause dic use key's hash to store data
dic['a']
'a' in dic
dic.get('a', -1) # specify a default value
dic.pop('a') 

# set
s = set([1,2,3]) # only initial way, will remove repeat element by default
s.add(4)
s.remove(4)
s2 = set([5,6])
s & s2
s | s2

# const and variable
a = 'abc'
a.replace('a', 'A') # return 'Abc' however a == 'abc' still

# function rename
a = abs
a(1) == 1

# function
def myFun():
    pass # isinstance(x, (int, float))   x == int or float

def fun2():
    return 1,3     # actually 1,3  == (1,3)
a,b = fun2()       # return multiple value by using tuple

def fun3(x, n=3):
    return x*3    # set a default value for function
 
# >>> def add_end(L=[]):
# ...     L.append('END')
# ...     return L
# ...
# >>> add_end()
# ['END']
# >>> add_end()
# ['END', 'END']

# default value must be a const, either it will be recycle in function, cause it will store value

# variable argument
def cal(*numbers):
    pass
cal(1,2,3,4)
cal(2,3,4)
cal(*[1,2,3])

def person(name, age, **kw):
    print(kw.keys())
    print(kw.values())
data = {'job': 'none', 'plate':'川a123455'}
person('mike', 29, **data)

def person(name, age, *, job, plate): # specify what **kw could be transfer to function
    pass

# specify item if supports iter
from collections.abc import Iterable
isinstance('abxc', Iterable)

for index,value in enumerate(['a','b','c']):
    print(index, value)

# list comprehensions
[x * x for x in range(1,11)]
[x * y for x in range(1,3) for y in range(0,2)] # 4 values
# expression and condition
[x if x>>2 == 0 else -x for x in range(4)]
[x for x in range(4) if x>>2 ==0]

# generator
l = (x * x for x in range(1,11))
next(l)
# generator function
def odd():
    print('step 1')
    yield 1             # it will return 1 and stop 
    print('step 2')     # after call next(), function will continue here
    yield(3)
    print('step 3')
    yield(5)

next(odd()) == next(odd())
odds = odd()
next(odds) != next(odds)

# iterator and iterable
# iterable !=  iterator
# one could be used in for is iterable, one could call next() is iterator

# function could be argument
def add(x, y, f):
    return f(x) + f(y)
add(5,-3, abs)

# map/reduce
# 映射/子函数迭代
# map(function, iterable), return a iterator

from functools import reduce
# def add(x, y):
#     return x + y
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# lambda 匿名函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def f(s):
    return DIGITS[s]
reduce(lambda x, y: x*10+y, map(f, '123'))

# filter
# filter(is_odd, [list]), raeturn iterator

# sorted
a = [1,3,5,-6,-4]
sorted(a, key=abs, reverse=True)

# python can return a function
# it's Closure 闭包
# 闭包直到调用时，才会开始计算
# function itself is just an Object, It can act as argument/return value

# annouce outer element
def inc():
    x = 0
    def fn():
        nonlocal x # use the x out of fn() // x isn't argument
        x = x + 1
        return x
    return fn

# lambda function
def build(x, y):
    return lambda: x * x + y * y

# decorater
# 在代码运行期间动态增加功能的方式
# newFunc = decorate(oldFunc)
# decorator may have other arguments except function argument

# @functools.wraps(func)
# to restore the origin info about func, including __name__
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# quickly set up a new function with some default value
int2 = functools.partial(int, base=2)

# module
# heirachy
# mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py
# __init__.py will make the folder -> a module

' a test module '

__author__ = 'whoami'

# isinstance() / type()
# isinstance() will get father class 
# dir() return all elements. hasattr(obj, 'x', defaultRetureValue)

# dynamic add attrs to class/object
class Student(object):
    pass
s = Student()
# dynamic name attr
s.name = "Mike"
# dynamic method attr
from types import MethodType
# s.set_age() = MethodType(function, object)
# or Student.set_age = set_age    # differ from Student.set_age()

class Student(object):
# limit what attrs support, only limit for itself, not working for child class
    __slots__ = ('name', 'age')   

# limit the ability to change value
class Student(object):

    @property                  # announce score => score(), but object.score still support
    def score(self):
        return self._score

    @score.setter              # score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # f(x) can be called by Student or Student's object
    # staticmethod don't need self
    # staticmethod function is staticmethod object
    @staticmethod
    def f(x):
        print(x)
    
    # classmethod need cls, it can be called by class or object
    @classmethod
    def g(cls, x):
        print(cls, x)

# types.FunctionType
# type(abs)==types.BuiltinFunctionType
# type(lambda x: x)==types.LambdaType
# type((x for x in range(10)))==types.GeneratorType

# mixin
# add a parent class for a child class

# __str__() used for print function
# __repr__() used for developper to show identity
# you can make __repr__ = __str__ 

# __iter__() return a iterable which has __next__() 

# __getitem__() make object support object[] or object[:]
# you must specify how to handle with (int or slice)
# There is __setitem()__ / __delitem()__ to make your own class work like list/dic

# __call()__ make object itself callable
object()

# enum
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 
                       'May', 'Jun', 'Jul', 'Aug', 
                       'Sep', 'Oct', 'Nov', 'Dec'))
# enum member's value start from 1
# or you can specify the value
from enum import unique
@unique              # help determine unique
class Weekday(Enum):
    Sun = 0          # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# evaluate false
# []/set()/{}/None/False/emptyStr/0
# user-defined __bool__ or __eq__ of class

# global/nonlocal
# 在函数/闭包里对变量赋值时，python会认为这个变量是局部变量
# 闭包里使用nonlocal而非global

# test/unittest
# __init__.py make .py into package
# test should be a package located in the same file hierarchy
import unittest
import sys
class Test(unittest.TestCase):
    # test case should start with test
    def test_a(self):
        # ret = myFunc()
        self.assertEqual()
        self.assertTrue()
        with self.assertRaises(ValueError):
            print('h')
    
    # use decorator to skip test under some circumstance
    @unittest.skipIf(sys.platform == "win32")
    def test_b(self):
        pass

    @unittest.skipIf(sys.version_info < (3,7 ))
    def test_c(self):
        pass

# specify what test to run 
# python -m unitest test.test_file.test_class.test_func

# asyncio
# IO bound task prefer
# only one task is running
# coroutine
# coroutine function -> coroutine object --(event loop)--> task --> run
# await will also return running authority to event loop
# asyncio.create_task() will not return autority back to event loop 
# asyncio.gather() could gather coroutine and wait their return value into a list

# await
# await = yield from


# try:
#     pass
# else:
#     pass
# finally:
#     pass

# use finally to release resource despite of exception
# sy s.exit(0) -> raise a exception
# ctrl-c == sigint
# finally don't run when sigkill, sigterm and os._exit(0)

# from package import * 
# it will not import _fun (start with one _)
# _func (weak private)
# __func (relatively strong private) == _class__func
# __func__ magic method
