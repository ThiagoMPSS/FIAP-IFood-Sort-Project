from sort_alg import sort #Importa somente a função "sort" do arquivo sort_alg

#Nome do restaurante, Distancia, Avaliação, Valor do frete.
restaurantes = [#Inicia uma lista
				["Sukiya - Saúde", 2.5, 4.6, 7.99], #Dentro da lista a gente cria
													#outra lista(Sublista) para
													#podermos ter as informações
													#dos restaurantes
                ["Makis Place - Saúde", 2.0, 4.7, 7.99],
                ["Giraffas Carrefour Metrocar", 1.0, 4.4, 5.99],
                ["Viena - Shopping Santa Cruz", 4.8, 4.4, 12.49],
                ["Kibon Sorveteria - Saúde", 2.3, 4.9, 6.99],
                ["A Feijoada", 4.3, 4.4, 9.90]
			   ]#Finaliza a lista


def start():
	#Chama e percorre a lista de retorno da função sort com o argumento da lista restaurantes
	for s in sort(restaurantes):
		#Pega as informações da lista subLista
		nome = s[0]
		dist = s[1]
		aval = s[2]
		fret = s[3]

		#Exibe as informações do restaurante atual
		print("Nome     : {}".format(nome))
		print("Avaliação: {} ☆".format(aval))
		print("Distancia: {} km".format(dist))
		print("Frete    : R$ {:.2f}".format(fret))
		print("")

#Chama a função de inicio
start()
