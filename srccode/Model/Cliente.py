import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///mybank.db', echo=False)
conn = engine.connect()

Base = orm.declarative_base()

class cliente(Base):
    __tablename__= 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.CHAR, nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

class TipoConta:
    __tablename__= 'tipoconta'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)

class Contabancaria(Base):
    __tablename__= 'contabancaria'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipoconta.id'), nullable=False)
    saldo_inicial = db.Column(db.Float, nullable=False)

Base.metadata.create_all(engine)