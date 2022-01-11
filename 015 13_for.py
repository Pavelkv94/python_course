for x in range(1, 6):
    print(x)

new_list = []

for x in range(1, 16):
    new_list.append(x)

print(new_list)


numbers = [1,2,3,4,5]
print(numbers)

for i in numbers:
	print(i)

for i in numbers:
	print(i*i)

numbers = range(1,6)
for i in numbers:
	print(i)

numbers = range(1,16)
for x in numbers:
	print(x)

for i in range(1,16):
	print(i)

for i in range(1,6):
	if i % 2 == 0:
		print(f'{i} четное число')
	else:
		print(f'{i} нечетное число')

numbers = [1,2,3,4,5]
для индекса
for x in numbers:
	y = numbers[x]
print(y)

for x, item in enumerate(numbers):
	numbers[x] += 10
print(numbers)

name = 'Alex Jhonson'
for x in name:
	print(x)

for _ in range(5):
	print('Ошибка!')

some_tuple = (11, 'Alex', 3.14)
for x in some_tuple:
	print(x)

some_list = [('John', 22), ('Alex', 33), ('Artem', 44)]
for (name, age) in some_list:
	print(f'{name} is {age} years old')

some_dict = {
	'Alex': 111,
	'Maxim': 222,
	'Anna': 333
}
for x in some_dict:
	print(x)
for x in some_dict.items():
	print(x)
print(type(x))		
for x, y in some_dict.items():
	print(f'Ключ {x} Значение {y}')	
for value in some_dict.values():
	print(value)

# f_list = [2,4,-5,6,8,-2]
# s_list = [2,-6,8,3,5,-2]

# pairs = []
# for x in f_list:
# 	for y in s_list:
# 		cur_sum = x + y
# 		if cur_sum == 0:
# 			pairs.append((x,y))
# print(pairs)


