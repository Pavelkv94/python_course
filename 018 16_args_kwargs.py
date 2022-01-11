a, b, c = 10, 20, 30
a, b, c = ['Строка', 20, 3.14,]
a, b, c = ['Строка', 20, 3.14, 10]
a, b, c = ['Строка', 10, 20, 3.14, 10, 'Текст', 11, 22, 34]
a, *b, c = ['Строка', 10, 20, 3.14, 10, 'Текст', 11, 22, 34]
a, b, *c = ['Строка', 10, 20, 3.14, 10, 'Текст', 11, 22, 34]
*a, b, c = ('Строка', 10, 20, 3.14, 10, 'Текст', 11, 22, 34)
*a, b, c = 'Hello world'
*a, b, c = [1,2]
*a, b, c = [1]


print(a)
print(b)
print(c)

s = [4,10]
print(list(range(1,6)))
print(list(range(*s)))

def func(a,b,c,d):
	print(a,b,c,d)

a = ('hello', True, 78, [3,4,5])	
func(*a)
def func(*args):
	print(sum(args)*0.06)

func(1, 33,11444,1111,4444,)
func(1, 33,11444,1111,4444,1000, 4434, 4444, 6666)



def func(**kwargs):
	print(kwargs)

func(a=1, b=2, c=3)

def func(*args,**kwargs):
	print(args)
	print(kwargs)

func(1,2,3,4,5, a=1, b=2, c=3)