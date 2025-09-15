
from sys import exit

import pymongo

from processos import Processo
from multiprocessing import process

import time as t

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
    
    def iniciarTimer():
        pass
    
    def timer(self):
        tempo = 0
        while True:
            t.sleep(1)
            #! Não vai funcionar assim, precisa desenhar na tela
    
    
    
    def sair(self, evento) -> None:
        exit()
        return None