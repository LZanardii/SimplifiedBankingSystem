import numbers
from sre_parse import State
import tkinter as tk
import tkinter.ttk as ttk
from typing_extensions import IntVar, Self
import sqlalchemy as db
import sqlalchemy.orm as orm


class CriarNovaConta(tk.Tk):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    conta_bancaria = {}
    numbers = []
    def __init__(self):
        super().__init__()
        self.title("MyBank app")
        self.geometry('700x680')
        self.conta_bancaria = {
            'cpf_cliente': tk.StringVar(),
            'tipo_conta': tk.StringVar(),
            'saldo_inicial': tk.DoubleVar()
        }
        self.numbers = [0,1,2,3,4,5,6,8,9]
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
        combo_type['values']=('Conta poupança', 'Conta Corrente', 'Conta de Investimentos')
        combo_type['state']='readonly'
        self.create_widget(tk.Label, text='Deposite um valor inicial: ')
        self.create_widget(tk.Entry, textvariable=self.conta_bancaria.get('saldo_inicial'))
        self.create_widget(tk.Button, text='Criar conta', command=self.validateAll)
    
    def validateAll(self):
        validation = True
        print(list(self.conta_bancaria.items())[0])
        validation = validation and self.validate_cpf(list(self.conta_bancaria.items())[0][1])
        if validation:
            #TODO chamada função salvamento
            print('true')
            return 'ds'
        else:
            #TODO chamada warning msg
            print('false')
            return 'sdo'
        return 'a'

    def validate_cpf(self, cpf):
        valid = True
        for char in cpf.get():
            if char in self.numbers == False:
                valid = False
        print(cpf.get())
        return valid

if __name__=='__main__':
    screen = CriarNovaConta()
    screen.mainloop()