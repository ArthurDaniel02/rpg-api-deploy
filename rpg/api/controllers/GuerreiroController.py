import json
from api.interfaces.controllers.IGuerreiroController import IGuerreiroController

class GuerreiroControllerImpl(IGuerreiroController):
    def __init__(self, guerreiro_dao=None):
        self.guerreiro_dao = guerreiro_dao

    def salvar(self, request):
        dados = request.data
        self.guerreiro_dao.salvar(dados)
        return {"data": {"mensagem": "Guerreiro criado"}, "status": 201}

    def alterar(self, request, pk):
        dados = request.data
        dados['id'] = pk
        self.guerreiro_dao.alterar(dados)
        return {"data": {"mensagem": "Guerreiro alterado"}, "status": 200}

    def deletar(self, request, pk):
        self.guerreiro_dao.deletar({"id": pk})
        return {"data": {"mensagem": "Guerreiro deletado"}, "status": 200}

    def consultar(self, request):
        return {"data": self.guerreiro_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        res = self.guerreiro_dao.consultarbyId({"id": pk})
        return {"data": res, "status": 200 if res else 404}