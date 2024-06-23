# edutech
Hello! Welcome to Edutech.com documentation


Requirements to run this project.
1. Python 3.10
2. django==5.0.6
3. postgressql 12+


Steps to run this project in your local machine.
you can skip step 1 and step 2 if you have python 3.10 and GIT in your local systen.

step1. Install python3.10 in your local system.
step2. Install GIT in your local system.
step3. Clone the respository into you local system using this cmd.
    -->     git clone https://github.com/rbose7375/edutech.git
step4. Create a virtual envirment for this project dependencies run bellow cmd in command prompt.
    -->     python -m pip install virtualenv
    -->     virtualenv venv
step5. now activate enviroment and install dependencies.
    -->     venv\Scripts\activate
    -->     cd edutech
    -->     pip install -r requirments/requirement.txt  or python -m pip install -r requirments/requirement.txt
<!-- now installation is started  -->
<!-- your project is ready to run just need few more configuration to run project -->
<!-- now we do database configuration -->
setp6. create database name called 'eductech' in postgresql use this cmd in psql shell.
    -->     CREATE DATABASE edutech;
    1. change password of postgresql in django env edutech_io/.env file here change value of 'DB_SETTING_PASSWORD' put you system psql password.

step7. now load database for run project.
    -->     python manage.py migrate     
    -->     python manage.py loaddata requirments/site_data.json

<!-- now everything alright lets start the project -->

step8. python manage.py runserver

Enjoy your project in now run open in browser at http://127.0.0.1:8000


 
HERE IS API Structrue of your requiment.

search - /api/v1/search :- get request 'query' param
category - /api/v1/get-gategories :-getreq

favirote api - /api/v1/interest-list   : post / get req   post - 'service_id' in data also token in authentication
book oreder api - /api/v1/book-class  :get - post  post - 'service_id' in data also send token in header as authentication
