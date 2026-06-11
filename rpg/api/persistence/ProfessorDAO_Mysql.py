from api.models import Professor as ProfessorModel

class ProfessorDAOMysql:
    def salvar(self, p):
        model = ProfessorModel(
            nome=p.getNome(), 
            cpf=p.getCpf(), 
            conta_id=p.getConta(),
        )
        model.save()
        return True

    def alterar(self, p):
        m = ProfessorModel.objects.get(id=p.getIdPessoa())
        
      
        if p.getNome() is not None: m.nome = p.getNome()
        if p.getCpf() is not None: m.cpf = p.getCpf()
        if p.getConta() is not None: m.conta_id = p.getConta()
        
        m.save()
        return True

    def deletar(self, p):
        ProfessorModel.objects.filter(id=p.getIdPessoa()).delete()
        return True

    def consultar(self):
        return list(ProfessorModel.objects.all().values())

    def consultarbyId(self, p):
        try:
            return ProfessorModel.objects.filter(id=p.getIdPessoa()).values().first()
        except:
            return None