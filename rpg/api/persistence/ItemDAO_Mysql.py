from api.models import Item as ItemModel

class ItemDAOMysql:
    def salvar(self, i):
        model = ItemModel(
            nome=i.getNomeItem(), 
            preco=i.getPrecoMoedas(),
            descricao=i.getDescricao()
        )
        model.save()
        return True
        
    def alterar(self, i):
        m = ItemModel.objects.get(id=i.getIdItem())
        m.nome = i.getNomeItem()
        m.preco = i.getPrecoMoedas()
        m.descricao = i.getDescricao()
        m.save()
        return True
        
    def deletar(self, i):
        ItemModel.objects.filter(id=i.getIdItem()).delete()
        return True
        
    def consultar(self):
        return list(ItemModel.objects.all().values())
        
    def consultarbyId(self, i):
        try:
            return ItemModel.objects.filter(id=i.getIdItem()).values().first()
        except:
            return None