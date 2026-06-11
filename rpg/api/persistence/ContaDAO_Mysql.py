from api.models import Conta as ContaModel

class ContaDAOMysql:
    def salvar(self, c):
        model = ContaModel(
            login=c.getLogin(), 
            senha=c.getSenha(), 
            email=c.getEmail(),
            tipo_conta=c.getTipoConta()
        )
        model.save()
        return True
        
    def autenticar(self, email, senha):
        return ContaModel.objects.filter(email=email, senha=senha).first()
    
    def alterar(self, c):
        model = ContaModel.objects.get(id=c.getIdConta())
        
        if c.getLogin() is not None: model.login = c.getLogin()
        if c.getSenha() is not None: model.senha = c.getSenha()
        if c.getEmail() is not None: model.email = c.getEmail()
        if c.getTipoConta() is not None: model.tipo_conta = c.getTipoConta()
        
        model.save()
        return True

    def deletar(self, c):
        ContaModel.objects.filter(id=c.getIdConta()).delete()
        return True

    def consultar(self):
        return list(ContaModel.objects.all().values())

    def consultarbyId(self, c):
        try:
            return ContaModel.objects.filter(id=c.getIdConta()).values().first()
        except: 
            return None