a = 10
API_KEY = '123qwe456'

def nfunc(x):
	a = 5
	for i in range(x):
		n=i+1
		print(n)

print(n)
nfunc(5)

def nfunc(x):
	global a
	a = 5
	for i in range(x):
		n=i+1
		print(n)


nfunc(5)


name = 'Anna'

def print_1():
	print('Первая функция, имя: ' + name)
	def print_2():
		name = 'alex'
		print('Вторая функция, имя: ' + name)
	print_2()


print_1()

 