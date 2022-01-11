map(func, iterable)

def map(func, iterable):
	for i in iterable:
		yield func(i)


 
def sq(x):
	return x**2

a = [-2, -1, 5, 7, 3]

wait 10 sek

b = map(sq, a)
print(b)

c = list(map(sq, a))

print(c) 




a = ['hello', 'abc', 'good']

b = list(map(str.upper, a))
print(b)



def is_adult(age):
	return age >= 18


age = [11, 20, 18, 33, 14, 12]	

print(filter(is_adult, age))
print(list(filter(is_adult, age)))


def is_adult(age):
	return age >= 18

is_adult = lambda age: age >= 18

print(list(filter(is_adult, age)))

age = [11, 20, 18, 33, 14, 12]

print(list(filter(lambda age: age >= 18, age)))