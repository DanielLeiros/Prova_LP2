class node():
	def __init__(self, data=None, nextN = None):
		self.data = data
		self.nextN = nextN

class linkedHash():
	def __init__(self):
		self.head = node()
		self.size = 0
		self.tabela = [self.head]*10

	def funcaoHash(self,data):
		return data%10

	def findNum(self,data):
		self.key = self.funcaoHash(data)
		atual = self.tabela[self.key]
		while atual.nextN != None:
			if atual.nextN.data == data:
				return True
			atual = atual.nextN
		return False

	def insert(self, data):
		self.key = self.funcaoHash(data)
		if self.findNum(data):
			print("Esse elemento já está na tabela")
			return
		atual = self.tabela[self.key]
		while atual.nextN != None:
			atual = atual.nextN	
		atual.nextN = node(data)

	def remove(self,data):
		self.key = self.funcaoHash(data)
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
