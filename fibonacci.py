Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
	print(a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
>>> a,b = 0,1
>>> while a < 55
SyntaxError: invalid syntax
>>> a,b = 0,1
>>> while a  < 55:
	print (a)
	a,b = b, a+b

	
0
1
1
2
3
5
8
13
21
34
>>> a,b = 0,1
>>> while a < 17711:
	print (a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
>>> 