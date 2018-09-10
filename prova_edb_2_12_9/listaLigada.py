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
		cur = self.tail
		cur.nextN = node(data)
		cur.nextN.prevN = cur
		self.tail = cur.nextN
		self.size +=1
	def remove(self,idx):
		aux = 0
		if idx == self.size-1:
			cur = self.tail
			cur.prevN.nextN = None
			self.tail = cur.prevN
			return
		elif idx > self.size:
			print("Unable to remove, this index exceeds the size of the list")
			return
		cur = self.head.nextN			
		while aux != idx:
			cur = cur.nextN
			aux +=1
		cur.prevN.nextN = cur.nextN
		cur.nextN.prevN = cur.prevN

	def display(self):
		vet = []
		cur = self.head
		while cur.nextN != None:
			vet.append(cur.nextN.data)
			cur = cur.nextN
		return vet

a = doubleLinkedList()
a.insert(1)
print(a.display())
a.insert(4)
print(a.display())
a.insert(2)
print(a.display())
a.remove(1)
print(a.display())
a.remove(5)
print(a.display())
a.remove(0)
print(a.display())
a.insert(10)
print(a.display())
