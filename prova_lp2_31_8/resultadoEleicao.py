from operator import itemgetter
total_cadeiras = 29
QE = 12684

dados = []
num = []
nome = []
partColig = []
votos = []
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        lineCatcher = line.split(';')
        dados.append(lineCatcher)	
        votosCacth = lineCatcher[3].split('\n')
        partColig.append(lineCatcher[2])
        votos.append(int(votosCacth[0]))
partidoIdx = [idx for idx,val in enumerate(partColig) if partColig[idx] != partColig[idx-1]]
dadosOrdenados = sorted(dados,key=itemgetter(2))

votosPorPartido = [sum(votos[partidoIdx[i]:partidoIdx[i+1]]) for i in range(len(partidoIdx)-1)]
print(votos)
print(votosPorPartido)



        # num.append(lineCatcher[0])
        # nome.append(lineCatcher[1])
        