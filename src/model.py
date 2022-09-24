import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///myBank.db', echo=True)
conn = engine.connect()

Base = orm.declarative_base()

class Cliente(Base):
    __tablename__= 'cliente'
    cpf = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.CHAR, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

class ContaBancaria(Base):
    __tablename__= 'contaBancaria'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.String(14), db.ForeignKey('cliente.cpf'), nullable=False)
    tipo_conta_id = db.Column(db.Integer, db.ForeignKey('tipoConta.id'), nullable=False)
    saldo_inicial = db.Column(db.Float, nullable=False)
    
class TipoConta(Base):
    __tablename__= 'tipoConta'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)
    
class Movimentacao(Base):
    __tablename__= 'movimentacao'
    id = db.Column(db.Integer, primary_key=True)
    tipo_movimentacao_id = db.Column(db.Integer, db.ForeignKey('tipoMovimentacao.id'), nullable=False)
    conta_bancaria_id = db.Column(db.Integer, db.ForeignKey('contaBancaria.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    valor = db.Column(db.Float, nullable=False)

class TipoMovimentacao(Base):
    __tablename__= 'tipoMovimentacao'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False )

Cliente.conta_bancaria = orm.relationship('ContaBancaria', back_populates='cliente')
ContaBancaria.cliente = orm.relationship('Cliente', back_populates='conta_bancaria')

ContaBancaria.tipo_conta = orm.relationship('TipoConta', back_populates='contas')
TipoConta.contas = orm.relationship('ContaBancaria', back_populates='tipo_conta')

ContaBancaria.movimentacoes = orm.relationship('Movimentacao', back_populates='conta')
Movimentacao.conta = orm.relationship('ContaBancaria', back_populates='movimentacoes')

Movimentacao.tipo = orm.relationship('TipoMovimentacao', back_populates='movimentacoes')
TipoMovimentacao.movimentacoes = orm.relationship('Movimentacao', back_populates='tipo')

Base.metadata.create_all(engine)