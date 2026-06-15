import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from api.interfaces.controllers.IQuestsController import IQuestsController
from api.models_domain.Quests import Quests
from api.models_domain.Aluno import Aluno

class QuestsControllerImpl(IQuestsController):
    def __init__(self, quests_dao=None):
        self._quests_dao = quests_dao
        self._aluno_dao = None 

    def salvar(self, request):
        try:
            dados = request.data
            
            if not dados.get('titulo') or not dados.get('disciplina_id') or not dados.get('resposta_correta'):
                return {"data": {"erro": "Título, disciplina_id e resposta_correta são obrigatórios."}, "status": 400}

            resposta = dados.get('resposta_correta').strip().upper()
            if resposta not in ['A', 'B', 'C', 'D']:
                return {"data": {"erro": "A resposta correta deve ser A, B, C ou D."}, "status": 400}

            q_obj = Quests()
            q_obj.setTitulo(dados.get('titulo'))
            q_obj.setDescricao(dados.get('descricao', ''))
            q_obj.setAlternativaA(dados.get('alternativa_a', ''))
            q_obj.setAlternativaB(dados.get('alternativa_b', ''))
            q_obj.setAlternativaC(dados.get('alternativa_c', ''))
            q_obj.setAlternativaD(dados.get('alternativa_d', ''))
            q_obj.setRespostaCorreta(resposta)
            q_obj.setRecompensa(dados.get('recompensa', 50))
            q_obj.addDisciplina(dados.get('disciplina_id'))
            
            self._quests_dao.salvar(q_obj)
            return {"data": {"mensagem": "Quest criada com sucesso!"}, "status": 201}
            
        except IntegrityError:
            return {"data": {"erro": "Verifique se a disciplina_id realmente existe no banco."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno: {str(e)}"}, "status": 500}

    def alterar(self, request, pk):
        try:
            dados = request.data
            q_obj = Quests()
            q_obj.setIdQuest(pk)
            
            if 'titulo' in dados: q_obj.setTitulo(dados.get('titulo'))
            if 'descricao' in dados: q_obj.setDescricao(dados.get('descricao'))
            if 'alternativa_a' in dados: q_obj.setAlternativaA(dados.get('alternativa_a'))
            if 'alternativa_b' in dados: q_obj.setAlternativaB(dados.get('alternativa_b'))
            if 'alternativa_c' in dados: q_obj.setAlternativaC(dados.get('alternativa_c'))
            if 'alternativa_d' in dados: q_obj.setAlternativaD(dados.get('alternativa_d'))
            
            if 'resposta_correta' in dados: 
                resposta = dados.get('resposta_correta').strip().upper()
                if resposta not in ['A', 'B', 'C', 'D']:
                    return {"data": {"erro": "A resposta correta deve ser A, B, C ou D."}, "status": 400}
                q_obj.setRespostaCorreta(resposta)
                
            if 'disciplina_id' in dados: q_obj.addDisciplina(dados.get('disciplina_id'))
            
            self._quests_dao.alterar(q_obj)
            return {"data": {"mensagem": "Quest alterada com sucesso"}, "status": 200}
        except Exception as e:
            return {"data": {"erro": f"Erro interno: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        try:
            q_obj = Quests()
            q_obj.setIdQuest(pk)
            self._quests_dao.deletar(q_obj)
            return {"data": {"mensagem": "Quest deletada com sucesso"}, "status": 200}
        except Exception as e:
            return {"data": {"erro": f"Erro interno: {str(e)}"}, "status": 500}

    def consultar(self, request):
        return {"data": self._quests_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        q_obj = Quests()
        q_obj.setIdQuest(pk)
        res = self._quests_dao.consultarbyId(q_obj)
        return {"data": res, "status": 200 if res else 404}

   
    def responderQuest(self, request):
        try:
            dados = request.data
            quest_id = dados.get('quest_id')
            aluno_id = dados.get('aluno_id')
            resposta_aluno = dados.get('resposta') 

            if not quest_id or not aluno_id or not resposta_aluno:
                return {"data": {"erro": "quest_id, aluno_id e resposta são campos obrigatórios."}, "status": 400}

            q_req = Quests()
            q_req.setIdQuest(quest_id)
            quest_data = self._quests_dao.consultarbyId(q_req)

            if not quest_data:
                return {"data": {"erro": "Quest não encontrada."}, "status": 404}

            resposta_certa = quest_data.get('resposta_correta', '').strip().upper()
            resposta_enviada = str(resposta_aluno).strip().upper()
            valor_premio = quest_data.get('recompensa', 50)


            if resposta_enviada != resposta_certa:
                return {"data": {"erro": "Resposta incorreta. Tente novamente!"}, "status": 400}
            
           
            if not self._aluno_dao:
                return {"data": {"erro": "Erro de infraestrutura: O DAO do Aluno não foi injetado no QuestsController."}, "status": 500}

            
            a_req = Aluno()
            a_req.setIdPessoa(aluno_id)
            aluno_data = self._aluno_dao.consultarbyId(a_req)
            
            if not aluno_data:
                return {"data": {"erro": f"Aluno com ID {aluno_id} não foi encontrado no banco de dados para receber a recompensa."}, "status": 404}
            
            
            a_obj = Aluno()
            a_obj.setIdPessoa(aluno_data['id'])
            a_obj.setNome(aluno_data['nome'])
            a_obj.setCpf(aluno_data['cpf'])
            a_obj.addConta(aluno_data.get('conta_id'))
            
           
            novo_saldo = aluno_data.get('moedas', 0) + valor_premio
            a_obj.setMoedas(novo_saldo)
            
            
            self._aluno_dao.alterar(a_obj)
            

            return {
                "data": {
                    "mensagem": f"Acerto Crítico! Você ganhou {valor_premio} moedas.", 
                    "saldo_atual": novo_saldo
                }, 
                "status": 200
            }

        except Exception as e:
            return {"data": {"erro": f"Erro interno ao responder: {str(e)}"}, "status": 500}