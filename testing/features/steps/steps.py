from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

#Random string generator
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Open browser
try:
	browser = webdriver.Chrome()
except:
	browser = webdriver.Firefox()	

#Generate user info
firstName = randomString(6)
lastName = randomString(6)
password = randomString(8)
email = 'ngeiger2@kent.edu'
phone = '330-697-5806'

#Scenario: navigate to sign up page

@given(u'we are at the homepage')
def step_impl(context):
	context.browser = browser #Set browser
	context.browser.get('http://callwaiting.pythonanywhere.com') #Go to home

@when(u'we click on Customer Login')
def step_impl(context):
        elem = context.browser.find_elements_by_class_name('btn')[0] #Find first "btn" class
        elem.click()

@when(u'we click on Create an Account')
def step_impl(context):
	elem = context.browser.find_element_by_link_text('Create an Account') #Find create account button
	elem.click() #Click to go to create account page

@then(u'we should go to the customer registration page')
def step_impl(context):
        assert 'Please fill in this form to create an account.' in context.browser.page_source
        #assert 'http://callwaiting.pythonanywhere.com/register' in context.browser.title

#Scenario: sign up as caller (stub)

@given(u'we are at the sign up page')
def step_impl(context):
        context.browser = browser #Set browser
        context.browser.get('http://callwaiting.pythonanywhere.com/register') #Go to sign up

@when(u'we fill in all fields')
def step_impl(context):
        #First name
        elem = context.browser.find_element_by_name('firstname')
        elem.send_keys(firstName)
        #Last name
        elem = context.browser.find_element_by_name('lastname')
        elem.send_keys(lastName)
        #Email
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(email)
        #Phone
        elem = context.browser.find_element_by_name('phonenumber')
        elem.send_keys(phone)
        #Password
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(password)
        #Confirm pw
        elem = context.browser.find_element_by_name('psw-repeat')
        elem.send_keys(password)

@when(u'we click Submit')
def step_impl(context):
        assert 1

@then(u'we should be able to login')
def step_impl(context):
        assert 1

#Scenario: log in as caller (stub)

@when(u'we enter our email and password and hit enter')
def step_impl(context):
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(email)
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(password)
        elem.send_keys(Keys.ENTER)

@then(u'we should be logged in')
def step_impl(context):
        assert 1
        #assert 'http://callwaiting.pythonanywhere.com/main' in context.browser.title


