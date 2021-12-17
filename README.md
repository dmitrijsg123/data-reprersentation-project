# data-representation-project

For the project I created an inventory website of imaginary Bicycle shop "Mike's bikes". A person can log into the website, authorize themselves (enter username and password), after that they are re-directed on to the main page where they can see two inventory tables. 1st table has accessories inventory, 2nd table- bicycles/ scooters inventory. The tables are linked to remote MySQL tables (stock and stockk, respectively) from Datarep database. Data from each of the two tables can be manipulated - deleted, updated, or new data entered (CRUD operations). 

The code itself of the for_server.py file is heavily based on the code provided to us by Andrew Beatty at his Data Representation module.

Data Representation Project

FLASK INSTALLATION
python -m venv venv

.\venv\scripts\activate.bat

pip freeze

pip install flask

pip freeze > requirements.txt

python for_server.py

Open your browser and go to your browser to load this url
http://127.0.0.1:5000/index.html

Website credentials:
Username: 1234
Password: 1234
