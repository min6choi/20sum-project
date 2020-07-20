Python 3.8.4 (v3.8.4:dfa645a65e, Jul 13 2020, 10:45:06) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> x
10
>>> y='Hello,world!'
>>> y
'Hello,world!'
>>> type(x)
<class 'int'>
>>> type(y)
<class 'str'>
>>> x,y,z=10,20,30
>>> x
10
>>> y
20
>>> z
30
>>> x,y,z=10,20
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x,y,z=10,20
ValueError: not enough values to unpack (expected 3, got 2)
>>> x=y=z=10
>>> x
10
>>> y
10
>>> z
10
>>> x,y=10,20
>>> x,y=y,x
>>> x
20
>>> y
10
>>> x=10
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=None
>>> print(x)
None
>>> a=10
>>> b=20
>>> c=a+b
>>> c
30
>>> a=10
>>> a+20
30
>>> a
10
>>> a=10
>>> a=a+20
>>> a
30
>>> a=10
>>> a+=20
>>> a
30
>>> # a+20=30=a
>>> x=-10
>>> +x
-10
>>> =-x
SyntaxError: invalid syntax
>>> -x
10
>>> input()
Hello, world!
'Hello, world!'
>>> x=input()
Hello, world!
>>> x
'Hello, world!'
>>> x=input('input the letter:')
input the letter:Hellow, world!
>>> x
'Hellow, world!'
>>> a=input('input the first number:')
input the first number:10
>>> b=input('input the second number:')
input the second number:20
>>> print(a+b)
1020
>>> type(a)
<class 'str'>
>>> a=int(input('input the first number:'))
input the first number:10
>>> b=int(input('input the second number:'))
input the second number:20
>>> print(a+b)
30
>>> a,b=input('input two letters:').split()
input two letters:Hello Python
>>> print(a)
Hello
>>> print(b)
Python
>>> a,b=input('input two letters:').split()
input two letters:10 20
>>> print(a+b)
1020
>>> a,b=input('input two letters:').split()
input two letters:10 20
>>> a=int(a)
>>> b=int(b)
>>> print(a+b)
30
>>> a,b=input('input two letters:').split()
input two letters:10 20 
>>> print(int(a)+int(b))
30
>>> a,b=map(int,input('input two letters:').split())
input two letters:10 20 
>>> print(a+b)
30
>>> a,b=map(int, input('input two numbers:').split(','))
input two numbers:10 20 
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a,b=map(int, input('input two numbers:').split(','))
ValueError: invalid literal for int() with base 10: '10 20 '
>>> a,b=map(int,input('input two numbers:').split(','))
input two numbers:10,20
>>> print(a+b)
30
>>> 