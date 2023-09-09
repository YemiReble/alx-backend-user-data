#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User


""" Retreive this user via the class BasicAuth """

#user_email = 

a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else "None")

#u = a.user_object_from_credentials("email@notfound.com", "pwd")
#print(u.display_name() if u is not None else "None")

#u = a.user_object_from_credentials(user_email, "pwd")
#print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials('user_email', 'user_clear_pwd')
print(u.display_name() if u is not None else "None")
