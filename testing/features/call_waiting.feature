Feature: sign up to Call Waiting

	Scenario: Go to customer registration page
		Given we are at the homepage
		When we click on Customer Login
		And we click on Create an Account
		Then we should go to the customer registration page

	Scenario: Sign up as a caller
		Given we are at the sign up page
		When we fill in all fields
		And we click submit
		Then we should be able to login
