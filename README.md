# Rafiki
This is a web application that allows  users to sign up ,log in and hire local personnel who can help them with domestic tasks like; laundry ,gardening,dog walking or car washing


## User Stories
A user of the application can:
* Sign in / login to the application to start using either as an employer or as an employee.
* workers can Set up a profile about me and a general location and availability.
* Employers can Find a list of different domestic workers offering different services.
* Employers can click on an employee and Find Contact Information 



## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| User Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| employees feed | **Feed page** | Display employees available for work |
| Click on an employee| **On  employee image  click** | A display the employees profile and availability |
| To search for an employee  | **Through employer welcome page | Click on services to search for employees based on category |



## Technologies used
* Python3.8.10
* Django 



## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/Liz2222/rafiki.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual``

3. Activating the virtual environment
>``source virtual/bin/activate``

4. Running the application
>``python3 manage.py runserverserver``

5. Running tests

 > ``python3 manage.py test.``

## [License]()

## Collaboraters
[Liz2222](https://github.com/Liz2222) 
[joey57](https://github.com/joey57)
[aust1inn](https://github.com/aust1inn)
[christine-nkatha](https://github.com/christine-nkatha)