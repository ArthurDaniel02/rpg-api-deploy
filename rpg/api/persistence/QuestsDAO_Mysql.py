from api.models import Quests as QuestsModel

class QuestsDAOMysql:
    def salvar(self, q):
        model = QuestsModel(
            titulo=q.getTitulo(), 
            descricao=q.getDescricao(), 
            alternativa_a=q.getAlternativaA(),
            alternativa_b=q.getAlternativaB(),
            alternativa_c=q.getAlternativaC(),
            alternativa_d=q.getAlternativaD(),
            resposta_correta=q.getRespostaCorreta(), 
            disciplina_id=q.getDisciplina()
        )
        model.save()
        return True

    def alterar(self, q):
        m = QuestsModel.objects.get(id=q.getIdQuest())
        
        if q.getTitulo() is not None: m.titulo = q.getTitulo()
        if q.getDescricao() is not None: m.descricao = q.getDescricao()
        if q.getAlternativaA() is not None: m.alternativa_a = q.getAlternativaA()
        if q.getAlternativaB() is not None: m.alternativa_b = q.getAlternativaB()
        if q.getAlternativaC() is not None: m.alternativa_c = q.getAlternativaC()
        if q.getAlternativaD() is not None: m.alternativa_d = q.getAlternativaD()
        if q.getRespostaCorreta() is not None: m.resposta_correta = q.getRespostaCorreta()
        if q.getDisciplina() is not None: m.disciplina_id = q.getDisciplina()
        
        m.save()
        return True

    def deletar(self, q):
        QuestsModel.objects.filter(id=q.getIdQuest()).delete()
        return True

    def consultar(self):
        return list(QuestsModel.objects.all().values())

    def consultarbyId(self, q):
        try:
            return QuestsModel.objects.filter(id=q.getIdQuest()).values().first()
        except:
            return None