"""
Exemplo de Divisão e Conquista, com Ordenação e mesclagem.
"""


def merge_sort(elements: list) -> list:
    """
    Função recebe uma lista não ordenada, então ultilizando
    o conceito de 'divisão e conquista', fará a divisão da lista
    em sublistas até que reste somente um elemento. em paralelo
    invoca a função merge para fazer a mesclagem, ja ordenando 
    os elementos.
    """
    #TODO: Caso base: Se o tamanho ad lista for 1 elemento
    # Caso Base
    if len(elements) == 1:
        return elements
    
    mid = len(elements) // 2
    first = elements[:mid]
    second = elements[mid:]
    
    # Caso de loop
    first_half = merge_sort(first)
    second_half = merge_sort(second)
    
    return merge(first_half, second_half)
    
    #TODO: Encontrar o meio da lista (Divisão Inteira)
    #TODO: Cada metade dividir ao meio até restar 1 elemento (Caso base acionado)
    #TODO> Cado de loop: cada vez que dividir, invoca a função merge
    ...
    

def merge(first: list, second: list):
    """
    Juntar os elementos de forma ordenada em uma lista.
    """
    index1, index2 = 0
    elements = []
    
    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elements.append(first[index1])
            index1 += 1
        else:
            elements.append(second[index2])
            index2 += 1
            
    while index1 < len(first):
        elements.append((first[index1]))
        index1 += 1
        
    while index2 < len(second):
        elements.append((second[index2]))
        index2 += 1
        
    return elements
            
            
    
elements = [12,11,7,41,61,13,16,14]
print(merge_sort(elements))
