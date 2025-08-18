
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
        
        self.root.columnconfigure([0, 2], weight=1)
        self.root.columnconfigure(1, weight=3)
        
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.root.rowconfigure(5, weight=2)
        fonte = 'Yu Gothic UI Semibold'
        
        titulo = ctk.CTkLabel(self.root,
                              text="Tela de Login",
                              font=(fonte, 50))
        
        userLabel = ctk.CTkLabel(self.root,
                                 text="Insira seu usuário",
                                 font=(fonte, 20))
        userInput = ctk.CTkEntry(self.root,
                                 width=500,
                                 font=(fonte, 20))
        senhaLabel = ctk.CTkLabel(self.root,
                                  text="Insira sua senha",
                                  font=(fonte, 20))
        senhaInput = ctk.CTkEntry(self.root,
                                  width=500,
                                  font=(fonte, 20))
        
        botoesFrame = ctk.CTkFrame(master=self.root)
        limpar = ctk.CTkButton(master=botoesFrame,
                               text="Limpar",
                               command=lambda: self.limpar(userInput,
                                                           senhaInput),
                               font=(fonte, 15))
        salvar = ctk.CTkButton(master=botoesFrame,
                               text="Salvar",
                               command=lambda: self.salvar(userInput,
                                                           senhaInput),
                               font=(fonte, 15))
        
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