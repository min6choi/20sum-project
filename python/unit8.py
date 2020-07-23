Python 3.8.4 (v3.8.4:dfa645a65e, Jul 13 2020, 10:45:06) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3>1
True
>>> 10 == 10
True
>>> 3<1
False
>>> 10 != 5
True
>>> 10 != 10
False
>>> 'Python' == 'Python'
True
>>> 'Python' == 'Python'
True
>>> 'Python' == 'python'
False
>>> 'Python' != 'python'
True
>>> 10>20
False
>>> 10<20
True
>>> 10>=10
True
>>> 10<-10
False
>>> 1==1.0
True
>>> 1 is 1.0
False
>>> 1 is not 1.0
True
>>> id(1)
4465703616
>>> id(1.0)
4492458224
>>> a = -5
>>> a is -5
True
>>> a = -6
>>> a is -6
False
>>> a == -6
True
>>> # Do not use 'is' when you compare with the number
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not False
True
>>> not True and False or not False
True
>>> False and False or True
True
>>> False or True
True
>>> 10 == 10 and 10 != 5
True
>>> 10 > 5 or 10 < 3
True
>>> not 10 > 5
False
>>> not 1 is 1.0
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(1.5)
True
>>> bool('False')
True
>>> #except 0 every integer is True
>>> bool(' ')
True
>>> bool('')
False
>>> bool("")
False
>>> #short-circuit evalution
>>> print(False and True)
False
>>> print(False and False)
False
>>> print(True or True)
True
>>> print(True or False)
True
>>> True and 'Pythone'
'Pythone'
>>> False and 'Pythone'
False
>>> 0 and 'Pythone'
0
>>> # 0 is False
>>> False or 'Python'
'Python'
>>> 0 or False
False
>>> 6 == 2 * 3
True
>>> 4 != 2 + 2
False
>>> 2 * 3 is 3 + 3
True
>>> 8 is 4 * 2.0
False
>>> 5 is 6 - 1.1
False
>>> a = 10
>>> b = 20
>>> a == 10 or b == 10
True
>>> a >= 10 and b < 30
True
>>> not a == 10
False
>>> b != 20 or a != 10
False
>>> not b != 20 and a>5
True
>>> Korean = 92
>>> english = 47
>>> mathematics = 86
>>> science = 81
>>> print(Korean >= 50 and english >= 50 and mathematics >= 50 and science >=50)
False
>>> 