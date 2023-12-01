#!/usr/bin/python3
""" pyhton file that contains the class definition of a state
and an instance """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ Class City that inherits from Base """

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
