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
```
## walkthrough
--swagger documentation
```
http://127.0.0.1:8000/doc-api/
```
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
3- now with access token you can make GET requests to search for products
```
http://127.0.0.1:8000/products/?ordering=id
http://127.0.0.1:8000/products/?ordering=name
http://127.0.0.1:8000/products/?ordering=category
http://127.0.0.1:8000/products/?min_price=4.000&max_price=90.000
http://127.0.0.1:8000/products/?category=finance&name=&min_price=5.000&max_price=90.000&min_quantity=4&max_quantity=30&brand=&rating=&created_at=
http://127.0.0.1:8000/products/?search=finance
```
4- you can acess to cart and make crud operation
```
[GET]http://127.0.0.1:8000/cart
[POST]http://127.0.0.1:8000/cart
[GET]http://127.0.0.1:8000/cart/1
[PUT]http://127.0.0.1:8000/cart/1
[DELETE]http://127.0.0.1:8000/cart/1
```
5- finally you can make test on the api
```
python manage.py test products
```


