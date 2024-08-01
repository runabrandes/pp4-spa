<h1 align=center>Portfolio Project 4</h1>

<h2 align=center>Mountain Mist Spa</h2>

## FINAL DESIGN

![Final project image home page](templates/documentation/images/PP4_AIR.png) [Am I Responsive](https://amiresponsive.co.uk/)

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

## OVERVIEW

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

#

### Scope

#### Agile Methodology

This project was developed using the Agile methodology.<br>
All  user stories implementation progress was recorded using [GitHub](https://github.com/).
As user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress** to **Done**. The board can be viewed [here](https://github.com/users/runabrandes/projects/2).

#### Simple and Intuitive UX

- Create a responsive navigation bar for easy access to all pages.
- Develop a footer with social media links and copyright.
- Include the spa location and phone number.
- Ensure that users receive visual notifications for all changes to their account, particularly regarding booking modifications and cancellations.
- Maintain user orientation throughout their website experience, enhancing usability.

#### Relevant Content

- Ensure all available spa services and treatments are clearly listed on the site.
- Display the spa's address prominently so users can easily locate it.
- Only allow users to book available time slots for treatments.

#### Responsiveness

- Create a responsive website that functions seamlessly across all devices and screen sizes.

#

### Structure

The website is designed with the user in mind, and once users are logged in, they have access to different pages:

- Home Page
- Make A Booking
- Upcoming Bookings (including edit and delete functionalities)
- Past Booking (including edit and delete functionalities)
- Account Logout

There are also 2 pages available to users who are not signed in:

- Create Account
- Login

#

### Wireframes

The website layout has been planned through the creation of detailed wireframes that outline the desired structure  of the Mountain Mist Spa website. These wireframes serve as a visual guide, illustrating the placement of key elements such as navigation menus, service listings, booking forms and booking overviews.

- Wireframes for home page
![wireframes_home](templates/documentation/images/home_wireframes.png)

- Wireframes for making a booking
![wireframes_make_booking](templates/documentation/images/make_booking_wireframes.png)

- Wireframes for booking overview
![wireframes_overview](templates/documentation/images/overview_wireframe.png)

- Wireframes for sign in 
![wireframes_signin](templates/documentation/images/signin_wireframe.png)

- Wireframes for sign out
![wireframes_signout](templates/documentation/images/signout_wireframe.png)

- Wireframes for sign up
![wireframes_signup](templates/documentation/images/signup_wireframes.png)

#

### Database Schema
![database_schema](templates/documentation/images/database_schema.png)

#

### Features

#### Navigation

The navbar along the top of the pages is always displayed, allowing the user to easily navigate around the site. The styling is consistent across the different pages but has different links on display depending on if users are logged in or out. 

![navbar](templates/documentation/images/navbar.png)

#### Footer

The footer displays on all pages of the webiste and has been styled consistently.
It features two social media links (Facebook, Instagram).

![footer](templates/documentation/images/footer.png)

#### Logo and Welcome message

The logo for the website has been designed with a simple, cursive style that gives it a unique look. When users log in, they see a welcoming message, and if they are not logged in, a message stating "You are not logged in!" appears, making it clear whether they have access to personalised features. This straightforward approach helps users understand their status on the site.

![logo](templates/documentation/images/logo%20and%20welcome.png)

#### Hero Image

The hero image chosen for the spa aligns well with its name and showcases a misty mountain forest setting, creating a tranquil and serene atmosphere that reflects the spa's focus on relaxation and natural beauty.

![hero](templates/documentation/images/hero_imagine.png)

#### Introduction

The spa introduction serves as an inviting gateway, emphasizing the salon's dedication to creating a serene environment where guests can unwind. It clearly outlines the spa’s focus. 

![intro](templates/documentation/images/intro.png)

#### Service overview

The service overview feature provides a clear summary of the spa’s offerings. When clicking a service button, a modal is triggered which displays each service, a brief description and the pricing.

![service](templates/documentation/images/services.png)

#### Map and contact information

The map and contact feature includes the spa's address, phone number, and an interactive map which navigates the user to Google Maps when clicked.

![map](templates/documentation/images/map_contact.png)

#### Make A Booking

The booking feature allows customers to easily schedule appointments online. User are required to select a desired service, choose a date and time, and provide necessary details. Form validation prevents appointments in the past to be booked as well as hinders users from booking appointments that have been taken by other users.

![booking_intro](templates/documentation/images/booking.png)
![booking_form](templates/documentation/images/bookingform.png)

#### Booking overview

In the upcoming bookings section, users can view a list of booked appointments, including service details, date, time and confirmation status, making it easy to keep track of their bookings. Edit and delete buttons are also present. When the user decides to edit a booking, a modal is triggered asking them to confirm the booking is to be updated. If yes, they are taken back to the booking form (now populated with the original booking information) where they can alter the details of the bookings. Once the booking has been altered the confirmation state chnages back to False. <br> 
If they decide to delete a booking instead, a modal is triggered when clicking the delete button, asking the user if they want to proceed with the deletion. If yes, the upcoming bookings page is refreshed and the deleted booking will no longer show in the list. <br>
The past bookings section provides a record of previous appointments, featuring service information and dates, enabling users to review their service history and rebook their favorite treatments.

![booking_overview](templates/documentation/images/bookings.png)
![booking_past](templates/documentation/images/past_bookings.png)

#### Sign Up, Sign In, Sign Out

The application provides sign up, sign in and sign out features as well as 'Forgot Password' and email address change options for enhanced security. <br> Users can create an account to access service bookings, log in with their credentials, and log out to protect their information.

![sign_up](templates/documentation/images/sign_up.png)
![sign_in](templates/documentation/images/sign_in.png)
![sign_out](templates/documentation/images/sign_out.png)

#### Colour schemes and fonts

The three colours used across the website are: <br>
- '#E8EEFA' - Alice Blue
- 'EBA4A4' - Melon
- 'F8F9FA' - Sea Salt

![colours](templates/documentation/images/colours.png)

#### Admin panel

The website features a standard Django admin panel. 
Here, superusers can view information regarding accounts that have been created for the website and add services to the wesbite. This will generate more buttons and modals for the service overview. <br>
Search and filter functions are present for made bookings and admins can confirm the booking status. 

#### Future Features

- Add profile section where users can add a profile picture and update their username
- Add chat function so users can get in touch with the salon via the website rather than having to call
- Add email confirmations for bookings made, as well as updates and deletions of bookings. 

#

## TESTING 

All testing has been documented in [Testing](TESTING.md)

#

## BUGS

A few bugs I have encountered during working on this project were:

- URL paths not found - return of 404 page.   

This was due to syntax errors in the URL patterns I have written or the files not being linked as they should have been. <br>
All the bugs surrounding URL paths have been fixed and the links are now fully functional. 


- Salon services were not showing on home page as expected.

This was due to a syntax error. The relevant variable name was misspelled which stopped the list I tried to access from being iterated through. <br> This bug has been fixed and the services are now displaying as desired. 

- Function for ValidationErrors not functional

The function to raise ValidationErrors was not functional after it had just been written. This was due to me writing it as 2 separate functions in the beginning and the logic not working.  After I combined the two, the ValidationErrors displayed to the user as expected. 

- Tables for upcoming and past bookings were not centering in the middle of the page as desired.

This was due to a Bootstrap error. Instead of the correct class ‘col-md-12’ I had initially used the class ‘col-md-8’ which stopped the whole width of the page being used. <br>
This has been corrected. 

- When trying to cancel bookings a 404 error was returned

The error message: ’The view didn’t return a HttpResponse’ was displayed. This was due to an indentation error which I was able to resolve. 

# 

## TOOLS USED

- [GitHub](https://github.com/)
- [Gitpod Enterprise](https://codeinstitute-ide.net/) for writing the code
- [Heroku](https://heroku.com/) used for deploying the project
- [PostgresSQL from Code Institute](https://dbs.ci-dbs.net/)
- [Balsamiq Wireframes](https://balsamiq.com/wireframes/) for creating the wireframes - the desktop version was used
- [LucidChart](https://www.lucidchart.com/) for creating the Database Schema
- [Font Awesome](https://fontawesome.com/) for the site's icons
- [Bootstrap](https://getbootstrap.com/) for the initial styling of of the site
- [Google Fonts](https://fonts.google.com/) for the typography
- [Code Institute Pylint](https://pep8ci.herokuapp.com/) for validating the python code
- [HTML - W3C HTML Validator](https://validator.w3.org/) for validating the HTML
- [CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) for validating the CSS
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) for debugging the project
- [W.A.V.E.](https://wave.webaim.org/) for testing accessibility
- [Cloudinary](https://cloudinary.com/) for storing static data
- [Chrome LightHouse extension](https://developer.chrome.com/docs/lighthouse/overview/) for testing performance
- [Flaticon](https://www.flaticon.com/) for sourcing the sites favicon
- [Pexels](https://www.pexels.com/) for the hero and booking page images

### Python packages used

- [Django](https://www.djangoproject.com/) was used as the framework for the site.
- [Allauth](https://docs.allauth.org/en/latest/) for the login authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/) for help styling the forms.
- [Cloudinary](https://cloudinary.com/) for hosting the images.
- [Gunicorn](https://gunicorn.org/) for handling the HTTP requests in production.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) for deploying the static files to Heroku.

A full list of the requirements and the versions used can be found in the requirements.txt file.

To create the requirements.txt file following command was run:<br>
`pip3 freeze > requirements.txt`

To create a superuser the following command was used: <br>
`python3 manage.py createsuperuser`

To run the migrations to the database the following commands were used:<br>
`python3 manage.py makemigrations` <br>
`python3 manage.py migrate`

To collect the static files for deployment run the following command: <br>
`python3 manage.py collectstatic`

To view a preview of the project (port 8000) following command was used:
`python3 manage.py runserver`
After running the command, port 8000 was selected and opened from the PORTS tab. 

#

## DEPLOYMENT 

### Heroku Deployment

IMPORTANT: prior to deploying ensure all dependencies are listed within the requirements.txt file

Within the terminal in Gitpod Enterprise type `pip3 --local freeze > requirements.txt` and a list with all requirements will be created to be read by Heroku.


1. Navigate to [Heroku.com](https://www.heroku.com/) and login (or create a new account).
2. On the top right hand side, click the `New` button.
3. Inside the dropdown menu, select `Create new app`.
4. Create a new name for your app (making sure the name chosen is available) in this case it is `pp4-spa`. 
App names can only be in lowercase letters, numbers and dashes.
5. Select your region, in this case `Europe`.
6. Click on the `Create App` button.  
7. This will create your app in Heroku and take you to the dashboard.
8. Navigate to the settings tab and scroll down to the button `Reveal Config vars`.
9. Replace the word `KEY` and enter `DATABASE_URL` and then replace the word `VALUE` and enter your personalised URL to the relevant database, then click the `Add` button.
10. Add a further Config Vars, replace the word `KEY` and enter `CLOUDINARY_URL` and then replace the word `VALUE` and enter your personalised URL to your Cloudinary, then click on the `Add` button.
11. To add the final Config Vars to this project, replace the word `KEY` and enter `SECRET_KEY` and then replace the word `VALUE` and enter your personalised SECRET KEY, then click on the `Add` button.
12. Below `Config vars` is `Buildpacks`. Click the `Add Buildpack` button.
13. In the pop up window, select `python` and save changes.
14. Next, navigate to the `Deploy` tab at the top left.
15. Select `Github, 'connect to github'` as the deployment method.
16. Search for the Github Repository in the search field (in this case `pp4-spa`) and click `Search`.
17. When the search is complete, click `Connect`.
18. Once your repository is connected to [Heroku](https://heroku.com/), click the `Enable Automatic Deploys` button for automatic deployment.
19. Alternatively you can manually deploy by selecting a branch to deploy from and clicking `Deploy Branch`. 
20. If you choose to `Enable Automatic Deploys`, [Heroku](https://heroku.com/) will build a new version of the app when a change to `gitpod` is pushed to `Github`.  
21. Manual deployment allows you to update the app whenever you click `Deploy Branch`. For this project, the manual way was chosen and the branch deployed from is `main`. 
22. Once the build process is complete you will be able to view the live app by clicking on the `Open app` button.

#

## VERSION CONTROL

These commands were used for version control during development:

- git commit -m "example message" - to commit changes to the local repository
- git push - to push all committed changes to the GitHub repository
- git pull - to pull all code into main branch once the feature branch had been merged and deleted
- git status - to see if the branch currently working on is up to date or if the are any unstaged changes
- git log --oneline - to see the last commit
- git commit --amend - to amend the most recent commit message

#

#### How to fork a repository:

If you need to `FORK` a repository:

1. Login in to [GitHub](www.github.com) and go to [https://github.com/runabrandes/pp4-spa](https://github.com/runabrandes/pp4-spa)
2. In the top right corner, click `Fork`
3. The next page will be the forked version of [https://github.com/runabrandes/pp4-spa](https://github.com/runabrandes/pp4-spa) but in your own repositories

#

#### How to clone a repository:

If you need to make a clone of this repository:

1. Fork the repository [https://github.com/runabrandes/pp4-spa](https://github.com/runabrandes/pp4-spa) using the steps above
2. Above the file list, click `Code`
3. Choose if you want to clone using HTTPS, SSH or GitHub CLI, then click the copy button
4. Open Git Bash
5. Change the directory to where you want your clone to go (in your own github)
6. Type `git clone` and then paste the URL you copied in step 4
7. Press `Enter` to create your clone

#

#### How to make a local clone:

If you need to make a local clone:

1. Login in to [GitHub](www.github.com) and go to [https://github.com/runabrandes/pp4-spa](https://github.com/runabrandes/pp4-spa)
2. Under the repository name, above the list of files, click `Code`
3. Here you will have two options, `Clone` or `Download` the repository
4. You should close the repository using HTTPS, clicking on the icon to copy the link
5. At this point, you can launch the `Gitpod workspace` or choose your own directory
5. Open Git Bash
6. Change the current working directory to the new location of where you want the cloned directory to be
7. Type git clone and then paste the URL you copied in step 4
8. Press Enter, to create your local clone to your chosen directory

#

## CREDITS

- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- The Code Institute CodeStar walkthrough project
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django Documentation](https://docs.djangoproject.com/en/5.0/)

#

## ACKNOWLEDGEMENTS

* My husband Jamie for his support and reading through my code! It's good being on this coding journey together!!
* My mentor Rory for being supportive and giving me great advice when I thought I was unable to solve some issues and showing me that sometimes a solution is a lot simpler than I assumed! Thanks for helping me!
* All ghe tutors at Code Institute K have spoken to throughout the development of this project! Thank you all for the advice!
* To members from Slack when I was struggling to find solutions to issues or just had general questions regarding the project. 