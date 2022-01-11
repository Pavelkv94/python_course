x = 'Alex'
print(x)
y = "Some text 123"
print(y)
z = 'Some 'long' text'
z = "Some 'long' text"
print(z)

x = "Some 'long', and 'awesome' text"
print(x)

x = "Some \'long\', and \'awesome\' text"
print(x)
y = 'C:\\Users\\dell\\Desktop\\Py_lesson'
print(y)
z = r'C:\Users\dell\Desktop\Py_lesson'
print(z)
x = 'some long text \nand new string \nand new string \nand new string'
print(x)

text = str('hello world')
print(text)
print(text[0])
print(text[0]+text[1])
print(text[-1]+text[1])
print(text[6:]+text[1])
print(text[6:]+' '+text[:6])
print(text[6:8])
print(text[::1])
print(text[::2])
x = 'hello'
y = 'world'
print(x + ' ' + y)
print('%s %s' % (x, y))
print('{} {}'.format(x, y))
z = 'text '
print(z*6)