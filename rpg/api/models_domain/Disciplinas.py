class Disciplina:
    def __init__(self):
        self._idDisciplina = None
        self._nome = None
        self._codigo = None
        self._professor = None
        self._alunos = []
        self._quests = []
    
    def add(self): return True
    
    def setIdDisciplina(self, id): self._idDisciplina = id
    def getIdDisciplina(self): return self._idDisciplina
    
    def setNome(self, n): self._nome = n
    def getNome(self): return self._nome
    
    def setCodigo(self, c): self._codigo = c
    def getCodigo(self): return self._codigo
    
    def addProfessor(self, p): self._professor = p
    def getProfessor(self): return self._professor
    
    def addAluno(self, a): self._alunos.append(a)
    def getAlunos(self): return self._alunos
    
    def addQuest(self, q): self._quests.append(q)
    def getQuests(self): return self._quests