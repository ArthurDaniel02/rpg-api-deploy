from api.models import Aluno as AlunoModel

class AlunoDAOMysql:
    def salvar(self, a):
        model = AlunoModel(
            nome=a.getNome(), 
            cpf=a.getCpf(), 
            conta_id=a.getConta(), 
            moedas=a.getMoedas()
        )
        model.save()
        return True

    def alterar(self, a):
        m = AlunoModel.objects.get(id=a.getIdPessoa()) 
        
        if a.getNome() is not None: m.nome = a.getNome()
        if a.getCpf() is not None: m.cpf = a.getCpf()
        if a.getConta() is not None: m.conta_id = a.getConta()
        if a.getMoedas() is not None: m.moedas = a.getMoedas()
        
        m.save()
        return True

    def deletar(self, a):
        AlunoModel.objects.filter(id=a.getIdPessoa()).delete()
        return True

    def consultar(self):
        return list(AlunoModel.objects.all().values())

    def consultarbyId(self, a):
        try:
            return AlunoModel.objects.filter(id=a.getIdPessoa()).values().first()
        except:
            return None