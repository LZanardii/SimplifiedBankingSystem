import tkinter as tk
import tkinter.ttk as ttk
import sqlalchemy as db
import sqlalchemy.orm as orm

class CadastroUsuario(tk.Tk):
    engine = db.create_engine('sqlite:///myBank.db', echo=True)
    
    def __init__(self):
        super().__init__()
        self.title("MyBank app")
        self.geometry('700x680')
        self.create_widgets()

        self.cliente = {
            'name': tk.StringVar(),
            'cpf': tk.StringVar(),
            'sexo': tk.StringVar(),
            'data_nascimento': tk.StringVar()
        }

        Session = orm.sessionmaker(bind=self.engine)
        self.session = Session()
        self.db_student = None
        
        self.create_widgets()

    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(10, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Label, text='Nome')
        self.create_widget(tk.Entry, textvariable=self.cliente.get('name'))
        self.create_widget(tk.Label, text='CPF')
        # self.create_widget(tk.Entry, textvariable=self.cliente.get('cpf'))
        self.create_widget(tk.Label, text='Sexo')
        # self.create_widget(ttk.Combobox, textvariable=self.cliente.get('sexo'), values=('M', 'F'), state='readonly')
        self.create_widget(tk.Label, text='Data de Nascimento')
        self.create_widget(tk.Button, text='Salvar', command=self.save_data)

    def save_data(self):
        print(self.cliente)
        # if self.db_student:
        #     # Save Student
        #     for k, v in self.var_student.items():
        #         setattr(self.db_student, k, v.get())

        #     # Save Addresses
        #     addrs = self.db_student.addresses
        #     for item in self.grid.get_children():
        #         addr_id = self.grid.item(item).get('tags')[0]
        #         addr = [row for row in addrs if getattr(row, 'id') == addr_id]
        #         if addr:
        #             item_val = dict(zip(self.grid_columns.keys(), self.grid.item(item).get('values')))
        #             for k in self.grid_columns.keys():
        #                 setattr(addr[0], k, item_val[k])

        #     self.session.commit()
    
if __name__=='__main__':
    screen = CadastroUsuario()
    screen.mainloop()
