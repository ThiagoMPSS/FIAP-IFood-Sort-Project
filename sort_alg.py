#Função usada para classificar as empresas
def classificar(item_atual, item_target):
	#Cria as variaveis e atribui a elas os valores(Distancia, Avaliação e Frete)
	#do Item(Empresa) a ser comparado
    target_dist = item_target[1]
    target_aval = item_target[2]
    target_fret = item_target[3]

	#Cria as variaveis e atribui a elas os valores(Distancia, Avaliação e Frete)
	#do Item atual separado para a comparação
    atual_dist = item_atual[1]
    atual_aval = item_atual[2]
    atual_fret = item_atual[3]

	#Verifica o Item com menor distancia, se for menor ele ganha um valor positivo,
	#se maior negativo, quando dá empate, resulta em zero!
    criterio_dist = -1 #Atribui o valor -1 logo no começo assim não será necessario
					   #usar o Else na operação condicional, pois se as condições 
					   #anteriores não forem atendidas esse valor simplesmente não 
					   #irá alterar
    if (atual_dist < target_dist): criterio_dist = 1
    elif (target_dist == atual_dist): criterio_dist = 0

    criterio_aval = -3
    if (atual_aval < target_aval): criterio_aval = 3
    elif (atual_aval == target_aval): criterio_aval = 0

    criterio_fret = -2
    if (target_fret < atual_fret): criterio_fret = 2
    elif (target_fret == atual_fret): criterio_fret = 0

    return criterio_aval + criterio_dist + criterio_fret #Soma o resultado de todos os
														 #criterios e os retorna junto
														 #com a função

#Função que percorre a lista para somar todos os itens uns com os outros
def mapear(lista):
    for i in range(0, len(lista)): #Seleciona o Item atual a ser observado
        lista[i].append(0) #Adiciona mais uma coluna na subLista(usada para dar a
						   #informação das empresas), coluna essa usada para indicar a
						   #classificação dela em relação as outras
        for j in range(0, len(lista)): #Seleciona o Item a ser comparado
            if (i != j): #Verifica se o index(Indice/posição) dele na lista é diferente
						 #ao Item do Item que está sendo observado
				#Adiciona na coluna recem-criada o valor retornado da
				#classificação + o valor que ela já tinha
                lista[i][len(lista[i]) - 1] += classificar(lista[i], lista[j])
    return lista #Retorna a lista modificada

#Função usada para trocar a posição dos itens da lista
def trocar_pos(lista, index, alvo):
    aux = lista[index] #Variavel Auxiliar usada para armazenar temporariamente o valor
					   #do item a ser trocado de localização
	#Troca os Itens de posição
    lista[index] = lista[alvo]
    lista[alvo] = aux
    return lista #Retorna a lista modificada

def sort(lista):
    lista = mapear(lista) #Usa a função Mapear passando a lista

    i_class = len(lista[0]) - 1  #pega Indice(Index/Posição na lista) da classificação
	#Percorre cada um dos itens da lista 2 vezes, para cada 1 item que é percorrido no
	#primeiro loop, é percorrido 1 vez no segundo
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
			#Faz a comparação pra saber quem obteve o menor valor de classificação
			#e o coloca antes do anterior na lista
            if (lista[i][i_class] < lista[j][i_class]):
                lista = trocar_pos(lista, i, j) #Troca a posição usando a função
												#Troca_Pos, e pega o retorno
												#adicionando as modificações para
												#a variavel local
    return lista #Retorna a lista modificada
