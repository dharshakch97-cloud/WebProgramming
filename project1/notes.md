# Project 1

Web Programming with Python and JavaScript

Task 1 Postgresql - Reflection
1. What is the need for Add Ons in Heroku?
   Heroku add-ons are components that support your application, such as data storage, monitoring, analytics, data processing, and more. 
   The add-ons are fully maintained for you by either a third-party provider or by Heroku. 
   Add-ons exist so that developers can focus on their own application logic, and not the additional complexity of keeping supporting services running at full production capacity.

2. What exactly happens when you click on provision while configuring the Postgres addon?
   Before provisioning the postgres addon, we need to confirm first that it isn't already provisioned. Provisioning actually means DATABASE_URL designates the URL of an app's primary database.

3. What is the use of Adminer? How does it work?
   It is a database management tool for creating, assessing, and managing SQL databases through a web browser. With Adminer, we can run SQL commands, import and export data. 

Task 2 Python and Flask - Reflection
1. How do I manage to use python 3.6 if I already have python 2.7?
2. What is the role of pip and how does it work?
   Pip is a package management system used to install and manage software packages, such as those found in the Python Package Index. 
   Pip is a replacement for easy_install. 
   
3. What is the role of requirements.txt and how does it work with pip?
   To install custom packages that are required for the project, we keep all those in a text file & install those packages using pip.

4. Which packages are installed and why are they required?
   Flask, Flask-session, SQLAlchemy.
   Flask is a python web framework which used to build the webpages in python programming language. 
   SQLAlchemy - It is an SQL toolkit and object relational mapper. It gives flexibility of SQL to an application developer. It allows object-model and database schema to create database tables, and develop applications.

5. Which environment variables set for Flask to work? What is the purpose of each variable?
   The environment variable set for Flask to work is FLASK_APP. It actually enables the flask for the the python file and runs the server.
   
6. What happens when the Flask run command is issued on the terminal?
   Wnen we give flask run command on the terminal, it starts the application we can run in the web browser by passing the URL.

7. On which port is Flask running and can it be changed?
   The Flask runs on the localhost on our personal computer. Yes, we can change the port number by directly passing the port number in app.run()

8. How is Flask different from the tiny web server?
   Flask is a web developement framework which sets the tools and libraries that makes easier for developing web applications. But web server means that a website deploys a computer.
   
Task 3 Goodreads API - Reflection
1. What are the various categories of web APIs available on good reads?
2. Is there a limit on the use of the web API? What are the limits?
