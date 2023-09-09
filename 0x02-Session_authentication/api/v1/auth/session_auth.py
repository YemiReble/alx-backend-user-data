#!/usr/bin/env python3
""" User Session authentication mechanism
"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ User Session Class
    """
    user_id_by_session_id = {}

    def __init__(self):
        """ User Session-Initialization
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """ Function that create session
        """
        if user_id is None:
            return None
        elif not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid4())
            self.user_id_by_session_id = {session_id: user_id}
            return session_id  # self.user_id_by_session_id
