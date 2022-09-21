from cmath import isnan
import math
from sre_parse import State
import tkinter as tk
import tkinter.ttk as ttk
from typing_extensions import IntVar, Self
import sqlalchemy as db
import sqlalchemy.orm as orm
import model
from tkinter import N, messagebox
from utils import *

class CriarNovaConta(tk.Tk):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    conn = engine.connect()
    conta_bancaria = {}
    def __init__(self):
        super().__init__()
        self.title("MyBank app")
        self.geometry('700x680')
        self.conta_bancaria = {
            'cpf_cliente': tk.StringVar(),
            'tipo_conta': tk.StringVar(),
            'saldo_inicial': tk.DoubleVar()
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
        self.create_widget(tk.Label, text='Cpf: ')
        self.create_widget(tk.Entry, textvariable=self.conta_bancaria.get('cpf_cliente'))
        self.create_widget(tk.Label, text='Tipo de conta: ')
        combo_type = None
        combo_type = self.create_widget(ttk.Combobox, textvariable=self.conta_bancaria.get('tipo_conta'), )
        combo_type['values']=('Poupança', 'Corrente', 'Investimento')
        combo_type['state']='readonly'
        self.create_widget(tk.Label, text='Deposite um valor inicial: ')
        self.create_widget(tk.Entry, textvariable=self.conta_bancaria.get('saldo_inicial'))
        self.create_widget(tk.Button, text='Criar conta', command=self.validateAll)
    
    def validateAll(self):
        validation = True
        validation = (validation and self.validate_cpf(list(self.conta_bancaria.items())[0][1].get())
        and self.validate_init_saldo(list(self.conta_bancaria.items())[2][1].get())
        and self.validate_tipo_conta(list(self.conta_bancaria.items())[1][1].get()))
        if validation:
            self.saveForm()

    def validate_cpf(self, cpf):
        if validate_cpf(cpf):
            try:
                client = self.session.query(model.Cliente.nome).where(model.Cliente.cpf == cpf)
                test = client[0]
                try:
                    alreay_exists_account = self.session.query(model.ContaBancaria.cliente_id).where(model.ContaBancaria.cliente_id == cpf)
                    test_account = alreay_exists_account[0]
                    messagebox.showwarning('Warning', 'O cpf informado já possui uma conta cadastrada!')
                    return False
                except:
                    return True
            except:
                messagebox.showwarning('Warning', 'Verifique se o cpf pertence há um cliente já cadastrado!')
                return False
        else:
            messagebox.showwarning('Warning', 'Insira um cpf válido!')
            return False
    
    def validate_init_saldo(self, saldo):
        if saldo >= 0:
            if not math.isnan(saldo):
                return True
            else:
                messagebox.showwarning('Warning', 'Informe um valor de saldo válido!')
                return False
        else:
            messagebox.showwarning('Warning', 'Deposite um saldo inicial válido (maior ou igual a 0)!')
            return False
    
    def validate_tipo_conta(self, tipo):
        if tipo == '':
            messagebox.showwarning('Warning', 'Selecione um tipo de conta!')
            return False
        else:
            return True
            
    def saveForm(self):
        conta_properties = []
        for k, v in self.conta_bancaria.items():
            conta_properties.append(v.get())
        cliente_cpf = self.session.query(model.Cliente.cpf).where(model.Cliente.cpf == conta_properties[0])
        tipo_conta_id = self.session.query(model.TipoConta.id).where(model.TipoConta.tipo == conta_properties[1])
        conta_final = model.ContaBancaria(cliente_id=cliente_cpf[0][0], tipo_conta_id=tipo_conta_id[0][0], saldo_inicial=conta_properties[2] )
        self.session.add(conta_final)
        self.session.commit()
        messagebox.showinfo('Confirmação', 'A conta foi criada com sucesso!')
        
if __name__=='__main__':
    screen = CriarNovaConta()
    screen.mainloop()