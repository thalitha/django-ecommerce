# Old Currency

The Old Currency is a ecommerce website where people are able to search about old currencies and learn about the historical details of each currency. Besides of that if they register in the website, they are able to buy the old currency (ies) advertised. For buying any currency it is essential to provide a credit card details. The website has an safe authentication mechanism that xxxxx
 
### UX
The main aims of the project are as follows:
1. Be able to see the currency historic but not buying unless that the user register 
2. To allow the user to register and have their own user profile and see their orders
3. It should be intuitive and easy for the user to use

* **User Stories:**
To understand why people might choose to use this site and therefore provide direction on its creation, I created a number of user stories as follows...

Story 1: As a regular user, I want to be able for searching for currencies

Story 2: As a user, I'd like to see the historic of each currency, their image and price

Story 3: As a user, I want to be able to register in the website

Story 4: As a user, I would like to buy a currency that I am interested in

Story e: As a user, I need to be able to pay for the currency that I am buying

The website will provide a complete solution for these users

* **Wireframes**
Build the designs and do a web link to access it - as this example did:https://github.com/Code-Institute-Submissions/Django-Milestone-Project-2

### Features
* **View of the products** - The website is designed to be extremely straight forward, on the very first webpage you can see the old currency titles, images and their price and by clicking on the title you will access the historic about it. There is no clutter on the homepage, no distractions, its designed so it is not confusing and grabs the user very quickly. 

* **Search bar** - There is a general search field in the top-right-corner of the homepage where the user sees a "magnifying glass" and by clicking on that it will display a green big bar on the top of the page which enables the user to type the word(s) and click for searching on the "magnifying glass". So in this search engine, the user can enter words like new zeland, australian, bronze or whatever to find what they are looking for, which will obviously bring up another page with the results. 

* **User authentication** - Register, Login, Logout - The application contains an Authentication app. This allows the user to login, logout, register with the site.

***Register*** - user can register by providing username and password in register form. Password needs to be confirmed in extra field. The password can’t be too similar to their other personal information, it must contain at least 8 characters, it can’t be a commonly used password and it can’t be entirely numeric; otherwise the website won't allow the user to register. After successful registering user is redirected to the home page which will have the message: "Hi (user name created), Welcome to Older Currency!"

***Log in, Log out*** - user can register by providing username and password in register form. After successful registering user is redirected to the home page.

* **User Profile - My Orders** After logging the user will be able to se the button "My orders" on the top and by clicking on it will access their orders.

* **Users' can buy the products**
The user is able to buy the products following the steps:
1. Go to homepage
2. Click on the button: "On Sale Now"
3. In the next page click on the button "Buy now"
4. In the next click on "Confim payment"
5. In the next page click on "Pay with card"
6. In the next page fill out the form proving data as: e-mail, card no, valid date and cvc.
For testing the website you can use the follow data:
credit card no: 4242 4242 4242 4242
valid date: 06/20 
cvc: 123
9. Click on "pay" button
8. The next page will show the message: "Order Number No Thanks, you paid € (the amount paid)!

This is done using the STRIPE API.

* **Footer** - Contains linked social icons.

### Future plans include:
* An option to review the product bought.
* Filters for searching such as year of the currency and value.

### Technologies used
This website is written in Python and uses Django.

* **Bootstrap**
* **CSS**  
* **Github**
* **Heroku**
* **HTML5**
* **JS**
* **Postgres**
* **Python**
* **Stripe**

### Testing
User stories from the UX section were tested to ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals and seems to be working well.
Each functionality has been tested and are described on the Validation documents (pages 01-03).
The webpage is responsive adapting to different sizes of the devices.
The www.jshint.com validator coding was used.
HTML and Css code for this website were validated using W3C Validation Service. No errros were found in the code.

### Deployment
The webpage was deployed using Github and Heroku. The link to the website is: http://oldcurrencyapp.herokuapp.com/

After the Download or Clone of the project, you should create an Virtual Environment to run Old Currency Ecommerce inside the Django Platform .

```bash
python -m venv  ./venv
```
***Installation of Dependencies***

Now we have our Virtual Environment ready, we have to install the dependencies of our project.

Command to install all dependencies:

```bash
pip install -r requirements.txt
```
***Setup the Server***
You can setup the server using the command below:

```bash
python manage.py runserver     

```
***Run the Migrations***

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

### Credits
*Update this part*

* Content for Recipes from the BBC website: https://www.bbc.co.uk/food/recipes
* For text correction: https://www.grammarly.com/grammar-check
* For pictures: https://www.istockphoto.com/ie and https://www.bbc.co.uk/food/recipes
* For validation: www.jshint.com




