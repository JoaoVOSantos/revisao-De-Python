"""
Exemplo de Busca Binária, ultilizando o conceito 
de 'Divisão e Conquista'.
"""


def search(elements: list, element: int, end: int, start: int = 0):
    """
    Função que Divide a lista, descarta uma metade
    divide outra metade e recomeça.
    """
    # caso base
    while start <= end:
        mid = start + ((end - start) // 2)
        
        # caso de loop
        if elements[mid] == element:
            return mid
        elif elements[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return 'Elemento não encontrado.'
    ...

elements = [4,7,8,9,10,23,40,567,7854,23423]
element = 23423

result = search(elements, element, len(elements) -1)
print(f"O indice do elemento procurado é: {result}")