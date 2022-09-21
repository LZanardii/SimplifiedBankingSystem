from datetime import datetime
import sqlalchemy.orm as orm
import sqlalchemy as db
from model import TipoConta, TipoMovimentacao, Cliente


engine = db.create_engine('sqlite:///myBank.db', echo=True)
conn = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

# Insert
try:
    tc1 = TipoConta(tipo='Poupança')
    tc2 = TipoConta(tipo='Corrente')
    tc3 = TipoConta(tipo='Investimento')
    tm1 = TipoMovimentacao(tipo='Depósito')
    tm2 = TipoMovimentacao(tipo='Saque')
    tm3 = TipoMovimentacao(tipo='Aplicar Juros')
    data = datetime(2001, 1, 1)
    cl2 = Cliente(cpf='03690128013', nome='Pedro', sexo='M', data_nascimento=data)
    cl3 = Cliente(cpf='05046035073', nome='Pedro', sexo='M', data_nascimento=data)
    session.add(tc1)
    session.add(tc2)
    session.add(tc3)
    session.add(tm1)
    session.add(tm2)
    session.add(tm3)
    session.add(cl2)
    session.add(cl3)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()