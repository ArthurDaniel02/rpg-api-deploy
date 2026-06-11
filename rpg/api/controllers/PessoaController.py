import json
from api.interfaces.controllers.IPessoaController import IPessoaController

class PessoaControllerImpl(IPessoaController):
    def __init__(self, pessoa_dao=None):
        self._pessoa_dao = pessoa_dao

    def salvar(self, request):
        dados = request.data
        self._pessoa_dao.salvar(dados)
        return {"data": {"mensagem": "Pessoa cadastrada com sucesso"}, "status": 201}

    def alterar(self, request, pk):
        dados = request.data
        dados['id'] = pk
        self._pessoa_dao.alterar(dados)
        return {"data": {"mensagem": "Pessoa atualizada com sucesso"}, "status": 200}

    def deletar(self, request, pk):
        self._pessoa_dao.deletar({"id": pk})
        return {"data": {"mensagem": "Pessoa deletada com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._pessoa_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        res = self._pessoa_dao.consultarbyId({"id": pk})
        return {"data": res, "status": 200 if res else 404}