from api.interfaces.controllers.IItemController import IItemController
from api.models_domain.Item import Item 

class ItemControllerImpl(IItemController):
    def __init__(self, item_dao=None):
        self._item_dao = item_dao

    def salvar(self, request):
        dados = request.data

        item_obj = Item()
        item_obj.setNomeItem(dados.get('nome'))
        item_obj.setPrecoMoedas(dados.get('preco', 0))
        item_obj.setDescricao(dados.get('descricao', ''))
        
        self._item_dao.salvar(item_obj)
        return {"data": {"mensagem": "Item criado com sucesso"}, "status": 201}

    def alterar(self, request, pk):
        dados = request.data
        
        item_obj = Item()
        item_obj.setIdItem(pk)
        item_obj.setNomeItem(dados.get('nome'))
        item_obj.setPrecoMoedas(dados.get('preco', 0))
        item_obj.setDescricao(dados.get('descricao', ''))
        
        self._item_dao.alterar(item_obj)
        return {"data": {"mensagem": "Item atualizado com sucesso"}, "status": 200}

    def deletar(self, request, pk):
        item_obj = Item()
        item_obj.setIdItem(pk)
        
        self._item_dao.deletar(item_obj)
        return {"data": {"mensagem": "Item deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._item_dao.consultar(), "status": 200}

    def consultarbyId(self, request, pk):
        item_obj = Item()
        item_obj.setIdItem(pk)
        
        res = self._item_dao.consultarbyId(item_obj)
        return {"data": res, "status": 200 if res else 404}