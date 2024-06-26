#!/usr/bin/python3
"""This module declares an instance of Declarative and also
defines a class that inherits from the declarative base class"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base = declarative_base()


class State(Base):
    """This class represents a table in a mysql database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
