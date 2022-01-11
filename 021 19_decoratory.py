def tagMaker(func):
    def wrapper(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return wrapper


# @tagMaker
def printText(text):
    print(text)


tag1 = tagMaker(printText)
tag1('hello')
#printText('Hello World')

def tagMaker(func):
	def wrapper(*args, **kwargs):
		print('<div>')
		res = func(*args, **kwargs)
		print('</div>')
		return res
	return wrapper

@tagMaker
def printText(text):	
	print(text)

printText('Hello World')


import time
import datetime


def recTime(func):
	def wrapper(*args, **kwargs):
		start = datetime.datetime.now()
		func(*args, **kwargs)
		bone = datetime.datetime.now() - start
		print(f'Функция завершилась за {bone} сек')
	return wrapper


import time
import datetime

def recTime(func):
	def wrapper(*args, **kwargs):
		start = datetime.datetime.now()
		func(*args, **kwargs)
		bone = datetime.datetime.now() - start
		print(f'Функция завершилась за {bone} сек')
	return wrapper

def tagMaker(func):
	def wrapper(*args, **kwargs):
		print('<div>')
		func(*args, **kwargs)
		print('</div>')
	return wrapper

# @tagMaker
@recTime
def printText(text):
    time.sleep(3)
    print(text)

# t1 = tagMaker(printText)
# t1('hello')
printText('Hello World')

# from functools import wraps

def tagMaker(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        '''Декоратор который добавляет див
        :param func:
        :return:
        '''
        print('<div>')
        res = func(*args, **kwargs)
        print('</div>')
        return res
    return wrapper

@tagMaker
def printText(*args):
    ''' Функция принт текст
    :param args:
    :return:
    '''
    print(args)

printText('Hello World')

help(printText)