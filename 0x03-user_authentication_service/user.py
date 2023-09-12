#!/usr/bin/env python3
"""
SQLalcheme model for User
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User class declaration
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True)
    hashed_pasword = Column(String(250))
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
