"""
Exemplo de algoritimo ganancioso - dijakstra
Solução do caminho mais curto.
"""

#1. Definir: representar o grafo (mapa) e a tabela de soluçoes.
DISTANCIA = 0
BOLINHADAFRENTE = 1 
INFINITO = float("inf")

mapa = {
    "A":{"B": 4,"C": 3,},
    "B":{"A": 4, "C": 5, "D": 2},
    "C":{"A": 3, "B": 5, "D": 1, "E": 3},
    "D":{"B": 2, "C": 1, "E": 4},
    "E":{"C": 3,"D": 4},
}
tabela = {
    "A": [0, None],
    "B": [INFINITO, None],
    "C": [INFINITO, None],
    "D": [INFINITO, None],
    "E": [INFINITO, None]
}

#TODO: 2. Definir função que retorna a distancia mais curta de um vertice a partir da origem.
def Saber_Menor_Distancia(tabela, Ligacao) -> int:
    """
    retorna a distancia mais curta de um vertice a partir da origem.
    (A) ------> (B)
    """
    return tabela[Ligacao][DISTANCIA]

#TODO: 3. Definir função que atualiza a distancia mais curta na tabela.
def Colocar_Na_Tabela_Distancia_Mais_Curta(tabela, Ligacao, distancia):
    """
    Função que atualiza a distância mais curta na tabela.
    (A) ------> (B) = 4
    """
    tabela[Ligacao][DISTANCIA] = distancia

#TODO: 4. Definir função que atualiza o antecessor na tabela
def Colocar_Antecessor(tabela, Ligacao, Predessesor):
    """
    Função que atualiza o antecessor do vértice na tabela.
    (A) ------> (B) = 4, Agora estou no (B)
    """
    tabela[Ligacao][BOLINHADAFRENTE] = Predessesor
    
#TODO: 5. Definir função que retorna a distancia entre 2 vertices
def Pegar_Distancia(mapa, Primeiro_Vertice, Segundo_Vertice):
    """
    Função que retorna a distância entre 2 vértices.
    (A) -------> (B) -------> (D) = 6
    """
    return mapa[Primeiro_Vertice][Segundo_Vertice]

#TODO: 6. Definir função que retorna o proximo vertice a ser visitado.
def Pegar_Proximo_Vertice(tabela, visitei):
    """
    Função que retorna o próximo vértice a ser visitado.
    """
    # Criado um codigo que lista todos os indices(vertices) não visitados.
    #No Caso Diferentes de visitado
    naoVisitei = list(
        set(
            tabela.keys()
        ).difference(visitei)
    )

    #Variaveis contam tudo
    NumeroMinimoDeVerticesNaoVisitados = naoVisitei[0]
    NumeroMinimoDeDistanciaPercorrida = tabela[naoVisitei[0]][DISTANCIA]

    # laço para retornar de acordo com a tabela, quantos Vertices Eu nao Visitei
    for vertice in naoVisitei:
        if tabela[vertice][DISTANCIA] < NumeroMinimoDeDistanciaPercorrida:
            NumeroMinimoDeVerticesNaoVisitados = vertice
            NumeroMinimoDeDistanciaPercorrida = tabela[vertice][DISTANCIA]
    
    return NumeroMinimoDeVerticesNaoVisitados

#TODO: 7. Definir função principal que resolve o problema do caminho mais curto.
def find_shortes_path(mapa: dict, table: dict, origin: str = "A"):
    """
    Função principal que resolve o problema do caminho mais curto.
    """ 
    visited = []
    current = origin
    start = origin

    while True:
        adjacent_vertex = mapa[current]

        if set(adjacent_vertex).issubset(set(visited)):
            ...
        else:
            unvisted = set(adjacent_vertex).difference(set(visited))

            for vertex in unvisted:
                distance_from_start = Saber_Menor_Distancia(table, vertex)

                if distance_from_start == INFINITO and current == start:
                    total_distance = Pegar_Distancia(mapa, vertex, current)
                else:
                    total_distance = Saber_Menor_Distancia(table, current)
                    total_distance += Pegar_Distancia(mapa, current, vertex)

                if total_distance < distance_from_start:
                    Colocar_Na_Tabela_Distancia_Mais_Curta(table, vertex, total_distance)
                    Colocar_Antecessor(table, vertex, current)
                    
        visited.append(current)
                
        if len(visited) == len(table.keys()):
            break

        current = Pegar_Proximo_Vertice(table, visited)

    return table


#TODO: 8. Definir For para se passar por gps.
def gps(destino, solucoes):
    rota = []
    atual = destino
    
    while atual is not None:
        rota.append(atual)
        atual = solucoes[atual][1]
    
    return rota[::-1]
    
 
 
 

result = find_shortes_path(mapa, tabela)
print(result)

rota = gps("D",tabela)
print(rota)