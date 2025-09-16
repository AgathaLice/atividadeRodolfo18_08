
from sys import exit

import pymongo
from processos import Processo
from random import randint

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        SisOpr = dbMain["SO"]
        self.users = SisOpr["Users"]
        
        self.procs = []
        self.execucao = None
        self.dados = {"ids": [0],
                      "nome": ["Excel", "Word", "Powerpoint", "Google Chrome", "Ibis Paint",
                               "Firefox", "Github Desktop", "Explorador de Arquivos",
                               "Configurações", "Prompt de Comando", "Gerenciador de  Tarefas"],
                      "user": ["Alice", "Jonas", "Roberta", "Admin", "Rodolfo"], #? self.getUsers(),
                      "memória": ['0x4b7d2', '0x9f13c', '0x65a1e', '0x7c3d9',
                                  '0x2d41a', '0x81ff2', '0x3ab70',
                                  '0xed120','0x1576c', '0x5bcde'],
                      "estado": ["INÍCIO", "PRONTO", "EXECUÇÃO", "ESPERA", "TÉRMINO"]}
        self.tempo = 0
        self.timerOn = False
        self.timerId = None
        self.qtdProcs = 0
    
    
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
    
    def timer(self):
        if not self.timerOn:
            self.updateTimer()
        
    def updateTimer(self):
        if not self.timerOn:
            return None
        if self.qtdProcs >= 8:
            self.procs[0].estado = "TÉRMINO"
        if self.tempo % 5 == 0:
            proc = Processo(self.dados["ids"][-1],
                            self.dados["nomes"][0],
                            str(randint(1, 12)) + "%",
                            self.dados["user"][0],
                            self.dados["memória"][randint(0, 9)])
            self.procs.append(proc)
            
            self.dados["ids"].append(self.dados["ids"][-1] + 1)
            self.dados["nomes"].pop(0)
            #user
            self.verificarEstado()
        
    
    def killProc(self):
        pass
    
    def verificarEstado(self):
        for i in self.procs:
            if i.estado == "INÍCIO":
                i.estado = "PRONTO"
            if i.estado == "PRONTO" and self.execucao is None:
                i.estado = "EXECUÇÃO"
                self.execucao = i
            if i.estado == "EXECUÇÃO":
                n = randint(0,1)
                if n == 0:
                    
    
    def sair(self, evento) -> None:
        exit()
        return None