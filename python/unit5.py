Python 3.8.4 (v3.8.4:dfa645a65e, Jul 13 2020, 10:45:06) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 1-1
0
>>> 2*2
4
>>> 5/2
2.5
>>> # // floor division
>>> 4//2
2
>>> 4/2
2.0
>>> 5%2
1
>>> 2**3
8
>>> 2**10
1024
>>> int(2.2)
2
>>> int('10')
10
>>> int('10.3')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int('10.3')
ValueError: invalid literal for int() with base 10: '10.3'
>>> # only integer accepts
>>> type(10)
<class 'int'>
>>> divmod(5,2)
(2, 1)
>>> a,b=divmod(5,2)
>>> print(a,b)
2 1
>>> 0b110
6
>>> 0o10
8
>>> 0xf
15
>>> 3.5+2.1
5.6
>>> 4.3-2.7
1.5999999999999996
>>> 1.5*3.1
4.65
>>> 5.5/3.1
1.7741935483870968
>>> float(5)
5.0
>>> float('5.3')
5.3
>>> type(3.5)
<class 'float'>
>>> 1.2+1.3j
(1.2+1.3j)
>>> #complex number
>>> complex(1.2,1.3)
(1.2+1.3j)
>>> 35+1*2
37
>>> (35+1)*2
72
>>> float(10//3)
3.0
>>> float(10/3)
3.3333333333333335
>>> int(10/3)
3
>>> 