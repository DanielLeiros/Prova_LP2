from operator import itemgetter

def clusterPartColig(dados,partColig,):
	listaAux = []
	idx = 0
	for i in partColig:
		listaAux.append(i.split()[0])
	nomePorPartido = set(listaAux) 
	for i in set(listaAux):
		for j in range(len(dados)):
			if i in dados[j][2] and dados[j][4] == None:
				print('aqui')
				dados[j][4] = idx;
		idx +=1
	for i in dados:
		print(i)			

total_cadeiras = 29
QE = 12684

dados = []
num = []
nome = []
partColig = []
votos = []
#Pegado os dados da tabela e transferindo
# dados = dados gerais tabelão que será indexado pra clusterizar por part/colig
# votosCacth = vetor só de votos por candidado
# partColig= ajudar a separar solo de coligação
# votos = voto transformado em 'int';
with open("eleicao.csv", encoding="utf-8") as f:
	f.readline()
	for line in f:
		lineCatcher = line.split(';')
		lineCatcher.append(None)
		dados.append(lineCatcher)	
		votosCacth = lineCatcher[3].split('\n')
		votos.append(int(votosCacth[0]))
		partColig.append(lineCatcher[2])

#separando os indices que separam os grupos
partidoIdx = [idx for idx,val in enumerate(partColig) if partColig[idx] != partColig[idx-1]]

#votos por partido
votosEPartido = [[partColig[partidoIdx[i]],sum(votos[partidoIdx[i]:partidoIdx[i+1]])] for i in range(len(partidoIdx)-1)]

votosEPartido.append([partColig[partidoIdx[-1]],sum(votos[partidoIdx[-1]:])])

print(votos)

clusterPartColig(dados, partColig)
for i in sorted(votosEPartido):
	print(i)



        # num.append(lineCatcher[0])
        # nome.append(lineCatcher[1])
        # dadosOrdenados = sorted(dados,key=itemgetter(2)) ordenar por coluna