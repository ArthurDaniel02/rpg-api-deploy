from api.models import Pessoa as PessoaModel

class PessoaDAOMysql:
    def salvar(self, p):
        model = PessoaModel(nome=p.getNome(), cpf=p.getCpf(), conta_id=p.getContaId())
        model.save()
        return True

    def alterar(self, p):
        m = PessoaModel.objects.get(id=p.getIdPessoa())
        m.nome = p.getNome()
        m.cpf = p.getCpf()
        m.conta_id = p.getContaId()
        m.save()
        return True

    def deletar(self, p):
        PessoaModel.objects.filter(id=p.getIdPessoa()).delete()
        return True

    def consultar(self):
        return list(PessoaModel.objects.all().values())

    def consultarbyId(self, p):
        try:
            return PessoaModel.objects.filter(id=p.getIdPessoa()).values().first()
        except:
            return None