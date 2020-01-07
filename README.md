# Old Currency

The Old Currency is a ecommerce website where people are able to search about old currencies and learn about the historical details of each currency. Besides of that if they register in the website, they are able to advertise/sell a currency and even buy the old currency (ies) advertised. For buying any currency it is essential to provide a credit card details. The website has an safe authentication mechanism that xxxxx
 
### UX
The main aims of the project are as follows:
1. Be able to see the currency historic but not selling or buying unless that the user register
2.To allow the user to register and create their own user profile
It should be intuitive and easy for the user to use.

USER STORIES:
To understand why people might choose to use this site and therefore provide direction on its creation, I created a number of user stories as follows...

Story 1: As a regular user, I want to be able for searching for currency

Story 2: As a user, I'd like to see the historic of each currency, image and price

Story 3: As a user, I want to be able to register in the website

Story 4: As a user, I would like to buy a currency that I am interested in

Story e: As a user, I need to be able to pay for the currency that I want to

Although a big undertaking, the website will provide a complete solution for these users

WIREFRAMES - build the designs
Example 1:
Initial wireframes are slightly different from the actual design. 
Landing Page - Logged Users : From the beginning it was thought to have a unique landing page. The initial design is now used to display information for logged users.
Navigation Bar : This sections was planned to have a design that will differ for logged and non logged users. The actual design has more elements compared to the wireframe, it also displays user avatar and a cart.
Registration & Authentication
The following sections are accessible only to registered users
Add Ticket
Ticket List
Ticket Details
Checkout
There are also a number of pages that are similar to those mentioned above:
Form for password recovery. Has similar structure to login/registration form.
Thank you page. A page that is loaded when a user successfully purchases the App. Contains an image with a link to download the app. This page wasn't initially included in the design. I decided to add it to the checkout process in order to ensure a clear flow.

Example 2: The wireframes (found in the wireframes_and_design_notes folder) provide a good early indication of how I wanted the site to look and feel. The final site has stayed very close to this original design but has been modified to try and make it more user friendly.

After consideration of names, approach and colour schemes I decided to use a green, yellow, blue and black scheme (the green would work well for the football pitches) and I selected the name myTeam after consultation with a number of people in my football group.

The concept of what the site wants to achieve is sound but could become complicated for a user to get used to, therefore at times I broke away from the original wireframe to try and make the operation of the site as user friendly as possible, keeping the UX in mind at all times.

My website will is divided into 6 apps, accounts, groups, matches, profile_and_stats, subscriptions and team_gen.


### Features
draft: The website is designed to be extremely straight forward, there is a general search field in the top-right-corner of the homepage where the user sees a "magnifying glass" and by clicking on that it will display a green big bar on the top of the page which enables the user to type the word (s) for searching. There is no clutter on the homepage, no distractions, its designed so it is not confusing and grabs the user very quickly. So in this search engine, the user can enter words like new zeland, australian, bronze or whatever to find what they are looking for, which will obviously bring up another page with the results. 

User can buy.... and sell the coins by clicking on...


Top Nav Bar 
First is the option for the “Cook Book” which just brings you back to the homepage and the main search engine as described above.  Next they will see the “Search by Category” also described above.
The next Top Nav Bar options are “Big Trends”, “About Us”, “Connect with Us” and “ Recipe Management” which opens a dropdown list which gives a further two options: “Upload your Recipe” and “Edit & Delete a Recipe”.

* ***First Page***  
On the first page, in the middle of the screen there is the general search field where the user should type the keyword of the recipe desired and click on the button “Search”
* ***Search by Category page***  
On the Search by Category page the user should flag/select as many categories he/she wants and click on the button “Search” at the bottom. Above the Search button there is a display for the total amount of recipes available which will appear in the next page based on the current fields that are flagged.
Listed below are the options under each category:
  - “Dish”: Chicken, Fish, Pasta, Meet and Dessert
  - “Type of Cuisine”: Italian, French, Thai and Greek
  - “Type of Diet”: Vegan, Vegetarian, Light and Gluten-Free
* ***Recipes Resulted from the Search page***
This page displays the recipes which meets the criteria flagged on the search (whether they were from the General Search or Search by Category). In this page each recipe will be named and will provide a picture. Each recipe clearly has a “See More” option highlighted in blue allowing the user to go in and view, when the user clicks on this they will get all the information required in order to prepare the dish, including time needed, ingredients required, detailed preparation instructions and also a picture of the dish. 
* ***Big Trends***  
On the Big Trends page it shows pictures of 3 deluxe dishes (in a carrocel format)
* ***About Us***  
On this page the user can find out a little about the company that created the page and it’s purpose. It is on this page that the cooking knives are mentioned and promoted.
* ***Connect with Us***
This simply shows that we are on the three major social media channels, Instagram, Facebook, and Twitter. 
* ***Recipe Management***  
By clicking on Recipe Management, it will open a dropdown box with the option to go to the pages: “Upload your Recipe” and “Edit & Delete a Recipe”.
* ***Upload Your Recipe page***  
Allows the user to upload his/her own recipe. The titles and format is the same as when he/she views any other recipe on the site. They enter the Name of the Recipe, Time required, Ingredients required, Preparation details, and category details.  Upload a Picture and at the end click on the “Send” button. Then the “           Save” button will appear in green.
* ***Edit & Delete a Recipe page***   
Will display all recipes available on the website by name and with a picture and will have the options to “Edit” and “Delete” for each. The “Edit” page is essentially the same as the “Upload page” but obviously the text is already populated. 
 
### Future plans include:
* An option to register, login and log out. 
* Provide profile information for logged in members with graphics about how many recipes he/she has uploaded (and also a breakdown of them by category), and how the recipes that he/she uploaded have performed (how many likes has received).
* Provide detailed pages about knives and accessories for sale and provide purchase options.
* An option for members who upload numerous recipes receive 10% discounts of the knives.

### Technologies used
This website is a Flask Website that uses a Mongo backend.

* **Bootstrap**
* **CSS**
* **Flask**
* **HTML5**
* **JS**
* **Mongo**
* **Python**

### Testing
All features of the website has been tested and seems to be working well.
Each functionality has been tested and are described on the Validation documents (pages 01-03).
The webpage is responsive adapting to different sizes of the devices.
The www.jshint.com validator coding was used.
 
### Deployment
The webpage was deployed using Github and Heroku. The link to the website is: https://cookbookie.herokuapp.com/.

### Credits
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
