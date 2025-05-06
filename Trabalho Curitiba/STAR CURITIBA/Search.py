"""
Exemplo de GREED Search
"""


class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False

    def search(self, current):
        print(f"\nAtual: {current.label}")
        current.visited = True

        if current == self.target:
            self.found = True
        else:
            sorted_routes = SortMap(len(current))

            for adjacent in current.adjacent:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    sorted_routes.insert(adjacent)

            sorted_routes.show_array()

            if sorted_routes.array[0]:
                self.search(sorted_routes.array[0].vertex)

if __name__ == "__main__":
    map = Cidades()
    gps = Routes(map.portouniao)
    gps.search(map.curitiba)


