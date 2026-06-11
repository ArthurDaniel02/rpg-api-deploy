class Personagem:
    def __init__(self):
        self._idPersonagem = None
        self._nome = None
        self._classe = None
        self._nivel = 1
        self._moedas = 0
        self._aluno = None
    
    def add(self): return True
    
    def setIdPersonagem(self, id): self._idPersonagem = id
    def getIdPersonagem(self): return self._idPersonagem
    
    def setNome(self, n): self._nome = n
    def getNome(self): return self._nome
    
    def setClasse(self, c): self._classe = c
    def getClasse(self): return self._classe
    
    def setNivel(self, n): self._nivel = n
    def getNivel(self): return self._nivel
    
    def setMoedas(self, v): self._moedas = v
    def getMoedas(self): return self._moedas
    
    def customizarAvatar(self, c, o): pass
    def usarItem(self, idI): pass
    
    def addAluno(self, a): self._aluno = a
    def getAluno(self): return self._aluno