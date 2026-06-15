class Quests:
    def __init__(self):
        self._idQuest = None
        self._titulo = None
        self._descricao = None
        self._alternativa_a = None
        self._alternativa_b = None
        self._alternativa_c = None
        self._alternativa_d = None
        self._respostaCorreta = None
        self._disciplina = None
        self._recompensa = None
        self._alunos = []
    
    def add(self): return True
    
    def setIdQuest(self, id): self._idQuest = id
    def getIdQuest(self): return self._idQuest
    
    def setTitulo(self, t): self._titulo = t
    def getTitulo(self): return self._titulo
    
    def setDescricao(self, d): self._descricao = d
    def getDescricao(self): return self._descricao

    def setAlternativaA(self, a): self._alternativa_a = a
    def getAlternativaA(self): return self._alternativa_a

    def setAlternativaB(self, b): self._alternativa_b = b
    def getAlternativaB(self): return self._alternativa_b

    def setAlternativaC(self, c): self._alternativa_c = c
    def getAlternativaC(self): return self._alternativa_c

    def setAlternativaD(self, d): self._alternativa_d = d
    def getAlternativaD(self): return self._alternativa_d
    
    def setRespostaCorreta(self, r): self._respostaCorreta = r
    def getRespostaCorreta(self): return self._respostaCorreta
    
    def addDisciplina(self, d): self._disciplina = d
    def getDisciplina(self): return self._disciplina
    
    def addAluno(self, a): self._alunos.append(a)
    def getAlunos(self): return self._alunos

    def setRecompensa(self, r): self._recompensa = r
    def getRecompensa(self): return self._recompensa