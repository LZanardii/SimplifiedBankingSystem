import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///orm.db', echo=False)
conn = engine.connect()

Base = orm.declarative_base()

class Contabancaria(Base):
    __tablename__= 'contaBancaria'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipoConta.id'), nullable=False)
    saldo_inicial = db.Column(db.Float, nullable=False)

Base.metadata.create_all(engine)