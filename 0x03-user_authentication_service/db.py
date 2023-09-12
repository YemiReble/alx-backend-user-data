#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hash_password: str):
        """ Return User Object
        """
        self.id = User.id
        User.email = email
        User.hash_password = hash_password

    def find_user_by(self, **kwargs: str):
        """ Find User by their info
        """
        query = query(User).filter(User.id.in_(kwargs.values()))
        if user_data is None or query is None:
            raise NoResultFound
        if not isinstance(user_data, str):
            raise InvalidRequestError
        return query.first()
