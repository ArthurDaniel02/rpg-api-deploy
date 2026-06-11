from api.models import Personagem as PersonagemModel

class PersonagemDAOMysql:
    def salvar(self, p):
        model = PersonagemModel(
            nome=p.getNome(), 
            classe=p.getClasse(), 
            nivel=p.getNivel(), 
            aluno_id=p.getAluno() 
        )
        model.save()
        return True

    def alterar(self, p):
        m = PersonagemModel.objects.get(id=p.getIdPersonagem())
    
        if p.getNome() is not None: m.nome = p.getNome()
        if p.getClasse() is not None: m.classe = p.getClasse()
        if p.getNivel() is not None: m.nivel = p.getNivel()
        if p.getAluno() is not None: m.aluno_id = p.getAluno()
        
        m.save()
        return True

    def deletar(self, p):
        PersonagemModel.objects.filter(id=p.getIdPersonagem()).delete()
        return True

    def consultar(self):
        return list(PersonagemModel.objects.all().values())

    def consultarbyId(self, p):
        try:
            return PersonagemModel.objects.filter(id=p.getIdPersonagem()).values().first()
        except:
            return None