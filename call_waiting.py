#flask imports
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import jsonify
from flask import redirect

#other module imports
import os
import random
import time
import hashlib

#our imports
import storage

#TODO: more like stretch goal: run project in virtualenvironment
#TODO: more like stretch goal: change to SQLAlchemy

app = Flask(__name__)

#Encryption function. Duh!
def encrypt(password, salt):
    return hashlib.sha256((password+salt).encode()).hexdigest()
    
#Routing functions
#looking at the route should be self explanatory

@app.route("/register", methods=['GET'])
def user_account_creation():
    response = make_response(render_template("register.html"))
    return response
    
@app.route('/register', methods=['POST'])
def post_register():
    #Creating salt shit
    salt = str(time.time())[3:]
    
    #function call that passes a dictionary. Dictionary contains user profile information
    storage.add_profile({
        'firstName': request.form.get("firstname"),
        'lastName': request.form.get("lastname"),
        'email': request.form.get("email"),
        'phoneNumber': request.form.get("phonenumber"),
        'salt':salt,
        'password':encrypt(request.form.get("password"), salt)
    })
    
    if True:
        #if she works
        response =  make_response(redirect("/main"))
    else:
        #if she don't
        response =  make_response(redirect("/register"))
    return response
    
@app.route("/user_dashboard", methods=['GET'])
def get_udashboard():
    key = request.cookies.get("session_key")
    
    #response used if checks fail
    response =  make_response(redirect("/login"))
    response.set_cookie("session_key", "", expires=0)

    #check for key and session
    if not key:
        return response
    session = storage.get_session(key)
    if not session:
        return response

    #variable to display scheduled calls
    email = session['email']
    calls = storage.customer_scheduled_calls(email)

    #displaying page and updating session
    response = make_response(render_template("user_dashboard.html", session=session), calls)
    storage.update_session(key)
    response.set_cookie("session_key", key, max_age=600)
    return response
    
@app.route("/user_dashboard", methods=['POST'])
def post_udashboard():
    #get session key from users cookie. Could be dangerous. BE CAREFUL!!
    key = request.cookies.get("session_key")
    
    #response used if checks fail
    response =  make_response(redirect("/login"))
    response.set_cookie("session_key", "", expires=0)

    #check for key and session
    if not key:
        return response
    session = storage.get_session(key)
    if not session:
        return response

    #TODO: Something to look into: Might need to determine which button was clicked first

    #schedule/edit a call

    response = make_response(render_template("user_dashboard.html", session=session))
    storage.update_session(key)
    response.set_cookie("session_key", key, max_age=600)
    return response
    
@app.route("/provider_dashboard", methods=['GET'])
def get_pdashboard():
    #get session key from users cookie. Could be dangerous. BE CAREFUL!!
    key = request.cookies.get("session_key")
    
    #response used if checks fail
    response =  make_response(redirect("/login"))
    response.set_cookie("session_key", "", expires=0)

    #check for key and session
    if not key:
        return response
    session = storage.get_session(key)
    if not session:
        return response

    #view scheduled calls
    email = session['email']
    calls = storage.provider_scheduled_calls(email)

    response = make_response(render_template("provider_dashboard.html", session=session), calls)
    storage.update_session(key)
    response.set_cookie("session_key", key, max_age=600)
    return response
    
@app.route("/provider_dashboard", methods=['POST'])
def post_pdashboard():
    #get session key from users cookie. Could be dangerous. BE CAREFUL!!
    key = request.cookies.get("session_key")
    
    #response used if checks fail
    response =  make_response(redirect("/login"))
    response.set_cookie("session_key", "", expires=0)

    #check for key and session
    if not key:
        return response
    session = storage.get_session(key)
    if not session:
        return response

    #TODO: Something to look into: Might need to determine which button was clicked first

    #view scheduled calls

    response = make_response(render_template("provider_dashboard.html", session=session))
    storage.update_session(key)
    response.set_cookie("session_key", key, max_age=600)
    return response
    
#displays homepage
@app.route('/')
@app.route('/main', methods=['GET'])
def get_homepage():
    response = make_response(render_template("index.html"))
    return response
    

@app.route('/main', methods=['POST'])
def post_homepage():
    #we will obviosuly check the username and password before going to the dashboard
    #thats where the data API comes in
    #Dank Memes
        
    #getting username and password from front end
    email = request.form.get("email")
    password = request.form.get("password")
        
    #checking to see if profile is in database
    data = storage.get_profile(email, password)
    
    #used if profile is not found
    response =  make_response(redirect("/main"))
    response.set_cookie("session_key", "", expires=0)
    if not data:
        return response
    
    #this determines if the user is a customer or provider
    #Dank Memes
    if data['type']  == "customer":
        response = make_response(redirect("/user_dashboard"))
    elif data['type'] == "provider":
        response = make_response(redirect("/provider_dashboard"))

    #creating a session and storing a cookie
    key = "session." + str(random.randint(1000000000,1999999999))
    storage.add_session({"key":key, "email":email, "login":int(time.time())})
    response.set_cookie("session_key", key, max_age=600)
    
    return response
    
#for running on cloud 9
#app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

#for running on your local machine
#works for MAC and Linux. Windows users are S.O.L.
#1. export FLASK_APP=call_waiting.py
#2. flask run -h 0.0.0.0 -p 8080