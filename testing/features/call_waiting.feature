Feature: sign up to Call Waiting

	Scenario: Go to customer registration page
		Given we are at the homepage
		When we click on Customer Login
		And we click on "Create an Account"
		Then we should go to the customer registration page

	Scenario: Sign up as a caller
		Given we are at the sign up page
		When we fill in all fields and hit enter
		Then we should be able to login

	Scenario: Log in as a caller
		Given we are at the homepage
		When we click on Customer Login
		And we enter our email and password and hit enter
		Then we should be logged in

	Scenario: Schedule a call
		Given we are at the caller dashboard
		When we click on "Schedule A Call"
		And we enter our appointment time and hit enter
		Then the call should appear in our call list
		And we should receive an email verifying our call
