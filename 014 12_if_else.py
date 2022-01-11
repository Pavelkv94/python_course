if True:
	print('true')
elif True:
	print('true')
else:
	print('else')


print('Введите число от 1 до 10')
x = int(input())

if x < 4:
    print('число меньше четырех')
elif x == 5:
    print('число равно 5')
elif 10 > x > 6:
    print('число больше 6')
else:
    print('??? введите корректное число')


3
5
7
11

print('Введите число от 1 до 10')
x = int(input())

if x < 4:
    print('число меньше четырех')
elif x == 5:
    print('число равно 5')
elif 10 > x > 6:
    if 8 > x > 6:
    	print('число равно 7')
    elif 9 > x > 7:
    	print('число равно 8')
    else:
    	print('число равно 9')
else:
    print('??? введите корректное число')