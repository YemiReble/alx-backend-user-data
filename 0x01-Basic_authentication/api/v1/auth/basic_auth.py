#!/usr/bin/env python3
""" Basic Authentication Class that
that inherits from Auth Class from auth
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication Class that
        that inherits from Auth Class from auth
    """

    def __init__(self):
        """ Super function initialization
        """
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Function that returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if 'Basic ' not in authorization_header:
            return None
        else:
            base_64 = authorization_header.split(' ')
            for base in base_64[1:]:
                return base

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Function that decodes base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base_byte = base64_authorization_header
            data = base64.b64decode(base_byte)
            return data
        except:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ User credential
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            decode = decoded_base64_authorization_header.split(':')
            return tuple(decode)
