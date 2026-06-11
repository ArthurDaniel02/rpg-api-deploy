from api.models_domain.Personagem import Personagem

class Mago(Personagem):
    def __init__(self):
        super().__init__()
        self._inteligencia = 0
        
    def add(self): return True
    def setInteligencia(self, i): self._inteligencia = i
    def getInteligencia(self): return self._inteligencia
    def bolaDeFogo(self): pass