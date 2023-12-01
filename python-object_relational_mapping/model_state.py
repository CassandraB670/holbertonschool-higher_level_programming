#!/usr/bin/python3
""" pyhton file that contains the class definition of a state
and an instance """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class state that inherits from Base """

    __tablename__ = "states"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
