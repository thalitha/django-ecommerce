# Old Currency

Old Currency is a ecommerce website where users can search old currencies and learn about the historical details of each of them. If they register to the website they have more options, such as purchasing the old currencies advertised. For purchasing any currency it is essential to provide credit card details. The website has a safe authentication mechanism.
 
### UX
The main aims of the project are:
1. Be able find out about the old currencies, but only allowing registered customers to purchase. 
2. To allow the user to register and have their own user profile and see their orders
3. It is intuitive and easy to use

* **User Stories:**
Below are the user stories:

Story 1: As a regular user, I want to be able to search for various currencies

Story 2: As a user, I'd like to see the history of each currency, their image and price

Story 3: As a user, I want to be able to register in the website and have my own login

Story 4: As a user, I would like to buy currencies that I am interested in

Story e: As a user, I need to be able to easily pay for the currency by card

The website provides complete solution for the users

* **Wireframes**
See the Wireframe here: https://github.com/thalitha/django-ecommerce/blob/master/Wireframes.PNG 

### Features
* **Product Display** - The website is designed to be extremely straight forward, on the homepage you can see the old currency titles, images and their price. By clicking on the title you will access a story about the history of the currency. There is no clutter on the homepage, no distractions, its designed so it is not confusing and grabs the user very quickly. Within seconds of going into the homepage it is obvious to any user that this website is selling old currency. 

* **Search bar** - There is a general search field on the top-right-corner. Here the user sees a "magnifying glass" and by clicking on that it will display a green big bar on the top of the page which enables the user to type the keyword(s) and click on a second magnifying glass which has now appeared with the new bar. So here the user can enter words like New Zealand, Australia, bronze or whatever to find what they are looking for, which will obviously bring up another page with the results. 

* **User authentication** - Register, Login, Logout - The application contains an Authentication app. This allows the user to login, logout, register with the site.

***Register*** - users register by providing a username and password in the register form. The password needs to be confirmed in an extra field. The password can’t be too similar to their other personal information, it must contain at least 8 characters, it can’t be a commonly used password and it can’t be entirely numeric; if it is than they will have to create a different password. After successfully registering the user is redirected to the home page which now shows them that they are logged in under their own username

***Log in, Log out*** - After successful registering the user is redirected to the home page. Now a user can login and logout anytime they want to in the future. 

* **User Profile - My Orders** After logging in the user will be able to see the button "My orders" on the top and by clicking on it will access their orders.

* **Users can buy the products**
A user is able to buy the products by following these steps:
1. Go to the homepage
2. Click on the button: "On Sale Now"
3. In the next page click on the button "Buy now"
4. In the next click on "Confirm payment"
5. In the next page click on "Pay with card"
6. In the next page fill out the form proving data such as: e-mail, card no, expiry date and cvc.
For testing the website you can use the following data:
credit card no: 4242 4242 4242 4242
expiry date: 06/20 
cvc: 123
9. Click on "pay" button
8. The next page will show the order with the amount in Euros that you paid.

This is done using the STRIPE API.

* **Footer** - Contains links to social media, i.e. facebook and twitter

### Future plans include:
* An option to review products users have bought.
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
User stories from the UX section were tested to ensure that they all work as it was intended, with the site providing a straightforward way for the users to achieve their goals. It is all working smoothly. 
Each functionality has been tested and are described in the Test - Validation document (https://github.com/thalitha/django-ecommerce/blob/master/Test%20-%20Validation.pdf)
The webpage has been tested on different devices and works on all.
The www.jshint.com validator coding was used.
HTML and CSS code for this website were validated using W3C Validation Service. No errors were found in the code.

### Deployment
The webpage was deployed using Github and Heroku. The link to the website is: http://oldcurrencyapp.herokuapp.com/
After the Download or Clone of the project, you should create a Virtual Environment to run Old Currency Ecommerce inside the Django Platform .

```bash
python -m venv  ./venv
```
***Installation of Dependencies***

After the Virtual Environment is ready, it is necessary to install the dependencies of the project.

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

It is necessary to connect to the Database. To do it, you can run a command line to help to create in the database:Table, Indices, Constraints and Relationship between tables.  

Create the Migrations

```bash
python manage.py makemigrations  

```
Run the command line to execute it and create the tables in our Database. You do it using the migrate command:

```bash
python manage.py migrate

```
To have access to the database it is necessary to create an admin user. There is a specific command to do it

```bash
python manage.py createsuperuser

```
Now you should be able to access the Old Currency Admin.

### Credits

* Product content from the All Coin Values website: https://www.allcoinvalues.com/
* For pictures (removal of the background of the coins pictured): https://www.remove.bg/upload
* For text correction: https://www.grammarly.com/grammar-check
* For validation: www.jshint.com
