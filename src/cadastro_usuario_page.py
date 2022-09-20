import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlalchemy as db
import sqlalchemy.orm as orm
import model

class CadastroUsuario(tk.Tk):
    engine = ""
    cliente = {}

    def __init__(self):
        super().__init__()
        self.title("MyBank app")
        self.geometry('700x680')
        self.engine = db.create_engine('sqlite:///myBank.db', echo=True)
        
        self.cliente = {
            'nome': tk.StringVar(),
            'cpf': tk.StringVar(),
            'sexo': tk.StringVar(),
            'data_nascimento': tk.StringVar()
        }

        Session = orm.sessionmaker(bind=self.engine)
        self.session = Session()
        self.create_widgets()

    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(10, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label, text='Nome')
        self.create_widget(tk.Entry, textvariable=self.cliente.get('nome'))
        self.create_widget(tk.Label, text='CPF')
        self.create_widget(tk.Entry, textvariable=self.cliente.get('cpf'))
        self.create_widget(tk.Label, text='Sexo')
        self.create_widget(ttk.Combobox, textvariable=self.cliente.get('sexo'), values=('M', 'F'), state='readonly')
        self.create_widget(tk.Label, text='Data de Nascimento')
        self.create_widget(ttk.Entry, textvariable=self.cliente.get('data_nascimento'))
        self.create_widget(tk.Button, text='Salvar', command=self.save_data)

    def save_data(self):
        try:
            cliente_values = []
            for k, v in self.cliente.items():
                cliente_values.append(v.get())
            cliente_final = model.Cliente(nome=cliente_values[0], cpf=cliente_values[1], sexo=cliente_values[2], data_nascimento=cliente_values[3])
            self.session.add(cliente_final)
            self.session.commit()
        except:
            messagebox.showwarning('Warning', 'Erro ao cadastrar novo Cliente! Revise os dados inseridos')
    
if __name__=='__main__':
    screen = CadastroUsuario()
    screen.mainloop()
