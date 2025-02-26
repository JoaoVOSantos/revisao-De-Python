"""
Revisão sobre classes em python.
- Getter
- Setter
"""


class Person:
    """
    Classe Pessoa, que...
    """
    
    
    def __init__(self, name: str, age: str):
        """
        Método Contrutor
        estes são atributos da classe
        """
        self.name = name
        self.age = age    
        
    def speak(self):
        """
        Este método faz a pessoa falar.
        """
        print(f"Meu nome é {self.name} e tenho { self.age} anos.")
        
        
    @property
    def person_name(self):
        return self.name    
        
    
    @person_name.setter
    def person_name(self, name):
        self.name = name    
        
leticia = Person("Leticia","19")
leticia.speak()
print(leticia.person_name)
leticia.person_name = "Leticia Amorim Furuse"
print(leticia.person_name)