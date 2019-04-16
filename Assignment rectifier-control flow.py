Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> b=[]
>>> for x in range(0,100):
	if x%9 == 0 and x%11 == 0:
		a.append(x)
		b.append(x)
	elif x%9 == 0:
		a.append(x)
	elif x%11 == 0:
		b.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 
>>> 
>>> def hello():
	print("Hello AkiraChix")

	
>>> hello()
Hello AkiraChix
>>> 
>>> d=[]
>>> f=34,45,76,98]
SyntaxError: invalid syntax
>>> hello()
Hello AkiraChix
>>> 
>>> def hello("name"):
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> def hello(name):
	print
