#!/usr/bin/python3
"""Module that defines the City class, mapped to the cities
table, using SQLAlchemy's declarative base.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city, linked to the MySQL table cities."""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
