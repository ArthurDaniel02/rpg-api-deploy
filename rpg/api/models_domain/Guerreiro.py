from api.models_domain.Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self):
        super().__init__()
        self._forca = 0
        
    def add(self): return True
    def setForca(self, f): self._forca = f
    def getForca(self): return self._forca
    def furia(self): pass