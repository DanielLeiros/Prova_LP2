from operator import itemgetter
from math import floor
def clusterPartColig(dados,partColig,):
	listaAux = []
	idx = 0
	for i in partColig:
		if len(i) <= 7:
			listaAux.append(i)
		else: 
			listaAux.append(i.split('-')[1])
	for i in sorted(set(listaAux)):
		for j in range(len(dados)):
			if len(i) <= 7:
				if i == dados[j][2]:
					 dados[j][4] = idx
			else:			 
				if i in dados[j][2]:
					dados[j][4] = idx;
		idx +=1
	#-------------------------------------------#
	# dados = sorted(dados,key=itemgetter(4))
	for i in range(len(dados)):
	  	print(dados[i][2],dados[i][4])
#---------------------------- main ----------------------#	 
total_cadeiras = 29
QE = 12684
dados = []
num = []
nome = []
partColig = []
votos = []
#Pegado os dados da tabela e transferindo
# dados = dados gerais tabelão que será indexado pra clusterizar por part/colig
# votosCacth = vetor só de votos por candidado tratar \n
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
# O grande objetivo dessa área é agrupar os partido e coligações, chamando a função cluster
# E depois salvar os índices dos grupos, pra ajudar nos cálculos dos votos por partidos e co-
# ligações, facilitando pegar também os que serão direcionados para as vigas.
clusterPartColig(dados, partColig)
dados = sorted(dados,key=itemgetter(4))
partidoIdx = [idx for idx,val in enumerate(dados) if dados[idx][4] != dados[idx-1][4]]
for i in dados:
	print (i[4])
votosPorOrdem = [int(i[3].split('\n')[0]) for i in dados]
votosPorGrupo = [sum(votosPorOrdem[partidoIdx[i]:partidoIdx[i+1]]) for i in range(len(partidoIdx)-1)]
votosPorGrupo.append(sum(votosPorOrdem[partidoIdx[-1]:]))
print(partidoIdx)
print(votosPorGrupo)
#-------------Agora já tenho separdamente os votos por partido/coligação------------------#
#Em votosPorGrupo/dados (ordenado)
vagasPorGrupo = [floor(i/QE) for i in votosPorGrupo]
print (vagasPorGrupo)
while sum(vagasPorGrupo) != total_cadeiras:
	pontuacaoVagas = [votosPorGrupo[i]/(vagasPorGrupo[i]+1) for i in range(len(vagasPorGrupo))]
	vagasPorGrupo[pontuacaoVagas.index(max(pontuacaoVagas))] +=1
	print(max(pontuacaoVagas))
print (vagasPorGrupo)