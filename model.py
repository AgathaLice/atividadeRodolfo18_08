
from sys import exit
import pymongo

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        SisOpr = dbMain["SO"]
        self.users = SisOpr["Users"]
    
    def salvar(self, userSenha) -> None:
        user = self.validarUser(userSenha["user"])
        senha = self.validarSenha(userSenha["senha"])
        print(self.guardarLogin(user, senha))
        return None
    
    def validarUser(self, user) -> None | str:
        # valida o user
        return user
    
    def validarSenha(self, senha) -> None | str:
        # valida a senha
        return senha
    
    def guardarLogin(self, user, senha) -> None | dict:
        self.users.insert_one({"usuário":user,"senha":senha})
        return print({"user":user, "senha":senha})
    
    def sair(self, evento) -> None:
        exit()
        return None