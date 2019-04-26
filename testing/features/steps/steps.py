from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'we are at the homepage')
def step_impl(context):
	#Open browser
	try:
		context.browser = webdriver.Chrome()
	except:
		context.browser = webdriver.Firefox()
	context.browser.get('http://callwaiting.pythonanywhere.com') #Go to site

@when(u'we click on Customer Login')
def step_impl(context):
	elem = context.browser.find_element_by_class_name('btn') #Find login button (do this twice to go to provider's)
	elem.click() #Click to open login menu

@when(u'we click on Create an Account')
def step_impl(context):
	elem = context.browser.find_element_by_link_text('Create an Account') #Find create account button
	elem.click() #Click to go to create account page

@then(u'we should go to the customer registration page')
def step_impl(context):
        assert "Please fill in this form to create an account." in context.browser.page_source
        #assert "http://callwaiting.pythonanywhere.com/register" in context.browser.title
