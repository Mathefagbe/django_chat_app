# django_chat_app
**THIS IS A CHAT WEBSITE BUILT USING DJANGO CHANNELS,JQUERY,JAVASCRIPTS,TAILWIND CSS AND FLOWBITE**
## *FEATURES*
* Authentication:User authenticate through username and password
* following system:The following system works using DOM manipulation using jquery to send request to django endpoints
* chat system:The chat system uses django channel and websocket to create connections
* One to One chat system:The app gives access to one to one chat between users in the website
* Responsivness:The website was responsive to any screen size this was done using tailwind css

## *SETUP*
* To setup the project first u folow tailwind css documentation in other to use tailwind with your project
* Once that is done follow installation project

## **Installation**
To run the Teragist API locally, follow these steps:
* Clone the repository:
  `git clone the repository`
* Create and activate a virtual environment:
  * for mac `python -m venv env source env/bin/activate`
  * for windows `python -m venv env env/scripts/activate`
* Install the project dependencies:
  `python -m pip install -r requirements.txt`
* Make migrations:
 `python manage.py makemigrations`
* Apply database migrations:
  `python manage.py migrate`
* Create a super admin:
  `python manage.py createsuperuser`

## **NOTE**
You system must be able to install redis for the channel layer to work.You can check django channels documentaions for more info
  
