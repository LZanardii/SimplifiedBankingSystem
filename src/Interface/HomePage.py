from cProfile import label
from cgitb import text
from sqlite3 import Row
from textwrap import fill
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from turtle import bgcolor, onclick

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
        btn_cadastro = Button(up_frame, text='Cadastrar usuário', pady=5, border=3, bg="#02c72a", command=abrir_cadastro_click).place(relx=.5, rely=.4, anchor=CENTER)
        btn_nova_conta = Button(middle_frame, text='Criar nova conta', pady=5, border=3, bg="#02c72a").place(relx=.5, rely=.5, anchor=CENTER)
        btn_login = Button(down_frame, text='Login em conta existente', pady=5, border=3, bg="#02c72a").place(relx=.5, rely=.6, anchor=CENTER)
        #TODO
        #Uma coisa que quero fazer quando tivermos o trabalho mais garantido de repente é adicionar uma imagem
        # "Mybank" a cima dos botões, se for fácil

    def start(self):
        self.mainloop()

    #Tava tentandof fazer com que ele desmontasse a tela atual para construir uma nova.
    def abrir_cadastro_click():
        self.forget(up_frame) 
        tela_cadastro = Frame(self)
        label(tela_cadastro, text='testestestestestes').pack(fill=BOTH)
    
if __name__=='__main__':
    screen = HomePage()
    screen.start()
