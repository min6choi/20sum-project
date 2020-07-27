Python 3.8.4 (v3.8.4:dfa645a65e, Jul 13 2020, 10:45:06) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # make a list
>>> a = [38, 21, 53, 62, 19]
>>> a
[38, 21, 53, 62, 19]
>>> # indivisual number is called
>>> person = ['James', 17, 175.3, True]
>>> person
['James', 17, 175.3, True]
>>> a = []
>>> a
[]
>>> b = list()
>>> b
[]
>>> range(10)
range(0, 10)
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = list(range(5, 12))
>>> b
[5, 6, 7, 8, 9, 10, 11]
>>> c = list(range(-4, 10, 2))
>>> c
[-4, -2, 0, 2, 4, 6, 8]
>>> d = list(range(10, 0, -1))
>>> d
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> # make a tuple
>>> a = (38, 21, 53, 62, 19)
>>> a
(38, 21, 53, 62, 19)
>>> a = 38, 21, 53, 62, 19
>>> a
(38, 21, 53, 62, 19)
>>> person = ('james', 17, 175.3, True)
>>> person
('james', 17, 175.3, True)
>>> # make a tuple
>>> # with range
>>> a = tuple(range(10))
>>> a
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> b = tuple(range(5,12))
>>> b
(5, 6, 7, 8, 9, 10, 11)
>>> c = tuple(range(-4, 10, 2))
>>> c
(-4, -2, 0, 2, 4, 6, 8)
>>> (38)
38
>>> (38,)
(38,)
>>> 38,
(38,)
>>> a = [1,2,3]
>>> tuple(a)
(1, 2, 3)
>>> b = (4,5,6)
>>> list(b)
[4, 5, 6]
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> tuple('Hello')
('H', 'e', 'l', 'l', 'o')
>>> a, b, c = [1, 2, 3]
>>> print(a,b,c)
1 2 3
>>> d, e, f = (4,5,6)
>>> print(d,e,f)
4 5 6
>>> x = [1, 2, 3]
>>> a,b,c = x
>>> print(a,b,c)
1 2 3
>>> y = (4,5,6)
>>> d,e,f = y
>>> print(d,e,f)
4 5 6
>>> input().split()
10 20 
['10', '20']
>>> x = input().split()
10 20 
>>> a, b = x
>>> print(a,b)
10 20
>>> 