# Acviss_Assignment

An easy to use website to scrape information from www.bseindia.com/ and collect BhavCopy from it.

# Basic Requirements:

Design and code a simple MVC module using the Django framework to do below.
* Create a table “batch” with which holds the batch code and the user who generated it.
* Create another table to store codes
* Generate X number of unique random 10 digits alphanumeric code.
* Consider you have to generate at least a min of 50k to a max of 5Lakhs codes per batch.
* Store the codes in the database (Assume that the database already has millions of codes).
* Create a UI for the admin to generate the codes. Use the default Django Auth layer.
* Show the history of codes generated by that admin.
* Token-based authentication in the frontend is to be implemented.
* Frontend framework is of your choice.
* Create a search page where the code can be searched.
* Handle all exceptions and all response codes sent.
* Cover the API’s and other processes with unit tests.

# Workflow:
- Admin logins into the side. He creates a batch by specifying the batch name and no of codes. The process will continue to happen. Admin will be then notified. At a time, only one batch of generation should happen

# Setup Guide:

- Start by cloning this project to your computer.
- Install virtualenv using : `pip install virtualenv`
- Create a virtual environment using : `virtualenv -p python3 env .` 
- Create an src folder and extract the files to this directory. This will serve as the root directory.
- Install dependencies using `pip install -r requirements.txt` in your terminal.

# Running the app :
On terminal, navigate to the env directory and activate the Virtual environment using  `.\Scripts\activate`.
Now, run `python manage.py runserver` command in the terminal :
- `python manage.py runserver`

Congrats, the web app should be up and running!

Thank you for reading! :book: :heart:
