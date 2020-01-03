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