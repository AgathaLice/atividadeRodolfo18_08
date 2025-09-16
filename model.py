
from sys import exit

import pymongo
from time import sleep

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        SisOpr = dbMain["SO"]
        self.users = SisOpr["Users"]
        
        self.dados = {"nome": ["Excel", "Word", "Powerpoint", "Google Chrome", "Ibis Paint",
                               "Firefox", "Github Desktop", "Explorador de Arquivos",
                               "Configurações", "Prompt de Comando", "Gerenciador de  Tarefas"],
                      "user": ["Alice", "Jonas", "Roberta", "Admin", "Rodolfo"], #? self.getUsers(),
                      "memória": ["1", "2", "3", "4", "5"],
                      "estado": ["INÍCIO", "PRONTO", "EXECUÇÃO", "ESPERA", "TÉRMINO"]}
        self.tempo = 0
    
    
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
    
    '''def timer(self):
        sleep(1)
        self.tempo += 1
        if self.tempo % 5 == 0:
            if self.quantidadeProcessos => 8:
                self.killProcesso()
            if self.quantidadeProcessos < 8:
                self.criarProcesso()'''
            
    
    
    def sair(self, evento) -> None:
        exit()
        return None