#functions for storage related calls
import os
import mysql.connector
from mysql.connector import Error

#TODO: Create some sort of logging

#Mysql connection stuff
#might revisit this idea later. Kinda ugly. Dank memes. This will work for now
def select_query(sql, param):
    results = None
    connection = mysql.connector.connect(host = "localhost", database = "school", user = "newuser", password = "password")
    cursor = connection.cursor()

    try:
        cursor.execute(sql, (param,))
        results = cursor.fetchall()
                
    except Error as e:
        print("Error: ", e)
    finally:
        cursor.close()
        connection.close()
        return results
        
def in_up_de_query(sql, param):
    connection = mysql.connector.connect(host = "localhost", database = "school", user = "newuser", password = "password")
    cursor = connection.cursor()

    try:
        cursor.execute(sql, param)
        connection.commit()
    except Error as e:
        print("Error: ", e)
    finally:
        cursor.close()
        connection.close()


#Manage user accounts

#TODO: redo passwords later. need to make it more secure
def get_profile(username, password):
    
    #checking customer table
    sql = "SELECT Email, Password From Customer WHERE Email = %s"
    param = username
    cusProfile = select_query(sql, param)
    
    if cusProfile:
        for item in cusProfile:
            profile = {
                "email": item[0],
                "password": item[1],
                "type": "customer"
            }
        return dict(profile)

    #checking provider table
    sql = "SELECT Email, Password From Provider WHERE Email = %s"
    param = username
    provProfile = select_query(sql, param)
    
    if provProfile:
        for item in provProfile:
            profile = {
                "email": item[0],
                "password": item[1],
                "type": "provider"
            }
        return dict(profile)
    return None
    
def add_profile(profile):
    #do some checking
    assert type(profile) is dict
    assert 'email' in profile
    assert type(profile['email']) is str

    #checking for email that already exists
    sql = "SELECT Email FROM Customer WHERE Email = %s"
    param = profile['email']
    query = select_query(sql, param)
    
    if query is None:
        #insert new profile
        sql = "INSERT INTO Customer (Email, Password) VALUES (%s, %s)"
        param = profile['email'], profile['password']
        in_up_de_query(sql, param)
    else:
        pass
    

#def delete_profile(user):
    #delete a profile - TODO: change this to mysql
    #profile_table.remove(where('user') == user)

#session stuff

def add_session(session):
    #check some stuff
    assert type(session) is dict
    assert 'key' in session
    assert type(session['key']) is str
    
    #insert into database
    sql = "INSERT INTO Session (SessionKey, Email, Login) VALUES (%s, %s, %s)"
    param = session['key'], session['email'], session['login']
    in_up_de_query(sql, param)
    
def get_session(key):
    sql = "SELECT SessionKey, Email, Login FROM Session WHERE SessionKey = %s"
    param = key
    query = select_query(sql, param)

    for item in query:
        session = {
            "key": item[0],
            "email": item[1],
            "password": item[2]
        }
    
    if session:
        return dict(session)
    return None
    
#not really used yet
def update_session(key):
    
    sql = "UPDATE"
    param = ""
    in_up_de_query(sql, param)

def delete_session(key):
    sql = "DELETE FROM Session WHERE SessionKey = %s"
    param = key
    in_up_de_query(sql, param)

#functions for customer/provider dashboards

#customer
def customer_scheduled_calls(email):
    query = "output"
    return query

#provider
def provider_scheduled_calls(email):
    query = "output"
    return query