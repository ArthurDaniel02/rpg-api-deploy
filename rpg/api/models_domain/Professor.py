from api.models_domain.Pessoa import Pessoa 

class Professor(Pessoa):
    def __init__(self):
        super().__init__() 
        self._disciplinas = []
    
    
    def criarDisciplina(self, n, d): return None
    def criarQuest(self, d, m): return None
    def editarQuest(self, idQ): pass
    def criarRaid(self, n, hp): return None 
    
    def addDisciplina(self, d): self._disciplinas.append(d)
    def getDisciplinas(self): return self._disciplinas