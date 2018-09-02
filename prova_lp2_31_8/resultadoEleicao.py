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
#----------------------------Principal ----------------------#	 
total_cadeiras = 29
QE = 12684
dados = []
num = []
nome = []
partColig = []
votos = []
candidatosEleitos = []
blocoPC = []
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
		votos = int(lineCatcher[3].split('\n')[0])
		partColig.append(lineCatcher[2])
# O grande objetivo dessa área é agrupar os partido e coligações, chamando a função cluster
# E depois salvar os índices dos grupos, pra ajudar nos cálculos dos votos por partidos e co-
# ligações, facilitando pegar também os que serão direcionados para as vigas.
clusterPartColig(dados, partColig)
dados = sorted(dados,key=itemgetter(4))
#salvar onde estão localizados os grupos no array por índices
partidoIdx = [idx for idx,val in enumerate(dados) if dados[idx][4] != dados[idx-1][4]]
votosPorOrdem = [int(i[3].split('\n')[0]) for i in dados]
votosPorGrupo = [sum(votosPorOrdem[partidoIdx[i]:partidoIdx[i+1]]) for i in range(len(partidoIdx)-1)]
votosPorGrupo.append(sum(votosPorOrdem[partidoIdx[-1]:]))
#pegndo os votos já limpos/int e passando para vetor principal 'dados'
for i,j in zip(dados,votosPorOrdem):
	i[3] = j
#-------------Agora já tenho separdamente os votos por partido/coligação------------------#
#Verificar quantas vagas para partidos e coligações
#E depois disso fazer o cálculo das resuduais
#A notação de grupo é fazedo referência aos partidos e coligações
vagasPorGrupo = [floor(i/QE) for i in votosPorGrupo]
tamanho = len(vagasPorGrupo)
while sum(vagasPorGrupo) != total_cadeiras:
	pontuacaoVagasResid = [votosPorGrupo[i]//(vagasPorGrupo[i]+1) if vagasPorGrupo[i] > 0 else 0 for i in range(tamanho)]
	pontuacaoVagasResidAux = sorted(pontuacaoVagasResid, reverse=True)
	vagasPorGrupo[pontuacaoVagasResid.index(pontuacaoVagasResidAux[0])] +=1
#Com as vagas já definidas, essa área quer realizar o ranking por grupo,
#para assim poder verificar quais candidatos irão representá-los
while len(candidatosEleitos) != total_cadeiras:
	for i in range(len(partidoIdx)):
		if partidoIdx[i] == partidoIdx[-1]:
			blocoPC = dados[partidoIdx[i]:]
			blocoPC = sorted(blocoPC,key=itemgetter(3),reverse = True)		
			for j in range(vagasPorGrupo[i]): 
				candidatosEleitos.append(blocoPC[j])
		else:	
			blocoPC = dados[partidoIdx[i]:partidoIdx[i+1]]
			blocoPC = sorted(blocoPC,key=itemgetter(3), reverse = True)
			for j in range(vagasPorGrupo[i]): 
				candidatosEleitos.append(blocoPC[j])
candidatosEleitos = sorted(candidatosEleitos,key=itemgetter(3), reverse = True)
with open ("resultado.tsv",'w') as file_out:
	for saida in candidatosEleitos:
		file_out.write(saida[0]+';'+saida[1]+';'+saida[2]+';'+ str(saida[3])+ '\n')