from cProfile import label
from cgitb import text
from sqlite3 import Row
from textwrap import fill
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from turtle import bgcolor, onclick
import cadastro_usuario_page
import criar_nova_conta_page

class HomePage(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("MyBank app")
        self.geometry('700x680')
        self.create_widgets()
    
    #se tirar a parte do command, vai ver a tela abrindo direitinho!
    def create_widgets(self):
        up_frame = Frame(self).pack(side=TOP, fill=X)
        middle_frame = Frame(self).pack(fill=BOTH, expand = True)
        down_frame = Frame(self).pack(side=BOTTOM, expand=True)
        btn_cadastro = Button(up_frame, text='Cadastrar usuário', pady=5, border=3, bg="#02c72a", command=self.abrir_cadastro_click).place(relx=.5, rely=.4, anchor=CENTER)
        btn_nova_conta = Button(middle_frame, text='Criar nova conta', pady=5, border=3, bg="#02c72a").place(relx=.5, rely=.5, anchor=CENTER)
        btn_login = Button(down_frame, text='Login em conta existente', pady=5, border=3, bg="#02c72a").place(relx=.5, rely=.6, anchor=CENTER)
        #TODO
        #Uma coisa que quero fazer quando tivermos o trabalho mais garantido de repente é adicionar uma imagem
        # "Mybank" a cima dos botões, se for fácil
        
    def abrir_cadastro_click(self):
        cadastro_usuario_page.CadastroUsuario()
    
    def criar_nova_conta_click(self):
        criar_nova_conta_page.CriarNovaConta()
        
    
if __name__=='__main__':
    screen = HomePage()
    screen.mainloop()
