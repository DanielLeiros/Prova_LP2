class Node:
	def __init__(self, data=None, father = None):
		self.data = data
		self.father = father
		self.child = []

class Tree:
	def __init__(self, data):
		self.root = Node(data)

	def auxSearch(self, val, fatherVal, cur):
		print('searching: ',cur.data)
		
		#condições de parada

		if cur.data == val:
			return cur
		if cur.data == fatherVal:
			print('father was founded: ', cur.data)
			return cur

		#percorrer vetor de child e faz as chamadas recursivas
		for i in cur.child:
			aux = self.auxSearch(val,fatherVal, i)
			if aux != None:
				return aux

	#Sempre que aux for 'None', significa que o auxSearch não achou nada.		
	
	#-------------------------------------------------------------------------------------#
	
	#As funções só passam para o auxSearch os parâmetros relevantes, isso elimina a necessidade
	#de if's no retorno, por isso que nas chamadas algumas passam 'None' como parâmetro, já que
	#aquele valor não interessa.

	def insert(self,val, fatherVal):
		aux = self.auxSearch(None,fatherVal, self.root)
		if aux != None:
			if aux.data == fatherVal: 
				print(aux.data,fatherVal)
				aux.child.append(Node(val, aux))
				print(val,"Inserted")
		else:
			print('Could not insert, element already inserted or parent is not part of tree')

	#-------------------------------------------------------------------------------------#

	#Ao achar, se o elemento possuir child, pega o valor do mais a esquerda e substitui no pai e 
	#o remove da lista de child, pois agora ele vira o pai, caso não possua child, apenas o re-
	#move dos child do pai.

	def remove(self, val):
		aux = self.auxSearch(val, None, self.root)
		if aux != None:
			if len(aux.child) != 0:
				aux.data = aux.child[0].data
				for i in aux.child[0].child:
					i.father = aux
				aux.child += aux.child[0].child
				aux.child.pop(0)
			else:
				aux.father.child.remove(aux)
			
			print('element was removed: ',val)

	#-------------------------------------------------------------------------------------#

	def search(self,val):
		aux = self.auxSearch(val, None, self.root)
		if aux == None:
			print("Element not founded")	
		else:
			print(aux.data, "Element founded")
	
	#-------------------------------------------------------------------------------------#

	# A inicialização da árvore já atribui um valor ao primeiro nó que será o raíz
	# Inserção necessita de 2 parâmetros valor_p_inserir e valor_do_pai
	# Remoção e busca apenas o falor a remover/buscar

a = Tree(6)
a.insert(8,6)
a.insert(5,6)
a.insert(7,6)
a.insert(1,7)
a.insert(82,8)
a.insert(8,9)
a.insert(34,1)
a.insert(44,8)
a.insert(12,34)
a.insert(99,5)
a.insert(67,99)
a.insert(77,67)
a.insert(14,1)
a.insert(11,12)
a.insert(100,99)
a.insert(66,100)

a.remove(99)
a.search(12)
a.search(8)
a.search(34)
a.search(7)
a.search(99)
a.search(9)
a.search(300)
a.search(45)
a.search(5)