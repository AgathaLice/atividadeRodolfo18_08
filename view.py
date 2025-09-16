
from controller import Controller

import customtkinter as ctk


class View():
    
    def __init__(self):
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.root = ctk.CTk()
        self.root.bind("<Escape>", self.sair)
        
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
        
        self.login.rowconfigure(0, weight=2)
        self.login.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.login.rowconfigure(5, weight=2)
        
        #!__________________________Tela_de_Login__________________________
        titulo = ctk.CTkLabel(self.login,
                              text="Tela de Login",
                              font=(fonte, 70))
        
        userLabel = ctk.CTkLabel(self.login,
                                 text="Insira seu usuário",
                                 font=(fonte, 40))
        userInput = ctk.CTkEntry(self.login,
                                 width=500,
                                 font=(fonte, 20))
        senhaLabel = ctk.CTkLabel(self.login,
                                  text="Insira sua senha",
                                  font=(fonte, 40))
        senhaInput = ctk.CTkEntry(self.login,
                                  width=500,
                                  font=(fonte, 20))
        
        
        botoesFrame = ctk.CTkFrame(self.login)
        
        limpar = ctk.CTkButton(botoesFrame,
                               text="Limpar",
                               font=(fonte, 20),
                               height=50,
                               command=lambda: self.limpar(userInput,
                                                           senhaInput))
        salvar = ctk.CTkButton(botoesFrame,
                               text="Salvar",
                               font=(fonte, 20),
                               height=50,
                               command=lambda: self.salvar(userInput,
                                                           senhaInput))
        entrar = ctk.CTkButton(botoesFrame,
                               text="Entrar",
                               font=(fonte, 20),
                               height=50,
                               command=lambda: self.entrar(userInput,
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
        limpar.pack(side="left", padx=(0, 25))
        salvar.pack(side="left", padx= 25)
        entrar.pack(side="left", padx=(25, 0))


        #? Frame de Processos-----------------------------------------------------------------------------------
        self.processos = ctk.CTkFrame(self.root)
        self.processos.grid(row=0, column=0, sticky="nsew")

        #! Processo, CPU, user, memória, estado
        self.processos.columnconfigure([0, 1, 2, 3, 4], weight=1)
        
        self.processos.rowconfigure(0, weight=1)
        self.processos.rowconfigure(1, weight=9)
        
        #!__________________________Tela_de_Processos__________________________
        
        segundosFrame = ctk.CTkFrame(self.processos)
        segundosLabel = ctk.CTkLabel(segundosFrame,
                                     text="SEGUNDOS:  ",
                                     font=(fonte, 40))
        self.secsNumLabel = ctk.CTkLabel(segundosFrame,
                                    text="--",
                                    font=(fonte, 40))
        
        #* Programa
        programaFrame = ctk.CTkFrame(self.processos,
                                     border_width=1,
                                     border_color="white")
        programaFrame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

        programaLabel = ctk.CTkLabel(programaFrame,
                                     text="PROGRAMA",
                                     font=(fonte, 30))
        progs1 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs2 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs3 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs4 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs5 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs6 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs7 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        progs8 = ctk.CTkLabel(programaFrame,
                              text="-----",
                              font=(fonte, 20))
        #* CPU
        cpuFrame = ctk.CTkFrame(self.processos,
                                border_width=1,
                                border_color="white")
        cpuFrame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

        cpuLabel = ctk.CTkLabel(cpuFrame,
                                text="CPU",
                                font=(fonte, 30))
        cpu1 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu2 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu3 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu4 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu5 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu6 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu7 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        cpu8 = ctk.CTkLabel(cpuFrame,
                               text="-----",
                               font=(fonte, 20))
        
        #* Usuário
        usuarioFrame = ctk.CTkFrame(self.processos,
                                    border_width=1,
                                    border_color="white")
        usuarioFrame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

        usuarioLabel = ctk.CTkLabel(usuarioFrame,
                                   text="USUÁRIO",
                                   font=(fonte, 30))
        user1 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user2 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user3 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user4 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user5 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user6 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user7 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        user8 = ctk.CTkLabel(usuarioFrame,
                             text="-----",
                             font=(fonte, 20))
        
        #* End. Memória
        endMemoriaFrame = ctk.CTkFrame(self.processos,
                                       border_width=1,
                                       border_color="white")
        endMemoriaFrame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

        endMemoriaLabel = ctk.CTkLabel(endMemoriaFrame,
                                   text="END. MEMÓRIA",
                                   font=(fonte, 30))
        memr1 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr2 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr3 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr4 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr5 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr6 = ctk.CTkLabel(endMemoriaFrame,
                            text="-----",
                             font=(fonte, 20))
        memr7 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        memr8 = ctk.CTkLabel(endMemoriaFrame,
                             text="-----",
                             font=(fonte, 20))
        
        #* Estado
        estadoFrame = ctk.CTkFrame(self.processos,
                                   border_width=1,
                                   border_color="white")
        estadoFrame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

        estadoLabel = ctk.CTkLabel(estadoFrame,
                                   text="ESTADO",
                                   font=(fonte, 30))
        estd1 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd2 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd3 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd4 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd5 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd6 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd7 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        estd8 = ctk.CTkLabel(estadoFrame,
                             text="-----",
                             font=(fonte, 20))
        

        segundosFrame.grid(row=0,
                           column=0,
                           sticky="nws")
        segundosLabel.pack(side="left")
        self.secsNumLabel.pack(side="left", padx=10)

        programaFrame.grid(row=1,
                           column=0,
                           sticky="nsew")
        programaLabel.grid(row=0,
                           column=0,
                           padx=(5, 0))
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
        progs6.grid(row=6,
                    column=0)
        progs7.grid(row=7,
                    column=0)
        progs8.grid(row=8,
                    column=0)
        
        cpuFrame.grid(row=1,
                      column=1,
                      sticky="nsew")
        cpuLabel.grid(row=0,
                      column=0,
                      padx=(5, 0))
        cpu1.grid(row=1,
                  column=0)
        cpu2.grid(row=2,
                  column=0)
        cpu3.grid(row=3,
                  column=0)
        cpu4.grid(row=4,
                  column=0)
        cpu5.grid(row=5,
                  column=0)
        cpu6.grid(row=6,
                    column=0)
        cpu7.grid(row=7,
                    column=0)
        cpu8.grid(row=8,
                    column=0)
        
        usuarioFrame.grid(row=1,
                          column=2,
                          sticky="nsew")
        usuarioLabel.grid(row=0,
                          column=0,
                          padx=(5, 0))
        user1.grid(row=1,
                   column=0)
        user2.grid(row=2,
                   column=0)
        user3.grid(row=3,
                   column=0)
        user4.grid(row=4,
                   column=0)
        user5.grid(row=5,
                   column=0)
        user6.grid(row=6,
                    column=0)
        user7.grid(row=7,
                    column=0)
        user8.grid(row=8,
                    column=0)
        
        endMemoriaFrame.grid(row=1,
                             column=3,
                             sticky="nsew")
        endMemoriaLabel.grid(row=0,
                             column=0,
                             padx=(5, 0))
        memr1.grid(row=1,
                   column=0)
        memr2.grid(row=2,
                   column=0)
        memr3.grid(row=3,
                   column=0)
        memr4.grid(row=4,
                   column=0)
        memr5.grid(row=5,
                   column=0)
        memr6.grid(row=6,
                    column=0)
        memr7.grid(row=7,
                    column=0)
        memr8.grid(row=8,
                    column=0)
        
        estadoFrame.grid(row=1,
                         column=4,
                         sticky="nsew")
        estadoLabel.grid(row=0,
                         column=0,
                         padx=(5, 0))
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
        estd6.grid(row=6,
                    column=0)
        estd7.grid(row=7,
                    column=0)
        estd8.grid(row=8,
                    column=0)
        

        #!__________________________Início_do_Programa__________________________
        self.levantar(self.login)
        self.root.mainloop()
    
    #!______________________________________________________________________________________________________________
    
    def levantar(self, tela) -> None:
        tela.tkraise()
        return None
    
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
    
    def entrar(self, userEntry, senhaEntry) -> None:
        user = userEntry.get()
        senha = senhaEntry.get()
        #? Fazer algo com o user
        self.levantar(self.processos)
        
    
    def timer(self):
        timeInfo = self.controller.timer()


    
    
    def sair(self, evento) -> None:
        self.controller.sair(evento)
        return None