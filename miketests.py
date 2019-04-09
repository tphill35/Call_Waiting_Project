import storage
import os
import time
import mysql.connector
from mysql.connector import Error

profile = storage.get_profile("bill", "password")
print(profile)

#profile = {'user': 'bill', 'password': 'password'}

#sql = "INSERT INTO Profile (UserName, Password) VALUES (%s, %s)"
#param = profile['user'], profile['password']
#storage.in_up_de_query(sql, param)
key = '111'
session = {"key": key, "email": "hello", "login": int(time.time())}
storage.add_session(session)