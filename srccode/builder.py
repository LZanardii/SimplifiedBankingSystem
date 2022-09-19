import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///orm.db', echo=False)
conn = engine.connect()

Base = orm.declarative_base()

class cliente(Base):
    __tablename__= 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.CHAR, nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

class tipo_conta:
    __tablename__= 'tipoConta'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)

class conta_bancaria(Base):
    __tablename__= 'contaBancaria'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_tipo_conta = db.Column(db.Integer, db.ForeignKey('tipoConta.id'), nullable=False)
    saldo_inicial = db.Column(db.Float, nullable=False)

class tipo_movimentacao(Base):
    __tablename__= 'tipoMovimentacao'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False )

class movimentacao(Base):
    __tablename__= 'movimentacao'
    id = db.Column(db.Integer, primary_key=True)
    id_tipo_movimentacao = db.Column(db.Integer, db.ForeignKey('tipoMovimentacao.id'), nullable=False)
    id_conta_bancaria = db.Column(db.Integer, db.ForeignKey('contaBancaria.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    valor = db.Column(db.Float, nullable=False)

conta_bancaria.cliente = orm.relationship('cliente', back_populates='conta_bancaria')
cliente.conta_bancaria = orm.relationship('contaBancaria', back_populates='cliente')

conta_bancaria.tipo = orm.relationship('tipoConta', back_populates='contas')
tipo_conta.contas = orm.relationship('contaBancaria', back_populates='tipo')

conta_bancaria.movimentacoes = orm.relationship('movimentacao', back_populates='conta')
movimentacao.conta = orm.relationship('contaBancaria', back_populates='movimentacoes')

movimentacao.tipo = orm.relationship('tipoMovimentacao', back_populates='movimentacoes')
tipo_movimentacao.movimentacoes = orm.relationship('movimentacao', back_populates='tipo')

Base.metadata.create_all(engine)