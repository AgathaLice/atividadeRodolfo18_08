
from model import Model

class Controller():
    def __init__(self, View):

        self.model = Model()

        self.view = View

    def salvar(self, userSenha) -> None:
        self.model.salvar(userSenha)
        return None
    
    def sair(self, evento) -> None:
        self.model.sair(evento)
        return None