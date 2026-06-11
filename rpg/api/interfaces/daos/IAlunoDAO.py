from abc import ABC, abstractmethod

class IAlunoDAO(ABC):
    @abstractmethod
    def salvar(self, obj) -> bool:
        pass

    @abstractmethod
    def alterar(self, obj) -> bool:
        pass

    @abstractmethod
    def deletar(self, obj) -> bool:
        pass

    @abstractmethod
    def consultar(self) -> list:
        pass

    @abstractmethod
    def consultarbyId(self, obj):
        pass