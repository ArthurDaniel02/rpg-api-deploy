class Conta:
    def __init__(self):
        self._idConta = None
        self._login = None
        self._senha = None
        self._email = None
        self._tipoConta = None
        self._pessoa = None
    
    def add(self): return True
    
    def setIdConta(self, id): self._idConta = id
    def getIdConta(self): return self._idConta
    
    def setLogin(self, l): self._login = l
    def getLogin(self): return self._login
    
    def setSenha(self, s): self._senha = s
    def getSenha(self): return self._senha
    
    def setEmail(self, e): self._email = e
    def getEmail(self): return self._email
    
    def setTipoConta(self, t): self._tipoConta = t
    def getTipoConta(self): return self._tipoConta
    
    def login(self, e, s): return True
    def logout(self): pass
    def recuperarSenha(self, e): pass
    
    def addPessoa(self, p): self._pessoa = p
    def getPessoa(self): return self._pessoa