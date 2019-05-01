from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import datetime

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
                return 'http://callwaiting.pythonanywhere.com/user_dashboard'

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
testEmail = 'callwaitingtest2@gmail.com'
testPW = '321drowssap'

testEmail2 = 'callwaitingtest3@gmail.com'
testPW2 = '654drowssap'

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
        time.sleep(3)

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
        time.sleep(3) #NOTE: need this delay or assert will fail
        assert 'Log Out' in context.browser.page_source
        assert 1

#Scenario: log in as caller (this should fail if the test account hasn't been signed up)

@when(u'we enter our email and password and hit enter')
def step_impl(context):
        #Log in using existing account
        elem = context.browser.find_element_by_name('email')
        elem.send_keys(testEmail)
        elem = context.browser.find_element_by_name('psw')
        elem.send_keys(testPW)
        elem.send_keys(Keys.ENTER)
        time.sleep(3) #NOTE: need this delay or assert will fail

@then(u'we should be logged in')
def step_impl(context):
        assert 'Log Out' in context.browser.page_source

#Scenario: schedule a call

##Generate date and time strings##
now = datetime.datetime.now()

yearStr = str(now.year)

#Choose day as either a week later, or first day of next month (let's ignore december for now)
if (now.day+7 <= 29):
        monthStr = '0'
        if now.month < 10:
                monthStr += str(now.month)
        else:
                monthStr = str(now.month)

        dayStr = '0'
        if now.day+7 < 10:
                dayStr += str(now.day+7)
        else:
                dayStr = str(now.day+7)
else:
        monthStr = '0'
        if now.month < 10:
                monthStr += str(now.month+1)
        else:
                monthStr = str(now.month+1)

        dayStr = '01'

hourStr = '0' + str(random.randint(1,5)) #Select random hour btwn 1 and 5

#Choose random 15-min slot
minStr = '00'
minResult = random.randint(1,4)
if minResult == 2:
        minStr = '15'
elif minResult == 3:
        minStr = '30'
elif minResult == 4:
        minStr = '45'

secStr = '00'

@when(u'we enter our appointment time and hit enter')
def step_impl(context):
        #Fill in fields  
        elem = context.browser.find_element_by_name('Appointment') #Date
        elem.click()
        elem.send_keys(monthStr + dayStr + yearStr)
        elem = context.browser.find_element_by_name('TimeStart') #Time
        elem.click()
        elem.send_keys(hourStr + minStr + secStr)
        elem = context.browser.find_element_by_name('appt') #Est. Time
        elem.send_keys('15')
        time.sleep(3)
        elem.send_keys(Keys.ENTER)

@then(u'the call should appear in our call list')
def step_impl(context):
	context.browser = browser
	context.browser.get(getUrl('caller dashboard'))
	assert (monthStr + '/' + dayStr + '/' + yearStr) in context.browser.page_source
	assert (hourStr + ':' + minStr) in context.browser.page_source

@then(u'we should receive an email verifying our call') #Stub
def step_impl(context):
        assert 1
