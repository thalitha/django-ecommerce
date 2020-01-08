# Old Currency

The Old Currency is a ecommerce website where people are able to search about old currencies and learn about the historical details of each currency. Besides of that if they register in the website, they are able to advertise/sell a currency and even buy the old currency (ies) advertised. For buying any currency it is essential to provide a credit card details. The website has an safe authentication mechanism that xxxxx
 
### UX
The main aims of the project are as follows:
1. Be able to see the currency historic but not selling or buying unless that the user register 
2. To allow the user to register and create their own user profile and see their orders
3. It should be intuitive and easy for the user to use

***USER STORIES:***
To understand why people might choose to use this site and therefore provide direction on its creation, I created a number of user stories as follows...

Story 1: As a regular user, I want to be able for searching for currencies

Story 2: As a user, I'd like to see the historic of each currency, image and price

Story 3: As a user, I want to be able to register in the website

Story 4: As a user, I would like to buy a currency that I am interested in

Story e: As a user, I need to be able to pay for the currency that I want to

Although a big undertaking, the website will provide a complete solution for these users

***WIREFRAMES*** - build the designs and do a web link to access it - as this example did:https://github.com/Code-Institute-Submissions/Django-Milestone-Project-2

### Features
draft: The website is designed to be extremely straight forward, on the very first webpage you can see the old currency title, image and price and by clicking on it you will access the historic about that coin. There is no clutter on the homepage, no distractions, its designed so it is not confusing and grabs the user very quickly. 
There is a general search field in the top-right-corner of the homepage where the user sees a "magnifying glass" and by clicking on that it will display a green big bar on the top of the page which enables the user to type the word (s) and click for searching on the "magnifying glass". So in this search engine, the user can enter words like new zeland, australian, bronze or whatever to find what they are looking for, which will obviously bring up another page with the results. 

* **View of the products**
* **Search bar** - This allows the user to narrow the search results presented to them by filtering results based on nationality of the coin
* **User authentication** - Register, Login, Logout - The application contains an Authentication app. This allows the user to login, logout, register with the site.

-Register - user can register by providing email address, username and password in register form. Password needs to be confirmed in extra field. If user tries to register username or email address that already exists in the database an error is displayed. After successful registering user is redirected to the home page.
-Log in, Log out - user can register by providing email address, username and password in register form. Password needs to be confirmed in extra field. If user tries to register username or email address that already exists in the database an error is displayed. After successful registering user is redirected to the home page.

* **User Profile**
* **User Edit Personal details**
* **Users' can view the contents of their cart by selecting the cart icon**
The application contains a checkout feature that allows the user to purchase the items they have placed into their cart. This is done by entering their details and using the STRIPE API.
* **Footer** - Contains linked social icons.

* **e-Commerce**

*double check* * **Full CRUD functionality***double check* Upon logging in, the application presents a paginated list of all the issues present in the database with a brief outline of each and a link button to bring the user to the single issue view.

 
### Future plans include:
* An option to review the product bought
* Another filters for searching such as year of the currency

### Technologies used
This website is a Flask Website that uses a Mongo backend.

* **Bootstrap**
* **CSS**  
* **Git & Github
* **Heroku**
* **HTML5**
* **JS**
* **Postgres**
* **Python**
* **Stripe**

### Testing
User stories from the UX section were tested to ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

All features of the website has been tested and seems to be working well.
Each functionality has been tested and are described on the Validation documents (pages 01-03).
The webpage is responsive adapting to different sizes of the devices.
The www.jshint.com validator coding was used.
HTML and Css code for this website were validated using W3C Validation Service. No errros were found in the code.

* Example of Testing:
A form of White Box testing was conducted by the developer using potential use cases or user stories to ensure that each link in the application followed the intended path. This was also done for each feature outlined in the Features section to ensure they were working as intended.
A form of Black Box testing was done by asking both a friend and the student's mentor on the course to use the application without instruction. Their feedback was then used to make improvements.
Fundamental testing was used to ensure that the stack of technologies was working together successfully. (e.g.) Retrieving one field from a document in the database, manipulating it with Python, passing it through the Django Full Stack framework and presenting it to the user.
Component testing was used for each block of code developed to serve a particular function. (e.g.) In lines 191-194 of the "recipe-app-test.py" file, the code block is attempting to filter result by category, placing only recipes with the same category as those selected by the user in the list of results. This was tested with using none, single and multiple categories selected, to ensure it was producing the correct result. Similar testing was used on all code blocks developed/used.
Combination testing was used to ensure that code blocks were working in conjunction to produce the intended and expected results.
The responsiveness of the application was tested using various browsers (Chrome, Safari, Internet Explorer, FireFox) and on different devices using the Google Chrome "Inspect" tab.
Automated tests were developed and conducted using the in-built Django tests package. They can be found in the test_forms.py, test_views.py and test_models.py file of the issues app. 20 tests were developed and conducted on the issues and progress apps. The results of these tests can be seen in the IMAGEFILE.jpg file located in the testing folder. Alternatively, one can run these tests by entering the following command into their own IDE once they have cloned the repository; python3 manage.py test.
 
### Deployment

The webpage was deployed using Github and Heroku. The link to the website is: xxxxx
**EXAMPLES**

* Example 1: My code has simply been deployed via heroku pages at the following link: yyyy
My code has simply been deployed via heroku pages at the following link - https://my-team-utility.herokuapp.com/

In order to do this I created a new app on the heroku site and linked to the app via the cloud9 terminal.

I created a Procfile and requirements.txt file which I then pushed to heroku with the main files.
These tell heroku that this is a web application and what tools in needs to load for the app to run correctly.

All commits have been made to the same master git branch.

A number of config vars are required as follows...

HOSTNAME - The web address of the site - django uses this as a security measure to ensure the page is authorised to be accessed

DATABASE_URL - This is the address of the production postgres database, mine is a heroku addon postgres database

AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY - As my static and media files are set up to be held in an S3 bucket, both of these are required.

DISABLE_COLLECTSTATIC - This should be set to 1 to prevent any static and media files being uploaded to heroku on each git push as they are hosted on AWS

EMAIL_ADDRESS & EMAIL_PASSWORD - As emails are sent via the site, a gmail address and password is required with less secure apps access

SECRET_KEY - This is the key that django uses to verify the site

STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY - These are required by stripe for a user to make payments via checkout.html

Other notes:

Newly created super users must create a profile in django admin after being added via terminal or profile page will not display, a profile per user is required...
Upon creating a user, the site will create a profile for that user via the UserProfileData model within the profile_and_stats app. However, when initially creating a superuser for django, a profile will not be created. Therefore, in order for the site to work for a superuser, they must manually add a profile via the django admin page and link it to their account using the many to many field. If this is not completed, the superuser will not be able to access their profile page as the record will not be found.

I have added version numbers to the css and js tags within base.html. These must be updated before every commit to ensure users get the most up to date styling and js logic files on their next visit.
In addition, I have added notes to a setting in settings.py to enable a developer to refresh there css and js files without having to collect static on every occasion to see any changes.

If a developer wants to push their static and media files to AWS, they must run the collectstatic command in the terminal with the following setting...

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

However, if you wish to refresh your development site without having to collectstatic, the settings should be as follows...

if development == False:
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

Collecting static with these settings will result in a folder being created in the root directory containing all of those files. Should this happen, the stray folder can be deleted without consequence.

*Example 2
To push this app to GitHub repository, the following actions were taken:
Installing git and creating a GitHub account.
Initializing a git repository in the root of the app folder, by running the git init command.
Creating a new repository on GitHub:
logging in and going to the GitHub home page. Clicking '+ New repository' button,
typing name of the repo and providing a brief description,
pressing the 'Create repository' button to make new repo,
following the '....or push an existing repository from the command line' section.
Adding, committing and pushing changes to GitHub repository.
Deploying to heroku took following steps:
Developing app and pushing it to GitHub.
Installing gunicorn, a package for django, used to run app on the server.
pip install gunicorn  
Installing psycopg2, to run PostgreSQL, because is easy to setup on Heroku, instead of MySql or Sqlite.
pip install psycopg2  
Installing dj_database_url, a package used to add database to django.
pip install dj_database_url  
Creating a requirements.txt file. That file contains all required packages to run the application.
pip freeze > requirements.txt
Creating a Procfile. Procfile is a mechanism for declaring what commands are run by application’s dynos on the Heroku platform. Procfile contains:
echo web: gunicorn issuetracker.wsgi:application > Procfile
Pushing changes on Github.
Creating an App on Heroku(before creating an app make sure your GitHub account is connected with Heroku Account):
click on Create new app an Heroku website
type app name and choose region
click create app button.
Adding PostgreSQL database.
heroku addons:create heroku-postgresql:hobby-dev
Creating config variables:
on Heroku app go to settings
click Reveal Vars
set EMAIL_PASSWORD, EMAIL_ADRESS, SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and HOSTNAME.
Deploying the app on Heroku:
open your Heroku app and go to deploy option
select the deployment method as Github,
search your repository with a name and click connect
app started to deploy on Heroku, wait for some time
after the successful message popup, app can be view using URL delivered by Heroku. Live version of this app can be found here.
To clone this repository and run the app locally following steps are needed:
On GitHub, navigate to the main page of the repository.
Under the repository name, click Clone or download.
In the Clone with HTTPs section, click an copy icon to copy the clone URL for the repository.
Open Git Bash and change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 2.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
Press Enter. Your local clone will be created.
Install requirements
pip install -r requirements.txt
Set the environmental variables:
create file env.py in the main folder of the app
set variables for EMAIL_PASSWORD, EMAIL_ADRESS, SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and HOSTNAME
Start the app
python manage.py runserver
and go to http://127.0.0.1:8000/

### Credits
*Update this part*

* I have seen the website and used some ideias from: Spencer https://github.com/5pence/recipeGlut and MiroslavSvec https://github.com/Code-Institute-Submissions/project-5
* Content for Recipes from the BBC website: https://www.bbc.co.uk/food/recipes
* For text correction: https://www.grammarly.com/grammar-check
* For pictures: https://www.istockphoto.com/ie and https://www.bbc.co.uk/food/recipes
* For dropzone http://www.dropzonejs.com (Matias Meno)
* For validation: www.jshint.com



# Old Currency Ecommerce

The Old Currency is an Ecommerce wrote in Python using Django Platform that allows you to sell your Old coins online.

## Introduction

You can access the Old Currency Ecommerce clicking in this link [Click here](http://oldcurrencyapp.herokuapp.com/).


## Installation

After the Download or Clone of the project, you should create an Virtual Environment to run Old Currency Ecommerce inside the Django Platform .

```bash
python -m venv  ./venv
```

## Installation of Dependencies

Now we have our Virtual Environment ready, we have to install the dependencies of our project.

Command to install all dependencies:

```bash
pip install -r requirements.txt
```


## Setup the Server

You can setup the server using the command below:


```bash
python manage.py runserver     

```


## Run the Migrations

We will have to connect to the Database, to do it, we can run some command line to help us to create everything in our database such as Table, Indices, Constraints and Relationship between tables.  

First we have to create the Migrations

```bash
python manage.py makemigrations  

```

Now we have the Migrations we will have to run the command line to execute it and create the tables in our Database. You do it using the migrate command:

```bash
python manage.py migrate

```

We are almost there, to have access to our database we have to create an admin user. There is a specific command to do it
```bash
python manage.py createsuperuser

```

Now you should be able to access the Old Currency Admin.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
