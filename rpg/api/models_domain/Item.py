class Item:
    def __init__(self):
        self._idItem = None
        self._nomeItem = None
        self._precoMoedas = 0
        self._descricao = None
        self._alunos = []
    
    def add(self): return True
    
    def setIdItem(self, id): self._idItem = id
    def getIdItem(self): return self._idItem
    
    def setNomeItem(self, n): self._nomeItem = n
    def getNomeItem(self): return self._nomeItem
    
    def setPrecoMoedas(self, p): self._precoMoedas = p
    def getPrecoMoedas(self): return self._precoMoedas
    
    def setDescricao(self, d): self._descricao = d
    def getDescricao(self): return self._descricao
    
    def addAluno(self, a): self._alunos.append(a)
    def getAlunos(self): return self._alunos