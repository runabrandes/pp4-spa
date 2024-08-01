<h1 align=center>TESTING</h1>

#

## AUTOMATED TESTING

I have attempted automated testing but have only written very few automated tests in the end. The relevant file can be found in `booking > test_forms.py `. 

- The test that caused failed results to appear was:
![removed_test](templates/documentation/images/removed_test.png)

- The terminal was showing following message:

![terminal_error](templates/documentation/images/terminal_error_test.png)

I have decided to remove the test that caused the issues and commit the test_forms.py file without it.

#

## MANUAL TESTING


### USER STORY: Deployed website

Description:
- The user can view the deployed site

Steps:
1. Go to [the deployed site](https://pp4-spa-4203ec483751.herokuapp.com/)
2. View the site

Expected:
- Site loads without errors

Actual:
- As expected


### USER STORY: Navbar

Description:
- A Navbar is displayed to users across all pages

Steps:
1. View all pages
2. Check Navbar is on display
3. Check all Navbar links work

Expected:
- Navbar is always on display
- Mountain Mist Spa logo takes the user to the home page when clicked
- Make A Booking takes the user to the booking form (when logged in)
- Upcoming Bookings takes the user to the upcoming bookings overview (when logged in)
- Past Bookings takes the user to the past bookings overview (when logged in)
- Create Account takes the user to the sign up page (when logged out)
- Account Login takes the user to the sign up page (when logged out)
- Account Logout takes the user to the sign out page (when logged in)

Actual:
- As expected


### USER STORY: Footer

Description:
- A footer is on display to the user across all pages

Steps:
1. View all pages
2. Check footer is on display

Expected:
- Footer is always on display
- The links all work:
    - Facebook takes the user to Facebook (opens in a new window)
    - Instagram takes the user to Instagram (opens in a new window)

Actual:
- As expected


### USER STORY: Services offered shown on home page 

Description:
- The user can view a list of all the service packages offered by the salon

Steps:
1. Go to the home page
2. Scroll to the Services section
3. Click on one of the service buttons

Expected:
- An overview of offered services is shown
- Clicking on a service button will display a modal with more information including:
    - Service name
    - Description
    - Price
    - Link to Book An Appointment

Actual:
- As expected


### USER STORY: Contact details and map

Description:
- The user can view contact details of the salon as well as a map showing the location of the spa

Steps:
1. Go to the home page
2. Scroll to the Contact section
3. View address, phone number and map

Expected:
- An overview of the address and phone number of the salon
- A map of the location of the salon (which opens Google Maps when clicked)

Actual:
- As expected


### USER STORY: Make a booking

Description:
- A user can fill in a form to make an appointment

Steps:
1. Click 'Make A Booking' in the navbar menu (when logged in)
2. Fill in sections of booking form
    - Date
    - Time
    - Service
    - Comments (optional)

Expected:
- A booking is made (this is confirmed by an on-screen message)
- Booked appointment can then be view in Upcoming Bookings section

Actual:
- As expected


### USER STORY: View upcoming bookings

Description:
- A user can view their own upcoming bookings

Steps:
1. Click 'Upcoming Bookings' in the navbar menu (when logged in)
2. View all upcoming bookings

Expected:
- All upcoming bookings are displayed including:
    - Date
    - Time
    - Service
    - Confirmation status
    - Options to edit / delete bookings

Actual:
- As expected


### USER STORY: View past bookings

Description:
- A user can view their own past bookings

Steps:
1. Click 'Past Bookings' in the navbar menu (when logged in)
2. View all past bookings

Expected:
- All past bookings are displayed including:
    - Date
    - Time
    - Service

Actual:
- As expected


### USER STORY: 404 page

Description:
- A user will see a custom 404 page when they try to access a page that is not part of the website

Steps:
1. A user should add some random letters to the end of the URL

Expected:
- Custom 404 page is displayed

Actual:
- As expected

