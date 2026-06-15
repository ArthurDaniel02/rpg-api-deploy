
from api.models import Disciplina as DisciplinaModel
from api.models import Aluno as AlunoModel 

class DisciplinaDAOMysql:
    def salvar(self, d):
        model = DisciplinaModel(
            nome=d.getNome(), 
            codigo=d.getCodigo(), 
            professor_id=d.getProfessor()
        )
        model.save()
        return True

    def alterar(self, d):
        m = DisciplinaModel.objects.get(id=d.getIdDisciplina())

        if d.getNome() is not None: m.nome = d.getNome()
        if d.getCodigo() is not None: m.codigo = d.getCodigo()
        if d.getProfessor() is not None: m.professor_id = d.getProfessor()
        
        m.save()
        return True

    def deletar(self, d):
        DisciplinaModel.objects.filter(id=d.getIdDisciplina()).delete()
        return True

    def consultar(self):
        return list(DisciplinaModel.objects.all().values())

    def consultarbyId(self, d):
        try:
            return DisciplinaModel.objects.filter(id=d.getIdDisciplina()).values().first()
        except:
            return None
            
    def matricular(self, d_obj, a_obj):
        try:
            disciplina_bd = DisciplinaModel.objects.get(id=d_obj.getIdDisciplina())
            aluno_bd = AlunoModel.objects.get(id=a_obj.getIdPessoa())
        
            disciplina_bd.alunos.add(aluno_bd)
            return True
        except (DisciplinaModel.DoesNotExist, AlunoModel.DoesNotExist):
            return False
    def consultarAlunos(self, d):
        try:
            m = DisciplinaModel.objects.get(id=d.getIdDisciplina())
            return list(m.alunos.all().values())
        except Exception:
            return []