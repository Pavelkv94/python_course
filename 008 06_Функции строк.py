x = 'some long and awesome TEXT'
print(len(x)) 
print(x[len(x)-1])
print(x[len(x)-4:len(x)])
print(x.count('o'))
print(x.find('a'))
print(x.find('o'))
print(x.find('o'))
print(x.find('o', 3, 7))
print(x.find('o', 7))
print(x.find('and'))
print(x.find('TEXT'))
print(x.find('abc'))
print(x.capitalize())
print(x.upper())
print(x.lower())
print('Old text: '+x)
upper_cased = x.upper()
lower_cased = x.lower()
print(upper_cased.isupper())
print(lower_cased.islower())
print(x.isupper())
print(x.islower())

print('xxx777'.isalnum())
print('xxx777!'.isalnum())
print('xxx777'.isalpha())
print('xxx'.isalpha())
print('   '.isspace())
print(''.isspace())
empty_string = ''
print(empty_string == '') #true
print(empty_string == ' ')  #false
print(empty_string.strip(' ') == '') #true
empty_string = ' '
print(empty_string.strip() == '')

empty_string = '' 
if not empty_string:
	print('not empty')
else:
	print('empty')

x = str('hello')
print(x.startswith('he'))
print(x.endswith('lo'))
split = x.split('l')
print(type(split))
print(split)
split = x.split('e')
print(split)
some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')
print(separated_data)
print(separated_data[3])
