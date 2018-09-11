class node():
	def __init__(self, data=None, nextN = None):
		self.data = data
		self.nextN = nextN

class linkedHash():
	def __init__(self):
		self.head = node()
		self.size = 0
		self.tabela = [self.head]*10

	def funcaoHash(self, data):
		return data%10

	def findNum(self,data):
		self.key = funcaoHash(data)
		print(self.key)
		atual = self.tabela[self.key]
		while atual.nextN != None:
			if atual.nextN.data == data:
				return True
			atual = atual.nextN
		return False

	def insert(self, data):
		self.key = funcaoHash(data)
		if self.findNum(data):
			print("Esse elemento já está na tabela")
			return
		atual = self.tabela[self.key]
		while atual.nextN != None:
			atual = atual.nextN	
		atual.nextN = node(data)

	def remove(self,data):
		self.key = funcaoHash(data)
		if self.findNum(data) == False:
			print("Esse elemento não está na tabela")
			return
		atual = self.tabela[self.key]
		while atual.nextN != None:
			if atual.nextN.data == data:
				if atual.nextN.nextN == None:
					atual.nextN = None
				else:
					atual.nextN = atual.nextN.nextN

a = linkedHash()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(10)
a.insert(11)
a.insert(22)
a.insert(13)
a.insert(42)
a.insert(15)
a.insert(62)
a.insert(17)
a.insert(82)
a.insert(19)
a.insert(20)
a.insert(81)
a.insert(92)
a.insert(71)
a.insert(62)
a.insert(-1)
a.insert(-423)
print(2,a.findNum(2))
print(62,a.findNum(2))
print(99,a.findNum(2))
print(-1,a.findNum(2))