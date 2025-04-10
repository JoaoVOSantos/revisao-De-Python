"""
Representacao do problema.
"""

pessoas = [
    ("Lisboa", "LIS"),
    ("Madrid", "MAD"),
    ("Paris", "CDG"),
    ("Dublin", "DUB"),
    ("Bruxelas", "BRU"),
    ("Londres", "LHR")
]

destino = "FCO"

# criacao da base de dados
painel_voos = {}


with open("flights.txt") as lista_voos:
    for voo in lista_voos.readlines():
        origem, destino, saida, chegada, preco = voo.split(",")
        painel_voos.setdefault((origem, destino), [])
        painel_voos[(origem, destino)].append((saida, chegada, int(preco)))
        
def listar_voos(agenda):
    voo = -1
    valor_total = 0
    
    for pessoa in range(len(pessoas)):
        nome = pessoas[pessoa][0]
        origem = pessoas[pessoa][1]
        
        voo += 1
        ida = painel_voos[(origem, destino)][agenda[voo]]
        voo += 1
        volta = painel_voos[(destino, origem)][agenda[voo]]
        valor_total = ida[2] + volta[2]
        
        print(
            f"{nome}: {ida[0]} -> {ida[1]} USD {ida[2]} | {volta[0]} -> {volta[1]} USD {volta[2]}"
        )
    print(f"Valor Total: USD {valor_total}")
    

def fitness_function(agenda):
    voo = -1
    valor_total = 0    
    
    for pessoa in range(len(pessoas)):
        origem = pessoas[pessoa][1]
        
        voo += 1
        ida = painel_voos[(origem, destino)][agenda[voo]]
        voo += 1
        volta = painel_voos[(destino, origem)][agenda[voo]]
        valor_total = ida[2] + volta[2]
    
    return valor_total