Python 3.8.4 (v3.8.4:dfa645a65e, Jul 13 2020, 10:45:06) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> 30 in a
True
>>> 100 in a
False
>>> 100 not in a
True
>>> 30 not in a
False
>>> 43 in (38, 76, 43, 62, 19)
True
>>> 1 in range(10)
True
>>> 'P' in 'Hello, Python'
True
>>> a = [0, 10, 20, 30]
>>> 
>>> b = [9, 8, 7, 6]
>>> a + b
[0, 10, 20, 30, 9, 8, 7, 6]
>>> range(0, 10) + range(10, 20)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    range(0, 10) + range(10, 20)
TypeError: unsupported operand type(s) for +: 'range' and 'range'
>>> list(range(0, 10)) + list(range(10, 20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> tuple(range(0, 10)) + tuple(range(10, 20))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> 'Hello,' + 'world!'
'Hello,world!'
>>> 'Hello,' + 10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    'Hello,' + 10
TypeError: can only concatenate str (not "int") to str
>>> 'Hello,' + str(10)
'Hello,10'
>>> 'Hello,' + str(1.5)
'Hello,1.5'
>>> [0, 10, 20, 30] * 3
[0, 10, 20, 30, 0, 10, 20, 30, 0, 10, 20, 30]
>>> range(0, 5, 2) *
SyntaxError: invalid syntax
>>> range(0, 5, 2) * 3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    range(0, 5, 2) * 3
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> list(range(0, 5, 2)) * 3
[0, 2, 4, 0, 2, 4, 0, 2, 4]
>>> tuple(range(0, 5, 2)) * 3
(0, 2, 4, 0, 2, 4, 0, 2, 4)
>>> 'Hello,' * 3
'Hello,Hello,Hello,'
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> len(a)
10
>>> b = (38, 76, 43, 62, 19)
>>> len(b)
5
>>> len(range(0, 10, 2))
5
>>> hello = 'Hello, world!'
>>> len(hello)
13
>>> a = [38, 21, 53, 62, 19]
>>> a[0]
38
>>> a[2]
53
>>> a[4]
19
>>> b = (38, 21, 53, 62, 19)
>>> b[0]
38
>>> r = range(0, 10, 2)
>>> r[2]
4
>>> hello = 'Hello, world!'
>>> hello[7]
'w'
>>> a = [38, 21, 53, 62, 19]
>>> a
[38, 21, 53, 62, 19]
>>> a[-1]
19
>>> a[-5]
38
>>> b = (38, 21, 53, 62, 19)
>>> b[-1]
19
>>> r = range(0, 10, 2)
>>> r[-3]
4
>>> hello = 'Hello, world!'
>>> hello[-4]
'r'
>>> a = [38, 21, 53, 62, 19]
>>> len(a)
5
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a[5]
IndexError: list index out of range
>>> a[4]
19
>>> a[len(a) = 1]
SyntaxError: invalid syntax
>>> a[len(a) - 1]
19
>>> a = [0, 0, 0, 0, 0]
>>> a[0] = 38
>>> a[1] = 21
>>> a[2] = 53
>>> a[3] = 62
>>> a[4] = 19
>>> a
[38, 21, 53, 62, 19]
>>> a[4]
19
>>> b = (0, 0, 0, 0, 0)
>>> b[0] = 38
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    b[0] = 38
TypeError: 'tuple' object does not support item assignment
>>> r = range(0, 10, 2)
>>> r[0] =3
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    r[0] =3
TypeError: 'range' object does not support item assignment
>>> a = [38, 21, 53, 62, 19]
>>> del a[2]
>>> a
[38, 21, 62, 19]
>>> b = (38, 21, 53, 62, 19)
>>> del b[2]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    del b[2]
TypeError: 'tuple' object doesn't support item deletion
>>> r = range(0, 10, 2)
>>> del r[2]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    del r[2]
TypeError: 'range' object doesn't support item deletion
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[0:4]
[0, 10, 20, 30]
>>> a[0:10]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[1:1]
[]
>>> a[1:2]
[10]
>>> a[4:7]
[40, 50, 60]
>>> a[4:-1]
[40, 50, 60, 70, 80]
>>> a[2:8:3]
[20, 50]
>>> a[2:9:3]
[20, 50, 80]
>>> a[:7]
[0, 10, 20, 30, 40, 50, 60]
>>> a[7:]
[70, 80, 90]
>>> a[:]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[:7:2]
[0, 20, 40, 60]
>>> a[7::2]
[70, 90]
>>> a[::2]
[0, 20, 40, 60, 80]
>>> a[::]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[5:1:-1]
[50, 40, 30, 20]
>>> a[::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[0:len(a)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[:len(a)]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> b= (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
>>> b[4:7]
(40, 50, 60)
>>> b[4:]
(40, 50, 60, 70, 80, 90)
>>> b[:7:2]
(0, 20, 40, 60)
>>> r = range(10)
>>> r
range(0, 10)
>>> r[4:7]
range(4, 7)
>>> r[4:]
range(4, 10)
>>> r[:7:2]
range(0, 7, 2)
>>> list(r[:7:2])
[0, 2, 4, 6]
>>> hello = 'Hello, world!'
>>> hello[2:9]
'llo, wo'
>>> hello[2:]
'llo, world!'
>>> hello[:9:2]
'Hlo o'
>>> range(10)[slice(4, 7, 2)]
range(4, 7, 2)
>>> range(10).__getitem__(slice(4, 7, 2))
range(4, 7, 2)
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> s = slice(4, 7)
>>> a[s]
[40, 50, 60]
>>> r = range(10)
>>> r[s]
range(4, 7)
>>> range(4, 7)
range(4, 7)
>>> hello = 'Hello, world!'
>>> hello[s]
'o, '
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> a[2:5] = ['a', 'b', 'c']
>>> a
[0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90]
>>> a[2:5] = ['a']
>>> a
[0, 10, 'a', 50, 60, 70, 80, 90]
>>> a[2:5] = ['a', 'b', 'c', 'd', 'e']
>>> a
[0, 10, 'a', 'b', 'c', 'd', 'e', 70, 80, 90]
>>> a[2:8:2] = ['a', 'b', 'c']
>>> a
[0, 10, 'a', 'b', 'b', 'd', 'c', 70, 80, 90]
>>> del a[2:5]
>>> a
[0, 10, 'd', 'c', 70, 80, 90]
>>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> del a[2:8:2]
>>> a
[0, 10, 30, 50, 70, 80, 90]
>>> 