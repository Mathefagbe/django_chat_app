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


daphne -b 0.0.0.0 dj_chat.asgi:application

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

## **Screenshots**
![Screenshot (378)](https://github.com/Mathefagbe/django_chat_app/assets/94699588/420c8285-f3ef-4561-881f-4dcdcbbc5eb8)
![Screenshot (379)](https://github.com/Mathefagbe/django_chat_app/assets/94699588/6fcca2b2-c5da-4d2b-93c1-7be194a05a98)![Screenshot (381)](https://github.com/Mathefagbe/django_chat_app/assets/94699588/80c7b88f-f469-4b56-9652-668d40c59c28)

## **Mobile screenshot**

![Screenshot_20231104-143307](https://github.com/Mathefagbe/django_chat_app/assets/94699588/9cd54f18-fd2c-4892-b033-0f446262dc29)![Screenshot_20231105-012120](https://github.com/Mathefagbe/django_chat_app/assets/94699588/752a9f91-f97e-460c-aee6-22fa22209c2d)

![Screenshot_20231105-012657](https://github.com/Mathefagbe/django_chat_app/assets/94699588/11410c8f-fe54-4bc8-ab92-3d01e80f2a4c)

  ![Screenshot_20231104-143330](https://github.com/Mathefagbe/django_chat_app/assets/94699588/cf033938-70f9-40b5-9891-b6d5b0b63714)

