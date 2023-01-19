# Python---Backend-Task
Django Rest Framework + Swagger Documentation
## Setup
The first thing to do is to clone the repository:
```
> $ git clone https://github.com/EslamRM/Python---Backend-Task.git
> $ cd Python---Backend-Task
```
Create a virtual environment to install dependencies in and activate it:
```
> $ virtualenv2 --no-site-packages env
> $ source env/bin/activate
```
Then install the dependencies:
```
> (env)$ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies:
```
> (env)$ cd project
> (env)$ python manage.py runserver
## walkthrough
1- first you have to register or create super user
```
POST http://127.0.0.1:8000/register/
params = {
    "username": "",
    "password": "",
    "password2": "",
    "email": "",
    "first_name": "",
    "last_name": ""
}
```
2-login to get access the products
```
POST http://127.0.0.1:8000/login/
params = {
    "username": "",
    "password": "",
}
and you should get response with access token and refresh token
```
3- now with access token you can make requests like below
