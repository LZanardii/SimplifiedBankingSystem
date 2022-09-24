import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlalchemy as db
import sqlalchemy.orm as orm
import model
from datetime import datetime
from tkcalendar import DateEntry
from utils import *
import math

class MyBankApp(tk.Tk):
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MyBank app")
        self.geometry('500x600')
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {} 
  
        for F in (HomePage, CadastroUsuario, CriarNovaConta, Operacoes, Deposito):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class HomePage(tk.Frame):
    ctr = {}
    
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.create_widgets()
        
        self.ctr = controller
    
    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(20, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Cadastrar usuário', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(CadastroUsuario))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Criar nova conta', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(CriarNovaConta))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Operações', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(Operacoes))
class CadastroUsuario(tk.Frame):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    cliente = {}
    ctr = {}

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.cliente = {
            'nome': tk.StringVar(),
            'cpf': tk.StringVar(),
            'sexo': tk.StringVar(),
            'data_nascimento': tk.StringVar()
        }
        
        self.ctr = controller
        self.create_widgets()

    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(20, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Nome')
        self.create_widget(tk.Entry, textvariable=self.cliente.get('nome'))
        self.create_widget(tk.Label, text='CPF')
        self.create_widget(tk.Entry, textvariable=self.cliente.get('cpf'))
        self.create_widget(tk.Label, text='Sexo')
        self.create_widget(ttk.Combobox, textvariable=self.cliente.get('sexo'), values=('M', 'F'), state='readonly')
        self.create_widget(tk.Label, text='Data de Nascimento')
        self.create_widget(DateEntry, textvariable=self.cliente.get('data_nascimento'))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Salvar', command=self.save_data)
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Retornar', pady=5, border=3, command = lambda : self.ctr.show_frame(HomePage))
        

    def save_data(self):
        conn = self.engine.connect()
        Session = orm.sessionmaker(bind=self.engine)
        session = Session()
        cliente_final = model.Cliente()
            
        try:
            for k, v in self.cliente.items():
                if (len(v.get()) == 0):
                    raise Exception("Campo {} não pode ser nulo".format(k))
                setattr(cliente_final, k, v.get())
            
            cliente_final.data_nascimento = datetime.strptime(cliente_final.data_nascimento, '%m/%d/%Y')
            
            if (validate_cpf(cliente_final.cpf) == False):
                raise Exception("Campo CPF está inválido")
            
            session.add(cliente_final)
            session.commit()
            session.close()
            messagebox.showinfo('Sucesso!','Cliente cadastrado com sucesso.')
                
        except Exception as e:
            messagebox.showwarning('Cuidado!', '''Erro ao cadastrar novo Cliente! Revise os dados inseridos.
{}
                                   '''.format(e))         
class CriarNovaConta(tk.Frame):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    conn = engine.connect()
    conta_bancaria = {}
    ctr = {}
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        self.conta_bancaria = {
            'cpf_cliente': tk.StringVar(),
            'tipo_conta': tk.StringVar(),
            'saldo_inicial': tk.DoubleVar()
        }

        self.ctr = controller
        self.create_widgets()
    
    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(20, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Cpf: ')
        self.create_widget(tk.Entry, textvariable=self.conta_bancaria.get('cpf_cliente'))
        self.create_widget(tk.Label, text='Tipo de conta: ')
        combo_type = self.create_widget(ttk.Combobox, textvariable=self.conta_bancaria.get('tipo_conta'), )
        combo_type['values']=('Poupança', 'Corrente', 'Investimento')
        combo_type['state']='readonly'
        self.create_widget(tk.Label, text='Deposite um valor inicial: ')
        self.create_widget(tk.Entry, textvariable=self.conta_bancaria.get('saldo_inicial'))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Criar conta', command=self.validateAll)
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Retornar', pady=5, border=3, command = lambda : self.ctr.show_frame(HomePage))
       
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
                Session = orm.sessionmaker(bind=self.engine)
                self.session = Session()
                client = self.session.query(model.Cliente.nome).where(model.Cliente.cpf == cpf)
                client[0]
                try:
                    alreay_exists_account = self.session.query(model.ContaBancaria.cliente_id).where(model.ContaBancaria.cliente_id == cpf)
                    alreay_exists_account[0]
                    messagebox.showwarning('Cuidado!', 'O cpf informado já possui uma conta cadastrada!')
                    self.session.close()
                    return False
                except Exception:
                    self.session.close()
                    return True
            except Exception:
                messagebox.showwarning('Cuidado!', 'Verifique se o cpf pertence a um cliente já cadastrado!')
                self.session.close()
                return False
        else:
            messagebox.showwarning('Cuidado!', 'Insira um cpf válido!')
            return False
    
    def validate_init_saldo(self, saldo):
        if not math.isnan(saldo):
            if saldo >= 0:
                return True
            else:
                messagebox.showwarning('Cuidado!', 'Deposite um saldo inicial válido (maior ou igual a 0)!')
                return False
        else:
            messagebox.showwarning('Cuidado!', 'Informe um saldo inicial válido!')
            return False
    
    def validate_tipo_conta(self, tipo):
        if tipo == '':
            messagebox.showwarning('Cuidado!', 'Selecione um tipo de conta!')
            return False
        else:
            return True
            
    def saveForm(self):
        Session = orm.sessionmaker(bind=self.engine)
        self.session = Session()
        
        conta_properties = []
        for k, v in self.conta_bancaria.items():
            conta_properties.append(v.get())
        cliente_cpf = self.session.query(model.Cliente.cpf).where(model.Cliente.cpf == conta_properties[0])
        tipo_conta_id = self.session.query(model.TipoConta.id).where(model.TipoConta.tipo == conta_properties[1])
        conta_final = model.ContaBancaria(cliente_id=cliente_cpf[0][0], tipo_conta_id=tipo_conta_id[0][0], saldo_inicial=conta_properties[2])
        
        self.session.add(conta_final)
        self.session.commit()
        self.session.close()
        messagebox.showinfo('Confirmação', 'A conta foi criada com sucesso!')        
class Operacoes(tk.Frame):
    prt = {}
    ctr = {}

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.prt = parent
        self.ctr = controller
        self.ctr = controller
        self.create_widgets()
    
    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(20, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Depósito', pady=5, border=3, bg="#02c72a",command = lambda : self.ctr.show_frame(Deposito))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Saque', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(HomePage))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Aplicar Juros', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(HomePage))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Extrato', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(HomePage))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Retornar', pady=5, border=3, command = lambda : self.ctr.show_frame(HomePage))     
class Deposito(tk.Frame):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    conn = engine.connect()
    prt = {}
    ctr = {}

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.login = {
            'cpf_cliente': tk.StringVar(),
            'nome': tk.StringVar(),
            'conta': tk.StringVar(),
            'tipo_conta': tk.IntVar(),
            'saldo_inicial': tk.DoubleVar()
        }
        
        self.deposito = {
            'deposito': tk.IntVar(),
        }
    
        self.prt = parent
        self.ctr = controller
        self.create_widgets()
       

    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(20, 0))
        return elem
    
    def create_widgets(self):
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Informe o cpf que deseja realizar o depósito e \n automagicamente os campos abaixo serão preenchidos' )
        self.create_widget(tk.Label, text='Cpf:' )
        self.create_widget(tk.Entry, textvariable=self.login.get('cpf_cliente'))
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Nome:' )
        self.create_widget(tk.Entry, textvariable=self.login.get('nome'), state='readonly')
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Conta:' )
        self.create_widget(tk.Entry, textvariable=self.login.get('conta'), state='readonly')
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Tipo de conta:' )
        self.create_widget(tk.Entry, textvariable=self.login.get('tipo_conta'), state='readonly' )
        self.create_widget(tk.Label)
        self.create_widget(tk.Label, text='Valor a Depositar:' )
        self.create_widget(tk.Entry, textvariable=self.deposito.get('deposito'))
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Depositar', pady=5, border=3, command = self.depositar)
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Validar Conta', pady=5, border=3, command =self.validate_cpf_login)
        self.create_widget(tk.Label)
        self.create_widget(tk.Button, text='Retornar', pady=5, border=3, command = lambda : self.ctr.show_frame(Operacoes))
 
    def depositar(self):
        valor_a_depositar = list(self.deposito.items())[0][1].get()
        if (valor_a_depositar == 0):
            messagebox.showwarning('Cuidado!', 'O valor de depósito está zerado.')
        else:
            try:
                session = orm.sessionmaker(bind=self.engine)
                self.session = session()
                saldo = list(self.login.items())[4][1].get()
                self.session.query(model.ContaBancaria).where(model.ContaBancaria.id == list(self.login.items())[2][1].get()).update({model.ContaBancaria.saldo_inicial: saldo + valor_a_depositar})
            except Exception as e:
                print(e)  
       

    def validate_cpf_login(self):
        cpf = list(self.login.items())[0][1].get()
        if validate_cpf(cpf):
            try:
                session = orm.sessionmaker(bind=self.engine)
                self.session = session()
                cliente = self.session.query(model.Cliente.cpf, model.Cliente.nome,).where(model.Cliente.cpf == cpf)
                cliente[0]
                list(self.login.items())[1][1].set(cliente[0].nome)
                try:
                    conta_cliente = self.session.query(model.ContaBancaria.tipo_conta_id, model.ContaBancaria.id, model.ContaBancaria.saldo_inicial).where(model.ContaBancaria.cliente_id == cpf)
                    conta_cliente[0]                  
                    list(self.login.items())[2][1].set(conta_cliente[0].id)
                    list(self.login.items())[3][1].set(self.busca_tipo_conta(conta_cliente[0].tipo_conta_id))
                    list(self.login.items())[4][1].set(conta_cliente[0].saldo_inicial)
                    messagebox.showinfo('Sucesso!', 'Login efetuado.')
                    self.session.close()
                except Exception:
                    messagebox.showwarning('Cuidado!', 'O cpf informado pertence a um cliente cadastrado, porém o mesmo não possui uma conta!')
                    self.session.close()
                    return False
            except Exception:
                messagebox.showwarning('Cuidado!', 'CPF não cadastrado!')
                self.session.close()
                return False
        else:
            messagebox.showwarning('Warning', 'Insira um cpf válido!')
            return False 
    
    def busca_tipo_conta(self, id):
        session = orm.sessionmaker(bind=self.engine)
        self.session = session()
        tipo_conta = self.session.query(model.TipoConta.tipo).where(model.TipoConta.id == id)
        self.session.close()
        return tipo_conta[0].tipo
        



app = MyBankApp()
app.mainloop()

