"""
Exemplo de Buscar Linear
"""


elements = [3,4,1,6,14]

def search(elements: list, element: int) -> int:
    """
    Função que recebe uma lista e um valor inteiro,
    para que o algoritimo fala a busca.
    """
    for index, value in enumerate(elements):
        # caso base - condição que faz o loop parar
        if value == element:
            return index
        
    return "Elemento não encontrado."



result = search(elements, 6)
print(f"O indice do elemento procurado é: {result}")