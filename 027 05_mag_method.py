class New():
	def __init__(self, name):
		self.name = name


	def __str__(self):
	# def __repr__(self):
		return self.name
		

new_obj = New('Иван')
print(new_obj)