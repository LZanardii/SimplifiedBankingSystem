import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///orm.db', echo=False)
conn = engine.connect()

Base = orm.declarative_base()

class TipoConta:
    __tablename__= 'tipoConta'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)

Base.metadata.create_all(engine)