Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sumlist(n):
	f=[]
	for x in range(1,n+1):
		f.append(x)
		b=sum(f)
	return b

>>> sumlist(100)
5050
>>> sumlist(10)
55
>>> sumlist(5)
15
>>> sumlist(20)
210
>>> sumlist(2)
3
>>> sumlist(9)
45
>>> 
>>> 
>>> def functionName(lists,i):
	d=[]
	e=[]
	for x in lists:
		if x%i==0:
			d.append(x)
		else:
			e.append(x)
	print(d)
	print(e)

	
>>> a=[1,2,3,4,5]
>>> functionName(a,2)
[2, 4]
[1, 3, 5]
>>> def functionName(lists,i):
	d=[]
	e=[]
	for x in lists:
		if x%i==0:
			d.append(x)
		else:
			e.append(x)
	print("The numbers divisible by the integer are in the following list: "d)
	print("The numbers not divisible by the integer are in the following list: "e)
	

>>> 
