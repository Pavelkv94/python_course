# в другом файле
# from auto_62 import calculate
# print(calculate(5, 10))


class ElectroCar(CarsClass):
	"""Класс электрокаров"""
	def __init__(self, brand, model, year, probeg):
		super().__init__(brand, model, year, probeg)
		self.battery = 100 #потом удалить

	def description_battery(self):
		'''Выводит информацию о батарее'''
		print('Этот автомобиль имеет мощьность ' + str(self.battery) + ' %')

	def showCar(self):
		"""Показать информацию о машине"""
		print(f'{self.brand}, {self.model}')




# в другом файле
a = 100

def calculate(a, b):
	return a + b


class CarsClass():
	"""Класс автомобилей"""
	def __init__(self, brand, model, year, probeg):
		"""Инициализация атрибутов"""
		self.brand = brand
		self.model = model
		self.year = year
		self.probeg = int(probeg)
	
	def showCar(self):
		"""Показать информацию о машине"""
		print(f'{self.brand}, {self.model}, {self.year} год, {self.probeg} km')

	def drowCar(self, km):
		""" Метод поездки авто """ 
		self.probeg = self.probeg + km


e_car = ElectroCar('Tesls', 'T', '2018', 99000)