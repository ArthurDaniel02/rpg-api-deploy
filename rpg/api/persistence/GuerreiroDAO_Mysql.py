from api.models import Guerreiro as GuerreiroModel

class GuerreiroDAOMysql:
    def salvar(self, g):
        model = GuerreiroModel(
            nome=g.getNome(), 
            classe="Guerreiro", 
            nivel=g.getNivel(), 
            aluno_id=g.getAluno(),
            forca=g.getForca()
        )
        model.save()
        return True

    def alterar(self, g):
        m = GuerreiroModel.objects.get(id=g.getIdPersonagem())
        m.nome = g.getNome()
        m.nivel = g.getNivel()
        m.aluno_id = g.getAluno()
        m.forca = g.getForca()
        m.save()
        return True

    def deletar(self, g):
        GuerreiroModel.objects.filter(id=g.getIdPersonagem()).delete()
        return True

    def consultar(self):
        return list(GuerreiroModel.objects.all().values())

    def consultarbyId(self, g):
        try:
            return GuerreiroModel.objects.filter(id=g.getIdPersonagem()).values().first()
        except:
            return None