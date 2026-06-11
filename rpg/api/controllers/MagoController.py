import json
from api.interfaces.controllers.IMagoController import IMagoController

class MagoControllerImpl(IMagoController):
    def __init__(self, mago_dao=None):
        self._mago_dao = mago_dao

    def salvar(self, request):
        dados = request.data
        self._mago_dao.salvar(dados)
        return {"data": {"mensagem": "Mago criado com sucesso"}, "status": 201}

    def alterar(self, request, pk):
        dados = request.data
        dados['id'] = pk
        self._mago_dao.alterar(dados)
        return {"data": {"mensagem": "Mago atualizado com sucesso"}, "status": 200}

    def deletar(self, request, pk):
        self._mago_dao.deletar({"id": pk})
        return {"data": {"mensagem": "Mago deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._mago_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        res = self._mago_dao.consultarbyId({"id": pk})
        return {"data": res, "status": 200 if res else 404}