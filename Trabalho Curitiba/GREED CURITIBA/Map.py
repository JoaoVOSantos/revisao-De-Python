"""
Representação do mapa Romenia, junto com a heuristica - distancia em linha reta
"""

class Vertex:
    def __init__(self, label: str, target_distance:int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False

    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(f"Adjacente: {adjacent.vertex.label}- {adjacent.cost} km")
            #TODO: mostrar o custo do vertice para o adjacent

class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

class Cidades:
    portouniao = Vertex("PortoUniao", 203)
    paulofrontin = Vertex("PauloFrontin", 172)
    canoinhas = Vertex("Canoinhas", 141)
    tresbarras = Vertex("TresBarras", 131)
    saomateusdosul = Vertex("SaoMateusDoSul", 123)
    irati = Vertex("Irati", 139)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    campolongo = Vertex("CampoLongo", 27)
    balsanova = Vertex("BalsaNova", 41)
    lapa = Vertex("Lapa", 74)
    tijucasdosul = Vertex("TijucasDoSul", 56)
    araucaria = Vertex("Araucaria", 23)
    saojosedospinhais = Vertex("SaoJoseDosPinhais", 13)
    contenda = Vertex("Contenta", 39)
    curitiba = Vertex("Curitiba", 0)

    portouniao.add_adjacent(Adjacent(paulofrontin, 46))
    portouniao.add_adjacent(Adjacent(saomateusdosul, 87))
    portouniao.add_adjacent(Adjacent(canoinhas, 78))

    paulofrontin.add_adjacent(Adjacent(portouniao, 46))
    paulofrontin.add_adjacent(Adjacent(irati, 75))

    canoinhas.add_adjacent(Adjacent(portouniao, 78))
    canoinhas.add_adjacent(Adjacent(tresbarras, 12))
    canoinhas.add_adjacent(Adjacent(mafra, 66))

    tresbarras.add_adjacent(Adjacent(saomateusdosul, 43))
    tresbarras.add_adjacent(Adjacent(canoinhas, 12))

    saomateusdosul.add_adjacent(Adjacent(tresbarras, 43))
    saomateusdosul.add_adjacent(Adjacent(lapa, 60))
    saomateusdosul.add_adjacent(Adjacent(palmeira, 77))
    saomateusdosul.add_adjacent(Adjacent(irati, 57))
    saomateusdosul.add_adjacent(Adjacent(portouniao, 87))

    irati.add_adjacent(Adjacent(palmeira, 75))
    irati.add_adjacent(Adjacent(saomateusdosul, 57))
    irati.add_adjacent(Adjacent(paulofrontin, 75))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(campolongo, 55))
    palmeira.add_adjacent(Adjacent(saomateusdosul, 77))

    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(tijucasdosul, 99))
    mafra.add_adjacent(Adjacent(canoinhas, 66))

    campolongo.add_adjacent(Adjacent(palmeira, 55))
    campolongo.add_adjacent(Adjacent(curitiba, 29))
    campolongo.add_adjacent(Adjacent(balsanova, 22))

    balsanova.add_adjacent(Adjacent(campolongo, 22))
    balsanova.add_adjacent(Adjacent(curitiba, 51))
    balsanova.add_adjacent(Adjacent(contenda, 19))

    lapa.add_adjacent(Adjacent(contenda, 26))
    lapa.add_adjacent(Adjacent(saomateusdosul, 60))
    lapa.add_adjacent(Adjacent(mafra, 57))

    tijucasdosul.add_adjacent(Adjacent(mafra, 99))
    tijucasdosul.add_adjacent(Adjacent(saojosedospinhais, 49))

    araucaria.add_adjacent(Adjacent(curitiba, 18))
    araucaria.add_adjacent(Adjacent(contenda, 37))

    saojosedospinhais.add_adjacent(Adjacent(curitiba, 15))
    saojosedospinhais.add_adjacent(Adjacent(tijucasdosul, 49))

    contenda.add_adjacent(Adjacent(balsanova, 19))
    contenda.add_adjacent(Adjacent(araucaria, 18))
    contenda.add_adjacent(Adjacent(lapa, 26))

    curitiba.add_adjacent(Adjacent(campolongo, 29))
    curitiba.add_adjacent(Adjacent(araucaria, 37))
    curitiba.add_adjacent(Adjacent(saojosedospinhais, 15))