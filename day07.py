#class_setter_getter

class Duck():  #완전한 private 구현이 아님 그저 흉내
	color = 'white'

	def __init__(self, input_name):
		self.hidden_name = input_name

	@staticmethod
	def test():
		print('staticmethod')

	@classmethod
	def ace(cls):
		print('classmethod')

	def get_name(self):              # 값을 꺼냄
		print('inside the getter')
		return self.hidden_name

	def set_name(self, input_name):  #값을 저장
		print('inside the setter')
		self.hidden_name = input_name

	name = property(get_name, set_name)

don = Duck('Donald')
# # print(don.get_name())
# print(don.name)  #get_name처럼 동작
# #don.set_name('Donna')
# don.name = 'Donna'  #set_name처럼 동작
# don.hidden_name = 'kiminha'  # 직접 접근이 가능할 것을 확인할 수 있음.
# #print(don.get_name())
# print(don.name)
print(Duck.color, don.color, '\n\n')
don.color = 'red'
print(Duck.color, don.color, '\n\n')
don2 = Duck('rola')
print(Duck.color, don.color, don2.color)

print(f'클래스 메서드 :{Duck.ace()}, {don.ace()}\n정적 메서드 :{Duck.test()}, {don.test()}')