class Pessoa:
    def __init__(self):
        self._idPessoa = None
        self._nome = None
        self._cpf = None
        self._conta = None
    
    def add(self): return True
    
    def setIdPessoa(self, id): self._idPessoa = id
    def getIdPessoa(self): return self._idPessoa
    
    def setNome(self, nome): self._nome = nome
    def getNome(self): return self._nome
    
    def setCpf(self, cpf): self._cpf = cpf
    def getCpf(self): return self._cpf
    
    def addConta(self, conta): self._conta = conta
    def getConta(self): return self._conta