from api.models_domain.Pessoa import Pessoa 

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self._moedas = 0
        self._disciplinas = []
        self._quests = []
        self._itens = []
        self._personagem = None
                        
                       
    
    def setMoedas(self, m): self._moedas = m
    def getMoedas(self): return self._moedas
    
    def responderQuest(self, idQ, res): return True
    def entrarDisciplina(self, cod): return True
    def comprarItem(self, idI): return True
    def visualizarPerfil(self): pass
    
    def addDisciplina(self, d): self._disciplinas.append(d)
    def getDisciplinas(self): return self._disciplinas
    
    def addQuest(self, q): self._quests.append(q)
    def getQuests(self): return self._quests
    
    def addItem(self, i): self._itens.append(i)
    def getItens(self): return self._itens
    
    def addPersonagem(self, p): self._personagem = p
    def getPersonagem(self): return self._personagem