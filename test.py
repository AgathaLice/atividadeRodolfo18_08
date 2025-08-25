
from controller import Controller

import sys
import customtkinter as ctk


class View():
    
    def __init__(self):
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.root = ctk.CTk()
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{str(self.width)}x{str(self.height)}")
        
        self.controller = Controller(self)
        
        self.root.after(0, lambda:self.root.state('zoomed'))

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        fonte = 'Yu Gothic UI Semibold'

        #? Frame de Login/Logon-----------------------------------------------------------------------------------
        self.login = ctk.CTkFrame(self.root)
        self.login.grid(row=0, column=0, sticky="nsew")

        self.login.columnconfigure([0, 2], weight=1)
        self.login.columnconfigure(1, weight=3)
        
        self.login.rowconfigure(0, weight=3)
        self.login.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.login.rowconfigure(5, weight=2)
        
        #!__________________________Tela_de_Login__________________________
        titulo = ctk.CTkLabel(self.login,
                              text="Tela de Login",
                              font=(fonte, 50))
        
        userLabel = ctk.CTkLabel(self.login,
                                 text="Insira seu usuário",
                                 font=(fonte, 20))
        userInput = ctk.CTkEntry(self.login,
                                 width=500,
                                 font=(fonte, 20))
        senhaLabel = ctk.CTkLabel(self.login,
                                  text="Insira sua senha",
                                  font=(fonte, 20))
        senhaInput = ctk.CTkEntry(self.login,
                                  width=500,
                                  font=(fonte, 20))
        
        botoesFrame = ctk.CTkFrame(self.login)
        limpar = ctk.CTkButton(botoesFrame,
                               text="Limpar",
                               font=(fonte, 15),
                               command=lambda: self.limpar(userInput,
                                                           senhaInput))
        salvar = ctk.CTkButton(botoesFrame,
                               text="Salvar",
                               font=(fonte, 15),
                               command=lambda: self.salvar(userInput,
                                                           senhaInput))
        
        titulo.grid(row=0,
                    column=1,
                    sticky="nsew")
        userLabel.grid(row=1,
                       column=1,
                       sticky="new")
        userInput.grid(row=2,
                       column=1,
                       sticky="new")
        senhaLabel.grid(row=3,
                        column=1,
                        sticky="new")
        senhaInput.grid(row=4,
                       column=1,
                       sticky="new")
        botoesFrame.grid(row=5,
                         column=1)
        limpar.pack(side="left")
        salvar.pack(side="left")


        #? Frame de Processos-----------------------------------------------------------------------------------
        self.processos = ctk.CTkFrame(self.root)
        self.processos.grid(row=0, column=0, sticky="nsew")

        self.processos.columnconfigure([0, 1], weight=1)
        
        self.processos.rowconfigure(0, weight=1)
        self.processos.rowconfigure(1, weight=9)
        
        #!__________________________Tela_de_Processos__________________________
        
        segundosFrame = ctk.CTkFrame(self.processos)
        segundosLabel = ctk.CTkLabel(segundosFrame,
                                     text="SEGUNDOS -> ",
                                     font=(fonte, 30))
        secsNumLabel = ctk.CTkLabel(segundosFrame,
                                    text="00",
                                    font=(fonte, 30))
        
        programaFrame = ctk.CTkFrame(self.processos)
        programaFrame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        programaLabel = ctk.CTkLabel(programaFrame,
                                     text="PROGRAMA",
                                     font=(fonte, 25))
        progs1 = ctk.CTkLabel(programaFrame,
                              text="Excel",
                              font=(fonte, 20))
        progs2 = ctk.CTkLabel(programaFrame,
                              text="Word",
                              font=(fonte, 20))
        progs3 = ctk.CTkLabel(programaFrame,
                              text="Powerpoint",
                              font=(fonte, 20))
        progs4 = ctk.CTkLabel(programaFrame,
                              text="Google Chrome",
                              font=(fonte, 20))
        progs5 = ctk.CTkLabel(programaFrame,
                              text="Ibis Paint",
                              font=(fonte, 20))

        estadoFrame = ctk.CTkFrame(self.processos)
        estadoFrame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        estadoLabel = ctk.CTkLabel(estadoFrame,
                                   text="ESTADO",
                                   font=(fonte, 25))
        estd1 = ctk.CTkLabel(estadoFrame,
                             text="ESPERA",
                             font=(fonte, 20))
        estd2 = ctk.CTkLabel(estadoFrame,
                             text="ESPERA",
                             font=(fonte, 20))
        estd3 = ctk.CTkLabel(estadoFrame,
                             text="PRONTO",
                             font=(fonte, 20))
        estd4 = ctk.CTkLabel(estadoFrame,
                             text="EXECUÇÃO",
                             font=(fonte, 20))
        estd5 = ctk.CTkLabel(estadoFrame,
                             text="PRONTO",
                             font=(fonte, 20))

        segundosFrame.grid(row=0,
                           column=0,
                           sticky="nws")
        segundosLabel.pack(side="left")
        secsNumLabel.pack(side="left")

        programaFrame.grid(row=1,
                           column=0,
                           sticky="nsew")
        programaLabel.grid(row=0,
                           column=0)
        progs1.grid(row=1,
                    column=0)
        progs2.grid(row=2,
                    column=0)
        progs3.grid(row=3,
                    column=0)
        progs4.grid(row=4,
                    column=0)
        progs5.grid(row=5,
                    column=0)
        
        estadoFrame.grid(row=1,
                         column=1,
                         sticky="nsew")
        estadoLabel.grid(row=0,
                         column=0)
        estd1.grid(row=1,
                   column=0)
        estd2.grid(row=2,
                   column=0)
        estd3.grid(row=3,
                   column=0)
        estd4.grid(row=4,
                   column=0)
        estd5.grid(row=5,
                   column=0)
        

        #!__________________________Início_do_Programa__________________________
        self.processos.tkraise()
        self.root.mainloop()
    
    #!______________________________________________________________________________________________________________
    
    def limpar(self, user, senha) -> None:
        user.delete(0, ctk.END)
        senha.delete(0, ctk.END)
        return None
    
    def salvar(self, userEntry, senhaEntry) -> None:
        user = userEntry.get()
        senha = senhaEntry.get()
        self.controller.salvar({"user":user, "senha":senha})
        self.limpar(userEntry, senhaEntry)
        return None
    

if __name__ == "__main__":
    View()
