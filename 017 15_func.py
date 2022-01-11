print()
type()
len()
sqrt()
round()
upper()

# printText()
def printText():
	print('Hello world')

printText()
printText()
printText()

r = 10
s = 3.1414*(r**2)
print(s)

def sqRing(r):
	s = 3.1415*(r**2)
	print(s)
	# return s
sqRing(20)
sqRing(33)
sqRing(70)

def sqRing(r):
	s = 3.1415*(r**2)
	# print(s)
	return s

print(sqRing(20))	

x = sqRing(20)
print(x) 

a = 30 
print(sqRing(a))

def getSquare(w, h):
	return 2*(w+h)
print(getSquare(5, 5))


def printText(msg, end='!'):
	print(msg+end)
printText('Text')
printText('Text', '?')

def printText(msg, end='!', sep=': '):
	print('Message'+sep+msg+end)
printText('Text')
printText('Text', '?')
printText('Text', '?', ' ')
printText('Text', sep =' ')


def getSquare(w, h):
	return 2*(w+h), w*h
print(type(getSquare(5, 5)))



some_argument = True

if some_argument:
	def someFunc(x,y,z):
		return x+y+z
else:
	def someFunc(a,b,c):
		x = a+b/c
		print(x)

someFunc(10, 20, 30)	



def function(a, b, c):
    '''
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a+b+c


help(function)	
# import math

# def function(a, b, c):
# 	p = (a+b+c)/2
# 	s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# 	print(s)




