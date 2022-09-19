from tkinter import *

class HomePage:
    def __init__(self) -> None:
        self.home_interface = Tk()
        self.home_interface.title("MyBank app")
        self.home_interface.geometry('700x680')
        btn_cadastro = Button(self.home_interface, text='Cadastrar usuário')
        btn_nova_conta = Button(self.home_interface, text='Criar nova conta')
        btn_login = Button(self.home_interface, text='Login em conta existente')

    def start(self):
        self.home_interface.mainloop()
    
    def addHandlers(self):
        

    
    