Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=range(99,109)
>>> b=[x*x for x in a]
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> squares b=[x*x for x in a]
SyntaxError: invalid syntax
>>> squares=[x*x for x in a]
>>> a
range(99, 109)
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> a
range(99, 109)
>>> 
>>> 
>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> b=[1,2,3,4,5,6,7,8,9]
>>> a[0:4]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a=[0:2]
SyntaxError: invalid syntax
>>> a=[1:2]
SyntaxError: invalid syntax
>>> a[0]
[1, 2, 3]
>>> a[1]
[4, 5, 6]
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a[2]
[7, 8, 9]
>>> b[0:2]
[1, 2]
>>> 
>>> b[0:3]
[1, 2, 3]
>>> b[5:7]
[6, 7]
>>> b[4:7]
[5, 6, 7]
>>> b[-4]
6
>>> b=[-1:-4]
SyntaxError: invalid syntax
>>> b[-1]
9
>>> b[7:11]
[8, 9]
>>> 
>>> 
>>> 
>>> a=[1,4,9,...........81]
SyntaxError: invalid syntax
>>> a=[1,4,9...81]
SyntaxError: invalid syntax
>>> a=[1,4,9,81]
>>> 
>>> square=[1,4,9,81]
>>> a=[[1,2,3],[4,5,6],[7,8,9]]




















