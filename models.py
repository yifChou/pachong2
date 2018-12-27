from sqlalchemy import create_engine,MetaData,Column,Integer,String,Table,ForeignKey,UniqueConstraint,Index,TIMESTAMP,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
import time
engine  = create_engine("mysql+pymysql://root:8597121@127.0.0.1:3306/test", max_overflow=5)
Base = declarative_base()
class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer,primary_key=True)
    musicid =  Column(String(30))
    title = Column(String(50))
    image = Column(String(250))
    singer = Column(String(30),unique=True)
    album = Column(String(150))
    comments = Column(String(30))
    publishdate = Column(String(50))

def init_db():
    Base.metadata.create_all(engine)
def drop_db():
    Base.metadata.drop_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
