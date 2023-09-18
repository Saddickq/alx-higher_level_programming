#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py\
        that contains the class definition of a City."""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """ City class which inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
