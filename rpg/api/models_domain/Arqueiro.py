from api.models_domain.Personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self):
        super().__init__()
        self._destreza = 0
        
    def add(self): return True
    def setDestreza(self, d): self._destreza = d
    def getDestreza(self): return self._destreza
    def tiroCerteiro(self): pass