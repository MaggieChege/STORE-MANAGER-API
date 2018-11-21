[![Build Status](https://travis-ci.org/MaggieChege/STORE-MANAGER-API.svg?branch=develop)](https://travis-ci.org/MaggieChege/STORE-MANAGER-API)

[![Coverage Status](https://coveralls.io/repos/github/MaggieChege/STORE-MANAGER-API-V2/badge.svg?branch=develop)](https://coveralls.io/github/MaggieChege/STORE-MANAGER-API-V2?branch=develop)

# STORE-MANAGER-API
These are the API endpoints to Both Products and Sales allowing Store Attendant/admin to add new Products/Sales 

The admin can do the following:

- Sign up  a new shop attendant
- Login 
- Add a new Product
- View all Products
- Make a sale
- View all sales
- View a particular sale by sale_id
- View a specific product by product_id
## Link to Pivotal tracker
``` https://www.pivotaltracker.com/n/projects/2203105 ```

## Runnig this App
  Clone this Repo

``` git clone https://github.com/MaggieChege/STORE-MANAGER-API.git ```

Navigate to the project directory
install virtual environment
``` virtualenv env ```
 Activate virtual environment

``` $ source env/bin/activate ```

 Install all dependencies for the project to work
``` $ pip install -r requirements.txt ```

 Install all dependencies for the project to work
``` $ pip install -r requirements.txt```

 Run the application
``` $ flask run ```


## TESTING APP

The endpoints can be tested using postman. If you're on linux install postman and launch
``` $ postman ```

## RUN TEST
To run the unittest. Ensure you set Pythonpath or the the location of you app
``` $ export PYTHONPATH=${PYTHONPATH}:Desktop/<dir> ```
Then run the test
``` $ pytest -v ```







