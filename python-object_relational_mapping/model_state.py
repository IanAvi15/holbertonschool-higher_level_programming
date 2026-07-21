#!/usr/bin/python3
"""Module that defines the State class, mapped to the states
table, using SQLAlchemy's declarative base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state, linked to the MySQL table states."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
