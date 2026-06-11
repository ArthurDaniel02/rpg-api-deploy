import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from api.interfaces.controllers.IPersonagemController import IPersonagemController

from api.models_domain.Personagem import Personagem
from api.models_domain.Mago import Mago
from api.models_domain.Guerreiro import Guerreiro
from api.models_domain.Arqueiro import Arqueiro

class PersonagemControllerImpl(IPersonagemController):
    def __init__(self, personagem_dao=None):
        self._personagem_dao = personagem_dao
        self._mago_dao = None
        self._guerreiro_dao = None
        self._arqueiro_dao = None

    def salvar(self, request):
        try:
            dados = request.data
            
            nome = dados.get('nome')
            classe_escolhida = dados.get('classe', '').lower()
            aluno_id = dados.get('aluno_id')

            if not nome or not classe_escolhida or not aluno_id:
                return {"data": {"erro": "Nome, classe e aluno_id são obrigatórios."}, "status": 400}

            if classe_escolhida == 'mago':
                p_obj = Mago()
                p_obj.setNome(nome)
                p_obj.setNivel(1)
                p_obj.addAluno(aluno_id)
                p_obj.setInteligencia(10) 
                self._mago_dao.salvar(p_obj) 

            elif classe_escolhida == 'guerreiro':
                p_obj = Guerreiro()
                p_obj.setNome(nome)
                p_obj.setNivel(1)
                p_obj.addAluno(aluno_id)
                p_obj.setForca(15) 
                self._guerreiro_dao.salvar(p_obj)

            elif classe_escolhida == 'arqueiro':
                p_obj = Arqueiro()
                p_obj.setNome(nome)
                p_obj.setNivel(1)
                p_obj.addAluno(aluno_id)
                p_obj.setDestreza(12) 
                self._arqueiro_dao.salvar(p_obj)

            else:
                return {"data": {"erro": "Classe inválida. Escolha: Mago, Guerreiro ou Arqueiro."}, "status": 400}
            
           
            return {"data": {"mensagem": f"{classe_escolhida.capitalize()} criado com sucesso!"}, "status": 201}

        except IntegrityError:
            return {"data": {"erro": "Aluno não encontrado ou este personagem já existe."}, "status": 409}
        except Exception as e:
            return {"data": {"erro": f"Erro interno: {str(e)}"}, "status": 500}

    def alterar(self, request, pk):
        try:
            dados = request.data
            
            p_obj = Personagem()
            p_obj.setIdPersonagem(pk)
            
            if 'nome' in dados: p_obj.setNome(dados.get('nome'))
            if 'nivel' in dados: p_obj.setNivel(dados.get('nivel'))
            if 'aluno_id' in dados: p_obj.addAluno(dados.get('aluno_id'))
            
            self._personagem_dao.alterar(p_obj)
            return {"data": {"mensagem": "Personagem atualizado com sucesso"}, "status": 200}
            
        except ObjectDoesNotExist:
             return {"data": {"erro": "Personagem não encontrado."}, "status": 404}
        except Exception as e:
            return {"data": {"erro": f"Erro interno: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        try:
            p_obj = Personagem()
            p_obj.setIdPersonagem(pk)
            
            self._personagem_dao.deletar(p_obj)
            return {"data": {"mensagem": "Personagem deletado com sucesso"}, "status": 200}
        except Exception as e:
            return {"data": {"erro": f"Erro ao deletar: {str(e)}"}, "status": 500}

    def consultar(self, request):
        try:
            return {"data": self._personagem_dao.consultar(), "status": 200}
        except Exception as e:
            return {"data": {"erro": f"Erro na consulta: {str(e)}"}, "status": 500}

    def consultarbyId(self, request, pk):
        try:
            p_obj = Personagem()
            p_obj.setIdPersonagem(pk)
            
            res = self._personagem_dao.consultarbyId(p_obj)
            return {"data": res, "status": 200 if res else 404}
        except Exception as e:
             return {"data": {"erro": f"Erro na consulta: {str(e)}"}, "status": 500}