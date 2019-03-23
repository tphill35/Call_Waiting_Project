from flask import Flask, request
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect

import os

import data_api

app = Flask(__name__)

#homepage
@app.route('/')
def my_form():
    return render_template('index.html')
    
@app.route("/register", methods=['GET'])
def user_account_creation():
    response = make_response(render_template("register.html"))
    return response
    
@app.route('/register', methods=['POST'])
def post_register():
    response = make_response(render_template("register.html"))
    return response
    
@app.route("/user_dashboard", methods=['GET'])
def get_udashboard():
    response = make_response(render_template("user_dashboard.html"))
    return response
    
@app.route("/user_dashboard", methods=['POST'])
def post_udashboard():
    response = make_response(render_template("user_dashboard.html"))
    return response
    
@app.route("/provider_dashboard", methods=['GET'])
def get_pdashboard():
    response = make_response(render_template("provider_dashboard.html"))
    return response
    
@app.route("/provider_dashboard", methods=['POST'])
def post_pdashboard():
    response = make_response(render_template("provider_dashboard.html"))
    return response
    
    
@app.route('/')
@app.route('/main', methods=['GET'])
def get_homepage():
    response = make_response(render_template("index.html"))
    return response
    
@app.route('/main', methods=['POST'])
def post_homepage():
 
    if request.form['login'] == "User Login":
        #we will obviosuly check the username and password before going to the dashboard
        #thats where the data API comes in
        #Dank Memes
        response = make_response(redirect("/user_dashboard"))
        return response
    elif request.form['login']:
        response = make_response(redirect("/provider_dashboard"))
        return response

    response = make_response(redirect("/main"))
    return response
    
#for running on cloud 9
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))