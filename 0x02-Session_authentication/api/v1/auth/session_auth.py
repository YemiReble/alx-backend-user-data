#!/usr/bin/env python3
""" User Session authentication mechanism
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ User Session Class
    """
    def __init__():
    """ User Session-Initialization
    """
    super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """ Function that create session
        """
        pass
