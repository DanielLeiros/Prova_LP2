class node():
	def __init__(self, data=None, nextN = None, prevN = None):
		self.data = data
		self.nextN = nextN
		self.prevN = prevN

class doubleLinkedList():
	def __init__(self):
		self.head = node()
		self.tail = self.head
		self.size = 0

	def insert(self, data):
		atual = self.tail
		atual.nextN = node(data)
		atual.nextN.prevN = atual
		self.tail = atual.nextN
		self.size +=1

	def remove(self,idx):
		aux = 0
		if idx == self.size-1:
			atual = self.tail
			atual.prevN.nextN = None
			self.tail = atual.prevN
			self.size -= 1
			return
		elif idx > self.size or idx < 0:
			print("Esse índice excede a lista...")
			return
		atual = self.head.nextN			
		while aux != idx:
			atual = atual.nextN
			aux +=1
		atual.prevN.nextN = atual.nextN
		atual.nextN.prevN = atual.prevN
		self.size -= 1

	def findNum(self, value):
		atual = self.head
		while atual.nextN != None:
			if atual.nextN.data == value:
				return True
			atual = atual.nextN
		return False

	def display(self):
		vet = []
		atual = self.head
		while atual.nextN != None:
			vet.append(atual.nextN.data)
			atual = atual.nextN
		return vet

	def swap(self, idx1, idx2):
		aux1 = 0
		aux2 = 0
		if idx1 > self.size or idx2 > self.size:
			print("Esse(s) índice(s) excede(m) a lista...")
			return
		else:
		#Resolvi fazer assim para que o cálculo não dependesse da ordem dos índices
			primeiro = self.head.nextN			
			while aux1 != idx1:
				primeiro = primeiro.nextN
				aux1 +=1
			segundo = self.head.nextN			
			while aux2 != idx2:
				segundo = segundo.nextN
				aux2 +=1
		temp = primeiro.data
		primeiro.data = segundo.data
		segundo.data = temp
		
	def shift(self):
		if self.size <= 1:
			self.head.nextN = None
			self.tail = self.head
			self.size = 0
			return
		atual = self.head.nextN
		atual = atual.nextN
		self.head.nextN = atual
		atual.prevN = self.head
		self.size -= 1
	
	def pop(self):
		if self.size <= 1:
			self.head.nextN = None
			self.tail = self.head
			self.size = 0
			return
		atual = self.tail
		atual = atual.prevN
		atual.nextN = None
		self.tail = atual
		self.size -= 1
