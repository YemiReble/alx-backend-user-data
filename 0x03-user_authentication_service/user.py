#!/usr/bin/env python3
"""
SQLalcheme model for User
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User class declaration
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_pasword = Column(String(250))
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    # def __repr__(self):
    #    return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    # self.email, self.hashed_password, self.session_id, self.reset_token)
