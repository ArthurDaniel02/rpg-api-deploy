import json
from api.interfaces.controllers.IContaController import IContaController
from api.models_domain.Conta import Conta
from django.core.validators import validate_email     
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class ContaControllerImpl(IContaController):
    def __init__(self, conta_dao=None):
        self._conta_dao = conta_dao

    def salvar(self, request):
        try:
            dados = request.data
        
            email_recebido = dados.get('email')
            try:
                validate_email(email_recebido)
            except ValidationError:
           
                return {"data": {"erro": "Formato de e-mail inválido. Verifique se digitou corretamente."}, "status": 400}

            tipo_recebido = dados.get('tipo_conta', 'aluno').lower()
            if tipo_recebido not in ['aluno', 'professor']:
                return {"data": {"erro": "Tipo de conta inválido. Escolha 'aluno' ou 'professor'."}, "status": 400}

            conta_obj = Conta()
            conta_obj.setLogin(dados.get('login'))
            conta_obj.setSenha(dados.get('senha'))
            conta_obj.setEmail(email_recebido)
            conta_obj.setTipoConta(tipo_recebido) 

            self._conta_dao.salvar(conta_obj)
            return {"data": {"mensagem": "Conta criada"}, "status": 201}
            
        except IntegrityError:
            return {"data": {"erro": "Esse login ou e-mail já está em uso!"}, "status": 409}
            
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}


    def alterar(self, request, pk):
        try:
            dados = request.data
        
            email_recebido = dados.get('email')
            if email_recebido:
                try:
                    validate_email(email_recebido)
                except ValidationError:
                    return {"data": {"erro": "Formato de e-mail inválido."}, "status": 400}

      
            tipo_recebido = dados.get('tipo_conta')
            if tipo_recebido is not None and tipo_recebido.lower() not in ['aluno', 'professor']:
                return {"data": {"erro": "Tipo de conta inválido. Escolha 'aluno' ou 'professor'."}, "status": 400}
  
            conta_obj = Conta()
            conta_obj.setIdConta(pk)
            conta_obj.setLogin(dados.get('login'))
            conta_obj.setSenha(dados.get('senha'))
            
            if email_recebido:
                conta_obj.setEmail(email_recebido)
            if tipo_recebido:
                conta_obj.setTipoConta(tipo_recebido.lower())
            
            self._conta_dao.alterar(conta_obj)
            return {"data": {"mensagem": "Conta atualizada"}, "status": 200}
            
        except IntegrityError:
            return {"data": {"erro": "Este e-mail ou login já pertence a outra conta."}, "status": 409}
            
        except Exception as e:
            return {"data": {"erro": f"Erro interno do servidor: {str(e)}"}, "status": 500}

    def deletar(self, request, pk):
        conta_obj = Conta()
        conta_obj.setIdConta(pk)
        
        self._conta_dao.deletar(conta_obj)
        return {"data": {"mensagem": "Conta deletada"}, "status": 200}

    def consultar(self, request):
        resultado = self._conta_dao.consultar()
        return {"data": resultado if resultado else [], "status": 200}

    def consultarbyId(self, request, pk):
        conta_obj = Conta()
        conta_obj.setIdConta(pk)
        
        resultado = self._conta_dao.consultarbyId(conta_obj)
        return {"data": resultado, "status": 200 if resultado else 404}

    def realizarLogin(self, request):
        dados = request.data
        email = dados.get("email")
        senha = dados.get("senha")

        conta = self._conta_dao.autenticar(email, senha)
        
        if conta:
            return {"data": {"mensagem": "Login OK", "id": conta.id, "tipo_conta": conta.tipo_conta}, "status": 200}
        else:
            return {"data": {"mensagem": "Credenciais inválidas"}, "status": 401}

    def realizarLogout(self, request):
        return {"data": {"mensagem": "Logout OK"}, "status": 200}

    def recuperarSenha(self, request):
        return {"data": {"mensagem": "Email enviado"}, "status": 200}