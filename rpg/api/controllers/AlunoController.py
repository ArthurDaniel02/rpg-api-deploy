import re
from django.db import IntegrityError
from api.interfaces.controllers.IAlunoController import IAlunoController
from api.models_domain.Aluno import Aluno
from api.models_domain.Item import Item
from django.core.exceptions import ObjectDoesNotExist

class AlunoControllerImpl(IAlunoController):
    def __init__(self, aluno_dao=None, item_dao=None):
        self._aluno_dao = aluno_dao
        self._item_dao = item_dao

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

        
            aluno_obj = Aluno()
            aluno_obj.setNome(dados.get('nome'))
            aluno_obj.setCpf(cpf_recebido)
            aluno_obj.addConta(dados.get('conta_id')) 
            aluno_obj.setMoedas(dados.get('moedas', 0))
            

            self._aluno_dao.salvar(aluno_obj)
            return {"data": {"mensagem": "Aluno cadastrado com sucesso!"}, "status": 201}
            
        except IntegrityError:
            
            return {"data": {"erro": "Este CPF ou Conta já estão vinculados a outro usuário."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def alterar(self, request, pk):
        try:
            dados = request.data
            aluno_obj = Aluno()
            aluno_obj.setIdPessoa(pk)
            
            cpf_recebido = dados.get('cpf')
            if cpf_recebido:
                if not self._validar_cpf(cpf_recebido):
                    return {"data": {"erro": "CPF inválido. Use o formato XXX.XXX.XXX-XX"}, "status": 400}
                aluno_obj.setCpf(cpf_recebido)
            
        
            if 'nome' in dados: aluno_obj.setNome(dados.get('nome'))
            if 'conta_id' in dados: aluno_obj.addConta(dados.get('conta_id'))
            if 'moedas' in dados: aluno_obj.setMoedas(dados.get('moedas'))

            self._aluno_dao.alterar(aluno_obj)
            return {"data": {"mensagem": "Aluno atualizado com sucesso"}, "status": 200}
            
        except IntegrityError:
            return {"data": {"erro": "Este CPF ou Conta já estão vinculados a outro usuário."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        aluno_obj = Aluno()
        aluno_obj.setIdPessoa(pk)
        
        self._aluno_dao.deletar(aluno_obj)
        return {"data": {"mensagem": "Aluno deletado"}, "status": 200}

    def consultar(self, request):
        return {"data": self._aluno_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        aluno_obj = Aluno()
        aluno_obj.setIdPessoa(pk)
        
        res = self._aluno_dao.consultarbyId(aluno_obj)
        return {"data": res, "status": 200 if res else 404}

    def comprarItem(self, request):
        try:
            dados = request.data

            aluno_req = Aluno()
            aluno_req.setIdPessoa(dados.get("aluno_id"))
            
            item_req = Item()
            item_req.setIdItem(dados.get("item_id"))

            aluno_data = self._aluno_dao.consultarbyId(aluno_req)
            item_data = self._item_dao.consultarbyId(item_req)

            if not aluno_data or not item_data:
                return {"data": {"erro": "Aluno ou Item não encontrado"}, "status": 404}

            aluno_obj = Aluno()
            aluno_obj.setIdPessoa(aluno_data['id'])
            aluno_obj.setNome(aluno_data['nome'])
            aluno_obj.setCpf(aluno_data['cpf'])
            aluno_obj.addConta(aluno_data.get('conta_id'))
            aluno_obj.setMoedas(aluno_data['moedas'])

            item_obj = Item()
            item_obj.setIdItem(item_data['id'])
            item_obj.setNomeItem(item_data['nome'])
            item_obj.setPrecoMoedas(item_data['preco'])
            item_obj.setDescricao(item_data['descricao'])

            if aluno_obj.getMoedas() >= item_obj.getPrecoMoedas():
                novo_saldo = aluno_obj.getMoedas() - item_obj.getPrecoMoedas()
                aluno_obj.setMoedas(novo_saldo)
                aluno_obj.addItem(item_obj)
                self._aluno_dao.alterar(aluno_obj)
                
                return {"data": {"mensagem": "Compra realizada com sucesso", "saldo_restante": novo_saldo}, "status": 200}
            
            return {"data": {"erro": "Saldo insuficiente"}, "status": 400}
        except Exception as e:
            return {"data": {"erro": f"Erro interno na compra: {str(e)}"}, "status": 500}
    def consultarItens(self, request, pk):
        try:
            a_obj = Aluno()
            a_obj.setIdPessoa(pk)
            
            res = self._aluno_dao.consultarItens(a_obj)
            return {"data": res, "status": 200}
            
        except ObjectDoesNotExist:
            return {"data": {"erro": f"Aluno com ID {pk} não foi encontrado no banco de dados."}, "status": 404}
        except Exception as e:
            
            return {
                "data": {
                    "erro": f"Erro ao listar itens: {str(e)}.",
                    "ajuda": "Verifique no seu arquivo api/models.py se o relacionamento ManyToMany com Item chama-se 'itens' ou se está definido no modelo Item."
                }, 
                "status": 500
            }