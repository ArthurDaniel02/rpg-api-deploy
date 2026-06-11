from api.models import Arqueiro as ArqueiroModel

class ArqueiroDAOMysql:
    def salvar(self, a):
        model = ArqueiroModel(
            nome=a.getNome(), 
            classe="Arqueiro", 
            nivel=a.getNivel(), 
            aluno_id=a.getAluno(),
            destreza=a.getDestreza()
        )
        model.save()
        return True

    def alterar(self, a):
        m = ArqueiroModel.objects.get(id=a.getIdPersonagem())
        m.nome = a.getNome()
        m.nivel = a.getNivel()
        m.aluno_id = a.getAluno()
        m.destreza = a.getDestreza()
        m.save()
        return True

    def deletar(self, a):
        ArqueiroModel.objects.filter(id=a.getIdPersonagem()).delete()
        return True

    def consultar(self):
        return list(ArqueiroModel.objects.all().values())

    def consultarbyId(self, a):
        try:
            return ArqueiroModel.objects.filter(id=a.getIdPersonagem()).values().first()
        except:
            return None