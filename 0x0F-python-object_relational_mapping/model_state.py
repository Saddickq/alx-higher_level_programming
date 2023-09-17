#!/usr/bin/python3
""" Write a python file that contains the class definition of a State\
        and an instance Base = declarative_base()"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ States class that inherites from Base class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
