import json
from api.interfaces.controllers.IArqueiroController import IArqueiroController

class ArqueiroControllerImpl(IArqueiroController):
    def __init__(self, arqueiro_dao=None):
        self._arqueiro_dao = arqueiro_dao

    def salvar(self, request):
        dados = request.data
        self._arqueiro_dao.salvar(dados)
        return {"data": {"mensagem": "Arqueiro criado"}, "status": 201}

    def alterar(self, request, pk):
        dados = request.data
        dados['id'] = pk
        self._arqueiro_dao.alterar(dados)
        return {"data": {"mensagem": "Arqueiro alterado"}, "status": 200}

    def deletar(self, request, pk):
        self._arqueiro_dao.deletar({"id": pk})
        return {"data": {"mensagem": "Arqueiro deletado"}, "status": 200}

    def consultar(self, request):
        return {"data": self._arqueiro_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        res = self._arqueiro_dao.consultarbyId({"id": pk})
        return {"data": res, "status": 200 if res else 404}