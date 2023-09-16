#!/usr/bin/python3
""" Write a python file that contains the class definition of a State\
        and an instance Base = declarative_base()"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://{}:{}@localhost:{}/{}'.format("saddy", "clear", 3306, "hbtn_0e_4_usa"), pool_pre_ping=True)
engine.connect()
Base = declarative_base()


class States(Base):
    """ States class that inherites from Base class """
    __tablename__ = 'states'
    id = Column(Integer, AUTO_INCREMENT=True, PRIMARY_KEY=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
