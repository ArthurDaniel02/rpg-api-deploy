import re
from django.db import IntegrityError
from api.interfaces.controllers.IProfessorController import IProfessorController
from api.models_domain.Professor import Professor

class ProfessorControllerImpl(IProfessorController):
    def __init__(self, professor_dao=None):
        self._professor_dao = professor_dao

    def _validar_cpf(self, cpf):
        if not cpf:
            return False
        padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        return re.match(padrao, cpf) is not None

    def salvar(self, request):
        try:
            dados = request.data
            

            cpf_recebido = dados.get('cpf')
            if not self._validar_cpf(cpf_recebido):
                return {"data": {"erro": "CPF inválido. Use o formato XXX.XXX.XXX-XX"}, "status": 400}


            prof_obj = Professor()
            prof_obj.setNome(dados.get('nome'))
            prof_obj.setCpf(cpf_recebido)
            prof_obj.addConta(dados.get('conta_id'))
            
      
            self._professor_dao.salvar(prof_obj)
            return {"data": {"mensagem": "Professor cadastrado com sucesso"}, "status": 201}
            
        except IntegrityError:

            return {"data": {"erro": "Este CPF ou Conta já estão vinculados a outro usuário."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def alterar(self, request, pk):
        try:
            dados = request.data
            prof_obj = Professor()
            prof_obj.setIdPessoa(pk)

            cpf_recebido = dados.get('cpf')
            if cpf_recebido:
                if not self._validar_cpf(cpf_recebido):
                    return {"data": {"erro": "CPF inválido. Use o formato XXX.XXX.XXX-XX"}, "status": 400}
                prof_obj.setCpf(cpf_recebido)
            

            if 'nome' in dados: prof_obj.setNome(dados.get('nome'))
            if 'conta_id' in dados: prof_obj.addConta(dados.get('conta_id'))

            self._professor_dao.alterar(prof_obj)
            return {"data": {"mensagem": "Professor atualizado com sucesso"}, "status": 200}
            
        except IntegrityError:
            return {"data": {"erro": "Este CPF ou Conta já estão vinculados a outro usuário."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        prof_obj = Professor()
        prof_obj.setIdPessoa(pk)
        
        self._professor_dao.deletar(prof_obj)
        return {"data": {"mensagem": "Professor deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._professor_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        prof_obj = Professor()
        prof_obj.setIdPessoa(pk)
        
        res = self._professor_dao.consultarbyId(prof_obj)
        return {"data": res, "status": 200 if res else 404}
    
    def consultarDisciplinas(self, request, pk):
        try:
            p_obj = Professor()
            p_obj.setIdPessoa(pk)
            res = self._professor_dao.consultarDisciplinas(p_obj)
            return {"data": res, "status": 200}
        except Exception as e:
            return {"data": {"erro": str(e)}, "status": 500}