print(type(list))
help(list)

new_list = [1, 2, 3]
new_list.append(4)
print(new_list)

delete all

class CommentFromWebsite():
	"""Коментарий с сайта"""
	def __init__(self, data, text, likes):
		self.data = data
		self.text = text
		self.likes = likes

создаём экземпляр класса
new_coment = CommentFromWebsite('11/02/20', 'Первый коментарий', '11')
print(type(new_coment))
print(new_coment.data)
print(new_coment.text)





	def showComment(self):
			print(f'Комментарй с сайта написан {data} \n текст коментария {text} \n лайков {likes}')



class CommentFromWebsite():
	"""Коментарии с сайта"""
	def __init__(self, data, text, likes):
		"""Инициализируем атрибуты класса"""
		self.data = data
		self.text = text
		self.likes = int(likes)

	def showComment(self):
		"""Вывести коментарий в консоль"""
		print(f'\nКомментарий с сайта,\n дата:  {self.data},\n текст коментария: {self.text}\n лайков: {self.likes}')

	def changeLikes(self):
		"""прибавить счётчик лайков""" добавить инт в селф
		self.likes = self.likes + 1

	def changeComment(self, new_text):
		"""Изменить текст коментария"""
		self.text = new_text


new_coment = CommentFromWebsite('11/02/20', 'Первый коментарий', '11')

print(type(new_coment))

print(new_coment.data)
print(new_coment.text)

new_coment.text = "Измененный коментарий"
print(new_coment.text)

new_coment2 = CommentFromWebsite('22/02/20', 'Второй коментарий', '22')


new_coment.showComment()
new_coment2.showComment()

new_coment2.changeLikes() 
new_coment2.showComment()
new_coment2.changeLikes() 
new_coment2.showComment()

new_coment2.changeComment('Новый')
new_coment2.showComment()

class CommentFromWebSite():
    """Комментарии с сайта"""
    def __init__(self, data, text, likes):
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComment(self):
        """Вывести комментарий в консоль"""
        print(f'\nКомментарий с сайта, \n дата: {self.data},'
              f'\n текст: {self.text}, лайков: {self.likes}')

    def changeLikes(self):
        '''Прибавляет один лайк'''
        self.likes = self.likes + 1

    def changeComment(self, new_text):
        """Изменение комментария"""
        self.text = new_text


new_coment = CommentFromWebSite('11/02/20', 'Первый!', '11')
new_coment2 = CommentFromWebSite('22/03/19', 'Второй!', '5')

new_coment2.showComment()
new_coment2.changeLikes()
new_coment2.changeLikes()
new_coment2.showComment()
new_coment.showComment()
new_coment.changeComment('Новый!!!')
new_coment.showComment()
