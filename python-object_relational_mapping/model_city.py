#!/usr/bin/python3
"""
model_city

This module defines the City class which maps to the 'cities' table
in the MySQL database. Each city belongs to a state via a foreign key.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """City class for MySQL cities table, inherits from Base"""
    
    __tablename__ = "cities"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
