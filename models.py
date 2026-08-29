from typing import Optional
import datetime

from sqlalchemy import Date, DateTime, Identity, Integer, PrimaryKeyConstraint, String, Text, UniqueConstraint, text, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Empresas(Base):
    __tablename__ = 'empresas'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='empresas_pkey'),
        UniqueConstraint('email', name='empresas_email_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_empresa: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    data_criação: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

class Empresas2(Base):
    __tablename__ = 'empresas2'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='empresas2_pkey'),
        UniqueConstraint('email', name='empresas2_email_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_empresa: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    data_criação: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Test(Base):
    __tablename__ = 'test'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='test_pkey'),
        UniqueConstraint('email', name='test_email_key')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False)
    criacao: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text('now()'))
    idade: Mapped[int] = mapped_column(Numeric, default = 0, nullable=True)
