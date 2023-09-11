#!/usr/bin/env python3
"""
SQLalcheme model for User
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String


class User(Base):
    """ User class declaration
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_pasword = Column(String(250))
    session_id = (String(250), default=None)
    reset_token = (String(250), default=None)
