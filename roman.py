"""
Projeto - Revisão
Converter números Inteiros para Romanos.
"""


"""
Int
float
str
bool

list
tuple
dict
set
"""

"""
animals = "turtle"
print(animals[1:5])
"""
# key -> VALUE

# nome: str = input("Qual seu nome? ")
# print(nome)

def int_to_roman(number: int) -> str:   
    """ 
    comentario dentro da função
    Função que recebe um valor int e retorna o valor 
    em romano, como string.
    """
    

    

    symbols = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',   
    }
    
    
    roman = ""
    for symbol in sorted(symbols.keys(), reverse=True):
        while number >= symbol:
            roman += symbols[symbol]
            number -= symbol
            
    return roman     
    
number = input("Digite um valor inteiro: ")
roman = int_to_roman(int(number))
print(roman)