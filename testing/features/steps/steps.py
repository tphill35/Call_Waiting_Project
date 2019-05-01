from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time

#Random string generator
def randomString(stringLength):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

#Url fetcher
def getUrl(page):
        if page == 'homepage':
                return 'http://callwaiting.pythonanywhere.com'
        elif page == 'sign up page':
                return 'http://callwaiting.pythonanywhere.com/register'
        elif page == 'caller dashboard':
                return '???'

#Open browser
try:
	browser = webdriver.Chrome()
except:
	browser = webdriver.Firefox()	

#Generate user info
randFName = randomString(6)
randLName = randomString(6)
randPW = randomString(8)
randEmail = randomString(8) + '@gmail.com'
randPhone = '000-000-0000'

#Account for testing email and phone
testEmail = 'callwaitingtest@gmail.com'
testPW = 'cs-33901'

#Clicking links (NOTE: use "" to distinguish clicking on a link using link text)
@when(u'we click on "{linktext}"')
def step_impl(context, linktext):
	elem = context.browser.find_element_by_link_text(linktext) #Find link text
	elem.click() #Click on link

#Go to url
@given(u'we are at the {page}')
def step_impl(context, page):
	context.browser = browser #Set browser
	context.browser.get(getUrl(page)) #Go to home

#Scenario: navigate to sign up page

@when(u'we click on Customer Login')
def step_impl(context):
        elem = context.browser.find_elements_by_class_name('btn')[0] #Find first "btn" class (second is provider)
        elem.click()

@then(u'we should go to the customer registration page')
def step_impl(context):
        assert 'Please fill in this form to create an account.' in context.browser.page_source
        #assert 'http://callwaiting.pythonanywhere.com/register' in context.browser.title

#Scenario: sign up as caller (stub)

@when(u'we fill in all fields and hit enter')
def step_impl(context):
        #First name
        elem = context.browser.find_element_by_name('firstname')
        elem.send_keys(randFName)
        #Last name
        elem = context.browser.find_element_by_name('lastname')
        elem.send_keys(randLName)
        #Email
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(randEmail)
        #Phone
        elem = context.browser.find_element_by_name('phonenumber')
        elem.send_keys(randPhone)
        #Password
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(randPW)
        #Confirm pw
        elem = context.browser.find_element_by_name('psw-repeat')
        elem.send_keys(randPW)
        elem.send_keys(Keys.ENTER)
        #time.sleep(5)

@then(u'we should be able to login')
def step_impl(context):
        #Run log in test using random email and password
        context.browser = browser
        context.browser.get(getUrl('homepage'))
        elem = context.browser.find_elements_by_class_name('btn')[0]
        elem.click()
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(randEmail)
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(randPW)
        elem.send_keys(Keys.ENTER)
        #time.sleep(5)
        assert 'Log Out' in context.browser.page_source

#Scenario: log in as caller (this should fail if the test account hasn't been signed up)

@when(u'we enter our email and password and hit enter')
def step_impl(context):
        #Log in using existing account
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(testEmail)
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(testPW)
        elem.send_keys(Keys.ENTER)

@then(u'we should be logged in')
def step_impl(context):
        assert 'Log Out' in context.browser.page_source

