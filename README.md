<h1 align=center>Portfolio Project 4</h1>

<h2 align=center>Mountain Mist Spa</h2>

## FINAL DESIGN

![Final project image home page](templates/documentation/images/PP4_AIR.png) Am I Responsive(https://amiresponsive.co.uk/)

[Here is a link to the final project](https://pp4-spa-4203ec483751.herokuapp.com/)

#

## PROJECT IDEA

My goal for this project was to create a website for a salon/spa that enables customers to easily book, edit, and cancel appointments online. The website also showcases the services offered by the business, as well as contact information for customers seeking to reach out or find the salon with ease.

The features I wanted the website to have:

1. Online appointment booking system  
2. Appointment editing and cancellation functionality  
3. Display of available services offered  
4. User-friendly interface for easy navigation  
5. Accessible contact information for the business  
6. Customer accounts for managing bookings  
7. Service descriptions and pricing information  
8. Display of upcoming bookings
9. Display of past bookings
10. Contact information 

#

## UX / UI

### User Stories

- As a user, I want to be able to book appointments online so that I can easily schedule my visits at my convenience.  
- As a user, I want to edit or cancel my appointments online so that I can manage my bookings without needing to call the salon.  
- As a user, I want to view the available services offered by the salon so that I can choose the right treatments for my needs.
- As a user, I want detailed descriptions and pricing for services so that I can make informed decisions before booking.   
- As a user, I want a user-friendly website interface so that I can navigate the website easily and quickly find what I'm looking for.  
- As a user, I want to access the salon's contact information so that I can reach if needed.
- As a user, I want to create a customer account to manage my bookings. 
- As a user, I want to have an overview of my upcoming appointments to ensure I don’t forget them.
- As a user, I want to have an overview of my past appointments so that I can review my service history and recall my favorite treatments.

## Overview

- The website was created using Django and features full CRUD (Create, Read, Update, Delete) functionality and a user-friendly UI to make booking an appointment at Mountain Mist Spa sraightforward.
- The user can sign up to the website an when logged in, they can make bookings, as well as edit and delete these.
- The user can see their upcoming and past bookings.
The upcoming bookings overview features visibility of the booking confirmation status and holds the edit and cancel functions.
- Admin users have extra functionality in the admin panel, being able to search bookings by date and username. They can also confirm, edit and cancel bookings.

#

### Strategy

#### Project Setup

- Django Application: Create the initial Django application tailored for Mountain Mist Spa.
- File Structure: Organise the project files to ensure maintainability.
- Database Models: Define and establish models to capture relevant data.
- Static Files: Link custom CSS and images for a polished look and feel.
- Base Template: Create a base.html file for consistent layout across all templates.
- Google Fonts: Integrate Google Fonts for enhanced typography.

#### UX Enhancements
- Favicon: Add a Favicon logo for brand recognition.
- Service Listings: Display a list of spa services, featuring a brief description and their costs.
- Styled Auth Pages: Customise the default allauth pages to reflect the spa's branding.
- Home Page: Create an inviting homepage showcasing the spa's introduction, offerings and contact details. 
- Map Section: Include a map area so customers can easily access the spa's location. 
- Booking History: Allow users to view spa treatment bookings.
- User Notifications: Display alerts and messages to inform users about booking statuses.

#### Navigation
- Navbar: Ensure a consistent navigation bar across all pages for easy access.
- Footer: Implement a standard footer on all pages for additional information (copyright) and social media links.

#### CRUD
- Upcoming Bookings: Enable users to view, modify and delete their upcoming spa treatment bookings.
- Online Booking: Provide a seamless interface for customers to book spa treatments.
- Admin Controls: Enhance admin capabilities for managing bookings and services.

#### Authentication
- User Accounts: Enable users to create and manage their personal accounts.
- Allauth Setup: Configure Django Allauth for robust user authentication.

#### Validation
- Booking Validation: Implement form validations to ensure bookings are valid and timeslots aren't double-booked.
- Ensure logged in user can only book appointments for their active account. 

#### Administration
- Admin Search: Allow admins to search and filter for bookings.
- User Account Management: Let users update their account details, including email and password.
- Booking Confirmation: Equip admins with tools to confirm spa treatment bookings.

#### Deployment
- Cloudinary for Media: Use Cloudinary for efficient media storage and delivery.
- PostgreSQL: for Database services. 
- Heroku Deployment: Deploy the application on Heroku.
- DEBUG Settings: Ensure the application is deployed with DEBUG set to False.

#### Testing
- Testing: Conduct thorough testing to ensure a smooth user experience and validate code (HTML and CSS validator, Python Linter, WAVE testing)

#### Documentation
- ReadMe: Create comprehensive documentation to guide in navigating and using the application as well as explaining the purpose of the website. 
- Testing: Create comprehensive documentation showcasing the different testing approaches. 

