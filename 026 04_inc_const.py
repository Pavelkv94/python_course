class VkAccountInWebSite():
	"""Ваш акккаунт в Vk, на сайте ВК"""
	def __init__(self, name, login_id, password):
		self.name = name
		self.login_id = login_id
		self.password = password

	def loginVk(self):
		if self.login_id == 123 and self.password == 456:
			print('Привет ' + self.name)
		return True


vkakk_1 = VkAccountInWebSite('Alex', 123, 456)
vkakk_1.loginVk()

vkakk_1.name = 'Andrey'

print(vkakk_1.name)
print(vkakk_1.login_id)
print(vkakk_1.password)


class VkAccountInWebSite():
	"""Ваш акккаунт в Vk, на сайте ВК"""
	def __init__(self, name, login_id, password):
		self.__name = name
		self.__login_id = login_id
		self.__password = password

	def publicLogin(self):
		self.__loginVk()

	def __loginVk(self):
		if self.__login_id == 123 and self.__password == 456:
			print('Привет ' + self.__name)
		return True

vkakk_1 = VkAccountInWebSite('Alex', 123, 456)
vkakk_1.loginVk()

#vkakk_1.name = 'Andrey'

print(vkakk_1.__name)
print(vkakk_1.__login_id)
print(vkakk_1.__password)

vkakk_1.publicLogin()

print(vkakk_1._VkAccountInWebSite__password)