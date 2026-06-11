from api.models import Mago as MagoModel

class MagoDAOMysql:
    def salvar(self, m):
        model = MagoModel(
            nome=m.getNome(), 
            classe="Mago", 
            nivel=m.getNivel(), 
            aluno_id=m.getAluno(),
            inteligencia=m.getInteligencia()
        )
        model.save()
        return True

    def alterar(self, m_obj):
        m = MagoModel.objects.get(id=m_obj.getIdPersonagem())
        m.nome = m_obj.getNome()
        m.nivel = m_obj.getNivel()
        m.aluno_id = m_obj.getAluno()
        m.inteligencia = m_obj.getInteligencia()
        m.save()
        return True

    def deletar(self, m_obj):
        MagoModel.objects.filter(id=m_obj.getIdPersonagem()).delete()
        return True

    def consultar(self):
        return list(MagoModel.objects.all().values())

    def consultarbyId(self, m_obj):
        try:
            return MagoModel.objects.filter(id=m_obj.getIdPersonagem()).values().first()
        except:
            return None