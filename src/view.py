import tkinter as tk
from tkinter import ttk
from ast import Raise
from http import client
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlalchemy as db
import sqlalchemy.orm as orm
import model
from datetime import datetime
from tkcalendar import DateEntry
from utils import validateCpf
  

class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MyBank app")
        self.geometry('700x680')
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {} 
  
        for F in (HomePage, CadastroUsuario):
  
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

        elem.pack(anchor='w', padx=(10, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Button, text='Cadastrar usuário', pady=5, border=3, bg="#02c72a", command = lambda : self.ctr.show_frame(CadastroUsuario))
        self.create_widget(tk.Button, text='Criar nova conta', pady=5, border=3, bg="#02c72a")
        self.create_widget(tk.Button, text='Login em conta existente', pady=5, border=3, bg="#02c72a")

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
        self.create_widget(DateEntry, textvariable=self.cliente.get('data_nascimento'))
        self.create_widget(tk.Button, text='Salvar', command=self.save_data)
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
            
            if (validateCpf(cliente_final.cpf) == False):
                raise Exception("Campo CPF está inválido")
            
            session.add(cliente_final)
            session.commit()
            session.close()
            answer = messagebox.showinfo('Sucesso!','Cliente cadastrado com sucesso.')
            # print(answer)
            # if answer == "ok":
            #     print("Entrei")
            #     lambda : self.ctr.show_frame(HomePage)
                
        except Exception as e:
            messagebox.showwarning('Cuidado!', '''Erro ao cadastrar novo Cliente! Revise os dados inseridos.
{}
                                   '''.format(e)) 

app = tkinterApp()
app.mainloop()