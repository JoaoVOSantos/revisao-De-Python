"""
Revisão de OO, relembrando injeção de dependência e 
estrutura de dados 'Grafo'.
obj mapa
- mundo
- pais
- estados

"""

class State:
    """
    Classe que define estados de uma nação.
    """
    
    def __init__(self, state_name, size):
        self.state_name = state_name
        self.size = size
    
    
class Country:
    """
    Classe que define uma nação.
    """ 
    
    def __init__(self, country_name: str, flag):
        self.country_name = country_name
        self.flag = flag
        self.states = []

    def add_state(self, state: State):
        self.states.append(state)
        
    def list_states(self):
        for state in self.states:
            print(state.state_name)
        
class World_Map:
    """
    Classe que cria o mapa mundi.
    """
    brazil = Country("Brazil","🇧🇷")
    argentina = Country("Argentina", "🇦🇷")
    
    brazil.add_state(State("São Paulo",10))
    brazil.add_state(State("Rio de Janeiro",11))
    brazil.add_state(State("Minas Gerais",12))
    
    
World_map = World_Map()
print(World_map.brazil.flag)
print(World_map.brazil.list_states())