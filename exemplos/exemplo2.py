from sqlalchemy import Column, Date, Integer, String, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    ...

class test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable= True)
    email = Column(String, nullable= True)
    criacao = Column(Date, server_default= func.now())