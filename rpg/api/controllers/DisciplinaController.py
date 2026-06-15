import json
from django.db import IntegrityError
from api.interfaces.controllers.IDisciplinaController import IDisciplinaController
from api.models_domain.Disciplinas import Disciplina  
from api.models_domain.Aluno import Aluno

class DisciplinaControllerImpl(IDisciplinaController):
    def __init__(self, disciplina_dao=None):
        self._disciplina_dao = disciplina_dao

    def salvar(self, request):
        try:
            dados = request.data
            
            if not dados.get('nome') or not dados.get('professor_id'):
                return {"data": {"erro": "Nome e professor_id são campos obrigatórios."}, "status": 400}

            d_obj = Disciplina()
            d_obj.setNome(dados.get('nome'))
            d_obj.setCodigo(dados.get('codigo'))
            d_obj.addProfessor(dados.get('professor_id')) 
            
            self._disciplina_dao.salvar(d_obj)
            return {"data": {"mensagem": "Disciplina criada com sucesso"}, "status": 201}
            
        except IntegrityError:
            return {"data": {"erro": "Professor não encontrado ou código de disciplina já existe."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def alterar(self, request, pk):
        try:
            dados = request.data
            
            d_obj = Disciplina()
            d_obj.setIdDisciplina(pk)
            if 'nome' in dados: d_obj.setNome(dados.get('nome'))
            if 'codigo' in dados: d_obj.setCodigo(dados.get('codigo'))
            if 'professor_id' in dados: d_obj.addProfessor(dados.get('professor_id'))
            
            self._disciplina_dao.alterar(d_obj)
            return {"data": {"mensagem": "Disciplina alterada com sucesso"}, "status": 200}
            
        except IntegrityError:
            return {"data": {"erro": "Falha na atualização. Verifique os dados enviados."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        d_obj = Disciplina()
        d_obj.setIdDisciplina(pk)
        
        self._disciplina_dao.deletar(d_obj)
        return {"data": {"mensagem": "Disciplina deletada com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._disciplina_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        d_obj = Disciplina()
        d_obj.setIdDisciplina(pk)
        
        res = self._disciplina_dao.consultarbyId(d_obj)
        return {"data": res, "status": 200 if res else 404}

    def matricularAluno(self, request):
        try:
            dados = request.data
            
            if not dados.get('disciplina_id') or not dados.get('aluno_id'):
                return {"data": {"erro": "ID do aluno e da disciplina são obrigatórios para a matrícula."}, "status": 400}
            
            d_obj = Disciplina()
            d_obj.setIdDisciplina(dados.get('disciplina_id'))
            
            a_obj = Aluno()
            a_obj.setIdPessoa(dados.get('aluno_id')) 
            
    
            d_obj.addAluno(a_obj)

            sucesso = self._disciplina_dao.matricular(d_obj, a_obj)
            
            if sucesso:
                return {"data": {"mensagem": "Aluno matriculado com sucesso na disciplina!"}, "status": 200}
            else:
                return {"data": {"erro": "Falha na matrícula. Disciplina ou Aluno não encontrados no banco."}, "status": 404}
                
        except Exception as e:
            return {"data": {"erro": f"Erro interno durante a matrícula: {str(e)}"}, "status": 500}
    def consultarAlunos(self, request, pk):
        try:
            d_obj = Disciplina()
            d_obj.setIdDisciplina(pk)
            res = self._disciplina_dao.consultarAlunos(d_obj)
            return {"data": res, "status": 200}
        except Exception as e:
            return {"data": {"erro": str(e)}, "status": 500}